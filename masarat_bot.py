# -*- coding: utf-8 -*-
"""
بوت مسارات الثلاث (صحي / هندسي / حاسوبي)
نسخة نهائية مصححة (تم حل مشكلة طول الـ callback_data لجميع الأزرار)
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ============ التوكن ============
TOKEN = "8880859850:AAF8h52qAVKv-tFL5EeeT-SR5bVFcEvm0TM"

# ============ قاعدة بيانات المدرسين مع معرفات قصيرة جداً لتجنب قيود تليجرام ============
DATA = {
    "sehi": {
        "title": "🩺 المسار الصحي",
        "subjects": {
            "comp": {
                "title": "🖥️ الحاسب والبرمجة",
                "tutors": [
                    {"id": "s_comp_1", "name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "phone": "غير متوفر", "price": "300 ريال"},
                    {"id": "s_comp_2", "name": "مسعد احمد", "contact": "https://t.me/computersciencewithmosaad", "phone": "غير متوفر", "price": "300 ريال"},
                    {"id": "s_comp_3", "name": "رنا العريقي ✅", "contact": "حاسب: https://t.me/RanaprogrammingNU\nبرمجة: https://t.me/+fMaCNdKHOlo1OTE0", "phone": "@Ra12na_IT", "price": "حاسب 250 ﷼ / برمجة 350 ﷼"},
                    {"id": "s_comp_4", "name": "رهيب محمد ✅", "contact": "https://t.me/+RlxTlc5FvJ5hZGQ0", "phone": "@Diamond246", "price": "حاسب 199 ﷼ / برمجة 299 ﷼"},
                ]
            },
            "elmi1": {
                "title": "🧪 علمي",
                "tutors": [
                    {"id": "s_el1_1", "name": "ابراهيم حمدان ✅", "contact": "https://t.me/+q4EoK2tTb8RkZjFk", "phone": "00201028212794", "price": "300 ﷼ (عن بعد)"},
                    {"id": "s_el1_2", "name": "نجوى الصعيدي ✅", "contact": "https://t.me/+dI3IpHw4bzw5ZjRk", "phone": "0020/1035231781", "price": "400 ﷼ (عن بعد)"},
                    {"id": "s_el1_3", "name": "احمد محمد ✅", "contact": "https://t.me/drAhmed135", "phone": "@Ahmed124201", "price": "100 ﷼ (عن بعد)"},
                    {"id": "s_el1_4", "name": "يوسف محمد ✅", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "350 ﷼"},
                    {"id": "s_el1_5", "name": "ام ميار ✅", "contact": "https://t.me/Najranshrohatammyar", "phone": "+966538135853", "price": "300 ﷼ (عن بعد)"},
                    {"id": "s_el1_6", "name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "phone": "غير متوفر", "price": "300 ريال"},
                    {"id": "s_el1_7", "name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "phone": "غير متوفر", "price": "350 ريال"},
                    {"id": "s_el1_8", "name": "احمد مكاوي", "contact": "https://t.me/ahmed11_nu", "phone": "0501381714", "price": "عن بعد 500 / حضوري 800"},
                    {"id": "s_el1_9", "name": "مصطفى محمود ✅", "contact": "https://t.me/gmustafamahmoud", "phone": "@EngUncle_lolm", "price": "150 ريال"},
                    {"id": "s_el1_10", "name": "علي محمد", "contact": "https://t.me/najran_math1", "phone": "غير متوفر", "price": "300 ريال"},
                    {"id": "s_el1_11", "name": "الصمادي", "contact": "https://t.me/alsmadi2024", "phone": "غير متوفر", "price": "عن بعد 400 / حضوري 800"},
                ]
            },
            "physics": {
                "title": "🔬 فيزياء",
                "tutors": [
                    {"id": "s_ph_1", "name": "يوسف محمد ✅", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "400 ﷼"},
                    {"id": "s_ph_2", "name": "ام ميار ✅", "contact": "https://t.me/Najranshrohatammyar", "phone": "+966538135853", "price": "300 ﷼ (عن بعد)"},
                    {"id": "s_ph_3", "name": "أريام محمد", "contact": "https://t.me/collegeless", "phone": "غير متوفر", "price": "350 ريال"},
                    {"id": "s_ph_4", "name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "phone": "0531461336", "price": "300 ريال"},
                    {"id": "s_ph_5", "name": "عبداللطيف", "contact": "https://t.me/abdullatifgameel999", "phone": "غير متوفر", "price": "400 ريال"},
                ]
            },
            "english": {
                "title": "🗣️ اللغة الإنجليزية",
                "tutors": [
                    {"id": "s_en_1", "name": "ابو مهند ✅", "contact": "https://t.me/+dunRnAL3ZEc0Njc0", "phone": "0508787470", "price": "400 ﷼ (عن بعد)"},
                    {"id": "s_en_2", "name": "اسماعيل ✅", "contact": "https://t.me/Abduali445", "phone": "@Abduali44", "price": "400 ﷼"},
                    {"id": "s_en_3", "name": "احمد محمد ✅", "contact": "https://t.me/drAhmed135", "phone": "@Ahmed124201", "price": "100 ﷼ (عن بعد)"},
                    {"id": "s_en_4", "name": "يوسف", "contact": "https://t.me/EnglishYusuf", "phone": "0540972198", "price": "300 ريال"},
                    {"id": "s_en_5", "name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "phone": "غير متوفر", "price": "350 ريال"},
                    {"id": "s_en_6", "name": "وليد", "contact": "https://t.me/Waleed_forEn", "phone": "غير متوفر", "price": "400 ريال (عن بعد وحضوري)"},
                    {"id": "s_en_7", "name": "محمود", "contact": "https://t.me/EnglishwithDrMahmoud", "phone": "0553408926", "price": "400 ريال"},
                    {"id": "s_en_8", "name": "ام مريم", "contact": "https://t.me/M_J_A_k", "phone": "0596502573", "price": "500 ريال"},
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
                    {"id": "h_ph_1", "name": "ام جنات ✅", "contact": "https://t.me/OmjannattCisvsvnjrn", "phone": "@Srrrr70A", "price": "400 ﷼ (عن بعد)"},
                    {"id": "h_ph_2", "name": "مصطفى محمود ✅", "contact": "https://t.me/gmustafamahmoud", "phone": "@EngUncle_lolm", "price": "300 ﷼ (عن بعد)"},
                    {"id": "h_ph_3", "name": "يوسف محمد ✅", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "400 ﷼"},
                    {"id": "h_ph_4", "name": "ام ميار ✅", "contact": "https://t.me/Najranshrohatammyar", "phone": "+966538135853", "price": "300 ﷼ (عن بعد)"},
                    {"id": "h_ph_5", "name": "أريام محمد", "contact": "https://t.me/collegeless", "phone": "غير متوفر", "price": "350 ريال"},
                    {"id": "h_ph_6", "name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "phone": "0531461336", "price": "300 ريال"},
                    {"id": "h_ph_7", "name": "عبداللطيف", "contact": "https://t.me/abdullatifgameel999", "phone": "غير متوفر", "price": "400 ريال"},
                    {"id": "h_ph_8", "name": "الصمادي", "contact": "https://t.me/alsmadi2024", "phone": "غير متوفر", "price": "عن بعد 400 / حضوري 800"},
                    {"id": "h_ph_9", "name": "احمد مكاوي", "contact": "https://t.me/ahmed11_nu", "phone": "0501381714", "price": "عن بعد 500 / حضوري 800"},
                ]
            },
            "math": {
                "title": "📐 رياضيات",
                "tutors": [
                    {"id": "h_ma_1", "name": "ام جنات ✅", "contact": "https://t.me/OmjannattCisvsvnjrn", "phone": "@Srrrr70A", "price": "400 ﷼ (عن بعد)"},
                    {"id": "h_ma_2", "name": "يوسف محمد ✅", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "400 ﷼"},
                    {"id": "h_ma_3", "name": "أريام محمد", "contact": "https://t.me/collegeless", "phone": "غير متوفر", "price": "350 ريال"},
                    {"id": "h_ma_4", "name": "علي محمد", "contact": "https://t.me/najran_math1", "phone": "غير متوفر", "price": "300 ريال"},
                    {"id": "h_ma_5", "name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "phone": "0531461336", "price": "300 ريال"},
                    {"id": "h_ma_6", "name": "عبدالله اللباد", "contact": "https://t.me/ABDULLAHclass", "phone": "غير متوفر", "price": "250 ريال"},
                    {"id": "h_ma_7", "name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "phone": "غير متوفر", "price": "300 ريال"},
                ]
            },
            "elmi": {
                "title": "🧪 علمي",
                "tutors": [
                    {"id": "h_el_1", "name": "ابراهيم حمدان ✅", "contact": "https://t.me/+q4EoK2tTb8RkZjFk", "phone": "00201028212794", "price": "300 ﷼ (عن بعد)"},
                ]
            },
            "prog": {
                "title": "🖥️ حاسب وبرمجة",
                "tutors": [
                    {"id": "h_pr_1", "name": "أدهم وليد ✅", "contact": "https://t.me/+fsBhyLBmkCs3MTFk", "phone": "0543646583", "price": "300 ﷼ (عن بعد)"},
                    {"id": "h_pr_2", "name": "رهيب محمد ✅", "contact": "https://t.me/+RlxTlc5FvJ5hZGQ0", "phone": "@Diamond246", "price": "حاسب 199 ﷼ / برمجة 299 ﷼"},
                    {"id": "h_pr_3", "name": "رنا العريقي ✅", "contact": "حاسب: https://t.me/RanaprogrammingNU\nبرمجة: https://t.me/+fMaCNdKHOlo1OTE0", "phone": "@Ra12na_IT", "price": "حاسب 250 ﷼ / برمجة 350 ﷼"},
                    {"id": "h_pr_4", "name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "phone": "غير متوفر", "price": "300 ريال"},
                    {"id": "h_pr_5", "name": "مسعد احمد", "contact": "https://t.me/computersciencewithmosaad", "phone": "غير متوفر", "price": "300 ريال"},
                ]
            },
            "english": {
                "title": "🗣️ اللغة الإنجليزية",
                "tutors": [
                    {"id": "h_en_1", "name": "ابو مهند ✅", "contact": "https://t.me/+dunRnAL3ZEc0Njc0", "phone": "0508787470", "price": "400 ﷼ (عن بعد)"},
                    {"id": "h_en_2", "name": "اسماعيل ✅", "contact": "https://t.me/Abduali445", "phone": "@Abduali44", "price": "400 ﷼"},
                    {"id": "h_en_3", "name": "يوسف", "contact": "https://t.me/EnglishYusuf", "phone": "0540972198", "price": "300 ريال"},
                    {"id": "h_en_4", "name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "phone": "غير متوفر", "price": "350 ريال"},
                    {"id": "h_en_5", "name": "وليد", "contact": "https://t.me/Waleed_forEn", "phone": "غير متوفر", "price": "400 ريال (عن بعد وحضوري)"},
                    {"id": "h_en_6", "name": "محمود", "contact": "https://t.me/EnglishwithDrMahmoud", "phone": "0553408926", "price": "400 ريال"},
                    {"id": "h_en_7", "name": "ام مريم", "contact": "https://t.me/M_J_A_k", "phone": "0596502573", "price": "500 ريال"},
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
                    {"id": "c_pr_1", "name": "أدهم وليد ✅", "contact": "https://t.me/+fsBhyLBmkCs3MTFk", "phone": "0543646583", "price": "300 ﷼ (عن بعد)"},
                    {"id": "c_pr_2", "name": "رهيب محمد ✅", "contact": "https://t.me/+RlxTlc5FvJ5hZGQ0", "phone": "@Diamond246", "price": "حاسب 199 ﷼ / برمجة 299 ﷼"},
                    {"id": "c_pr_3", "name": "رنا العريقي ✅", "contact": "حاسب: https://t.me/RanaprogrammingNU\nبرمجة: https://t.me/+fMaCNdKHOlo1OTE0", "phone": "@Ra12na_IT", "price": "حاسب 250 ﷼ / برمجة 350 ﷼"},
                    {"id": "c_pr_4", "name": "محمد الجنيدي", "contact": "https://t.me/njph80ysical", "phone": "غير متوفر", "price": "300 ريال"},
                    {"id": "c_pr_5", "name": "مسعد احمد", "contact": "https://t.me/computersciencewithmosaad", "phone": "غير متوفر", "price": "300 ريال"},
                ]
            },
            "math": {
                "title": "📐 رياضيات",
                "tutors": [
                    {"id": "c_ma_1", "name": "ام جنات ✅", "contact": "https://t.me/OmjannattCisvsvnjrn", "phone": "@Srrrr70A", "price": "400 ﷼ (عن بعد)"},
                    {"id": "c_ma_2", "name": "يوسف محمد ✅", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "400 ﷼"},
                    {"id": "c_ma_3", "name": "أريام محمد", "contact": "https://t.me/collegeless", "phone": "غير متوفر", "price": "350 ريال"},
                    {"id": "c_ma_4", "name": "علي محمد", "contact": "https://t.me/najran_math1", "phone": "غير متوفر", "price": "300 ريال"},
                    {"id": "c_ma_5", "name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "phone": "0531461336", "price": "300 ريال"},
                    {"id": "c_ma_6", "name": "عبدالله اللباد", "contact": "https://t.me/ABDULLAHclass", "phone": "غير متوفر", "price": "250 ريال"},
                ]
            },
            "physics": {
                "title": "🔬 فيزياء",
                "tutors": [
                    {"id": "c_ph_1", "name": "ام جنات ✅", "contact": "https://t.me/OmjannattCisvsvnjrn", "phone": "@Srrrr70A", "price": "400 ﷼ (عن بعد)"},
                    {"id": "c_ph_2", "name": "يوسف محمد ✅", "contact": "https://t.me/Preparatory_withYusuf", "phone": "0593812861", "price": "250 ريال"},
                    {"id": "c_ph_3", "name": "ام ميار ✅", "contact": "https://t.me/Najranshrohatammyar", "phone": "+966538135853", "price": "400 ريال"},
                    {"id": "c_ph_4", "name": "أريام محمد", "contact": "https://t.me/collegeless", "phone": "غير متوفر", "price": "350 ريال"},
                    {"id": "c_ph_5", "name": "اشرف رضوان", "contact": "https://t.me/DrAshraf20", "phone": "0531461336", "price": "300 ريال"},
                    {"id": "c_ph_6", "name": "عبداللطيف", "contact": "https://t.me/abdullatifgameel999", "phone": "غير متوفر", "price": "400 ريال"},
                    {"id": "c_ph_7", "name": "مصطفى محمود ✅", "contact": "https://t.me/gmustafamahmoud", "phone": "@EngUncle_lolm", "price": "150 ريال"},
                    {"id": "c_ph_8", "name": "الصمادي", "contact": "https://t.me/alsmadi2024", "phone": "غير متوفر", "price": "عن بعد 400 / حضوري 800"},
                    {"id": "c_ph_9", "name": "احمد مكاوي", "contact": "https://t.me/ahmed11_nu", "phone": "0501381714", "price": "عن بعد 500 / حضوري 800"},
                ]
            },
            "english": {
                "title": "🗣️ اللغة الإنجليزية",
                "tutors": [
                    {"id": "c_en_1", "name": "ابو مهند ✅", "contact": "https://t.me/+dunRnAL3ZEc0Njc0", "phone": "0508787470", "price": "400 ﷼ (عن بعد)"},
                    {"id": "c_en_2", "name": "اسماعيل ✅", "contact": "https://t.me/Abduali445", "phone": "@Abduali44", "price": "400 ﷼"},
                    {"id": "c_en_3", "name": "يوسف", "contact": "https://t.me/EnglishYusuf", "phone": "0540972198", "price": "300 ريال"},
                    {"id": "c_en_4", "name": "يارا الماوردي", "contact": "https://t.me/nagraantagreeby", "phone": "غير متوفر", "price": "350 ريال"},
                    {"id": "c_en_5", "name": "وليد", "contact": "https://t.me/Waleed_forEn", "phone": "غير متوفر", "price": "400 ريال (عن بعد وحضوري)"},
                    {"id": "c_en_6", "name": "محمود", "contact": "https://t.me/EnglishwithDrMahmoud", "phone": "0553408926", "price": "400 ريال"},
                    {"id": "c_en_7", "name": "ام مريم", "contact": "https://t.me/M_J_A_k", "phone": "0596502573", "price": "500 ريال"},
                ]
            },
        }
    },
}

WELCOME_MESSAGE = (
    "أهلاً بك 👋\n"
    "اختر مسارك عشان تشوف مدرسينه:\n\n"
    "ملاحظة: الخصوصيين المعلّم عليهم بـ ✅ قد تم التواصل معهم والتحقق من بياناتهم واعتمادهم."
)


# ============ دالة البحث عن المدرس بواسطة الـ id ============
def find_tutor_by_id(tutor_id):
    for path_key, path_data in DATA.items():
        for subj_key, subj_data in path_data["subjects"].items():
            for tutor in subj_data["tutors"]:
                if tutor["id"] == tutor_id:
                    return tutor, path_key, subj_key
    return None, None, None


# ============ الأوامر والأحداث ============

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(DATA["sehi"]["title"], callback_data="path_sehi")],
        [InlineKeyboardButton(DATA["handasi"]["title"], callback_data="path_handasi")],
        [InlineKeyboardButton(DATA["hasoobi"]["title"], callback_data="path_hasoobi")],
    ]
    await update.message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "main_menu":
        keyboard = [
            [InlineKeyboardButton(DATA["sehi"]["title"], callback_data="path_sehi")],
            [InlineKeyboardButton(DATA["handasi"]["title"], callback_data="path_handasi")],
            [InlineKeyboardButton(DATA["hasoobi"]["title"], callback_data="path_hasoobi")],
        ]
        await query.message.edit_text(
            WELCOME_MESSAGE,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data.startswith("path_"):
        path_key = data.split("_")[1]
        path = DATA[path_key]
        subjects = path["subjects"]

        keyboard = []
        for subj_key, subj in subjects.items():
            keyboard.append([InlineKeyboardButton(subj["title"], callback_data=f"subj_{path_key}_{subj_key}")])
        
        keyboard.append([InlineKeyboardButton("🔙 رجوع للمسارات", callback_data="main_menu")])

        await query.message.edit_text(
            f"{path['title']}\n\nاختر المادة:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data.startswith("subj_"):
        parts = data.split("_")
        path_key, subj_key = parts[1], parts[2]
        subject = DATA[path_key]["subjects"][subj_key]
        tutors = subject["tutors"]

        keyboard = []
        for tutor in tutors:
            keyboard.append([InlineKeyboardButton(tutor["name"], callback_data=f"tutor_{tutor['id']}")])
        
        keyboard.append([InlineKeyboardButton("🔙 رجوع للمواد", callback_data=f"path_{path_key}")])

        await query.message.edit_text(
            f"{subject['title']}\n\nاختر المدرس:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data.startswith("tutor_"):
        tutor_id = data.replace("tutor_", "", 1)
        tutor, path_key, subj_key = find_tutor_by_id(tutor_id)

        if not tutor:
            await query.message.edit_text("عذراً، لم يتم العثور على بيانات المدرس.")
            return

        text = (
            f"👤 **{tutor['name']}**\n"
            f"🔗 **رابط القناة:**\n{tutor['contact']}\n"
            f"📞 **الهاتف / التواصل:** {tutor['phone']}\n"
            f"💰 **السعر:** {tutor['price']}"
        )
        
        keyboard = [[InlineKeyboardButton("🔙 رجوع للمدرسين", callback_data=f"subj_{path_key}_{subj_key}")]]
        
        await query.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("البوت شغال...")
    app.run_polling()


if __name__ == "__main__":
    main()
