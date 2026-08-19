import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# ----------------- القوائم الرئيسية -----------------

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎓 الكليات والقروبات", callback_data="colleges_menu"),
         InlineKeyboardButton("📈 شروط المعدل", callback_data="gpa_conditions")],
        [InlineKeyboardButton("🏢 السكن الجامعي", callback_data="housing_menu"),
         InlineKeyboardButton("📝 الحركات الأكاديمية", callback_data="academic_menu")],
        [InlineKeyboardButton("🏥 المستشفى الجامعي", callback_data="hospital_menu"),
         InlineKeyboardButton("📅 التقويم الجامعي", callback_data="calendar")],
        [InlineKeyboardButton("⭐ مراتب الشرف", callback_data="honors"),
         InlineKeyboardButton("🗺️ أرقام المباني", callback_data="buildings")],
        [InlineKeyboardButton("🔄 نظام وتحويل الكليات", callback_data="transfer_system"),
         InlineKeyboardButton("📋 شروط القبول", callback_data="admission_guide")],
        [InlineKeyboardButton("📞 أرقام التواصل والمسؤولين", callback_data="contacts_guide"),
         InlineKeyboardButton("📚 توصيف المقرر", callback_data="course_desc")],
        [InlineKeyboardButton("📢 القناة الرسمية", url="https://t.me/NAJRAN1_NU")]
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

def cs_keyboard():
    keyboard = [
        [InlineKeyboardButton("علوم الحاسب ونظم المعلومات", url="https://t.me/cscis_NU")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def sharia_keyboard():
    keyboard = [
        [InlineKeyboardButton("شريعه", url="https://t.me/nuedu6")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

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

# ----------------- القوائم الفرعية -----------------

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
        [InlineKeyboardButton("🔄 إعادة القيد للمنقطع", callback_data="re_enroll_img"),
         InlineKeyboardButton("📈 احتساب المعدل المتوقع", callback_data="expected_gpa_img")],
        [InlineKeyboardButton("⏳ تأجيل الفصل الدراسي", callback_data="postpone_img"),
         InlineKeyboardButton("🚶‍♂️ الطلبة الزائرون", callback_data="visitor_img")],
        [InlineKeyboardButton("⚖️ الفرق بين التأجيل والاعتذار", callback_data="diff_img")],
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
            "⚠️ **طريقة الاعتذار عن فصل أو مقرر:**\n\n"
            "• موعد التقديم: متاح حتى قبل الاختبارات النهائية بخمسة أسابيع.\n"
            "• آلية الاحتساب: محسوب ضمن المدة الدراسية والمكافآت.\n"
            "• طريقة التقديم: البوابة الإلكترونية ⬅️ الطلبات الأكاديمية ⬅️ الحركات الأكاديمية ⬅️ نوع الحركة: اعتذار."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    
    # الحركات الأكاديمية مع إرسال الصورة والشرح النصي معاً
    elif data == "re_enroll_img":
        caption_text = "🔄 **إعادة القيد للمنقطع:**\nيحق للطالب المنقطع أو المنسحب التقدم بطلب إعادة القيد عبر البوابة الإلكترونية للعودة إلى نفس تجميعه ومستواه الأكاديمي ضمن المدة النظامية."
        await query.message.reply_photo(photo="AgACAgQAAxkBAAIC...re_enroll", caption=caption_text, parse_mode="Markdown")
        await query.message.reply_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())
    elif data == "expected_gpa_img":
        caption_text = "📈 **احتساب المعدل المتوقع:**\nيمكنك من خلال هذه الخدمة حساب معدلك الفصلي والتراكمي المتوقع بناءً على الدرجات والساعات المتوقعة."
        await query.message.reply_photo(photo="AgACAgQAAxkBAAIC...gpa", caption=caption_text, parse_mode="Markdown")
        await query.message.reply_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())
    elif data == "postpone_img":
        caption_text = "⏳ **تأجيل الفصل الدراسي:**\n• موعد التقديم: قبل بدء الدراسة.\n• آلية الاحتساب: غير محسوب ضمن المدة الدراسية ولا يدخل ضمن المكافآت.\n• طريقة التقديم: إلكترونياً عبر البوابة الأكاديمية."
        await query.message.reply_photo(photo="AgACAgQAAxkBAAIC...postpone", caption=caption_text, parse_mode="Markdown")
        await query.message.reply_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())
    elif data == "visitor_img":
        caption_text = "🚶‍♂️ **الطلبة الزائرون:**\nيتاح للطالب دراسة مقررات في جامعة أخرى أو فرع آخر وفق شروط محددة وموافقة القسم العلمي عبر البوابة الأكاديمية."
        await query.message.reply_photo(photo="AgACAgQAAxkBAAIC...visitor", caption=caption_text, parse_mode="Markdown")
        await query.message.reply_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())
    elif data == "diff_img":
        caption_text = "⚖️ **الفرق بين التأجيل والاعتذار:**\nمقارنة رسمية توضح الفروقات الكاملة من حيث مدة الدراسة، المكافآت، ومواعيد التقديم."
        await query.message.reply_photo(photo="AgACAgQAAxkBAAIC...diff", caption=caption_text, parse_mode="Markdown")
        await query.message.reply_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())

    # مراتب الشرف
    elif data == "honors":
        caption_text = "⭐ **شروط وتفاصيل مراتب الشرف:**\nتمنح مرتبة الشرف الأولى أو الثانية بناءً على المعدل التراكمي واجتياز الساعات المحددة."
        await query.message.reply_photo(photo="AgACAgQAAxkBAAIC...honors", caption=caption_text, parse_mode="Markdown")
        await query.message.reply_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())

    # شروط القبول العامة
    elif data == "admission_guide":
        caption_text = "📋 **شروط القبول العامة بجامعة نجران:**\nتوضيح كامل للشروط والمعايير الخاصة بالقبول في برامج البكالوريوس والدبلوم."
        await query.message.reply_photo(photo="AgACAgQAAxkBAAIC...admission", caption=caption_text, parse_mode="Markdown")
        await query.message.reply_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())

    # أرقام المباني
    elif data == "buildings":
        caption_text = "🗺️ **دليل أرقام ومواقع المباني بجامعة نجران:**\nدليل إرشادي يوضح أرقام جميع المباني بالمدينة الجامعية من 1 إلى 75."
        await query.message.reply_photo(photo="AgACAgQAAxkBAAIC...buildings", caption=caption_text, parse_mode="Markdown")
        await query.message.reply_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())

    # التقويم الجامعي
    elif data == "calendar":
        caption_text = "📅 **التقويم الجامعي:**\nيوضح مواعيد بداية ونهاية الفصل الدراسي، الإجازات، وفترات الحذف والإضافة والاختبارات."
        await query.message.reply_photo(photo="AgACAgQAAxkBAAIC...calendar", caption=caption_text, parse_mode="Markdown")
        await query.message.reply_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())

    # نظام التحويل بين الكليات
    elif data == "transfer_system":
        text = (
            "🔄 **نظام التحويل بين الكليات والتخصصات:**\n\n"
            "• التحويل متاح إلكترونياً عبر البوابة الأكاديمية.\n"
            "• يشترط تحقيق المعدل المطلوب للتخصص المراد التحويل إليه.\n"
            "• توافر مقاعد شاغرة في التخصص.\n"
            "• الالتزام بالمواعيد المحددة للتحويل في التقويم الجامعي.\n"
            "• عند التحويل من تخصص أدبي لعلمي يُشترط أن تكون الثانوية علمية."
        )
        await query.edit_message_text(text, reply_markup=back_to_main_keyboard(), parse_mode="Markdown")

    # أرقام التواصل والمسؤولين (ملف PDF)
    elif data == "contacts_guide":
        await query.message.reply_document(document="BQACAgQAAxkBAAIC...contacts_pdf", caption="📞 دليل أرقام التواصل والمسؤولين بعمادة القبول والتسجيل")
        await query.message.reply_text("القائمة الرئيسية:", reply_markup=main_menu_keyboard())

    # المستشفى الجامعي
    elif data == "hospital_menu":
        text = (
            "🏥 **المستشفى الجامعي:**\n\n"
            "☎️ التقارير الطبية والاستفسارات.\n"
            "💼 حجز ومتابعة المواعيد: 0175416322\n"
            "📞 لطلب فتح ملف جديد: +966 17 541 6304\n\n"
            "📋 **المتطلبات:** صورة الهوية، البطاقة الجامعية، العنوان السكني، توكلنا."
        )
        await query.edit_message_text(text, reply_markup=back_to_main_keyboard(), parse_mode="Markdown")

    # شرط المعدل بعد السنة المشتركة
    elif data == "gpa_conditions":
        text = (
            "📈 **شرط المعدل بعد السنة المشتركة:**\n\n"
            "• 4.25 فأعلى ← الطب والجراحة\n"
            "• 3.75 فأعلى ← طب الأسنان\n"
            "• 3.25 فأعلى ← دكتور صيدلي والتمريض\n"
            "• 3.25 فأعلى ← علوم الحاسب ونظم المعلومات\n"
            "• 3.00 فأعلى ← الهندسة والعلوم الطبية التطبيقية"
        )
        await query.edit_message_text(text, reply_markup=back_to_main_keyboard(), parse_mode="Markdown")

    # توصيف المقرر
    elif data == "course_desc":
        text = (
            "📚 **طريقة إظهار توصيف المقرر:**\n\n"
            "موقع الجامعة ⬅️ الثلاث شخطات ⬅️ الكليات ⬅️ الكلية والتخصص ⬅️ برنامج ⬅️ توصيف المقرر."
        )
        await query.edit_message_text(text, reply_markup=back_to_main_keyboard(), parse_mode="Markdown")

    elif data == "no_link":
        await query.answer("عذراً، هذا التخصص ليس له رابط حالياً.", show_alert=True)

def main():
    TOKEN = "8722924986:AAEVU_oqQDYFs6LG18D-A0VJJfr9Ry2Jyr0"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("🤖 البوت يعمل بكامل الأقسام والصور والشرح النصي المدمج...")
    app.run_polling()

if __name__ == "__main__":
    main()
