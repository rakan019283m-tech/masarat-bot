import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

# تفعيل تسجيل الأخطاء
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ----------------- القوائم والأزرار -----------------

# القائمة الرئيسية
def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🎓 الكليات والتخصصات", callback_data="colleges"),
            InlineKeyboardButton(
                "📢 قناة القناة الرسمية", url="https://t.me/NAJRAN1_NU"
            ),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


# قائمة الكليات الرئيسية
def colleges_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🩺 الكليات الصحية", callback_data="health_colleges"),
            InlineKeyboardButton(
                "⚙️ كلية الهندسة", callback_data="engineering_college"
            ),
        ],
        [
            InlineKeyboardButton(
                "💻 الحاسب وعلوم المعلومات", callback_data="cs_college"
            ),
            InlineKeyboardButton("⚖️ الشريعة وأصول الدين", callback_data="sharia_college"),
        ],
        [
            InlineKeyboardButton("📊 الكلية التطبيقية (دبلومات)", callback_data="applied_college"),
            InlineKeyboardButton("💼 إدارة الأعمال والأنظمة", callback_data="business_college"),
        ],
        [InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")],
    ]
    return InlineKeyboardMarkup(keyboard)


# 1. الكليات الصحية
def health_colleges_keyboard():
    keyboard = [
        [InlineKeyboardButton("الطب", url="https://t.me/Najranmed")],
        [InlineKeyboardButton("طب الأسنان", url="https://t.me/DentistryNu1")],
        [InlineKeyboardButton("التمريض", url="https://t.me/najran_Rn")],
        [InlineKeyboardButton("الصيدلة", url="https://t.me/NU_Pharmacy")],
        [InlineKeyboardButton("المختبرات الإكلينيكية", url="https://t.me/Ky5nvumgDnEyMTk0")],
        [InlineKeyboardButton("الأشعة التشخيصية", url="https://t.me/radiology154")],
        [InlineKeyboardButton("العلاج الطبيعي", url="https://t.me/UN_Physicaltherapy")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges")],
    ]
    return InlineKeyboardMarkup(keyboard)


# 2. كلية الهندسة
def engineering_keyboard():
    keyboard = [
        [InlineKeyboardButton("الهندسة الميكانيكية", url="https://t.me/Eng_Najran/4605")],
        [InlineKeyboardButton("الهندسة المدنية", url="https://t.me/Eng_Najran/4602")],
        [InlineKeyboardButton("العمارة", url="https://t.me/Eng_Najran/4586")],
        [InlineKeyboardButton("التصميم الداخلي", url="https://t.me/Eng_Najran/49819")],
        [InlineKeyboardButton("الهندسة الكهربائية", url="https://t.me/Eng_Najran/4604")],
        [InlineKeyboardButton("الهندسة الكيميائية", url="https://t.me/Eng_Najran/4603")],
        [InlineKeyboardButton("هندسة الميكاترونيكس", url="https://t.me/Eng_Najran/56657")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges")],
    ]
    return InlineKeyboardMarkup(keyboard)


# 3. الحاسب وعلوم المعلومات
def cs_keyboard():
    keyboard = [
        [InlineKeyboardButton("علوم الحاسب ونظم المعلومات", url="https://t.me/cscis_NU")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges")],
    ]
    return InlineKeyboardMarkup(keyboard)


# 4. الشريعة
def sharia_keyboard():
    keyboard = [
        [InlineKeyboardButton("شريعة", url="https://t.me/nuedu6")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges")],
    ]
    return InlineKeyboardMarkup(keyboard)


# 5. الكلية التطبيقية (دبلومات)
def applied_keyboard():
    keyboard = [
        [InlineKeyboardButton("محاسبة (دبلوم)", url="https://t.me/appliedaccountingNu")],
        [InlineKeyboardButton("إدارة أعمال (دبلوم)", url="https://t.me/NUBAdiploma")],
        [InlineKeyboardButton("دعم فني (دبلوم)", url="https://t.me/NAJRANnu")],
        [InlineKeyboardButton("إدارة الابتكار وريادة الأعمال (دبلوم)", url="https://t.me/najran288")],
        [InlineKeyboardButton("التسويق التطبيقي", callback_data="no_link")],
        [InlineKeyboardButton("برمجة وقواعد البيانات (دبلوم)", url="https://t.me/Nu_121")],
        [InlineKeyboardButton("نظم المعلومات (دبلوم)", callback_data="no_link")],
        [InlineKeyboardButton("ذكاء الأعمال وتحليل البيانات (دبلوم)", url="https://t.me/zcq52")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges")],
    ]
    return InlineKeyboardMarkup(keyboard)


# 6. إدارة الأعمال والأنظمة
def business_keyboard():
    keyboard = [
        [InlineKeyboardButton("إدارة الأعمال", callback_data="no_link")],
        [InlineKeyboardButton("الأنظمة (القانون)", callback_data="no_link")],
        [InlineKeyboardButton("المحاسبة", callback_data="no_link")],
        [InlineKeyboardButton("التسويق والتجارة الإلكترونية", callback_data="no_link")],
        [InlineKeyboardButton("الموارد البشرية", callback_data="no_link")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges")],
    ]
    return InlineKeyboardMarkup(keyboard)


# ----------------- الدوال والأوامر -----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"أهلاً بك يا {user_name} في بوت خدمات طلاب جامعة نجران 🎓\n\n"
        "اختر القسم المناسب لتنتقل إلى قروب التخصص مباشرة:"
    )
    if update.message:
        await update.message.reply_text(welcome_text, reply_markup=main_menu_keyboard())
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(welcome_text, reply_markup=main_menu_keyboard())


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "main_menu":
        await query.edit_message_text(
            "القائمة الرئيسية:", reply_markup=main_menu_keyboard()
        )
    elif data == "colleges":
        await query.edit_message_text(
            "اختر الكلية أو المسار المطلوب:", reply_markup=colleges_keyboard()
        )
    elif data == "health_colleges":
        await query.edit_message_text(
            "🩺 الكليات الصحية (اختر تخصصك):", reply_markup=health_colleges_keyboard()
        )
    elif data == "engineering_college":
        await query.edit_message_text(
            "⚙️ كلية الهندسة (اختر تخصصك):", reply_markup=engineering_keyboard()
        )
    elif data == "cs_college":
        await query.edit_message_text(
            "💻 كلية الحاسب وعلوم المعلومات:", reply_markup=cs_keyboard()
        )
    elif data == "sharia_college":
        await query.edit_message_text(
            "⚖️ كلية الشريعة وأصول الدين:", reply_markup=sharia_keyboard()
        )
    elif data == "applied_college":
        await query.edit_message_text(
            "📊 الكلية التطبيقية والدبلومات:", reply_markup=applied_keyboard()
        )
    elif data == "business_college":
        await query.edit_message_text(
            "💼 إدارة الأعمال والأنظمة:", reply_markup=business_keyboard()
        )
    elif data == "no_link":
        await query.answer(
            "عذراً، رابط هذا التخصص غير متوفر حالياً سيتم إضافته قريباً!",
            show_alert=True,
        )


def main():
    # ضع التوكن الخاص بالبوت الجديد هنا بين العلامتين ('')
    TOKEN = "8722924986:AAEVU_oqQDYFs6LG18D-A0VJJfr9Ry2Jyr0"


    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 البوت يعمل الآن...")
    app.run_polling()


if __name__ == "__main__":
    main()
