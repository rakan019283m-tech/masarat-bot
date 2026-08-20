"""
planner.py
----------
منطق "الخطة الدراسية الذكي": يحسب المواد المتاحة للطالب حسب المواد
اللي خلصها، ويتحقق من المتطلبات السابقة، وتعارض الجدول، وينبه على
المواد الحرجة.

هذا الملف لا يعرف شي عن تيليجرام إطلاقًا - فقط منطق أعمال (business logic)
عشان يسهل اختباره أو استخدامه في أي واجهة ثانية بالمستقبل.
"""

import json
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def load_courses():
    with open(DATA_DIR / "courses.json", encoding="utf-8") as f:
        return json.load(f)


def load_terms():
    with open(DATA_DIR / "terms.json", encoding="utf-8") as f:
        return json.load(f)


def _to_minutes(hhmm: str) -> int:
    """يحول '08:30' إلى عدد دقائق من بداية اليوم، عشان نقارن الأوقات بسهولة."""
    t = datetime.strptime(hhmm, "%H:%M")
    return t.hour * 60 + t.minute


def sections_overlap(sec_a: dict, sec_b: dict) -> bool:
    """يرجع True إذا شعبتين تتعارضن باليوم والوقت."""
    if sec_a["day"] != sec_b["day"]:
        return False
    a_start, a_end = _to_minutes(sec_a["start"]), _to_minutes(sec_a["end"])
    b_start, b_end = _to_minutes(sec_b["start"]), _to_minutes(sec_b["end"])
    return a_start < b_end and b_start < a_end


def get_eligible_courses(completed: list[str], term: str, courses=None):
    """
    يرجع قائمة المواد اللي يقدر الطالب يسجلها في هذا الترم:
    - ما أخذها قبل
    - خلص كل متطلباتها السابقة
    - تُطرح في هذا الترم
    """
    if courses is None:
        courses = load_courses()

    completed_set = set(completed)
    eligible = []

    for course in courses:
        if course["code"] in completed_set:
            continue
        if term not in course["term_offered"]:
            continue
        missing_prereqs = [
            p for p in course["prerequisites"] if p not in completed_set
        ]
        if missing_prereqs:
            continue
        eligible.append(course)

    return eligible


def find_conflicts(course_codes: list[str], term: str, terms_data=None):
    """
    يفحص قائمة رموز مواد ويرجع قائمة أزواج (code_a, code_b) اللي
    تتعارض بالجدول في هذا الترم.
    """
    if terms_data is None:
        terms_data = load_terms()

    term_sections = terms_data.get(term, {})
    conflicts = []

    for i, code_a in enumerate(course_codes):
        for code_b in course_codes[i + 1:]:
            secs_a = term_sections.get(code_a, [])
            secs_b = term_sections.get(code_b, [])
            for sa in secs_a:
                for sb in secs_b:
                    if sections_overlap(sa, sb):
                        conflicts.append((code_a, code_b))

    return conflicts


def suggest_plan(
    completed: list[str],
    term: str,
    max_hours: int = 18,
    courses=None,
    terms_data=None,
):
    """
    يبني اقتراح خطة تسجيل للترم: يعطي أولوية للمواد الحرجة (critical)
    ثم الأقل مستوى، ويتجنب أي مادة تتعارض بالجدول مع مادة تم اختيارها
    قبلها، ولا يتجاوز الحد الأقصى للساعات.
    """
    eligible = get_eligible_courses(completed, term, courses)
    terms_data = terms_data or load_terms()

    # رتب: الحرجة أولاً، وبعدين الأقل مستوى (عشان ما تتراكم)
    eligible.sort(key=lambda c: (not c["critical"], c["level"]))

    term_sections = terms_data.get(term, {})
    selected = []
    total_hours = 0

    for course in eligible:
        if total_hours + course["hours"] > max_hours:
            continue

        conflict_found = False
        for chosen in selected:
            for sa in term_sections.get(course["code"], []):
                for sb in term_sections.get(chosen["code"], []):
                    if sections_overlap(sa, sb):
                        conflict_found = True
                        break

        if conflict_found:
            continue

        selected.append(course)
        total_hours += course["hours"]

    skipped = [c for c in eligible if c not in selected]

    return {
        "selected": selected,
        "skipped_due_to_conflict_or_hours": skipped,
        "total_hours": total_hours,
    }


def remaining_critical_courses(completed: list[str], courses=None):
    """المواد الحرجة اللي لسا ما أخذها الطالب - تنبيه بمواد ممكن تأخر تخرجه."""
    if courses is None:
        courses = load_courses()
    completed_set = set(completed)
    return [
        c for c in courses
        if c["critical"] and c["code"] not in completed_set
    ]
