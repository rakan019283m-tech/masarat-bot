import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# ----------------- القوائم الرئيسية -----------------

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎓 الكليات والقروبات", callback_data="colleges_menu"),
         InlineKeyboardButton("شروط الاستمرار", callback_data="gpa_conditions")],
        [InlineKeyboardButton("🏢 السكن الجامعي", callback_data="housing_menu"),
         InlineKeyboardButton("📝 الحركات الأكاديمية", callback_data="academic_menu")],
        [InlineKeyboardButton("🏥 المستشفى الجامعي", callback_data="hospital_menu"),
         InlineKeyboardButton("📅 التقويم الجامعي", url="https://t.me/Najran1_NU/1553668")],
        [InlineKeyboardButton("📊 نسب القبول", url="https://t.me/Najran1_NU/1555365"),
         InlineKeyboardButton("📋 شروط القبول", callback_data="admission_guide")],
        [InlineKeyboardButton("📋 خطط التخصصات", callback_data="study_plans_menu")],
        [InlineKeyboardButton("⭐ مراتب الشرف", url="https://t.me/Najran1_NU/1553663"),
         InlineKeyboardButton("🗺️ أرقام المباني", url="https://t.me/Najran1_NU/1553674")],
        [InlineKeyboardButton("📞 أرقام التواصل والمسؤولين", url="https://t.me/Najran1_NU/1553665"),
         InlineKeyboardButton("🔗 روابط مهمة", callback_data="important_links")],
        [InlineKeyboardButton("📢 قناة جامعة نجران", url="https://t.me/Najran_channel")]
    ]
    return InlineKeyboardMarkup(keyboard)

# ----------------- قوائم الكليات والتخصصات -----------------

def colleges_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🩺 الكليات الصحية", callback_data="health_colleges"),
         InlineKeyboardButton("⚙️ كلية الهندسة", callback_data="eng_colleges")],
        [InlineKeyboardButton("💻 الحاسب وعلوم المعلومات", callback_data="cs_college"),
         InlineKeyboardButton("⚖️ الشريعة وأصول الدين", callback_data="sharia_college")],
        [InlineKeyboardButton("📊 الكلية التطبيقية (دبلومات)", callback_data="applied_college"),
         InlineKeyboardButton("💼 إدارة الأعمال والأنظمة", callback_data="business_college")],
        [InlineKeyboardButton("🏛️ كليه اداره الأعمال", callback_data="admsci_college")],
        [InlineKeyboardButton("📖 كلية التربية", url="https://t.me/education_NU"),
         InlineKeyboardButton("🗣️ اللغات والترجمة", url="https://t.me/Najran_Translation")],
        [InlineKeyboardButton("🧪 العلوم والآداب", url="https://t.me/Arts_sciencesNU")],
        [InlineKeyboardButton("📖 الجامعة الإلكترونية", url="https://t.me/Saudi_EUnu"),
         InlineKeyboardButton("🎓 الدراسات العليا", url="https://t.me/DpgsNU")],
        [InlineKeyboardButton("🏆 قناة الشهادات الإحترافية", url="https://t.me/NUprofcert_channel"),
         InlineKeyboardButton("👥 قروب الشهادات الإحترافية", url="https://t.me/NUprofcert")],
        [InlineKeyboardButton("📚 تبادل كتب", url="https://t.me/book_exchangeNU"),
         InlineKeyboardButton("🎯 مبادرات ودورات جامعة نجران", url="https://t.me/NajranUniEvents")],
        [InlineKeyboardButton("📢 قنوات الجامعة", url="https://t.me/Najran1_NU/1524031")],
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
        [InlineKeyboardButton("مساري الصحي", url="https://t.me/HealthyPathNu")],
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
        [InlineKeyboardButton("مساري الهندسي", url="https://t.me/EngineeringPathNu")],
        [InlineKeyboardButton("قروب كليه الهندسه", url="https://t.me/NajranEng")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def cs_keyboard():
    keyboard = [
        [InlineKeyboardButton("علوم الحاسب ونظم المعلومات", url="https://t.me/cscis_NU")],
        [InlineKeyboardButton("مساري الحاسوبي", url="https://t.me/ComputerPathNu")],
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
        [InlineKeyboardButton("قروب كليه التطبيقيه", url="https://t.me/AppliedNU")],
        [InlineKeyboardButton("محاسبة دبلوم", url="https://t.me/appliedaccountingNu")],
        [InlineKeyboardButton("ادارة اعمال دبلوم", url="https://t.me/NUBAdiploma")],
        [InlineKeyboardButton("دعم فني دبلوم", url="https://t.me/NAJRANnu")],
        [InlineKeyboardButton("ادارة الابتكار وريادة الاعمال دبلوم", url="https://t.me/najran288")],
        [InlineKeyboardButton("برمجة وقواعد البيانات دبلوم", url="https://t.me/Nu_121")],
        [InlineKeyboardButton("ذكاء الاعمال وتحليل البيانات دبلوم", url="https://t.me/zcq52")],
        [InlineKeyboardButton("التسويق التطبيقي دبلوم", url="https://t.me/+ij6m8sT76N41NGI0")],
        [InlineKeyboardButton("نظم المعلومات", url="https://t.me/+ypdmQZXamzE4NzU0")],
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

def admsci_keyboard():
    keyboard = [
        [InlineKeyboardButton("قروبات تخصصات الاداره", url="https://t.me/admsci")],
        [InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="colleges_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# ----------------- قوائم خطط التخصصات -----------------

def study_plans_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("⚙️ المسار الهندسي", callback_data="plan_eng"),
         InlineKeyboardButton("🩺 المسار الصحي", callback_data="plan_health")],
        [InlineKeyboardButton("💼 إدارة الأعمال", callback_data="plan_biz"),
         InlineKeyboardButton("📊 الكلية التطبيقية", callback_data="plan_applied")],
        [InlineKeyboardButton("🗣️ اللغات والترجمة", callback_data="plan_langs"),
         InlineKeyboardButton("🧪 العلوم والآداب", callback_data="plan_arts")],
        [InlineKeyboardButton("💻 علوم الحاسب ونظم المعلومات", callback_data="plan_cs")],
        [InlineKeyboardButton("🛤️ المسارات التحضيرية", callback_data="plan_paths")],
        [InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def plan_eng_keyboard():
    keyboard = [
        [InlineKeyboardButton("خطة الهندسة المعمارية", url="https://t.me/NuPlans/8")],
        [InlineKeyboardButton("خطة الهندسة الميكانيكية", url="https://t.me/NuPlans/9")],
        [InlineKeyboardButton("خطة الهندسة الكيميائية", url="https://t.me/NuPlans/10")],
        [InlineKeyboardButton("خطة الهندسة الكهربائية", url="https://t.me/NuPlans/19")],
        [InlineKeyboardButton("خطة الهندسة المدنية", url="https://t.me/NuPlans/20")],
        [InlineKeyboardButton("خطة التصميم الداخلي", url="https://t.me/NuPlans/21")],
        [InlineKeyboardButton("⬅️ رجوع للخطط", callback_data="study_plans_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def plan_health_keyboard():
    keyboard = [
        [InlineKeyboardButton("خطة دكتور صيدلي", url="https://t.me/NuPlans/23")],
        [InlineKeyboardButton("خطة علوم مختبرات", url="https://t.me/NuPlans/24")],
        [InlineKeyboardButton("خطة طب الأسنان", url="https://t.me/NuPlans/25")],
        [InlineKeyboardButton("خطة الطب", url="https://t.me/NuPlans/26")],
        [InlineKeyboardButton("خطة الأشعة التشخيصية", url="https://t.me/NuPlans/27")],
        [InlineKeyboardButton("خطة التمريض", url="https://t.me/NuPlans/28")],
        [InlineKeyboardButton("خطة العلاج الطبيعي", url="https://t.me/NuPlans/29")],
        [InlineKeyboardButton("⬅️ رجوع للخطط", callback_data="study_plans_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def plan_biz_keyboard():
    keyboard = [
        [InlineKeyboardButton("التسويق والتجارة الالكترونية", url="https://t.me/NuPlans/31")],
        [InlineKeyboardButton("ادارة الموارد البشرية", url="https://t.me/NuPlans/32")],
        [InlineKeyboardButton("الأنظمة (قانون)", url="https://t.me/NuPlans/33")],
        [InlineKeyboardButton("المحاسبة", url="https://t.me/NuPlans/34")],
        [InlineKeyboardButton("إدارة اعمال", url="https://t.me/NuPlans/35")],
        [InlineKeyboardButton("⬅️ رجوع للخطط", callback_data="study_plans_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def plan_applied_keyboard():
    keyboard = [
        [InlineKeyboardButton("محاسبة", url="https://t.me/NuPlans/37")],
        [InlineKeyboardButton("دعم فني", url="https://t.me/NuPlans/38")],
        [InlineKeyboardButton("ادارة اعمال", url="https://t.me/NuPlans/39")],
        [InlineKeyboardButton("البرمجة وقواعد بيانات", url="https://t.me/NuPlans/40")],
        [InlineKeyboardButton("نظم معلومات", url="https://t.me/NuPlans/41")],
        [InlineKeyboardButton("إدارة الابتكار وريادة الأعمال", url="https://t.me/NuPlans/42")],
        [InlineKeyboardButton("التسويق التطبيقي", url="https://t.me/NuPlans/44")],
        [InlineKeyboardButton("⬅️ رجوع للخطط", callback_data="study_plans_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def plan_langs_keyboard():
    keyboard = [
        [InlineKeyboardButton("الترجمة", url="https://t.me/NuPlans/46")],
        [InlineKeyboardButton("اللغة الإنجليزية", url="https://t.me/NuPlans/47")],
        [InlineKeyboardButton("⬅️ رجوع للخطط", callback_data="study_plans_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def plan_arts_keyboard():
    keyboard = [
        [InlineKeyboardButton("فيزياء", url="https://t.me/NuPlans/49")],
        [InlineKeyboardButton("احياء", url="https://t.me/NuPlans/50")],
        [InlineKeyboardButton("كيمياء", url="https://t.me/NuPlans/51")],
        [InlineKeyboardButton("رياضيات", url="https://t.me/NuPlans/52")],
        [InlineKeyboardButton("رياضيات المالية والاكتوارية", url="https://t.me/NuPlans/53")],
        [InlineKeyboardButton("الاحصاء التطبيقي", url="https://t.me/NuPlans/54")],
        [InlineKeyboardButton("اللغه العربيه", url="https://t.me/NuPlans/55")],
        [InlineKeyboardButton("⬅️ رجوع للخطط", callback_data="study_plans_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def plan_cs_keyboard():
    keyboard = [
        [InlineKeyboardButton("شبكات الحاسب والإتصالات", url="https://t.me/NuPlans/60")],
        [InlineKeyboardButton("نظم معلومات", url="https://t.me/NuPlans/61")],
        [InlineKeyboardButton("علوم الحاسب", url="https://t.me/NuPlans/66")],
        [InlineKeyboardButton("⬅️ رجوع للخطط", callback_data="study_plans_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def plan_paths_keyboard():
    keyboard = [
        [InlineKeyboardButton("المسار الصحي", url="https://t.me/NuPlans/68")],
        [InlineKeyboardButton("المسار الحاسوبي", url="https://t.me/NuPlans/69")],
        [InlineKeyboardButton("المسار الهندسي", url="https://t.me/NuPlans/70")],
        [InlineKeyboardButton("⬅️ رجوع للخطط", callback_data="study_plans_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

# ----------------- القوائم الفرعية -----------------

def housing_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🏠 سكن الطلاب", callback_data="housing_boys"),
         InlineKeyboardButton("👩‍🎓 سكن الطالبات", callback_data="housing_girls")],
        [InlineKeyboardButton("📜 شروط السكن", callback_data="housing_conditions")],
        [InlineKeyboardButton("🔗 قروب السكن", url="https://t.me/NajranUniversity_housing")],
        [InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def academic_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("طريقة الانسحاب", callback_data="withdraw"),
         InlineKeyboardButton("طريقة الاعتذار", callback_data="apology")],
        [InlineKeyboardButton("🔄 إعادة القيد للمنقطع", callback_data="re_enroll"),
         InlineKeyboardButton("📈 احتساب المعدل المتوقع", callback_data="expected_gpa")],
        [InlineKeyboardButton("⏳ تأجيل الفصل الدراسي", callback_data="postpone"),
         InlineKeyboardButton("🚶‍♂️ الطلبة الزائرون", callback_data="visitor")],
        [InlineKeyboardButton("⚖️ الفرق بين التأجيل والاعتذار", callback_data="diff")],
        [InlineKeyboardButton("📚 توصيف المقرر", callback_data="course_desc")],
        [InlineKeyboardButton("📋 خطط التخصصات", callback_data="study_plans_menu")],
        [InlineKeyboardButton("🔄 نظام وتحويل الكليات", url="https://t.me/Najran1_NU/1553671")],
        [InlineKeyboardButton("📊 التقديرات", url="https://t.me/Najran1_NU/1553731"),
         InlineKeyboardButton("⚠️ انقطاع المكافأة", callback_data="reward_stop")],
        [InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def important_links_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎓 البلاك بورد", url="https://lms.nu.edu.sa/")],
        [InlineKeyboardButton("🌐 البوابة الإلكترونية", url="https://edugate.nu.edu.sa/nu/init")],
        [InlineKeyboardButton("✉️ الإيميل الجامعي", callback_data="university_email")],
        [InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def admission_guide_keyboard():
    keyboard = [
        [InlineKeyboardButton("📊 توزيع النسب", url="https://t.me/Najran1_NU/1553739")],
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

    # خطط التخصصات
    elif data == "study_plans_menu":
        await query.edit_message_text("📋 اختر الكلية أو المسار لعرض خطط التخصصات:", reply_markup=study_plans_menu_keyboard())
    elif data == "plan_eng":
        await query.edit_message_text("⚙️ خطط تخصصات المسار الهندسي:", reply_markup=plan_eng_keyboard())
    elif data == "plan_health":
        await query.edit_message_text("🩺 خطط تخصصات المسار الصحي:", reply_markup=plan_health_keyboard())
    elif data == "plan_biz":
        await query.edit_message_text("💼 خطط تخصصات إدارة الأعمال:", reply_markup=plan_biz_keyboard())
    elif data == "plan_applied":
        await query.edit_message_text("📊 خطط تخصصات الكلية التطبيقية:", reply_markup=plan_applied_keyboard())
    elif data == "plan_langs":
        await query.edit_message_text("🗣️ خطط تخصصات كلية اللغات والترجمة:", reply_markup=plan_langs_keyboard())
    elif data == "plan_arts":
        await query.edit_message_text("🧪 خطط تخصصات كلية العلوم والآداب:", reply_markup=plan_arts_keyboard())
    elif data == "plan_cs":
        await query.edit_message_text("💻 خطط تخصصات علوم الحاسب ونظم المعلومات:", reply_markup=plan_cs_keyboard())
    elif data == "plan_paths":
        await query.edit_message_text("🛤️ خطط تخصصات المسارات التحضيرية:", reply_markup=plan_paths_keyboard())

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
    elif data == "admsci_college":
        await query.edit_message_text("🏛️ كليه اداره الأعمال:", reply_markup=admsci_keyboard())

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
    elif data == "housing_conditions":
        text = (
            "أن تكون المسافة بين مقر إقامة الطالب / الطالبة ومقر الإسكان الطلابي (80) كيلومترا فأكثر.\n\n"
            "أن تكون المسافة بين مقر الثانوية العامة التي درس فيها الطالب / الطالبة ومقر الإسكان الطلابي (80) كيلومترا فأكثر.\n\n"
            "احضار صورة واضحة من شهادة الثانوية العامة للتحقق من مقر الجهة التعليمية المانحة للشهادة ومدى استيفاء شرط المسافة المعتمد.\n\n"
            "في حالة ثبوت عدم استيفاء شرط المسافة، يُستبعد طلب الطالب / الطالبة من إجراءات الفرز والمفاضلة على السكن الطلابي، مع اتخاذ ما يلزم وفق الأنظمة واللوائح المعتمدة."
        )
        await query.edit_message_text(text, reply_markup=housing_menu_keyboard())

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
    elif data == "re_enroll":
        text = (
            "🔄 **إعادة القيد للمنقطع:**\n\n"
            "يحق للطالب المنقطع أو المنسحب التقدم بطلب إعادة القيد عبر البوابة الإلكترونية للعودة إلى نفس تجميعه ومستواه الأكاديمي ضمن المدة النظامية."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "expected_gpa":
        text = (
            "📈 **احتساب المعدل المتوقع:**\n\n"
            "يمكنك من خلال هذه الخدمة حساب معدلك الفصلي والتراكمي المتوقع بناءً على الدرجات والساعات المتوقعة عبر البوابة الأكاديمية."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "postpone":
        text = (
            "⏳ **تأجيل الفصل الدراسي:**\n\n"
            "• موعد التقديم: قبل بدء الدراسة.\n"
            "• آلية الاحتساب: غير محسوب ضمن المدة الدراسية ولا يدخل ضمن المكافآت.\n"
            "• طريقة التقديم: إلكترونياً عبر البوابة الأكاديمية."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "visitor":
        text = (
            "🚶‍♂️ **الطلبة الزائرون:**\n\n"
            "يتاح للطالب دراسة مقررات في جامعة أخرى أو فرع آخر وفق شروط محددة وموافقة القسم العلمي عبر البوابة الأكاديمية."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "diff":
        text = (
            "⚖️ **الفرق بين التأجيل والاعتذار:**\n\n"
            "• **التأجيل:** يطلب قبل الفصل، لا يُحسب من المدة، ولا يقطع المكافأة.\n"
            "• **الاعتذار:** يطلب خلال الفصل، يُحسب من المدة الدراسية، ويؤثر على المكافأة بحسب اللائحة."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "reward_stop":
        text = (
            "🔺 حالات انقطاع المكافأة:\n"
            "- عند انخفاض المعدل التراكمي 1.99 فأقل.\n"
            "- عند الانسحاب أو تأجيل الفصل الدراسي.\n"
            "- عند طيّ القيد\n"
            "- عند تجاوز الخطة \n"
            "- عند صدور قرار تأديبي بحق الطالب.؜"
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "course_desc":
        text = (
            "🔺 لإظهار توصيف المقرر :\n"
            "https://www.nu.edu.sa/\n"
            "ادخل الموقع هنا \n"
            "> الثلاث الشرطات \n"
            "> الكليات \n"
            "> تختار الكلية \n"
            "> اذا كانت لها اكثر من تخصص \n"
            "> تختار التخصص \n"
            "> برنامج \n"
            "> توصيف المقرر ㅤ؜؜؜"
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard())

    # روابط مهمة
    elif data == "important_links":
        await query.edit_message_text("🔗 الروابط المهمة والأنظمة الإلكترونية:", reply_markup=important_links_keyboard())
    elif data == "university_email":
        text = (
            "👥جميع طلاب وطالبات جامعة نجران لديهم إيميل جامعي بصيغة:\n"
            "الرقم الجامعي @nu.edu.sa\n"
            "مثال:\n"
            "123456789@nu.edu.sa\n\n"
            "🔒كلمة المرور:\n"
            "هي نفسها كلمة مرور الدخول على البوابة الإلكترونية.\n\n"
            "✅ طريقة التفعيل:\n"
            "عند الضغط على إضافة حساب وإكمال البيانات المطلوبة، يتم تفعيل الإيميل مباشرة.\n\n"
            "👤 الدخول على الإيميل:\n"
            "عن طريق موقع Outlook ✉️\n\n"
            "📋 ملاحظة:\n"
            "تفعيل الإيميل الجامعي ضروري لاستقبال وإرسال الرسائل مع دكاترة المقررات والإدارة. ㅤ ㅤ؜"
        )
        await query.edit_message_text(text, reply_markup=important_links_keyboard())

    # شروط القبول العامة
    elif data == "admission_guide":
        text = (
            "📋 **شروط القبول العامة بجامعة نجران:**\n\n"
            "توضيح كامل للشروط والمعايير الخاصة بالقبول في برامج البكالوريوس والدبلوم عبر بوابة العمادة."
        )
        await query.edit_message_text(text, reply_markup=admission_guide_keyboard(), parse_mode="Markdown")

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

    # شروط الاستمرار بعد السنة المشتركة
    elif data == "gpa_conditions":
        text = (
            "📈 **شروط الإكمال في البرنامج بعد اجتياز السنة المشتركة:**\n\n"
            "**أولاً:** الحصول على معدل تراكمي يتيح للطالب الاستمرار في البرنامج، وفق التفصيل أدناه:\n"
            "• الحصول على معدل 4.25 فأعلى للإكمال على تخصص الطب والجراحة.\n"
            "• الحصول على معدل تراكمي 3.75 فأعلى للإكمال على تخصص طب الأسنان.\n"
            "• الحصول على معدل 3.25 فأعلى للإكمال على تخصص دكتور صيدلي.\n"
            "• الحصول على معدل تراكمي 3.25 فأعلى للإكمال على التمريض.\n"
            "• الحصول على معدل 3 فأعلى للإكمال على تخصصات كلية العلوم الطبية التطبيقية.\n"
            "• الحصول على معدل 3.25 فأعلى للإكمال على تخصصات كلية علوم الحاسب ونظم المعلومات.\n"
            "• الحصول على معدل 3 فأعلى للإكمال على تخصصات كلية الهندسة.\n"
            "(شرط المعدل التراكمي بعد اجتياز المسار)\n\n"
            "**ثانياً:** يجوز النزول عن المعدلات المشار إليها أعلاه في حال توفر مقاعد شاغرة.\n\n"
            "**ثالثاً:** إذا لم يحقق الطالب الحد الأدنى لمعدل الاستمرار في البرنامج، فيتاح له التحويل إلى أحد البرامج ضمن المسار ذاته، شريطة استيفاء شرط المعدل المحدد لذلك البرنامج، وتوفر مقاعد شاغرة فيه.\n\n"
            "**رابعاً:** في حال عدم توفر مقاعد شاغرة في أيّ من برامج المسار، يُحوّل الطالب إلى أحد برامج البكالوريوس التي لا تتطلب السنة المشتركة، أو إلى أحد برامج الدبلوم، وذلك وفقاً للمقاعد المتاحة."
        )
        await query.edit_message_text(text, reply_markup=back_to_main_keyboard(), parse_mode="Markdown")

def main():
    TOKEN = "8722924986:AAEVU_oqQDYFs6LG18D-A0VJJfr9Ry2Jyr0"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("🤖 البوت يعمل بكامل التحديثات الأخيرة...")
    app.run_polling()

if __name__ == "__main__":
    main()
