"""
Weakness log store functions.
These handle reading/writing the weakness_log Supabase table.
"""

import json
from datetime import date
import streamlit as st
from db import _sb


def log_weakness(
    lesson_id: str,
    score: int,
    question_type: str,
    weakness_categories: list,
    specific_gaps: list,
    raw_answer: str = "",
    kb_items_tested: list = None,
    kb_items_failed: list = None,
    competency_scores: dict = None,
):
    """
    Write one row to the weakness_log table.
    Call this after every AI-marked attempt.
    """
    stream = lesson_id[:1]
    stream_name = {"U": "korean", "P": "physics", "R": "raf"}.get(stream, "general")

    row = {
        "lesson_id": lesson_id,
        "date": date.today().isoformat(),
        "stream": stream_name,
        "score": score,
        "question_type": question_type,
        "weakness_categories": json.dumps(weakness_categories),
        "specific_gaps": json.dumps(specific_gaps),
        "kb_items_tested": json.dumps(kb_items_tested or []),
        "kb_items_failed": json.dumps(kb_items_failed or []),
        "raw_answer": raw_answer[:1000],  # Truncate long answers
        "competency_scores": json.dumps(competency_scores or {}),
    }

    sb = _sb()
    if sb:
        try:
            sb.table("weakness_log").insert(row).execute()
            # Invalidate ALL weakness log cache keys (per-lesson and global)
            keys_to_clear = [k for k in st.session_state if k.startswith("_weakness_log_cache")]
            for k in keys_to_clear:
                del st.session_state[k]
        except Exception as e:
            st.session_state.setdefault("_weakness_log", []).append(row)
    else:
        st.session_state.setdefault("_weakness_log", []).append(row)


def load_weakness_log(lesson_id: str = None, stream: str = None, limit: int = 100) -> list:
    """
    Load weakness_log rows. Optionally filter by lesson_id or stream.
    Results are parsed from JSON strings back to Python objects.
    """
    cache_key = f"_weakness_log_cache_{lesson_id or ''}_{stream or ''}"
    if cache_key in st.session_state:
        return st.session_state[cache_key]

    sb = _sb()
    rows = []
    if sb:
        try:
            query = sb.table("weakness_log").select("*").order("date", desc=True).limit(limit)
            if lesson_id:
                query = query.eq("lesson_id", lesson_id)
            if stream:
                query = query.eq("stream", stream)
            rows = query.execute().data
        except Exception:
            rows = st.session_state.get("_weakness_log", [])
    else:
        rows = st.session_state.get("_weakness_log", [])

    # Parse JSON columns back to Python
    parsed = []
    for row in rows:
        r = dict(row)
        for col in ["weakness_categories", "specific_gaps", "kb_items_tested", "kb_items_failed"]:
            if isinstance(r.get(col), str):
                try:
                    r[col] = json.loads(r[col])
                except Exception:
                    r[col] = []
        if isinstance(r.get("competency_scores"), str):
            try:
                r["competency_scores"] = json.loads(r["competency_scores"])
            except Exception:
                r["competency_scores"] = {}
        parsed.append(r)

    st.session_state[cache_key] = parsed
    return parsed


def get_lesson_weakness_summary(lesson_id: str) -> dict:
    """
    Get a summary of weaknesses for one lesson.
    Returns: {attempts, avg_score, top_gaps, top_categories, last_date}
    """
    rows = load_weakness_log(lesson_id=lesson_id)
    if not rows:
        return {"attempts": 0, "avg_score": 0, "top_gaps": [], "top_categories": [], "last_date": None}

    from collections import Counter
    scores = [r["score"] for r in rows if r.get("score")]
    all_gaps = []
    all_cats = []
    for r in rows:
        all_gaps.extend(r.get("specific_gaps", []))
        all_cats.extend(r.get("weakness_categories", []))

    return {
        "attempts": len(rows),
        "avg_score": round(sum(scores) / len(scores), 1) if scores else 0,
        "top_gaps": [g for g, _ in Counter(all_gaps).most_common(5)],
        "top_categories": [c for c, _ in Counter(all_cats).most_common(3)],
        "last_date": rows[0].get("date") if rows else None,
    }
