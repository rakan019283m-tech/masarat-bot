"""
bot.py
------
بوت تيليجرام "الخطة الدراسية الذكي".
"""

import logging
import os

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from planner import (
    load_courses,
    load_terms,
    remaining_critical_courses,
    suggest_plan,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

ASK_COMPLETED, ASK_TERM = range(2)
TERMS = ["أول", "ثاني", "صيفي"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    courses = load_courses()
    codes_list = ", ".join(c["code"] for c in courses)

    await update.message.reply_text(
        "أهلًا 👋 أنا بوت الخطة الدراسية الذكي.\n\n"
        "أرسل لي رموز المواد اللي خلصها مفصولة بفواصل، مثال:\n"
        "CS101, MATH101\n\n"
        "أو اكتب 'لا شيء' إذا ما خلصت أي مادة بعد.\n\n"
        f"رموز المواد المتاحة بالخطة:\n{codes_list}",
        reply_markup=ReplyKeyboardRemove(),
    )
    return ASK_COMPLETED


async def receive_completed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = update.message.text.strip()

    if text in ("لا شيء", "لاشيء", "لا", "-"):
        completed = []
    else:
        completed = [code.strip().upper() for code in text.split(",") if code.strip()]

    valid_codes = {c["code"] for c in load_courses()}
    unknown = [c for c in completed if c not in valid_codes]
    if unknown:
        await update.message.reply_text(
            "⚠️ ما لقيت هالرموز بالخطة: " + ", ".join(unknown) +
            "\nتأكد من الرموز وحاول مرة ثانية، أو اكتب 'لا شيء'."
        )
        return ASK_COMPLETED

    context.user_data["completed"] = completed

    keyboard = ReplyKeyboardMarkup([TERMS], one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("تمام ✅ وش الترم اللي بتسجل له؟", reply_markup=keyboard)
    return ASK_TERM


async def receive_term(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    term = update.message.text.strip()
    if term not in TERMS:
        await update.message.reply_text("اختر ترم من الأزرار: أول / ثاني / صيفي")
        return ASK_TERM

    completed = context.user_data.get("completed", [])
    result = suggest_plan(completed, term)
    critical_left = remaining_critical_courses(completed)

    lines = [f"📚 اقتراح خطة تسجيل ({term}):\n"]

    if result["selected"]:
        for c in result["selected"]:
            tag = " 🔴 حرجة" if c["critical"] else ""
            lines.append(f"• {c['code']} - {c['name']} ({c['hours']} ساعات){tag}")
        lines.append(f"\nإجمالي الساعات المقترحة: {result['total_hours']}")
    else:
        lines.append("ما فيه مواد متاحة لك هذا الترم حسب البيانات الحالية.")

    if result["skipped_due_to_conflict_or_hours"]:
        lines.append("\n⏱️ مواد ثانية كانت متاحة بس استُبعدت (تعارض وقت أو تجاوز سقف الساعات):")
        for c in result["skipped_due_to_conflict_or_hours"]:
            lines.append(f"• {c['code']} - {c['name']}")

    if critical_left:
        remaining_not_selected = [
            c for c in critical_left
            if c not in result["selected"]
        ]
        if remaining_not_selected:
            lines.append("\n🚨 مواد حرجة لسا ما أخذتها (تأخير هالمواد ممكن يأخر تخرجك):")
            for c in remaining_not_selected:
                lines.append(f"• {c['code']} - {c['name']}")

    await update.message.reply_text(
        "\n".join(lines), reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "تم الإلغاء. اكتب /start عشان تبدأ من جديد.",
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END


def main() -> None:
    load_dotenv()
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "لازم تحدد متغير البيئة BOT_TOKEN بتوكن البوت اللي أخذته من BotFather."
        )

    application = Application.builder().token(token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASK_COMPLETED: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_completed)],
            ASK_TERM: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_term)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # تشغيل البوت بنظام Polling مع تنظيف أي تعارضات سابقة تلقائياً
    logger.info("تشغيل البوت بنظام Polling")
    application.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
