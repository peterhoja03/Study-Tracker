"""
How to Study Korean — Full Curriculum
Built lesson-by-lesson from PDF screenshots of the HTSK website.

Each lesson contains:
  id                    : unique string e.g. "U0L1"
  title                 : lesson title
  subtitle              : one-line descriptor
  url                   : direct HTSK link
  estimated_minutes     : total reading/study time
  split                 : True if this lesson should be spread across blocks
  learning_goals        : list of specific, measurable goals for THIS lesson
  techniques            : study techniques suited to this content
  key_vocab             : list of Korean words/forms introduced
  feynman_prompt        : one targeted Feynman-technique prompt
  active_recall_questions : list of questions (can reference prior lessons)
  resources             : list of {name, url} dicts
  topik_vocab_count     : approximate TOPIK I words introduced (int)
  knowledge_bank        : {summary: str, facts: [str]} — feeds AI marking
  expected_answers      : {question_str: answer_str} — feeds AI marking

Partial completion:
  Progress is stored in Supabase with a `completion_pct` field (0–100).
  A lesson with completion_pct < 100 shows as "in_progress".
  A lesson with completion_pct == 100 shows as "completed".
  This allows a hard lesson to be split across multiple 25-min blocks.

TOPIK constants
───────────────
TOPIK_I_TARGET  : recommended word count to sit TOPIK I comfortably (Level 1–2)
TOPIK_I_FULL    : full official TOPIK I vocabulary list size
"""

# ─── TOPIK constants ──────────────────────────────────────────────────────────
TOPIK_I_TARGET = 1200   # recommended comfortable threshold for TOPIK I exam
TOPIK_I_FULL   = 1671   # full official TOPIK I word list (Tammy Korean / NIIED)

# ─── Curriculum ───────────────────────────────────────────────────────────────
# Lessons are added here progressively as PDFs are uploaded and verified.
# Do not add any lesson until its PDF content has been confirmed accurate.

CURRICULUM = {
    # Units will be added here as PDFs are processed.
    # Example structure (do not uncomment — placeholder only):
    #
    # "Unit 0": {
    #     "title": "Learning How to Read (Hangul)",
    #     "level": "Absolute Beginner",
    #     "description": "Master the Korean alphabet before touching grammar.",
    #     "color": "#4A90D9",
    #     "url": "https://www.howtostudykorean.com/unit0/",
    #     "lessons": [
    #         {
    #             "id": "U0L1",
    #             "title": "...",
    #             ...
    #         },
    #     ],
    # },
}

# ─── Spaced repetition intervals (days) ──────────────────────────────────────
SR_INTERVALS = {
    0: 1,    # New → review tomorrow
    1: 3,    # 2nd review → in 3 days
    2: 7,    # 3rd review → in 1 week
    3: 14,   # 4th review → in 2 weeks
    4: 30,   # 5th review → in 1 month
    5: 90,   # 6th review → in 3 months
}

# ─── Curriculum helpers ───────────────────────────────────────────────────────

def get_all_lessons():
    """Return a flat list of all lessons across all units."""
    lessons = []
    for unit_name, unit_data in CURRICULUM.items():
        for lesson in unit_data["lessons"]:
            lesson_copy = lesson.copy()
            lesson_copy["unit"] = unit_name
            lesson_copy["unit_title"] = unit_data["title"]
            lesson_copy["unit_color"] = unit_data["color"]
            lesson_copy["unit_level"] = unit_data["level"]
            lessons.append(lesson_copy)
    return lessons


def get_lesson_by_id(lesson_id):
    """Find a lesson by its ID."""
    for lesson in get_all_lessons():
        if lesson["id"] == lesson_id:
            return lesson
    return None


def get_unit_progress_summary(progress_data):
    """Calculate completion stats per unit."""
    summary = {}
    for unit_name, unit_data in CURRICULUM.items():
        total = len(unit_data["lessons"])
        completed = sum(
            1 for l in unit_data["lessons"]
            if progress_data.get(l["id"], {}).get("completion_pct", 0) == 100
        )
        summary[unit_name] = {
            "total": total,
            "completed": completed,
            "percent": round((completed / total * 100) if total > 0 else 0, 1),
            "color": unit_data["color"],
            "title": unit_data["title"],
            "level": unit_data["level"],
        }
    return summary


# ─── TOPIK Progress Helpers ───────────────────────────────────────────────────

def get_topik_vocab_total(progress_data: dict) -> int:
    """
    Return the cumulative TOPIK I vocab count for all fully completed lessons.
    Uses `topik_vocab_count` field on each lesson (defaults to 0 if absent).
    Only counts lessons where completion_pct == 100.
    """
    total = 0
    for unit_data in CURRICULUM.values():
        for lesson in unit_data["lessons"]:
            if progress_data.get(lesson["id"], {}).get("completion_pct", 0) == 100:
                total += lesson.get("topik_vocab_count", 0)
    return total


def get_topik_progress_summary(progress_data: dict) -> dict:
    """
    Return a dict with TOPIK vocab progress stats.
    {
        'words_known': int,
        'target': int (TOPIK_I_TARGET),
        'full': int (TOPIK_I_FULL),
        'percent_of_target': float,
        'percent_of_full': float,
        'ready_for_topik': bool,
    }
    """
    known = get_topik_vocab_total(progress_data)
    return {
        "words_known": known,
        "target": TOPIK_I_TARGET,
        "full": TOPIK_I_FULL,
        "percent_of_target": round(known / TOPIK_I_TARGET * 100, 1),
        "percent_of_full": round(known / TOPIK_I_FULL * 100, 1),
        "ready_for_topik": known >= TOPIK_I_TARGET,
    }
