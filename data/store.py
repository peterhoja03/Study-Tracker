"""
Data store — reads/writes to Supabase for persistent cross-device storage.
Falls back gracefully to session state if connection fails.
"""

import os
from datetime import date, datetime, timedelta

import streamlit as st


# ─── Supabase client ──────────────────────────────────────────────────────────

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from db import _sb


# ─── Progress ────────────────────────────────────────────────────────────────

def load_progress() -> dict:
    sb = _sb()
    if sb:
        try:
            res = sb.table("progress").select("*").execute()
            return {row["lesson_id"]: row for row in res.data}
        except Exception:
            pass
    return st.session_state.get("_progress", {})


def save_progress(progress: dict):
    st.session_state["_progress"] = progress


def _upsert_lesson(lesson_id: str, fields: dict):
    sb = _sb()
    fields["lesson_id"] = lesson_id
    fields["updated_at"] = datetime.now().isoformat()
    if sb:
        try:
            sb.table("progress").upsert(fields).execute()
        except Exception:
            pass
    progress = st.session_state.get("_progress", {})
    progress.setdefault(lesson_id, {}).update(fields)
    st.session_state["_progress"] = progress


def mark_lesson_complete(lesson_id: str, score: int = None, time_spent: int = 25):
    from data.curriculum import SR_INTERVALS
    progress = load_progress()
    existing = progress.get(lesson_id, {})
    review_count = existing.get("review_count", 0) + 1
    days_until_next = SR_INTERVALS.get(min(review_count, max(SR_INTERVALS.keys())), 90)
    next_review = (date.today() + timedelta(days=days_until_next)).isoformat()
    fields = {
        "status": "completed",
        "completed_date": date.today().isoformat(),
        "score": score,
        "review_count": review_count,
        "next_review": next_review,
        "feynman_done": existing.get("feynman_done", False),
        "notes": existing.get("notes", ""),
        "time_spent": time_spent,
    }
    _upsert_lesson(lesson_id, fields)
    return fields


def mark_lesson_in_progress(lesson_id: str):
    progress = load_progress()
    if progress.get(lesson_id, {}).get("status") != "completed":
        _upsert_lesson(lesson_id, {"status": "in_progress"})


def save_lesson_notes(lesson_id: str, notes: str):
    _upsert_lesson(lesson_id, {"notes": notes})


def mark_feynman_done(lesson_id: str):
    _upsert_lesson(lesson_id, {"feynman_done": True})


# ─── Spaced Repetition Queue ──────────────────────────────────────────────────

def get_due_reviews() -> list:
    progress = load_progress()
    today = date.today().isoformat()
    return [
        lid for lid, data in progress.items()
        if data.get("status") == "completed"
        and data.get("next_review")
        and data["next_review"] <= today
    ]


def get_upcoming_reviews(days_ahead: int = 7) -> dict:
    progress = load_progress()
    today = date.today()
    upcoming = {}
    for i in range(days_ahead + 1):
        check_date = (today + timedelta(days=i)).isoformat()
        due = [
            lid for lid, data in progress.items()
            if data.get("status") == "completed"
            and data.get("next_review") == check_date
        ]
        if due:
            upcoming[check_date] = due
    return upcoming


# ─── Study Sessions ───────────────────────────────────────────────────────────

def log_study_session(lesson_id: str, duration_min: int, activity_type: str, notes: str = ""):
    sb = _sb()
    row = {
        "lesson_id": lesson_id,
        "date": date.today().isoformat(),
        "time": datetime.now().strftime("%H:%M"),
        "duration": duration_min,
        "activity_type": activity_type,
    }
    if sb:
        try:
            sb.table("sessions").insert(row).execute()
        except Exception:
            pass
    sessions = st.session_state.get("_sessions", [])
    sessions.append(row)
    st.session_state["_sessions"] = sessions


def load_sessions() -> list:
    sb = _sb()
    if sb:
        try:
            res = sb.table("sessions").select("*").order("date", desc=True).execute()
            return res.data
        except Exception:
            pass
    return st.session_state.get("_sessions", [])


def get_total_study_time() -> int:
    return sum(s.get("duration", 0) for s in load_sessions())


def get_streak() -> int:
    sessions = load_sessions()
    if not sessions:
        return 0
    study_dates = sorted(set(s["date"] for s in sessions), reverse=True)
    today = date.today().isoformat()
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    if study_dates[0] not in (today, yesterday):
        return 0
    streak = 0
    check = date.today() if study_dates[0] == today else date.today() - timedelta(days=1)
    for d in study_dates:
        if d == check.isoformat():
            streak += 1
            check -= timedelta(days=1)
        else:
            break
    return streak


def get_weekly_study_minutes() -> dict:
    sessions = load_sessions()
    today = date.today()
    return {
        (today - timedelta(days=i)).isoformat():
        sum(s.get("duration", 0) for s in sessions if s["date"] == (today - timedelta(days=i)).isoformat())
        for i in range(6, -1, -1)
    }


# ─── Goals ───────────────────────────────────────────────────────────────────

def load_goals() -> dict:
    sb = _sb()
    default = {
        "weekly_sessions": 3,
        "daily_minutes": 25,
        "target_unit": "Unit 1",
        "target_date": "",
        "motivation": "",
    }
    if sb:
        try:
            res = sb.table("goals").select("*").eq("id", 1).execute()
            if res.data:
                return {**default, **res.data[0]}
        except Exception:
            pass
    return st.session_state.get("_goals", default)


def save_goals(goals: dict):
    sb = _sb()
    goals["id"] = 1
    if sb:
        try:
            sb.table("goals").upsert(goals).execute()
        except Exception:
            pass
    st.session_state["_goals"] = goals


# ─── Vocab scores (session state only) ───────────────────────────────────────

def load_vocab_scores() -> dict:
    return st.session_state.get("_vocab_scores", {})


def update_vocab_score(word: str, correct: bool):
    scores = load_vocab_scores()
    scores.setdefault(word, {"correct": 0, "total": 0})
    scores[word]["total"] += 1
    if correct:
        scores[word]["correct"] += 1
    st.session_state["_vocab_scores"] = scores


# ─── Dashboard stats ─────────────────────────────────────────────────────────

def get_dashboard_stats() -> dict:
    progress = load_progress()
    total_completed = sum(1 for d in progress.values() if d.get("status") == "completed")
    total_in_progress = sum(1 for d in progress.values() if d.get("status") == "in_progress")
    due_reviews = len(get_due_reviews())
    streak = get_streak()
    total_time = get_total_study_time()
    return {
        "total_completed": total_completed,
        "total_in_progress": total_in_progress,
        "due_reviews": due_reviews,
        "streak": streak,
        "total_study_hours": round(total_time / 60, 1),
        "total_study_minutes": total_time,
    }
