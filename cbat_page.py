"""
CBAT Practice Tracker
Logs practice sessions per subtest, self-rated 1-5 + notes.
On-demand AI analysis identifies weak subtests and patterns.
Source: rafcbat.wordpress.com — 23 subtests mapped to free practice resources.
"""

import streamlit as st
from datetime import date, datetime, timedelta
import json


# ─── CBAT Subtests (from rafcbat.wordpress.com) ───────────────────────────────

CBAT_SUBTESTS = [
    {
        "id": "ANT",
        "name": "Airborne Numerical Test",
        "abbr": "ANT",
        "category": "Numerical",
        "description": "Speed, distance, time, fuel calculations, and arithmetic under time pressure.",
        "tips": "Focus on SDT calculations and mental arithmetic. Accuracy under time pressure is key.",
        "resources": [
            {"name": "That Quiz (Arithmetic)", "url": "https://www.thatquiz.org/tq-1/math/arithmetic/"},
            {"name": "Speed Distance Time", "url": "https://www.speeddistancetime.info/test"},
            {"name": "Fuel Calculations", "url": "https://www.speeddistancetime.info/fuel-test"},
        ]
    },
    {
        "id": "ABD",
        "name": "Angles, Bearings & Degrees",
        "abbr": "ABD",
        "category": "Spatial",
        "description": "Estimating and calculating angles, compass bearings, and degree measurements.",
        "tips": "Practice angle estimation quickly. Khan Academy has a good free angle estimator.",
        "resources": [
            {"name": "Khan Academy Angles", "url": "https://www.khanacademy.org/math/basic-geo/basic-geo-angle/measure-angles/e/estimate-angle-measures"},
        ]
    },
    {
        "id": "ACT",
        "name": "Auditory Capacity Test",
        "abbr": "ACT",
        "category": "Working Memory",
        "description": "Listening to spoken sequences and responding to them while performing other tasks.",
        "tips": "Limited free practice available. Focus on dual-task exercises and listening games.",
        "resources": [
            {"name": "Military Aptitude (paid)", "url": "https://www.militaryaptitude.com/s/store/courses/description/Military-Aviation-Cognitive-Testing-Online-Course"},
        ]
    },
    {
        "id": "CUT",
        "name": "Cognitive Updating Test",
        "abbr": "CUT",
        "category": "Working Memory",
        "description": "Updating information held in working memory as new information arrives.",
        "tips": "N-back tasks are the closest free equivalent. Cambridge Brain Sciences has good working memory tools.",
        "resources": [
            {"name": "Cambridge Brain Sciences", "url": "https://www.cambridgebrainsciences.com/"},
        ]
    },
    {
        "id": "FLAG",
        "name": "Figures, Logistics and Groups / CLAN",
        "abbr": "FLAG/CLAN",
        "category": "Processing Speed",
        "description": "Rapid classification of figures, letters, numbers, or colours into categories.",
        "tips": "Speed and accuracy. CLAN is the colour/letter/number variant. That Quiz arithmetic helps with CLAN.",
        "resources": [
            {"name": "That Quiz (Arithmetic)", "url": "https://www.thatquiz.org/tq-1/math/arithmetic/"},
        ]
    },
    {
        "id": "DRT",
        "name": "Digit Recognition Test",
        "abbr": "DRT",
        "category": "Processing Speed",
        "description": "Rapidly identifying whether a digit matches a target. Not included in Royal Navy FAT.",
        "tips": "Speed and accuracy of digit matching. Practice with any rapid number recognition exercise.",
        "resources": []
    },
    {
        "id": "DAD",
        "name": "Directions and Distances",
        "abbr": "DAD",
        "category": "Spatial",
        "description": "Following a series of directions and calculating final position or distance.",
        "tips": "Draw the route mentally step by step. Practice compass directions and dead reckoning.",
        "resources": [
            {"name": "CBAT Guide (DAD)", "url": "https://rafcbat.wordpress.com/dad/"},
        ]
    },
    {
        "id": "DPT",
        "name": "Dynamic Projection Test",
        "abbr": "DPT",
        "category": "Spatial",
        "description": "Predicting where a moving object will be after a given time. Not in Royal Navy FAT.",
        "tips": "Visualise trajectory and estimate intercept. Limited free practice — focus on mental projection exercises.",
        "resources": [
            {"name": "CBAT Guide (DPT)", "url": "https://rafcbat.wordpress.com/dynamic-projection-test-dpt/"},
        ]
    },
    {
        "id": "INSC",
        "name": "Instrument Comprehension Test",
        "abbr": "INSC",
        "category": "Spatial",
        "description": "Reading aviation instruments (attitude indicator, altimeter, heading) and determining aircraft orientation.",
        "tips": "This is one of the most trainable CBAT tests. Practice both Fibonicci and AFOQT versions regularly.",
        "resources": [
            {"name": "Fibonicci Pilot Test", "url": "https://www.fibonicci.com/spatial-awareness/airforce-pilot-test/"},
            {"name": "AFOQT Instrument Test", "url": "https://afoqtpracticetest.com/instrument-comprehension/"},
        ]
    },
    {
        "id": "NOT",
        "name": "Numerical Operations Test",
        "abbr": "NOT",
        "category": "Numerical",
        "description": "Basic arithmetic operations performed rapidly. Not in Royal Navy FAT.",
        "tips": "Pure speed arithmetic. That Quiz is excellent for this.",
        "resources": [
            {"name": "That Quiz (Arithmetic)", "url": "https://www.thatquiz.org/tq-1/math/arithmetic/"},
        ]
    },
    {
        "id": "RTT",
        "name": "Rapid Tracking Test",
        "abbr": "RTT",
        "category": "Psychomotor",
        "description": "Keeping a cursor on a moving target using a joystick. Tests hand-eye coordination and tracking.",
        "tips": "Hard to replicate without CBAT equipment. Practice mouse tracking games as a proxy.",
        "resources": [
            {"name": "CBAT Equipment Guide", "url": "https://rafcbat.wordpress.com/cbat-equipment-explained/"},
        ]
    },
    {
        "id": "SMA",
        "name": "Sensory Motor Apparatus Test",
        "abbr": "SMA",
        "category": "Psychomotor",
        "description": "Dual-task: tracking with joystick while responding to visual/auditory signals with rudder pedals.",
        "tips": "The most pilot-specific test — requires the actual CBAT hardware. Familiarise yourself with the equipment description.",
        "resources": [
            {"name": "CBAT Equipment Guide", "url": "https://rafcbat.wordpress.com/cbat-equipment-explained/"},
            {"name": "Military Aptitude (paid)", "url": "https://www.militaryaptitude.com/s/store/courses/description/Military-Aviation-Cognitive-Testing-Online-Course"},
        ]
    },
    {
        "id": "SAT",
        "name": "Situational Awareness Test",
        "abbr": "SAT",
        "category": "Working Memory",
        "description": "Tracking multiple moving elements and responding to changes in a dynamic display.",
        "tips": "Multi-object tracking games help. NeuroTracker is the gold standard proxy but expensive.",
        "resources": [
            {"name": "CBAT Guide (SAT)", "url": "https://rafcbat.wordpress.com/situational-awareness-test/"},
        ]
    },
    {
        "id": "SIT",
        "name": "Spatial Integration Test",
        "abbr": "SIT",
        "category": "Spatial",
        "description": "Combining separate spatial elements to determine overall orientation or position.",
        "tips": "Practice mental rotation and spatial combination. Fibonicci SpaR is useful.",
        "resources": [
            {"name": "Fibonicci SpaR", "url": "https://www.fibonicci.com/spatial--awareness/spatial-reasoning-test/hard/"},
        ]
    },
    {
        "id": "SLT",
        "name": "System Logic Test",
        "abbr": "SLT",
        "category": "Reasoning",
        "description": "Following logical rules governing a system to predict correct outputs.",
        "tips": "Read rules carefully and apply them systematically. Verbal reasoning practice helps with rule-following.",
        "resources": [
            {"name": "CBAT Guide (SLT)", "url": "https://rafcbat.wordpress.com/system-logic-test-slt/"},
        ]
    },
    {
        "id": "MATF",
        "name": "Table Reading Test",
        "abbr": "MATF",
        "category": "Processing Speed",
        "description": "Rapidly locating values in a table given row and column coordinates.",
        "tips": "Pure speed. Practice scanning tables. AFOQT table reading tests are a good proxy.",
        "resources": [
            {"name": "CBAT Guide (MATF)", "url": "https://rafcbat.wordpress.com/table-reading-test-matf/"},
        ]
    },
    {
        "id": "TRT",
        "name": "Target Recognition Test",
        "abbr": "TRT",
        "category": "Processing Speed",
        "description": "Rapidly identifying whether a briefly displayed target matches a memorised set.",
        "tips": "Speed and visual memory. Practice with any rapid pattern/symbol matching exercise.",
        "resources": []
    },
    {
        "id": "TRAC1",
        "name": "Trace Test 1",
        "abbr": "TRAC1",
        "category": "Spatial",
        "description": "Following a path through a complex visual display to identify where it ends.",
        "tips": "Visual tracking and concentration. Slow down initially to build accuracy before speed.",
        "resources": [
            {"name": "CBAT Guide (TRAC1)", "url": "https://rafcbat.wordpress.com/trace-test-1-trac1/"},
        ]
    },
    {
        "id": "TRAC2",
        "name": "Trace Test 2",
        "abbr": "TRAC2",
        "category": "Spatial",
        "description": "More complex variant of the trace test.",
        "tips": "Same approach as TRAC1 — visual tracking with increasing complexity.",
        "resources": [
            {"name": "CBAT Guide (TRAC2)", "url": "https://rafcbat.wordpress.com/trace-test-2-trac2/"},
        ]
    },
    {
        "id": "VLT",
        "name": "Verbal Logic Test",
        "abbr": "VLT",
        "category": "Reasoning",
        "description": "Applying logical rules expressed in verbal form to determine correct conclusions.",
        "tips": "True/False/Cannot Say logic. Apply only what the passage states — never infer beyond it.",
        "resources": [
            {"name": "Practice Aptitude Tests (Verbal)", "url": "https://www.practiceaptitudetests.com/verbal-reasoning-tests/"},
        ]
    },
    {
        "id": "VST",
        "name": "Visual Search Test",
        "abbr": "VST",
        "category": "Processing Speed",
        "description": "Rapidly locating a target symbol within a cluttered visual display. Not in Royal Navy FAT.",
        "tips": "Speed and accuracy of visual search. Practice with any visual scanning exercise.",
        "resources": []
    },
    {
        "id": "VIS",
        "name": "Visualisation Tests",
        "abbr": "VIS",
        "category": "Spatial",
        "description": "Mental rotation and 3D spatial reasoning tasks.",
        "tips": "The most trainable spatial test. Fibonicci SpaR and daily mental rotation practice make a difference.",
        "resources": [
            {"name": "Fibonicci SpaR", "url": "https://www.fibonicci.com/spatial--awareness/spatial-reasoning-test/hard/"},
        ]
    },
    {
        "id": "VIG",
        "name": "Vigilance Test",
        "abbr": "VIG",
        "category": "Working Memory",
        "description": "Sustained attention over time — detecting rare target events in a continuous stream.",
        "tips": "Concentration and sustained attention. Hard to practice with free tools. Any sustained-focus exercise helps.",
        "resources": [
            {"name": "CBAT Guide (Vigilance)", "url": "https://rafcbat.wordpress.com/vigilance-test/"},
        ]
    },
]

CATEGORY_COLORS = {
    "Numerical": "#1565c0",
    "Spatial": "#4a148c",
    "Working Memory": "#1b5e20",
    "Processing Speed": "#e65100",
    "Psychomotor": "#b71c1c",
    "Reasoning": "#004d40",
}

SCORE_LABELS = {
    1: ("😰 1 — Struggled significantly", "#e74c3c"),
    2: ("😕 2 — Below par, key errors", "#e67e22"),
    3: ("😐 3 — Mixed, some gaps", "#f1c40f"),
    4: ("🙂 4 — Solid, minor issues", "#2ecc71"),
    5: ("😊 5 — Strong performance", "#27ae60"),
}


# ─── Supabase helpers ─────────────────────────────────────────────────────────

def _sb():
    if "supabase_client" not in st.session_state:
        try:
            from supabase import create_client
            import os
            url = st.secrets.get("SUPABASE_URL", "") or os.environ.get("SUPABASE_URL", "")
            key = st.secrets.get("SUPABASE_KEY", "") or os.environ.get("SUPABASE_KEY", "")
            st.session_state["supabase_client"] = create_client(url, key) if url and key else None
        except Exception:
            st.session_state["supabase_client"] = None
    return st.session_state["supabase_client"]


def save_cbat_session(subtest_id: str, score: int, resource_used: str, notes: str):
    """Save one CBAT practice session to Supabase (table: cbat_sessions)."""
    row = {
        "subtest_id": subtest_id,
        "date": date.today().isoformat(),
        "time": datetime.now().strftime("%H:%M"),
        "score": score,
        "resource_used": resource_used,
        "notes": notes[:500],
    }
    sb = _sb()
    if sb:
        try:
            sb.table("cbat_sessions").insert(row).execute()
            st.session_state.pop("_cbat_sessions_cache", None)
        except Exception as e:
            _add_local(row)
    else:
        _add_local(row)


def _add_local(row):
    sessions = st.session_state.get("_cbat_sessions", [])
    sessions.append(row)
    st.session_state["_cbat_sessions"] = sessions


def load_cbat_sessions(subtest_id: str = None) -> list:
    cache_key = f"_cbat_sessions_cache_{subtest_id or 'all'}"
    if cache_key in st.session_state:
        return st.session_state[cache_key]
    sb = _sb()
    rows = []
    if sb:
        try:
            q = sb.table("cbat_sessions").select("*").order("date", desc=True)
            if subtest_id:
                q = q.eq("subtest_id", subtest_id)
            rows = q.execute().data
        except Exception:
            rows = st.session_state.get("_cbat_sessions", [])
    else:
        rows = st.session_state.get("_cbat_sessions", [])
    if subtest_id:
        rows = [r for r in rows if r.get("subtest_id") == subtest_id]
    st.session_state[cache_key] = rows
    return rows


def get_subtest_summary(subtest_id: str) -> dict:
    rows = load_cbat_sessions(subtest_id)
    if not rows:
        return {"attempts": 0, "avg_score": 0, "last_score": None, "last_date": None, "trend": None}
    scores = [r["score"] for r in rows if r.get("score")]
    avg = round(sum(scores) / len(scores), 1) if scores else 0
    last = rows[0]
    trend = None
    if len(scores) >= 3:
        recent = scores[:3]
        older = scores[3:6]
        if older:
            trend = "up" if sum(recent) / len(recent) > sum(older) / len(older) else "down"
    return {
        "attempts": len(rows),
        "avg_score": avg,
        "last_score": last.get("score"),
        "last_date": last.get("date"),
        "trend": trend,
    }


# ─── AI Analysis ──────────────────────────────────────────────────────────────

def generate_cbat_analysis(all_sessions: list) -> str:
    """
    Send all CBAT session data to Claude and get a coached analysis.
    Returns plain text.
    """
    from ai_helper import ask_claude

    if not all_sessions:
        return "No CBAT practice sessions logged yet. Log at least a few sessions per subtest before running analysis."

    # Build summary per subtest
    from collections import defaultdict
    subtest_data = defaultdict(list)
    for s in all_sessions:
        subtest_data[s["subtest_id"]].append(s)

    summary_lines = []
    for st_id, sessions in sorted(subtest_data.items()):
        scores = [s["score"] for s in sessions if s.get("score")]
        notes = [s["notes"] for s in sessions if s.get("notes", "").strip()]
        avg = round(sum(scores) / len(scores), 1) if scores else 0
        last_score = scores[0] if scores else None
        # Find subtest name
        name = next((s["name"] for s in CBAT_SUBTESTS if s["id"] == st_id), st_id)
        category = next((s["category"] for s in CBAT_SUBTESTS if s["id"] == st_id), "")
        summary_lines.append(
            f"{name} ({category}): {len(sessions)} session(s), avg {avg}/5, last {last_score}/5"
            + (f", notes: {'; '.join(notes[-3:])}" if notes else "")
        )

    data_block = "\n".join(summary_lines)

    system = """You are a pilot aptitude coach analysing a candidate's CBAT practice data.
The CBAT (Computer-Based Aptitude Test) is a 23-subtest battery at RAF Cranwell for pilot selection.
Be direct, specific, and practical. No fluff. 3-4 paragraphs maximum.
End with exactly 3 concrete, prioritised suggestions for what to practise next and how."""

    user = f"""CBAT practice session summary:

{data_block}

Write a frank analysis:
1. Which subtests are weakest (lowest avg score)?
2. Which show the slowest improvement trend?
3. Are there patterns in the notes suggesting a specific error type?
4. End with 3 prioritised practice recommendations."""

    return ask_claude(system, user, max_tokens=600)


# ─── Main Page ────────────────────────────────────────────────────────────────

def page_cbat():
    dark = st.session_state.get("dark_mode", False)
    card_bg = "#161b22" if dark else "#ffffff"
    card_bdr = "#30363d" if dark else "#e8e8f0"
    text_col = "#e6edf3" if dark else "#1a1a2e"
    sub_col = "#8b949e" if dark else "#666"
    prog_bg = "#21262d" if dark else "#eeeeee"

    st.markdown("# 🎯 CBAT Practice Tracker")
    st.markdown(
        "*Source: [rafcbat.wordpress.com](https://rafcbat.wordpress.com) — 23 subtests tracked · "
        "Log practice sessions · On-demand AI coaching analysis*"
    )
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📋 Subtest Dashboard", "➕ Log Session", "🤖 AI Analysis"])

    # ── Tab 1: Dashboard ──────────────────────────────────────────────────────
    with tab1:
        all_sessions = load_cbat_sessions()

        # Overall summary cards
        total_sessions = len(all_sessions)
        subtests_practiced = len(set(s["subtest_id"] for s in all_sessions))
        all_scores = [s["score"] for s in all_sessions if s.get("score")]
        overall_avg = round(sum(all_scores) / len(all_scores), 1) if all_scores else 0

        c1, c2, c3, c4 = st.columns(4)
        for col, label, val, color in [
            (c1, "Total Sessions", total_sessions, "#3498db"),
            (c2, "Subtests Practiced", f"{subtests_practiced}/23", "#9b59b6"),
            (c3, "Overall Avg Score", f"{overall_avg}/5" if all_scores else "—", "#27ae60"),
            (c4, "Subtests Remaining", 23 - subtests_practiced, "#e74c3c"),
        ]:
            with col:
                st.markdown(
                    f'<div style="background:{card_bg};border:1px solid {card_bdr};border-left:4px solid {color};'
                    f'border-radius:10px;padding:.9rem 1rem;text-align:center">'
                    f'<div style="font-size:1.5rem;font-weight:700;color:{text_col}">{val}</div>'
                    f'<div style="font-size:.72rem;color:{sub_col};text-transform:uppercase;letter-spacing:.06em">{label}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )

        st.markdown("<br>", unsafe_allow_html=True)

        # Group by category
        categories = list(dict.fromkeys(s["category"] for s in CBAT_SUBTESTS))
        for category in categories:
            cat_tests = [s for s in CBAT_SUBTESTS if s["category"] == category]
            color = CATEGORY_COLORS.get(category, "#888")

            st.markdown(
                f'<div style="background:{card_bg};border:1px solid {card_bdr};border-left:4px solid {color};'
                f'border-radius:10px;padding:.6rem 1rem;margin-bottom:.4rem">'
                f'<span style="font-size:.8rem;font-weight:700;color:{color};text-transform:uppercase;letter-spacing:.06em">'
                f'{category}</span></div>',
                unsafe_allow_html=True,
            )

            for test in cat_tests:
                summary = get_subtest_summary(test["id"])
                attempts = summary["attempts"]
                avg = summary["avg_score"]
                last = summary["last_score"]
                last_date = summary["last_date"]
                trend = summary["trend"]

                trend_icon = "" if not trend else ("📈" if trend == "up" else "📉")
                score_color = "#27ae60" if avg >= 4 else "#f39c12" if avg >= 3 else "#e74c3c" if avg > 0 else sub_col
                bar_width = int(avg / 5 * 100) if avg else 0

                with st.expander(
                    f"{test['abbr']} — {test['name']}  "
                    f"{'  · ' + str(attempts) + ' session(s) · avg ' + str(avg) + '/5 ' + trend_icon if attempts else '  · Not yet practiced'}"
                ):
                    col_a, col_b = st.columns([2, 1])
                    with col_a:
                        st.markdown(
                            f'<p style="color:{sub_col};font-size:.85rem;margin-bottom:.4rem">{test["description"]}</p>'
                            f'<p style="color:{sub_col};font-size:.82rem"><em>💡 {test["tips"]}</em></p>',
                            unsafe_allow_html=True,
                        )
                        if attempts:
                            st.markdown(
                                f'<div style="margin:.5rem 0">'
                                f'<div style="display:flex;justify-content:space-between;font-size:.78rem;color:{sub_col};margin-bottom:2px">'
                                f'<span>Avg score</span><span style="color:{score_color};font-weight:700">{avg}/5</span></div>'
                                f'<div style="background:{prog_bg};border-radius:4px;height:6px;overflow:hidden">'
                                f'<div style="width:{bar_width}%;height:100%;background:{score_color};border-radius:4px"></div>'
                                f'</div>'
                                f'<div style="font-size:.72rem;color:{sub_col};margin-top:2px">'
                                f'Last: {last}/5 on {last_date}</div>'
                                f'</div>',
                                unsafe_allow_html=True,
                            )
                    with col_b:
                        st.markdown("**Practice resources:**")
                        if test["resources"]:
                            for r in test["resources"]:
                                st.markdown(f"• [{r['name']}]({r['url']})")
                        else:
                            st.markdown(f"• [CBAT Guide for {test['abbr']}](https://rafcbat.wordpress.com/home/)")
                        st.markdown(f"• [rafcbat.wordpress.com](https://rafcbat.wordpress.com/home/)")

                    # Recent sessions
                    recent = load_cbat_sessions(test["id"])[:5]
                    if recent:
                        st.markdown("**Recent sessions:**")
                        for sess in recent:
                            score_l, score_c = SCORE_LABELS.get(sess.get("score", 0), ("—", sub_col))
                            st.markdown(
                                f'<div style="background:{card_bg};border:1px solid {card_bdr};border-radius:6px;'
                                f'padding:.4rem .7rem;margin:.2rem 0;font-size:.8rem">'
                                f'<span style="color:{score_c};font-weight:600">{score_l}</span>'
                                f'<span style="color:{sub_col}"> · {sess.get("date", "")} · {sess.get("resource_used", "—")}</span>'
                                + (f'<br><span style="color:{sub_col}">{sess.get("notes", "")}</span>' if sess.get("notes") else "")
                                + f'</div>',
                                unsafe_allow_html=True,
                            )

                    # Quick-log from dashboard
                    with st.form(f"quicklog_{test['id']}"):
                        ql1, ql2, ql3 = st.columns([1, 2, 1])
                        with ql1:
                            ql_score = st.selectbox("Score", [1, 2, 3, 4, 5], index=2, key=f"ql_score_{test['id']}")
                        with ql2:
                            ql_notes = st.text_input("Notes (optional)", placeholder="e.g. ran out of time on last 3", key=f"ql_notes_{test['id']}")
                        with ql3:
                            ql_resource = st.text_input("Resource", placeholder="e.g. Fibonicci", key=f"ql_resource_{test['id']}")
                        if st.form_submit_button("Log session", use_container_width=True):
                            save_cbat_session(test["id"], ql_score, ql_resource, ql_notes)
                            st.success(f"Session logged for {test['abbr']}!")
                            st.rerun()

    # ── Tab 2: Log Session ────────────────────────────────────────────────────
    with tab2:
        st.markdown("### Log a CBAT Practice Session")
        st.markdown("*Log sessions here, or use the quick-log inside each subtest on the Dashboard tab.*")

        subtest_options = {f"{s['abbr']} — {s['name']}": s["id"] for s in CBAT_SUBTESTS}

        with st.form("log_cbat_session"):
            c1, c2 = st.columns(2)
            with c1:
                selected_label = st.selectbox("Subtest", list(subtest_options.keys()))
                selected_id = subtest_options[selected_label]
            with c2:
                score = st.selectbox(
                    "Self-rated performance",
                    options=list(SCORE_LABELS.keys()),
                    format_func=lambda x: SCORE_LABELS[x][0],
                    index=2,
                )

            resource = st.text_input(
                "Resource used",
                placeholder="e.g. Fibonicci SpaR, That Quiz, militaryaptitude.com, Military Aptitude course..."
            )
            notes = st.text_area(
                "Notes — what happened? What went wrong? Be specific.",
                placeholder="e.g. 'Ran out of time on last 4 questions' · 'Kept confusing left bank vs right bank on INSC' · 'Improved significantly vs last week'",
                height=100
            )

            # Show tips for selected subtest
            test_info = next((s for s in CBAT_SUBTESTS if s["id"] == selected_id), None)
            if test_info:
                st.markdown(
                    f'<div style="background:#f0f7ff;border-left:3px solid #3498db;border-radius:0 8px 8px 0;'
                    f'padding:.6rem .9rem;font-size:.83rem;color:#1a1a2e">'
                    f'<strong>💡 {test_info["abbr"]} tip:</strong> {test_info["tips"]}</div>',
                    unsafe_allow_html=True,
                )

            if st.form_submit_button("✅ Log this session", use_container_width=True):
                if not resource.strip():
                    st.warning("Please note which resource you used — even if it's 'no tool, self-timed'.")
                else:
                    save_cbat_session(selected_id, score, resource, notes)
                    st.success(f"Session logged! {SCORE_LABELS[score][0]} for {selected_label}")
                    st.rerun()

    # ── Tab 3: AI Analysis ────────────────────────────────────────────────────
    with tab3:
        st.markdown("### 🤖 AI Coaching Analysis")
        st.markdown(
            "Claude reads all your logged CBAT sessions and returns a frank coaching summary: "
            "which subtests are weakest, which are plateauing, patterns in your notes, and 3 prioritised actions."
        )

        all_sessions = load_cbat_sessions()
        n_sessions = len(all_sessions)
        n_subtests = len(set(s["subtest_id"] for s in all_sessions))

        if n_sessions < 5:
            st.info(
                f"You have {n_sessions} session(s) logged across {n_subtests} subtest(s). "
                "Log at least 5 sessions (ideally spread across several subtests) to get a useful analysis."
            )

        col_a, col_b = st.columns([2, 1])
        with col_a:
            st.markdown(
                f'<div style="background:{card_bg};border:1px solid {card_bdr};border-radius:10px;padding:.8rem 1rem;font-size:.85rem">'
                f'<strong style="color:{text_col}">{n_sessions}</strong> <span style="color:{sub_col}">sessions logged · </span>'
                f'<strong style="color:{text_col}">{n_subtests}</strong> <span style="color:{sub_col}">subtests covered</span>'
                f'</div>',
                unsafe_allow_html=True,
            )

        with col_b:
            run_analysis = st.button("🔍 Run AI Analysis", use_container_width=True, disabled=(n_sessions == 0))

        if run_analysis:
            with st.spinner("Claude is analysing your CBAT practice data..."):
                analysis = generate_cbat_analysis(all_sessions)
            st.session_state["_cbat_analysis"] = analysis
            st.session_state["_cbat_analysis_date"] = date.today().isoformat()

        if st.session_state.get("_cbat_analysis"):
            analysis_date = st.session_state.get("_cbat_analysis_date", "")
            st.markdown(f"*Analysis generated: {analysis_date}*")
            st.markdown(
                f'<div style="background:{card_bg};border:1px solid {card_bdr};border-radius:12px;'
                f'padding:1.4rem 1.8rem;margin-top:.8rem;font-size:.92rem;line-height:1.8;color:{text_col}">'
                + st.session_state["_cbat_analysis"].replace("\n", "<br>")
                + "</div>",
                unsafe_allow_html=True,
            )
            if st.button("🗑 Clear analysis", key="clear_cbat_analysis"):
                st.session_state.pop("_cbat_analysis", None)
                st.rerun()

        st.markdown("---")
        st.markdown("#### 📚 CBAT Practice Resources")
        st.markdown(
            "The site [rafcbat.wordpress.com](https://rafcbat.wordpress.com) "
            "is the best unofficial guide. Key free resources:"
        )
        resource_rows = [
            ("All subtests — guide + context", "rafcbat.wordpress.com/home/", "https://rafcbat.wordpress.com/home/"),
            ("Instrument Comprehension (INSC)", "Fibonicci Pilot Test", "https://www.fibonicci.com/spatial-awareness/airforce-pilot-test/"),
            ("Instrument Comprehension (INSC)", "AFOQT Instrument Test", "https://afoqtpracticetest.com/instrument-comprehension/"),
            ("Spatial Reasoning (VIS, SIT)", "Fibonicci SpaR", "https://www.fibonicci.com/spatial--awareness/spatial-reasoning-test/hard/"),
            ("Angles & Bearings (ABD)", "Khan Academy Angles", "https://www.khanacademy.org/math/basic-geo/basic-geo-angle/measure-angles/e/estimate-angle-measures"),
            ("Numerical (ANT, NOT, CLAN)", "That Quiz Arithmetic", "https://www.thatquiz.org/tq-1/math/arithmetic/"),
            ("ANT — Speed/Distance/Time", "speeddistancetime.info", "https://www.speeddistancetime.info/test"),
            ("ANT — Fuel Calculations", "speeddistancetime.info/fuel", "https://www.speeddistancetime.info/fuel-test"),
            ("Verbal Logic (VLT)", "Practice Aptitude Tests", "https://www.practiceaptitudetests.com/verbal-reasoning-tests/"),
            ("Full CBAT suite (paid)", "Military Aptitude course", "https://www.militaryaptitude.com/s/store/courses/description/Military-Aviation-Cognitive-Testing-Online-Course"),
        ]

        for subtest_label, name, url in resource_rows:
            st.markdown(
                f'<div style="background:{card_bg};border:1px solid {card_bdr};border-radius:6px;'
                f'padding:.4rem .8rem;margin:.2rem 0;font-size:.83rem">'
                f'<span style="color:{sub_col}">{subtest_label}</span> · '
                f'<a href="{url}" target="_blank">{name}</a>'
                f'</div>',
                unsafe_allow_html=True,
            )
