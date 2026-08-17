# -*- coding: utf-8 -*-
"""
بوت مسارات الثلاث (صحي / هندسي / حاسوبي)
مع الروابط والمعرفات المباشرة للقنوات والأسعار
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ============ التوكن ============
TOKEN = "8880859850:AAF8h52qAVKv-tFL5EeeT-SR5bVFcEvm0TM"

# ============ قاعدة بيانات المدرسين والقنوات ============
DATA = {
    "sehi": {
        "title": "🩺 المسار الصحي",
        "subjects": {
            "comp": {
                "title": "🖥️ الحاسب",
                "tutors": [
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "price": "300 ريال"},
                    {"name": "مسعد احمد", "contact": "https://t.me/computersciencewithmosaad", "price": "300 ريال"},
                    {"name": "رنا", "contact": "https://t.me/RanaprogrammingNU", "price": "حاسب 250 / برمجة 350"},
                ]
            },
            "elmi1": {
                "title": "🧪 علمي (1)",
                "tutors": [
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "price": "300 ريال"},
                    {"name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "price": "350 ريال"},
                    {"name": "احمد مكاوي", "contact": "https://t.me/ahmed11_nu", "price": "عن بعد 500 / حضوري 800"},
                    {"name": "مصطفى", "contact": "https://t.me/gmustafamahmoud", "price": "150 ريال"},
                    {"name": "علي محمد", "contact": "https://t.me/najran_math1", "price": "300 ريال"},
                    {"name": "الصمادي", "contact": "https://t.me/alsmadi2024", "price": "عن بعد 400 / حضوري 800"},
                ]
            },
            "elmi2": {
                "title": "🧬 علمي (2)",
                "tutors": [
                    {"name": "أريام محمد", "contact": "https://t.me/collegeless", "price": "350 ريال"},
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "price": "250 ريال"},
                    {"name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "price": "300 ريال"},
                    {"name": "عبداللطيف", "contact": "https://t.me/abdullatifgameel999", "price": "400 ريال"},
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "price": "300 ريال"},
                    {"name": "ام ميار", "contact": "https://t.me/Najranshrohatammyar", "price": "400 ريال"},
                ]
            },
            "english": {
                "title": "🗣️ اللغة الإنجليزية",
                "tutors": [
                    {"name": "يوسف", "contact": "https://t.me/EnglishYusuf", "price": "300 ريال"},
                    {"name": "اسماعيل", "contact": "https://t.me/Abduali445", "price": "400 ريال"},
                    {"name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "price": "350 ريال"},
                    {"name": "وليد", "contact": "https://t.me/Waleed_forEn", "price": "400 ريال (عن بعد وحضوري)"},
                    {"name": "محمود", "contact": "https://t.me/EnglishwithDrMahmoud", "price": "400 ريال"},
                    {"name": "ام مريم", "contact": "https://t.me/M_J_A_k", "price": "500 ريال"},
                ]
            },
        }
    },
    "handasi": {
        "title": "⚙️ المسار الهندسي",
        "subjects": {
            "physics": {
                "title": "🔬 فيزياء",
                "tutors": [
                    {"name": "أريام محمد", "contact": "https://t.me/collegeless", "price": "350 ريال"},
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "price": "250 ريال"},
                    {"name": "ام ميار", "contact": "https://t.me/Najranshrohatammyar", "price": "400 ريال"},
                    {"name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "price": "300 ريال"},
                    {"name": "عبداللطيف", "contact": "https://t.me/abdullatifgameel999", "price": "400 ريال"},
                    {"name": "مصطفى", "contact": "https://t.me/gmustafamahmoud", "price": "150 ريال"},
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "price": "300 ريال"},
                    {"name": "الصمادي", "contact": "https://t.me/alsmadi2024", "price": "عن بعد 400 / حضوري 800"},
                    {"name": "احمد مكاوي", "contact": "https://t.me/ahmed11_nu", "price": "عن بعد 500 / حضوري 800"},
                ]
            },
            "prog": {
                "title": "🖥️ حاسب وبرمجة",
                "tutors": [
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "price": "300 ريال"},
                    {"name": "مسعد احمد", "contact": "https://t.me/computersciencewithmosaad", "price": "300 ريال"},
                    {"name": "رنا", "contact": "https://t.me/RanaprogrammingNU", "price": "حاسب 250 / برمجة 350"},
                ]
            },
            "math": {
                "title": "📐 رياضيات",
                "tutors": [
                    {"name": "أريام محمد", "contact": "https://t.me/collegeless", "price": "350 ريال"},
                    {"name": "علي محمد", "contact": "https://t.me/najran_math1", "price": "300 ريال"},
                    {"name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "price": "300 ريال"},
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "price": "300-350 ريال"},
                    {"name": "عبدالله اللباد", "contact": "https://t.me/ABDULLAHclass", "price": "250 ريال"},
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "price": "300 ريال"},
                ]
            },
            "english": {
                "title": "🗣️ اللغة الإنجليزية",
                "tutors": [
                    {"name": "يوسف", "contact": "https://t.me/EnglishYusuf", "price": "300 ريال"},
                    {"name": "اسماعيل", "contact": "https://t.me/Abduali445", "price": "400 ريال"},
                    {"name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "price": "350 ريال"},
                    {"name": "وليد", "contact": "https://t.me/Waleed_forEn", "price": "400 ريال (عن بعد وحضوري)"},
                    {"name": "محمود", "contact": "https://t.me/EnglishwithDrMahmoud", "price": "400 ريال"},
                    {"name": "ام مريم", "contact": "https://t.me/M_J_A_k", "price": "500 ريال"},
                ]
            },
        }
    },
    "hasoobi": {
        "title": "💻 المسار الحاسوبي",
        "subjects": {
            "prog": {
                "title": "🖥️ حاسب وبرمجة",
                "tutors": [
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "price": "300 ريال"},
                    {"name": "مسعد احمد", "contact": "https://t.me/computersciencewithmosaad", "price": "300 ريال"},
                    {"name": "رنا", "contact": "https://t.me/RanaprogrammingNU", "price": "حاسب 250 / برمجة 350"},
                ]
            },
            "math": {
                "title": "📐 رياضيات",
                "tutors": [
                    {"name": "أريام محمد", "contact": "https://t.me/collegeless", "price": "350 ريال"},
                    {"name": "علي محمد", "contact": "https://t.me/najran_math1", "price": "300 ريال"},
                    {"name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "price": "300 ريال"},
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "price": "300-350 ريال"},
                    {"name": "عبدالله اللباد", "contact": "https://t.me/ABDULLAHclass", "price": "250 ريال"},
                ]
            },
            "physics": {
                "title": "🔬 فيزياء",
                "tutors": [
                    {"name": "أريام محمد", "contact": "https://t.me/collegeless", "price": "350 ريال"},
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "price": "250 ريال"},
                    {"name": "ام ميار", "contact": "https://t.me/Najranshrohatammyar", "price": "400 ريال"},
                    {"name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "price": "300 ريال"},
                    {"name": "عبداللطيف", "contact": "https://t.me/abdullatifgameel999", "price": "400 ريال"},
                    {"name": "مصطفى", "contact": "https://t.me/gmustafamahmoud", "price": "150 ريال"},
                    {"name": "الصمادي", "contact": "https://t.me/alsmadi2024", "price": "عن بعد 400 / حضوري 800"},
                    {"name": "احمد مكاوي", "contact": "https://t.me/ahmed11_nu", "price": "عن بعد 500 / حضوري 800"},
                ]
            },
            "english": {
                "title": "🗣️ اللغة الإنجليزية",
                "tutors": [
                    {"name": "يوسف", "contact": "https://t.me/EnglishYusuf", "price": "300 ريال"},
                    {"name": "اسماعيل", "contact": "https://t.me/Abduali445", "price": "400 ريال"},
                    {"name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "price": "350 ريال"},
                    {"name": "وليد", "contact": "https://t.me/Waleed_forEn", "price": "400 ريال (عن بعد وحضوري)"},
                    {"name": "محمود", "contact": "https://t.me/EnglishwithDrMahmoud", "price": "400 ريال"},
                    {"name": "ام مريم", "contact": "https://t.me/M_J_A_k", "price": "500 ريال"},
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
    data = query.data

    parts = data.split("|")
    action = parts[0]

    if action == "main_menu":
        keyboard = [
            [InlineKeyboardButton(DATA["sehi"]["title"], callback_data="path|sehi")],
            [InlineKeyboardButton(DATA["handasi"]["title"], callback_data="path|handasi")],
            [InlineKeyboardButton(DATA["hasoobi"]["title"], callback_data="path|hasoobi")],
        ]
        await query.message.edit_text(
            "أهلاً بك 👋\nاختر مسارك عشان تشوف مدرسينه:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif action == "path":
        path_key = parts[1]
        path = DATA[path_key]
        subjects = path["subjects"]

        keyboard = []
        for subj_key, subj in subjects.items():
            keyboard.append([InlineKeyboardButton(subj["title"], callback_data=f"subj|{path_key}|{subj_key}")])
        
        keyboard.append([InlineKeyboardButton("🔙 رجوع للمسارات", callback_data="main_menu")])

        await query.message.edit_text(
            f"{path['title']}\n\nاختر المادة:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif action == "subj":
        path_key, subj_key = parts[1], parts[2]
        subject = DATA[path_key]["subjects"][subj_key]
        tutors = subject["tutors"]

        keyboard = []
        for i, tutor in enumerate(tutors):
            keyboard.append([InlineKeyboardButton(tutor["name"], callback_data=f"tutor|{path_key}|{subj_key}|{i}")])
        
        keyboard.append([InlineKeyboardButton("🔙 رجوع للمواد", callback_data=f"path|{path_key}")])

        await query.message.edit_text(
            f"{subject['title']}\n\nاختر المدرس:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif action == "tutor":
        path_key, subj_key, idx = parts[1], parts[2], int(parts[3])
        tutor = DATA[path_key]["subjects"][subj_key]["tutors"][idx]

        text = (
            f"👤 **{tutor['name']}**\n"
            f"🔗 [رابط القناة]({tutor['contact']})\n"
            f"💰 **{tutor['price']}**"
        )
        
        keyboard = [[InlineKeyboardButton("🔙 رجوع للمدرسين", callback_data=f"subj|{path_key}|{subj_key}")]]
        
        await query.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("البوت شغال...")
    app.run_polling()


if __name__ == "__main__":
    main()
