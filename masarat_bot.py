# -*- coding: utf-8 -*-
"""
بوت مسارات الثلاث (صحي / هندسي / حاسوبي)
مع الروابط، الأسماء، والأرقام والأسعار كاملة
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
                "title": "🖥️ الحاسب والبرمجة",
                "tutors": [
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "phone": "غير متوفر", "price": "300 ريال"},
                    {"name": "مسعد احمد", "contact": "https://t.me/computersciencewithmosaad", "phone": "غير متوفر", "price": "300 ريال"},
                    {"name": "رنا العريقي", "contact": "https://t.me/RanaprogrammingNU", "phone": "@Ra12na_IT", "price": "حاسب 250 ﷼ / برمجة 350 ﷼"},
                    {"name": "رهيب محمد", "contact": "https://t.me/+RlxTlc5FvJ5hZGQ0", "phone": "@Diamond246", "price": "حاسب 199 ﷼ / برمجة 299 ﷼"},
                ]
            },
            "elmi1": {
                "title": "🧪 علمي",
                "tutors": [
                    {"name": "ابراهيم حمدان", "contact": "https://t.me/+q4EoK2tTb8RkZjFk", "phone": "00201028212794", "price": "300 ﷼ (عن بعد)"},
                    {"name": "نجوى الصعيدي", "contact": "https://t.me/+dI3IpHw4bzw5ZjRk", "phone": "0020/1035231781", "price": "400 ﷼ (عن بعد)"},
                    {"name": "احمد محمد", "contact": "https://t.me/drAhmed135", "phone": "@Ahmed124201", "price": "100 ﷼ (عن بعد)"},
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "350 ﷼"},
                    {"name": "ام ميار", "contact": "https://t.me/Najranshrohatammyar", "phone": "+966538135853", "price": "300 ﷼ (عن بعد)"},
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "phone": "غير متوفر", "price": "300 ريال"},
                    {"name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "phone": "غير متوفر", "price": "350 ريال"},
                    {"name": "احمد مكاوي", "contact": "https://t.me/ahmed11_nu", "phone": "0501381714", "price": "عن بعد 500 / حضوري 800"},
                    {"name": "مصطفى", "contact": "https://t.me/gmustafamahmoud", "phone": "غير متوفر", "price": "150 ريال"},
                    {"name": "علي محمد", "contact": "https://t.me/najran_math1", "phone": "غير متوفر", "price": "300 ريال"},
                    {"name": "الصمادي", "contact": "https://t.me/alsmadi2024", "phone": "غير متوفر", "price": "عن بعد 400 / حضوري 800"},
                ]
            },
            "physics": {
                "title": "🔬 فيزياء",
                "tutors": [
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "400 ﷼"},
                    {"name": "ام ميار", "contact": "https://t.me/Najranshrohatammyar", "phone": "+966538135853", "price": "300 ﷼ (عن بعد)"},
                    {"name": "أريام محمد", "contact": "https://t.me/collegeless", "phone": "غير متوفر", "price": "350 ريال"},
                    {"name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "phone": "0531461336", "price": "300 ريال"},
                    {"name": "عبداللطيف", "contact": "https://t.me/abdullatifgameel999", "phone": "غير متوفر", "price": "400 ريال"},
                ]
            },
            "english": {
                "title": "🗣️ اللغة الإنجليزية",
                "tutors": [
                    {"name": "ابو مهند", "contact": "https://t.me/+dunRnAL3ZEc0Njc0", "phone": "0508787470", "price": "400 ﷼ (عن بعد)"},
                    {"name": "اسماعيل", "contact": "https://t.me/Abduali445", "phone": "@Abduali44", "price": "400 ﷼"},
                    {"name": "احمد محمد", "contact": "https://t.me/drAhmed135", "phone": "@Ahmed124201", "price": "100 ﷼ (عن بعد)"},
                    {"name": "يوسف", "contact": "https://t.me/EnglishYusuf", "phone": "0540972198", "price": "300 ريال"},
                    {"name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "phone": "غير متوفر", "price": "350 ريال"},
                    {"name": "وليد", "contact": "https://t.me/Waleed_forEn", "phone": "غير متوفر", "price": "400 ريال (عن بعد وحضوري)"},
                    {"name": "محمود", "contact": "https://t.me/EnglishwithDrMahmoud", "phone": "0553408926", "price": "400 ريال"},
                    {"name": "ام مريم", "contact": "https://t.me/M_J_A_k", "phone": "0596502573", "price": "500 ريال"},
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
                    {"name": "ام جنات", "contact": "https://t.me/OmjannattCisvsvnjrn", "phone": "@Srrrr70A", "price": "400 ﷼ (عن بعد)"},
                    {"name": "مصطفى محمود", "contact": "https://t.me/gmustafamahmoud", "phone": "@EngUncle_lolm", "price": "300 ﷼ (عن بعد)"},
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "400 ﷼"},
                    {"name": "ام ميار", "contact": "https://t.me/Najranshrohatammyar", "phone": "+966538135853", "price": "300 ﷼ (عن بعد)"},
                    {"name": "أريام محمد", "contact": "https://t.me/collegeless", "phone": "غير متوفر", "price": "350 ريال"},
                    {"name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "phone": "0531461336", "price": "300 ريال"},
                    {"name": "عبداللطيف", "contact": "https://t.me/abdullatifgameel999", "phone": "غير متوفر", "price": "400 ريال"},
                    {"name": "الصمادي", "contact": "https://t.me/alsmadi2024", "phone": "غير متوفر", "price": "عن بعد 400 / حضوري 800"},
                    {"name": "احمد مكاوي", "contact": "https://t.me/ahmed11_nu", "phone": "0501381714", "price": "عن بعد 500 / حضوري 800"},
                ]
            },
            "math": {
                "title": "📐 رياضيات",
                "tutors": [
                    {"name": "ام جنات", "contact": "https://t.me/OmjannattCisvsvnjrn", "phone": "@Srrrr70A", "price": "400 ﷼ (عن بعد)"},
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "400 ﷼"},
                    {"name": "أريام محمد", "contact": "https://t.me/collegeless", "phone": "غير متوفر", "price": "350 ريال"},
                    {"name": "علي محمد", "contact": "https://t.me/najran_math1", "phone": "غير متوفر", "price": "300 ريال"},
                    {"name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "phone": "0531461336", "price": "300 ريال"},
                    {"name": "عبدالله اللباد", "contact": "https://t.me/ABDULLAHclass", "phone": "غير متوفر", "price": "250 ريال"},
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "phone": "غير متوفر", "price": "300 ريال"},
                ]
            },
            "elmi": {
                "title": "🧪 علمي",
                "tutors": [
                    {"name": "ابراهيم حمدان", "contact": "https://t.me/+q4EoK2tTb8RkZjFk", "phone": "00201028212794", "price": "300 ﷼ (عن بعد)"},
                ]
            },
            "prog": {
                "title": "🖥️ حاسب وبرمجة",
                "tutors": [
                    {"name": "أدهم وليد", "contact": "https://t.me/+fsBhyLBmkCs3MTFk", "phone": "0543646583", "price": "300 ﷼ (عن بعد)"},
                    {"name": "رهيب محمد", "contact": "https://t.me/+RlxTlc5FvJ5hZGQ0", "phone": "@Diamond246", "price": "حاسب 199 ﷼ / برمجة 299 ﷼"},
                    {"name": "رنا العريقي", "contact": "https://t.me/RanaprogrammingNU", "phone": "@Ra12na_IT", "price": "حاسب 250 ﷼ / برمجة 350 ﷼"},
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "phone": "غير متوفر", "price": "300 ريال"},
                    {"name": "مسعد احمد", "contact": "https://t.me/computersciencewithmosaad", "phone": "غير متوفر", "price": "300 ريال"},
                ]
            },
            "english": {
                "title": "🗣️ اللغة الإنجليزية",
                "tutors": [
                    {"name": "ابو مهند", "contact": "https://t.me/+dunRnAL3ZEc0Njc0", "phone": "0508787470", "price": "400 ﷼ (عن بعد)"},
                    {"name": "اسماعيل", "contact": "https://t.me/Abduali445", "phone": "@Abduali44", "price": "400 ﷼"},
                    {"name": "يوسف", "contact": "https://t.me/EnglishYusuf", "phone": "0540972198", "price": "300 ريال"},
                    {"name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "phone": "غير متوفر", "price": "350 ريال"},
                    {"name": "وليد", "contact": "https://t.me/Waleed_forEn", "phone": "غير متوفر", "price": "400 ريال (عن بعد وحضوري)"},
                    {"name": "محمود", "contact": "https://t.me/EnglishwithDrMahmoud", "phone": "0553408926", "price": "400 ريال"},
                    {"name": "ام مريم", "contact": "https://t.me/M_J_A_k", "phone": "0596502573", "price": "500 ريال"},
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
                    {"name": "أدهم وليد", "contact": "https://t.me/+fsBhyLBmkCs3MTFk", "phone": "0543646583", "price": "300 ﷼ (عن بعد)"},
                    {"name": "رهيب محمد", "contact": "https://t.me/+RlxTlc5FvJ5hZGQ0", "phone": "@Diamond246", "price": "حاسب 199 ﷼ / برمجة 299 ﷼"},
                    {"name": "رنا العريقي", "contact": "https://t.me/RanaprogrammingNU", "phone": "@Ra12na_IT", "price": "حاسب 250 ﷼ / برمجة 350 ﷼"},
                    {"name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "phone": "غير متوفر", "price": "300 ريال"},
                    {"name": "مسعد احمد", "contact": "https://t.me/computersciencewithmosaad", "phone": "غير متوفر", "price": "300 ريال"},
                ]
            },
            "math": {
                "title": "📐 رياضيات",
                "tutors": [
                    {"name": "ام جنات", "contact": "https://t.me/OmjannattCisvsvnjrn", "phone": "@Srrrr70A", "price": "400 ﷼ (عن بعد)"},
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "400 ﷼"},
                    {"name": "أريام محمد", "contact": "https://t.me/collegeless", "phone": "غير متوفر", "price": "350 ريال"},
                    {"name": "علي محمد", "contact": "https://t.me/najran_math1", "phone": "غير متوفر", "price": "300 ريال"},
                    {"name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "phone": "0531461336", "price": "300 ريال"},
                    {"name": "عبدالله اللباد", "contact": "https://t.me/ABDULLAHclass", "phone": "غير متوفر", "price": "250 ريال"},
                ]
            },
            "physics": {
                "title": "🔬 فيزياء",
                "tutors": [
                    {"name": "ام جنات", "contact": "https://t.me/OmjannattCisvsvnjrn", "phone": "@Srrrr70A", "price": "400 ﷼ (عن بعد)"},
                    {"name": "يوسف محمد", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "250 ريال"},
                    {"name": "ام ميار", "contact": "https://t.me/Najranshrohatammyar", "phone": "+966538135853", "price": "400 ريال"},
                    {"name": "أريام محمد", "contact": "https://t.me/collegeless", "phone": "غير متوفر", "price": "350 ريال"},
                    {"name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "phone": "0531461336", "price": "300 ريال"},
                    {"name": "عبداللطيف", "contact": "https://t.me/abdullatifgameel999", "phone": "غير متوفر", "price": "400 ريال"},
                    {"name": "مصطفى", "contact": "https://t.me/gmustafamahmoud", "phone": "غير متوفر", "price": "150 ريال"},
                    {"name": "الصمادي", "contact": "https://t.me/alsmadi2024", "phone": "غير متوفر", "price": "عن بعد 400 / حضوري 800"},
                    {"name": "احمد مكاوي", "contact": "https://t.me/ahmed11_nu", "phone": "0501381714", "price": "عن بعد 500 / حضوري 800"},
                ]
            },
            "english": {
                "title": "🗣️ اللغة الإنجليزية",
                "tutors": [
                    {"name": "ابو مهند", "contact": "https://t.me/+dunRnAL3ZEc0Njc0", "phone": "0508787470", "price": "400 ﷼ (عن بعد)"},
                    {"name": "اسماعيل", "contact": "https://t.me/Abduali445", "phone": "@Abduali44", "price": "400 ﷼"},
                    {"name": "يوسف", "contact": "https://t.me/EnglishYusuf", "phone": "0540972198", "price": "300 ريال"},
                    {"name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "phone": "غير متوفر", "price": "350 ريال"},
                    {"name": "وليد", "contact": "https://t.me/Waleed_forEn", "phone": "غير متوفر", "price": "400 ريال (عن بعد وحضوري)"},
                    {"name": "محمود", "contact": "https://t.me/EnglishwithDrMahmoud", "phone": "0553408926", "price": "400 ريال"},
                    {"name": "ام مريم", "contact": "https://t.me/M_J_A_k", "phone": "0596502573", "price": "500 ريال"},
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
            f"📞 **الهاتف / واتساب:** {tutor['phone']}\n"
            f"💰 **السعر:** {tutor['price']}"
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
