# -*- coding: utf-8 -*-
"""
بوت مسارات الثلاث (صحي / هندسي / حاسوبي)
لكل مسار → مواد → مدرسين (كل مدرس زر مستقل)
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ============ التوكن ============
# حط توكن البوت حقك هنا (من BotFather)
TOKEN = "8880859850:AAF8h52qAVKv-tFL5EeeT-SR5bVFcEvm0TM"

# ============ قاعدة بيانات المدرسين ============
# عدّل / أضف بياناتك هنا. كل مسار فيه مواد، كل مادة فيها مدرسين.
DATA = {
    "sehi": {
        "title": "🩺 المسار الصحي",
        "subjects": {
            # مثال فارغ - عبّيه ببياناتك
            # "anatomy": {
            #     "title": "تشريح",
            #     "tutors": [
            #         {"name": "أ. فيصل", "contact": "@username", "price": "250 ريال"},
            #     ]
            # },
        }
    },
    "handasi": {
        "title": "⚙️ المسار الهندسي",
        "subjects": {
            # عبّيه ببياناتك
        }
    },
    "hasoobi": {
        "title": "💻 المسار الحاسوبي",
        "subjects": {
            "prog": {
                "title": "🖥️ حاسب وبرمجة",
                "tutors": [
                    {"name": "محمد الجنيدي", "contact": "@EngMsaD11", "price": "300 ريال"},
                    {"name": "مسعد احمد", "contact": "@Mosaad4567", "price": "300 ريال"},
                    {"name": "رهيب محمد", "contact": "@Diamond246", "price": "299 ريال"},
                    {"name": "رنا", "contact": "@Ra12na_IT", "price": "حاسب 250 / برمجة 350"},
                ]
            },
            "math": {
                "title": "📐 رياضيات",
                "tutors": [
                    {"name": "أريام محمد", "contact": "@RyamAmm", "price": "350 ريال"},
                    {"name": "حسين فلكه", "contact": "@hhhhxzm", "price": "عن بعد 400 / حضوري 800"},
                    {"name": "ريان", "contact": "@Rayanacad", "price": "350 ريال"},
                    {"name": "مازن", "contact": "@imezoi", "price": "250 ريال"},
                    {"name": "علي محمد", "contact": "@Alymohamed97", "price": "300 ريال"},
                    {"name": "أشرف رضوان", "contact": "0531461336 (واتساب)", "price": "300 ريال"},
                    {"name": "يوسف محمد", "contact": "0593812861 (واتساب)", "price": "300-350 ريال"},
                    {"name": "عبدالله اللباد", "contact": "@a5kur", "price": "250 ريال"},
                    {"name": "أبو ياسر", "contact": "@Aboyasser221", "price": "عن بعد 400 / حضوري 600"},
                ]
            },
            "physics": {
                "title": "🔬 فيزياء",
                "tutors": [
                    {"name": "مازن", "contact": "@imezoi", "price": "250 ريال"},
                    {"name": "أريام محمد", "contact": "@RyamAmm", "price": "350 ريال"},
                    {"name": "يوسف محمد", "contact": "0593812861 (واتساب)", "price": "250 ريال"},
                    {"name": "ام ميار", "contact": "0538135853 (واتساب)", "price": "400 ريال"},
                    {"name": "أشرف رضوان", "contact": "0531461336 (واتساب)", "price": "300 ريال"},
                    {"name": "عبداللطيف جميل", "contact": "@Abdullatif1128", "price": "400 ريال"},
                    {"name": "مصطفى محمود", "contact": "@EngUncle_lolm", "price": "150 ريال"},
                    {"name": "احمد الصمادي", "contact": "@T_AlSmadi", "price": "عن بعد 400 / حضوري 800"},
                    {"name": "احمد مكاوي", "contact": "0501381714 (واتساب)", "price": "عن بعد 500 / حضوري 800"},
                ]
            },
            "english": {
                "title": "🗣️ اللغة الإنجليزية",
                "tutors": [
                    {"name": "يوسف", "contact": "0540972198 (واتساب)", "price": "300 ريال"},
                    {"name": "اسماعيل", "contact": "@Abduali44", "price": "400 ريال"},
                    {"name": "يارا الماوردي", "contact": "@DrYaraMawardy", "price": "350 ريال"},
                    {"name": "وليد", "contact": "@Waleedj8", "price": "400 ريال (عن بعد وحضوري)"},
                    {"name": "محمود مرتضى", "contact": "0553408926 (واتساب)", "price": "400 ريال"},
                    {"name": "ام مريم", "contact": "0596502573 (واتساب)", "price": "500 ريال"},
                ]
            },
        }
    },
}


# ============ الأوامر ============

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(DATA["sehi"]["title"], callback_data="path|sehi")],
        [InlineKeyboardButton(DATA["handasi"]["title"], callback_data="path|handasi")],
        [InlineKeyboardButton(DATA["hasoobi"]["title"], callback_data="path|hasoobi")],
    ]
    await update.message.reply_text(
        "أهلاً بك 👋\nاختر مسارك عشان تشوف مدرسينه:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data  # مثال: path|hasoobi  أو  subj|hasoobi|math  أو  tutor|hasoobi|math|0

    parts = data.split("|")
    action = parts[0]

    # ----- اختار مسار -> اطلع له المواد -----
    if action == "path":
        path_key = parts[1]
        path = DATA[path_key]
        subjects = path["subjects"]

        if not subjects:
            await query.message.reply_text(f"{path['title']}\n\nما فيه مواد مضافة بعد 🙏")
            return

        keyboard = []
        for subj_key, subj in subjects.items():
            keyboard.append([InlineKeyboardButton(subj["title"], callback_data=f"subj|{path_key}|{subj_key}")])

        await query.message.reply_text(
            f"{path['title']}\n\nاختر المادة:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ----- اختار مادة -> اطلع له المدرسين -----
    elif action == "subj":
        path_key, subj_key = parts[1], parts[2]
        subject = DATA[path_key]["subjects"][subj_key]
        tutors = subject["tutors"]

        keyboard = []
        for i, tutor in enumerate(tutors):
            keyboard.append([InlineKeyboardButton(tutor["name"], callback_data=f"tutor|{path_key}|{subj_key}|{i}")])

        await query.message.reply_text(
            f"{subject['title']}\n\nاختر المدرس:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ----- اختار مدرس -> اطلع بياناته -----
    elif action == "tutor":
        path_key, subj_key, idx = parts[1], parts[2], int(parts[3])
        tutor = DATA[path_key]["subjects"][subj_key]["tutors"][idx]

        text = (
            f"👤 {tutor['name']}\n"
            f"📨 {tutor['contact']}\n"
            f"💰 {tutor['price']}"
        )
        await query.message.reply_text(text)


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("البوت شغال...")
    app.run_polling()


if __name__ == "__main__":
    main()
