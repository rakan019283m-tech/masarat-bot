# ----------------- القوائم الرئيسية (تم تحديث الرابط) -----------------

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎓 الكليات والقروبات", callback_data="colleges_menu"),
         InlineKeyboardButton("📈 شروط المعدل", callback_data="gpa_conditions")],
        [InlineKeyboardButton("🏢 السكن الجامعي", callback_data="housing_menu"),
         InlineKeyboardButton("📝 الحركات الأكاديمية", callback_data="academic_menu")],
        [InlineKeyboardButton("🏥 المستشفى الجامعي", callback_data="hospital_menu"),
         InlineKeyboardButton("📅 التقويم الجامعي", url="https://t.me/Najran1_NU/1553668")],
        [InlineKeyboardButton("📊 نسب القبول", url="https://t.me/Najran1_NU/1555365"),
         InlineKeyboardButton("📋 شروط القبول", callback_data="admission_guide")],
        [InlineKeyboardButton("⭐ مراتب الشرف", url="https://t.me/Najran1_NU/1553663"),
         InlineKeyboardButton("🗺️ أرقام المباني", url="https://t.me/Najran1_NU/1553674")],
        [InlineKeyboardButton("📞 أرقام التواصل والمسؤولين", url="https://t.me/Najran1_NU/1553665"),
         InlineKeyboardButton("🔗 روابط مهمة", callback_data="important_links")],
        [InlineKeyboardButton("📢 قناة جامعة نجران", url="https://t.me/Najran_channel")]
    ]
    return InlineKeyboardMarkup(keyboard)
