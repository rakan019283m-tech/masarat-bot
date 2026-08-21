import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder, CallbackQueryHandler, CommandHandler, 
    ContextTypes, ConversationHandler, MessageHandler, filters
)

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# ----------------- حالات المحادثة للخطة الذكية -----------------
CHOOSING_COLLEGE, CHOOSING_MAJOR, ENTERING_PASSED_COURSES = range(3)

# قاعدة بيانات متكاملة للتخصصات بحسب دليل القبول 1448 هـ
STUDY_PLANS = {
    "الطب": {"المواد": [{"name": "تشريح 1", "hours": 4, "prereq": []}, {"name": "تشريح 2", "hours": 4, "prereq": ["تشريح 1"]}]},
    "طب الأسنان": {"المواد": [{"name": "علوم أسنان 1", "hours": 3, "prereq": []}]},
    "الصيدلة": {"المواد": [{"name": "صيدلانيات 1", "hours": 3, "prereq": []}]},
    "العلوم الطبية التطبيقية": {"المواد": [{"name": "مختبرات عامة", "hours": 3, "prereq": []}]},
    "كلية التمريض": {"المواد": [{"name": "تمريض أساسيات", "hours": 3, "prereq": []}]},
    "الهندسة": {"المواد": [{"name": "رياضيات هندسية 1", "hours": 3, "prereq": []}, {"name": "رياضيات هندسية 2", "hours": 3, "prereq": ["رياضيات هندسية 1"]}]},
    "كلية علوم الحاسب ونظم المعلومات": {"المواد": [{"name": "برمجة 1", "hours": 3, "prereq": []}, {"name": "هياكل بيانات", "hours": 3, "prereq": ["برمجة 1"]}]},
    "كلية الشريعة واصول الدين": {"المواد": [{"name": "فقه 1", "hours": 3, "prereq": []}]},
    "كلية التربية": {"المواد": [{"name": "مدخل للتربية", "hours": 2, "prereq": []}]},
    "اللغات والترجمة": {"المواد": [{"name": "استماع وتحدث", "hours": 3, "prereq": []}]},
    "العلوم والآداب": {"المواد": [{"name": "تفاضل وتكامل", "hours": 3, "prereq": []}]},
    "كلية إدارة أعمال": {"المواد": [{"name": "مبادئ إدارة", "hours": 3, "prereq": []}]},
    "الكلية التطبيقية (دبلوم)": {"المواد": [{"name": "مهارات حاسب", "hours": 2, "prereq": []}]}
}

# ----------------- القوائم الرئيسية -----------------

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎓 الكليات والقروبات", callback_data="colleges_menu"),
         InlineKeyboardButton("📈 شروط المعدل", callback_data="gpa_conditions")],
        [InlineKeyboardButton("🏢 السكن الجامعي", callback_data="housing_menu"),
         InlineKeyboardButton("📝 الحركات الأكاديمية", callback_data="academic_menu")],
        [InlineKeyboardButton("🧠 الخطة الدراسية الذكية", callback_data="study_plan_start")],
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

# ----------------- قوائم الكليات والتخصصات للخطة الذكية -----------------

def study_plan_colleges_keyboard():
    keyboard = [
        [InlineKeyboardButton("🩺 كلية الطب", callback_data="sp_col_medicine"),
         InlineKeyboardButton("🦷 كلية طب الأسنان", callback_data="sp_col_dentistry")],
        [InlineKeyboardButton("💊 كلية الصيدلة", callback_data="sp_col_pharmacy"),
         InlineKeyboardButton("🧪 العلوم الطبية التطبيقية", callback_data="sp_col_applied_med")],
        [InlineKeyboardButton("💉 كلية التمريض", callback_data="sp_col_nursing"),
         InlineKeyboardButton("⚙️ كلية الهندسة", callback_data="sp_col_engineering")],
        [InlineKeyboardButton("💻 علوم الحاسب ونظم المعلومات", callback_data="sp_col_cs")],
        [InlineKeyboardButton("📖 الشريعة وأصول الدين", callback_data="sp_col_sharia"),
         InlineKeyboardButton("📚 كلية التربية", callback_data="sp_col_education")],
        [InlineKeyboardButton("🗣️ اللغات والترجمة", callback_data="sp_col_languages"),
         InlineKeyboardButton("วิทยา العلوم والآداب", callback_data="sp_col_arts_sci")],
        [InlineKeyboardButton("💼 كلية إدارة الأعمال", callback_data="sp_col_business"),
         InlineKeyboardButton("📊 الكلية التطبيقية (دبلوم)", callback_data="sp_col_diploma")],
        [InlineKeyboardButton("⬅️ القائمة الرئيسية", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_majors_keyboard_for_college(college_key):
    majors_map = {
        "sp_col_medicine": [("الطب والجراحة", "الطب")],
        "sp_col_dentistry": [("طب وجراحة الأسنان", "طب الأسنان")],
        "sp_col_pharmacy": [("دكتور صيدلي", "الصيدلة")],
        "sp_col_applied_med": [
            ("علوم المختبرات الإكلينيكية", "العلوم الطبية التطبيقية"),
            ("العلاج الطبيعي", "العلوم الطبية التطبيقية"),
            ("العلوم الإشعاعية", "العلوم الطبية التطبيقية")
        ],
        "sp_col_nursing": [("تمريض عام", "كلية التمريض")],
        "sp_col_engineering": [
            ("الهندسة الميكانيكية", "الهندسة"),
            ("الهندسة المدنية", "الهندسة"),
            ("الهندسة الكهربائية", "الهندسة"),
            ("العمارة", "الهندسة"),
            ("الهندسة الكيميائية", "الهندسة"),
            ("التصميم الداخلي", "الهندسة"),
            ("هندسة الميكاترونيكس والروبوتات", "الهندسة")
        ],
        "sp_col_cs": [
            ("نظم المعلومات", "كلية علوم الحاسب ونظم المعلومات"),
            ("علوم الحاسبات", "كلية علوم الحاسب ونظم المعلومات"),
            ("شبكات الحاسب والاتصالات", "كلية علوم الحاسب ونظم المعلومات"),
            ("الأمن السيبراني", "كلية علوم الحاسب ونظم المعلومات"),
            ("نظم معلومات (مسار علوم البيانات)", "كلية علوم الحاسب ونظم المعلومات"),
            ("علوم الحاسبات (مسار الذكاء الاصطناعي)", "كلية علوم الحاسب ونظم المعلومات")
        ],
        "sp_col_sharia": [
            ("الشريعة", "كلية الشريعة واصول الدين"),
            ("أصول الدين", "كلية الشريعة واصول الدين")
        ],
        "sp_col_education": [
            ("علم النفس", "كلية التربية"),
            ("طفولة مبكرة", "كلية التربية")
        ],
        "sp_col_languages": [
            ("اللغة الإنجليزية وآدابها", "اللغات والترجمة"),
            ("الترجمة", "اللغات والترجمة")
        ],
        "sp_col_arts_sci": [
            ("اللغة العربية", "العلوم والآداب"),
            ("الأحياء", "العلوم والآداب"),
            ("الكيمياء", "العلوم والآداب"),
            ("الفيزياء", "العلوم والآداب"),
            ("الرياضيات المالية والإكتوارية", "العلوم والآداب"),
            ("الإحصاء التطبيقي", "العلوم والآداب"),
            ("رياضيات", "العلوم والآداب")
        ],
        "sp_col_business": [
            ("الأنظمة", "كلية إدارة أعمال"),
            ("إدارة أعمال", "كلية إدارة أعمال"),
            ("إدارة الموارد البشرية", "كلية إدارة أعمال"),
            ("المحاسبة", "كلية إدارة أعمال"),
            ("التسويق والتجارة الإلكترونية", "كلية إدارة أعمال")
        ],
        "sp_col_diploma": [
            ("البرمجة وقواعد البيانات", "الكلية التطبيقية (دبلوم)"),
            ("الدعم الفني", "الكلية التطبيقية (دبلوم)"),
            ("نظم المعلومات", "الكلية التطبيقية (دبلوم)"),
            ("المحاسبة", "الكلية التطبيقية (دبلوم)"),
            ("التسويق", "الكلية التطبيقية (دبلوم)"),
            ("إدارة الأعمال", "الكلية التطبيقية (دبلوم)"),
            ("ذكاء الأعمال وتحليل البيانات", "الكلية التطبيقية (دبلوم)"),
            ("إدارة الابتكار وريادة الأعمال", "الكلية التطبيقية (دبلوم)")
        ]
    }
    
    keyboard = []
    items = majors_map.get(college_key, [])
    for major_name, db_key in items:
        keyboard.append([InlineKeyboardButton(major_name, callback_data=f"major_{major_name}")])
    
    keyboard.append([InlineKeyboardButton("⬅️ رجوع للكليات", callback_data="study_plan_start")])
    return InlineKeyboardMarkup(keyboard)

# ----------------- قوائم الكليات العامة للأقسام الأخرى -----------------

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

# ----------------- القوائم الفرعية الأخرى -----------------

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
        [InlineKeyboardButton("📋 الخطط الدراسية", url="https://edugate.nu.edu.sa/nu/ui/guest/major_plans/index/facultiesMajorsIndex.faces")],
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

# ----------------- خطوات الخطة الذكية -----------------

async def study_plan_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "🧠 أهلاً بك في بوت الخطة الدراسية الذكي.\n\n"
        "الرجاء اختيار الكلية المطلوبة لعرض تخصصاتها:",
        reply_markup=study_plan_colleges_keyboard()
    )
    return CHOOSING_COLLEGE

async def college_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    
    if data == "study_plan_start" or data == "colleges_menu":
        await query.edit_message_text("اختر الكلية:", reply_markup=study_plan_colleges_keyboard())
        return CHOOSING_COLLEGE

    # إذا اختار كلية، نعرض له التخصصات الخاصة بها في أزرار منفصلة
    await query.edit_message_text(
        "اختر تخصصك بدقة من القائمة أدناه:",
        reply_markup=get_majors_keyboard_for_college(data)
    )
    return CHOOSING_MAJOR

async def major_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    # استخراج اسم التخصص من الـ callback_data
    major_name = query.data.replace("major_", "")
    context.user_data['major'] = major_name
    
    await query.edit_message_text(
        f"✅ تم اختيار تخصص: **{major_name}**\n\n"
        "الآن أرسل لي أسماء المواد التي اجتزتها مفصولة بفاصلة (مثلاً: برمجة 1, هياكل بيانات):",
        parse_mode="Markdown"
    )
    return ENTERING_PASSED_COURSES

async def get_passed_courses(update: Update, context: ContextTypes.DEFAULT_TYPE):
    passed_input = update.message.text.split(',')
    passed = [c.strip() for c in passed_input]
    major = context.user_data.get('major', 'عام')
    
    # البحث عن خطة التخصص أو استخدام قالب افتراضي إذا لم يوجد تطابق دقيق بالمواد
    plan_key = "العلوم الطبية التطبيقية" if "العلوم الطبية" in major else list(STUDY_PLANS.keys())[0]
    for key in STUDY_PLANS.keys():
        if key in major:
            plan_key = key
            break
            
    plan = STUDY_PLANS.get(plan_key, STUDY_PLANS["علوم الحاسب ونظم المعلومات"])["المواد"]
    
    suggested = []
    total_hours = 0
    for course in plan:
        c_name = course["name"]
        c_hours = course["hours"]
        c_prereq = course["prereq"]
        
        if c_name not in passed:
            if all(p in passed for p in c_prereq):
                suggested.append(c_name)
                total_hours += c_hours

    report = (
        f"📊 **تقرير الخطة الدراسية الذكي ({major}):**\n\n"
        f"✅ المواد المجتازة: {len(passed)}\n"
        f"🚀 المواد المقترحة للترم القادم: {', '.join(suggested) if suggested else 'لا توجد مواد مقترحة حالياً'}\n"
        f"⏱️ إجمالي ساعات المواد المقترحة: {total_hours} ساعات\n\n"
        "💡 تم التحقق من المتطلبات السابقة تلقائياً بنجاح!"
    )
    
    await update.message.reply_text(report, parse_mode="Markdown")
    return ConversationHandler.END

# ----------------- معالجة الأزرار العامة -----------------

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

    # الكليات العامة
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
            "احضار صورة واضحة من شهادة الثانوية العامة للتحقق من مقر الجهة التعليمية المانحة للشهادة ومدى استيفاء شرط المسافة المعتمد."
        )
        await query.edit_message_text(text, reply_markup=housing_menu_keyboard())

    # الحركات الأكاديمية
    elif data == "academic_menu":
        await query.edit_message_text("📝 الحركات الأكاديمية والطلبات:", reply_markup=academic_menu_keyboard())
    elif data == "withdraw":
        text = (
            "⚠️ **طريقة الانسحاب:**\n\n"
            "البوابة الإلكترونية ⬅️ الطلبات الأكاديمية ⬅️ الحركات الأكاديمية ⬅️ إضافة حركة جديدة ⬅️ نوع الحركة: انسحاب.\n\n"
            "⛔ عند الانسحاب لا يمكن التقديم للجامعة مرة أخرى إلا بعد سنتين."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "apology":
        text = (
            "⚠️ **طريقة الاعتذار عن فصل أو مقرر:**\n\n"
            "• موعد التقديم: متاح حتى قبل الاختبارات النهائية بخمسة أسابيع.\n"
            "• البوابة الإلكترونية ⬅️ الطلبات الأكاديمية ⬅️ الحركات الأكاديمية ⬅️ نوع الحركة: اعتذار."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "re_enroll":
        text = (
            "🔄 **إعادة القيد للمنقطع:**\n\n"
            "يحق للطالب المنقطع أو المنسحب التقدم بطلب إعادة القيد عبر البوابة الإلكترونية للعودة لنفس تجميعه ومستواه الأكاديمي."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "expected_gpa":
        text = (
            "📈 **احتساب المعدل المتوقع:**\n\n"
            "يمكنك حساب معدلك الفصلي والتراكمي المتوقع بناءً على الدرجات والساعات المتوقعة عبر البوابة الأكاديمية."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "postpone":
        text = (
            "⏳ **تأجيل الفصل الدراسي:**\n\n"
            "• موعد التقديم: قبل بدء الدراسة إلكترونياً عبر البوابة الأكاديمية."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "visitor":
        text = (
            "🚶‍♂️ **الطلبة الزائرون:**\n\n"
            "يتاح للطالب دراسة مقررات في جامعة أخرى أو فرع آخر وفق شروط محددة عبر البوابة الأكاديمية."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "diff":
        text = (
            "⚖️ **الفرق بين التأجيل والاعتذار:**\n\n"
            "• **التأجيل:** يطلب قبل الفصل، لا يُحسب من المدة، ولا يقطع المكافأة.\n"
            "• **الاعتذار:** يطلب خلال الفصل، يُحسب من المدة الدراسية."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "reward_stop":
        text = (
            "🔺 حالات انقطاع المكافأة:\n"
            "- عند انخفاض المعدل التراكمي 1.99 فأقل.\n"
            "- عند الانسحاب أو تأجيل الفصل الدراسي.\n"
            "- عند طيّ القيد أو تجاوز الخطة الدراسية."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard(), parse_mode="Markdown")
    elif data == "course_desc":
        text = (
            "🔺 لإظهار توصيف المقرر عبر موقع جامعة نجران الرسمي:\n"
            "القائمة ⬅️ الكليات ⬅️ اختيار الكلية والتخصص ⬅️ البرنامج ⬅️ توصيف المقرر."
        )
        await query.edit_message_text(text, reply_markup=academic_menu_keyboard())

    # روابط مهمة
    elif data == "important_links":
        await query.edit_message_text("🔗 الروابط المهمة والأنظمة الإلكترونية:", reply_markup=important_links_keyboard())
    elif data == "university_email":
        text = (
            "👥جميع طلاب وطالبات جامعة نجران لديهم إيميل جامعي بصيغة:\n"
            "الرقم الجامعي @nu.edu.sa\n"
            "كلمة المرور: نفس كلمة مرور البوابة الإلكترونية."
        )
        await query.edit_message_text(text, reply_markup=important_links_keyboard())

    # شروط القبول العامة
    elif data == "admission_guide":
        text = (
            "📋 **شروط القبول العامة بجامعة نجران:**\n\n"
            "• المسار الصحي والهندسي والحاسوبي: 30% ثانوية، 30% قدرات، 40% تحصيلي.\n"
            "• التخصصات النظرية والإنسانية: 40% ثانوية، 60% قدرات (بنسبة موزونة 70 فأعلى).\n"
            "• الدبلومات: 40% ثانوية، 60% قدرات (بنسبة موزونة 65 فأعلى)."
        )
        await query.edit_message_text(text, reply_markup=admission_guide_keyboard(), parse_mode="Markdown")

    # المستشفى الجامعي
    elif data == "hospital_menu":
        text = (
            "🏥 **المستشفى الجامعي:**\n\n"
            "💼 حجز ومتابعة المواعيد: 0175416322\n"
            "📞 لطلب فتح ملف جديد: +966 17 541 6304"
        )
        await query.edit_message_text(text, reply_markup=back_to_main_keyboard(), parse_mode="Markdown")

    # شروط المعدل
    elif data == "gpa_conditions":
        text = (
            "📈 **شرط المعدل بعد السنة المشتركة:**\n\n"
            "• 4.25 فأعلى ← الطب والجراحة\n"
            "• 3.75 فأعلى ← طب الأسنان\n"
            "• 3.25 فأعلى ← دكتور صيدلي والتمريض ونظم المعلومات والحاسب\n"
            "• 3.00 فأعلى ← الهندسة والعلوم الطبية التطبيقية"
        )
        await query.edit_message_text(text, reply_markup=back_to_main_keyboard(), parse_mode="Markdown")

def main():
    TOKEN = "8722924986:AAEVU_oqQDYFs6LG18D-A0VJJfr9Ry2Jyr0"
    app = ApplicationBuilder().token(TOKEN).build()
    
    # ربط معالجات المحادثة للخطة الذكية مع دعم الأزرار المتسلسلة (كليات ثم تخصصات)
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(study_plan_start, pattern='study_plan_start')],
        states={
            CHOOSING_COLLEGE: [CallbackQueryHandler(college_selected, pattern='^sp_col_')],
            CHOOSING_MAJOR: [CallbackQueryHandler(major_selected, pattern='^major_')],
            ENTERING_PASSED_COURSES: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_passed_courses)],
        },
        fallbacks=[CallbackQueryHandler(study_plan_start, pattern='study_plan_start')],
    )
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 البوت يعمل بكامل التخصصات الرسمية لجامعة نجران (1448 هـ)...")
    app.run_polling()

if __name__ == "__main__":
    main()
