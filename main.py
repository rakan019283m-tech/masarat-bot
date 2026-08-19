import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

# تفعيل تسجيل الأخطاء
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# ----------------- القوائم الرئيسية -----------------

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎓 الكليات والتخصصات والقروبات", callback_data="colleges_menu")],
        [InlineKeyboardButton("🏢 السكن الجامعي", callback_data="housing_menu"),
         InlineKeyboardButton("📝 الحركات الأكاديمية", callback_data="academic_menu")],
        [InlineKeyboardButton("⭐ مراتب الشرف", callback_data="honors"),
         InlineKeyboardButton("📧 الإيميل الجامعي", callback_data="university_email")],
        [InlineKeyboardButton("🔗 روابط هامة", callback_data="links_menu"),
         InlineKeyboardButton("📢 القناة الرسمية", url="https://t.me/NAJRAN1_NU")]
    ]
    return InlineKeyboardMarkup(keyboard)

# ----------------- قوائم الكليات والتخصصات -----------------

def colleges_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🩺 الكليات الصحية", callback_data="health_colleges"),
         InlineKeyboardButton("⚙️ كلية الهندسة", callback_data="eng_colleges")],
        [InlineKeyboardButton("💻 الحاسب وعلوم المعلومات", callback_data="cs_college"),
         InlineKeyboardButton("⚖️ الشريعة", callback_data="sharia_college")],
        [InlineKeyboardButton("📊 الكلية التطبيقية (دبلومات)", callback_data="applied_college"),
         InlineKeyboardButton("💼 إدارة الأعمال والأنظمة", callback_data="business_college")],
        [InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# 1. الكليات الصحية
def health_keyboard():
    keyboard = [
        [InlineKeyboardButton("التمريض", url="https://t.me/najran_Rn")],
        [InlineKeyboardButton("طب الأسنان", url="https://t.me/DentistryNu1")],
        [InlineKeyboardButton("الطب", url="https://t.me/Najranmed")],
        [InlineKeyboardButton("الصيدلة", url="https://t.me/NU_Pharmacy")],
        [InlineKeyboardButton("المختبرات الإكلينيكية", url="https://t.me/Ky5nvumgDnEyMTk0")],
        [InlineKeyboardButton("الأشعة التشخيصية", url="https://t.me/radiology154")],
        [InlineKeyboardButton("العلاج الطبيعي", url="https://t.me/UN_Physicaltherapy")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# 2. الهندسة
def eng_keyboard():
    keyboard = [
        [InlineKeyboardButton("الهندسة الميكانيكية", url="https://t.me/Eng_Najran/4605")],
        [InlineKeyboardButton("الهندسة المدنية", url="https://t.me/Eng_Najran/4602")],
        [InlineKeyboardButton("العمارة", url="https://t.me/Eng_Najran/4586")],
        [InlineKeyboardButton("التصميم الداخلي", url="https://t.me/Eng_Najran/49819")],
        [InlineKeyboardButton("الهندسة الكهربائية", url="https://t.me/Eng_Najran/4604")],
        [InlineKeyboardButton("الهندسة الكيميائيه", url="https://t.me/Eng_Najran/4603")],
        [InlineKeyboardButton("هندسة الميكاترونيكس", url="https://t.me/Eng_Najran/56657")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# 3. الحاسب
def cs_keyboard():
    keyboard = [
        [InlineKeyboardButton("علوم الحاسب ونظم المعلومات", url="https://t.me/cscis_NU")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# 4. الشريعة
def sharia_keyboard():
    keyboard = [
        [InlineKeyboardButton("شريعه", url="https://t.me/nuedu6")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# 5. الكلية التطبيقية (دبلوم)
def applied_keyboard():
    keyboard = [
        [InlineKeyboardButton("محاسبة دبلوم", url="https://t.me/appliedaccountingNu")],
        [InlineKeyboardButton("ادارة اعمال دبلوم", url="https://t.me/NUBAdiploma")],
        [InlineKeyboardButton("دعم فني دبلوم", url="https://t.me/NAJRANnu")],
        [InlineKeyboardButton("ادارة الابتكار وريادة الاعمال دبلوم", url="https://t.me/najran288")],
        [InlineKeyboardButton("التسويق التطبيقي (لا يوجد رابط)", callback_data="no_link")],
        [InlineKeyboardButton("برمجة وقواعد البيانات دبلوم", url="https://t.me/Nu_121")],
        [InlineKeyboardButton("نظم المعلومات دبلوم (لا يوجد رابط)", callback_data="no_link")],
        [InlineKeyboardButton("ذكاء الاعمال وتحليل البيانات دبلوم", url="https://t.me/zcq52")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# 6. إدارة الأعمال والأنظمة
def business_keyboard():
    keyboard = [
        [InlineKeyboardButton("إدارة الاعمال", url="https://t.me/Business_NU")],
        [InlineKeyboardButton("الأنظمة (القانون)", url="https://t.me/NU_lawyer")],
        [InlineKeyboardButton("المحاسبه", url="https://t.me/AccountingNU")],
        [InlineKeyboardButton("التسويق والتجاره الالكترونيه", url="https://t.me/MarketingAndCommerce")],
        [InlineKeyboardButton("ادارة الموارد البشريه", url="https://t.me/Najran_HR")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# ----------------- قوائم السكن والحركات الأكاديمية -----------------

def housing_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🏠 سكن الطلاب", callback_data="housing_boys"),
         InlineKeyboardButton("👩‍🎓 سكن الطالبات", callback_data="housing_girls")],
        [InlineKeyboardButton("🔗 قروب السكن", url="https://t.me/NajranUniversity_housing")],
        [InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def academic_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("طريقة الانسحاب", callback_data="withdraw"),
         InlineKeyboardButton("طريقة الاعتذار", callback_data="apology")],
        [InlineKeyboardButton("طلبات اعادة قيد", callback_data="re_enroll"),
         InlineKeyboardButton("تأجيل فصل", callback_data="postpone")],
        [InlineKeyboardButton("طالب زائر", callback_data="visitor")],
        [InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def links_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🔗 رابط البوابة الإلكترونية", url="https://edugate.nu.edu.sa/nu/init"),
         InlineKeyboardButton("🔗 رابط بلاك بورد", url="https://lms.nu.edu.sa/")],
        [InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def back_to_main_keyboard():
    keyboard = [[InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]]
    return InlineKeyboardMarkup(keyboard)

# ----------------- معالجة الأزرار -----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"أهلاً بك يا {user_name} في بوت خدمات طلاب جامعة نجران 🎓\n\n"
        "اختر القسم المطلوب من القائمة أدناه:"
    )
    if update.message:
        await update.message.reply_text(welcome_text, reply_markup=main_menu_keyboard())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "main_menu":
        await query.edit_message_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())

    # الكليات
    elif data == "colleges_menu":
        await query.edit_message_text("اختر القسم أو الكلية:", reply_markup=colleges_menu_keyboard())
    elif data == "health_colleges":
        await query.edit_message_text("🩺 الكليات الصحية:", reply_markup=health_keyboard())
    elif data == "eng_colleges":
        await query.edit_message_text("⚙️ كلية الهندسة:", reply_markup=eng_keyboard())
    elif data == "cs_college":
        await query.edit_message_text("💻 الحاسب وعلوم المعلومات:", reply_markup=cs_keyboard())
    elif data == "sharia_college":
        await query.edit_message_text("⚖️ الشريعة وأصول الدين:", reply_markup=sharia_keyboard())
    elif data == "applied_college":
        await query.edit_message_text("📊 الكلية التطبيقية (الدبلومات):", reply_markup=applied_keyboard())
    elif data == "business_college":
        await query.edit_message_text("💼 إدارة الأعمال والأنظمة:", reply_markup=business_keyboard())

    # السكن
    elif data == "housing_menu":
        await query.edit_message_text("🏢 خدمات السكن الجامعي:", reply_markup=housing_menu_keyboard())
    elif data == "housing_boys":
        text = (
            "⚠️ **تعريف سكن الطلاب:**\n\n"
            "1️⃣ الفردي تم الغاؤه صار ثنائي تدفع 1200 بالترم، الثلاثي بـ 1000 بالترم.\n"
            "2️⃣ الشقة مافيها باب وتكون 4 غرف وحمام ومطبخ مشترك.\n"
            "3️⃣ تضيع مفتاحك غرامة 250، اذا سكرت عليه كلم المشرفين يفتحونه لك.\n"
            "4️⃣ ممنوع التدخين بجميع انواعه داخل المبنى.\n"
            "5️⃣ ممنوع تدخل السكن احد من برا منعًا باتًا.\n"
            "6️⃣ اذا بتجلس مع اخوياك اجلسوا بالصالة ممنوع التجمع بالغرف والإزعاج.\n"
            "7️⃣ ممنوع تأثث الغرفة بأثاث حجمه كبير مثل الكنب.\n"
            "8️⃣ اذا المطبخ كان وصخ يتسكر.\n"
            "9️⃣ الطلوع والدخول اي وقت عادي."
        )
        await query.edit_message_text(text, reply_markup=housing_menu_keyboard(), parse_mode="Markdown")
    elif data == "housing_girls":
        text = (
            "⚠️ **تعريف سكن الطالبات:**\n\n"
            "1️⃣ وقت التسجيل على حسب الاعلان بس غالبًا قبل الدراسة بأسبوع.\n"
            "2️⃣ التسجيل يكون إلكتروني.\n"
            "3️⃣ السكن الجديد نظام سيب وفيه 4 غرف وكل غرفة فيها بنتين (حمام ومطبخ مشترك، لا يوجد فردي).\n"
            "4️⃣ تدفعين 1200 للترم الواحد.\n"
            "5️⃣ تضيعين مفتاح الغرفة غرامة 200 ريال.\n"
            "6️⃣ ما تطلعين الا اذا عندك وكالة للأقارب درجة أولى.\n"
            "+ تقدرين تطلعين للنقل الجماعي والمطار بسائق خاص بوكالة من ولي أمرك."
        )
        await query.edit_message_text(text, reply_markup=housing_menu_keyboard(), parse_mode="Markdown")

    # الحركات الأكاديمية
    elif data == "academic_menu":
        await query.edit_message_text("📝 الحركات الأكاديمية والطلبات:", reply_markup=academic_menu_keyboard())
    elif data == "withdraw":
        text = (
            "⚠️ **طريقة الانسحاب:**\n\n"
            "البوابة الإلكترونية ⬅️ الطلبات الأكاديمية ⬅️ الحركات الأكاديمية ⬅️ إضافة حركة جديدة ⬅️ نوع الحركة: انسحاب.\n\n"
            "⛔ عند الانسحاب لا يمكن التقديم للجامعة مرة أخرى إلا بعد سنتين.\n"
            "⛔ يمكن طلب إعادة القيد خلال هذه المدة والعودة لنفس التخصص والمستوى."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "apology":
        text = (
            "⚠️ **طريقة الاعتذار (عن فصل - مقرر):**\n\n"
            "من البوابة الإلكترونية:\n"
            "• إدخال الطلبات\n"
            "• إدخال أو إظهار الحركات الأكاديمية\n"
            "• إدخال حركة أكاديمية جديدة\n"
            "• نوع الحركة: اعتذار عن (الفصل - مقرر)"
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "re_enroll":
        text = (
            "🔄 **طلبات إعادة قيد:**\n\n"
            "البوابة الإلكترونية ⬅️ إدخال الطلبات ⬅️ إدخال أو إظهار الحركات الأكاديمية ⬅️ طلب إعادة قيد (حفظ)."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "postpone":
        text = (
            "⏸️ **تأجيل فصل:**\n\n"
            "البوابة الإلكترونية ⬅️ إدخال الطلبات ⬅️ إدخال أو إظهار الحركات الأكاديمية ⬅️ طلب تأجيل ترم (حفظ)."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "visitor":
        text = (
            "🚶‍♂️ **طالب زائر:**\n\n"
            "البوابة الإلكترونية ⬅️ إدخال الطلبات ⬅️ إدخال طلب زائر ⬅️ بعد إدخال الطلب (حفظ)."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")

    # مراتب الشرف
    elif data == "honors":
        text = (
            "⭐ **مراتب الشرف:**\n\n"
            "رابط البوابة الإلكترونية:\nhttps://edugate.nu.edu.sa/nu/init\n\n"
            "رابط بلاك بورد:\nhttps://lms.nu.edu.sa/"
        )
        await query.edit_message_text(text, reply_markup=back_to_main_keyboard())

    # الإيميل الجامعي
    elif data == "university_email":
        text = (
            "👥 **الإيميل الجامعي:**\n\n"
            "جميع طلاب وطالبات جامعة نجران لديهم إيميل جامعي بصيغة:\n"
            "الرقم الجامعي @nu.edu.sa\n"
            "مثال: 123456789@nu.edu.sa\n\n"
            "🔒 **كلمة المرور:**\n"
            "هي نفسها كلمة مرور الدخول على البوابة الإلكترونية.\n\n"
            "✅ **طريقة التفعيل:**\n"
            "عند الضغط على إضافة حساب وإكمال البيانات المطلوبة، يتم تفعيل الإيميل مباشرة.\n\n"
            "👤 **الدخول على الإيميل:**\n"
            "عن طريق موقع Outlook ✉️\n\n"
            "📋 **ملاحظة:**\n"
            "تفعيل الإيميل الجامعي ضروري لاستقبال وإرسال الرسائل مع دكاترة المقررات والإدارة."
        )
        await query.edit_message_text(text, reply_markup=back_to_main_keyboard())

    elif data == "links_menu":
        await query.edit_message_text("🔗 الروابط الهامة:", reply_markup=links_menu_keyboard())

    elif data == "no_link":
        await query.answer("عذراً، هذا التخصص ليس له رابط حالياً.", show_alert=True)

def main():
    TOKEN = "8722924986:AAEVU_oqQDYFs6LG18D-A0VJJfr9Ry2Jyr0"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("🤖 البوت يعمل بكامل البيانات والتخصصات بدقة...")
    app.run_polling()

if __name__ == "__main__":
    main()
