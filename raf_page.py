"""
RAF Application page — replaces page_raf() in app.py.
Import this as: from raf_page import page_raf

Features:
  - OASC Tier 1/2/3 priority system (confidence rating 0–3 per lesson)
  - Tier 1 readiness panel (% at confidence 3)
  - CBAT button → routes to cbat_page
  - AI OASC analysis (on-demand, reads confidence scores)
  - Confidence ratings saved to Supabase progress table
"""

import streamlit as st
from datetime import date


# ─── Confidence helpers ───────────────────────────────────────────────────────

def _save_confidence(lesson_id: str, confidence: int):
    """Upsert confidence rating into Supabase progress table."""
    from datetime import datetime
    try:
        from app import _sb
        sb = _sb()
        if sb:
            sb.table("progress").upsert({
                "lesson_id": lesson_id,
                "confidence": confidence,
                "updated_at": datetime.now().isoformat(),
            }).execute()
            st.session_state.pop("_progress_cache", None)
    except Exception:
        pass
    progress = st.session_state.get("_progress_cache", st.session_state.get("_progress", {}))
    progress.setdefault(lesson_id, {})["confidence"] = confidence
    if "_progress_cache" in st.session_state:
        st.session_state["_progress_cache"][lesson_id] = progress[lesson_id]


def _load_progress():
    try:
        from app import load_progress
        return load_progress()
    except Exception:
        return st.session_state.get("_progress_cache", {})


# ─── OASC AI Analysis ─────────────────────────────────────────────────────────

def generate_oasc_readiness_analysis(progress: dict) -> str:
    """
    Send OASC topic confidence scores to Claude for a coaching analysis.
    Returns plain text.
    """
    from ai_helper import ask_claude
    from data.raf_curriculum import RAF_CURRICULUM, CONFIDENCE_LABELS

    lines = []
    for unit_name, unit_data in RAF_CURRICULUM.items():
        tier = unit_data.get("oasc_tier", 0)
        for lesson in unit_data["lessons"]:
            conf = progress.get(lesson["id"], {}).get("confidence", 0)
            conf_label = CONFIDENCE_LABELS.get(conf, ("Unknown", ""))[0]
            lines.append(f"[Tier {tier}] {lesson['title']}: {conf_label} ({conf}/3)")

    data_block = "\n".join(lines)

    system = """You are an RAF OASC preparation coach.
A candidate has self-rated their confidence on each OASC knowledge topic on a 3-point scale:
1 = Aware (knows it exists, couldn't explain it)
2 = Can explain (might stumble under pressure)
3 = Interview-ready (could answer cold in the OASC interview)

Be direct, specific, and honest. No fluff. 3-4 paragraphs.
End with exactly 3 concrete study recommendations for this week, prioritised by OASC criticality."""

    user = f"""Candidate's OASC topic confidence ratings:

{data_block}

Write a frank coaching analysis:
1. Which Tier 1 (OASC-Critical) topics are not yet at confidence 3?
2. Are there patterns — e.g. aviation knowledge weak, current affairs not started?
3. What is the honest assessment of OASC readiness based on these scores?
4. End with 3 prioritised study actions."""

    return ask_claude(system, user, max_tokens=600)


# ─── Main Page ────────────────────────────────────────────────────────────────

def page_raf():
    from data.raf_curriculum import (
        RAF_CURRICULUM, TIER_LABELS, CONFIDENCE_LABELS,
        get_tier1_readiness, get_raf_unit_progress_summary
    )

    dark = st.session_state.get("dark_mode", False)
    card_bg = "#161b22" if dark else "#ffffff"
    card_bdr = "#30363d" if dark else "#e8e8f0"
    text_col = "#e6edf3" if dark else "#1a1a2e"
    sub_col = "#8b949e" if dark else "#666"
    prog_bg = "#21262d" if dark else "#eeeeee"

    st.markdown("# ✈️ RAF Application")
    st.markdown("*Targeted prep: Medical → CBAT → OASC → IOT*")
    st.markdown("---")

    progress = _load_progress()

    # ── Top nav ───────────────────────────────────────────────────────────────
    n1, n2, n3, n4 = st.columns(4)
    with n1:
        if st.button("📊 OASC Overview", use_container_width=True, key="raf_nav_overview"):
            st.session_state["raf_view"] = "overview"
            st.rerun()
    with n2:
        if st.button("📚 Curriculum", use_container_width=True, key="raf_nav_curr"):
            st.session_state["raf_view"] = "curriculum"
            st.rerun()
    with n3:
        if st.button("🎯 CBAT Tracker", use_container_width=True, key="raf_nav_cbat"):
            st.session_state["current_page"] = "cbat"
            st.rerun()
    with n4:
        if st.button("🤖 OASC Analysis", use_container_width=True, key="raf_nav_analysis"):
            st.session_state["raf_view"] = "analysis"
            st.rerun()

    if "raf_view" not in st.session_state:
        st.session_state["raf_view"] = "overview"

    view = st.session_state["raf_view"]
    st.markdown("---")

    # ─────────────────────────────────────────────────────────────────────────
    # VIEW: OASC Overview
    # ─────────────────────────────────────────────────────────────────────────
    if view == "overview":
        t1_stats = get_tier1_readiness(progress)

        # Tier 1 readiness headline
        ready_pct = t1_stats["ready_pct"]
        ready_color = "#27ae60" if ready_pct >= 75 else "#f39c12" if ready_pct >= 40 else "#e74c3c"

        st.markdown(
            f'<div style="background:linear-gradient(135deg,#1a0505,#3d0000);border-radius:16px;'
            f'padding:1.4rem 1.8rem;margin-bottom:1.2rem;border:1px solid #5a0000;color:white">'
            f'<div style="font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:#c47c7c;margin-bottom:.4rem">'
            f'🔴 Tier 1 OASC-Critical Readiness</div>'
            f'<div style="display:flex;align-items:center;gap:1.5rem;flex-wrap:wrap">'
            f'<div style="font-size:2.5rem;font-weight:700;color:{ready_color}">{ready_pct}%</div>'
            f'<div>'
            f'<div style="font-size:.9rem;color:#ddd">topics at interview-ready (confidence 3)</div>'
            f'<div style="font-size:.8rem;color:#aaa">{t1_stats["at_3"]}/{t1_stats["total"]} topics ready · '
            f'{t1_stats["at_2"]} can explain · {t1_stats["at_1"]} aware · {t1_stats["at_0"]} not started</div>'
            f'</div></div>'
            f'<div style="background:rgba(255,255,255,.1);border-radius:4px;height:8px;margin-top:.8rem;overflow:hidden">'
            f'<div style="width:{ready_pct}%;height:100%;background:{ready_color};border-radius:4px"></div>'
            f'</div></div>',
            unsafe_allow_html=True,
        )

        # Per-tier summary cards
        tier_order = ["Tier 1 — OASC Critical", "Tier 2 — Good to Know", "Tier 3 — Post-Offer"]
        cols = st.columns(3)
        for i, unit_name in enumerate(tier_order):
            unit_data = RAF_CURRICULUM.get(unit_name, {})
            lessons = unit_data.get("lessons", [])
            tier_num = unit_data.get("oasc_tier", i + 1)
            tier_label, tier_desc, tier_color = TIER_LABELS.get(tier_num, (unit_name, "", "#888"))
            total = len(lessons)
            confidences = [progress.get(l["id"], {}).get("confidence", 0) for l in lessons]
            at_3 = sum(1 for c in confidences if c == 3)
            avg_conf = round(sum(confidences) / total, 1) if total else 0
            pct = round(at_3 / total * 100) if total else 0

            with cols[i]:
                st.markdown(
                    f'<div style="background:{card_bg};border:1px solid {card_bdr};border-left:4px solid {tier_color};'
                    f'border-radius:12px;padding:1rem 1.1rem">'
                    f'<div style="font-size:.7rem;color:{tier_color};font-weight:700;text-transform:uppercase;'
                    f'letter-spacing:.06em;margin-bottom:.3rem">{tier_label}</div>'
                    f'<div style="font-size:.75rem;color:{sub_col};margin-bottom:.5rem">{tier_desc}</div>'
                    f'<div style="font-size:1.4rem;font-weight:700;color:{text_col}">{at_3}/{total}</div>'
                    f'<div style="font-size:.75rem;color:{sub_col}">interview-ready · avg {avg_conf}/3</div>'
                    f'<div style="background:{prog_bg};border-radius:4px;height:5px;margin-top:.5rem;overflow:hidden">'
                    f'<div style="width:{pct}%;height:100%;background:{tier_color};border-radius:4px"></div>'
                    f'</div></div>',
                    unsafe_allow_html=True,
                )

        st.markdown("<br>", unsafe_allow_html=True)

        # CBAT status card
        try:
            from cbat_page import load_cbat_sessions
            cbat_sessions = load_cbat_sessions()
            n_cbat = len(cbat_sessions)
            n_subtests = len(set(s["subtest_id"] for s in cbat_sessions))
            cbat_scores = [s["score"] for s in cbat_sessions if s.get("score")]
            cbat_avg = round(sum(cbat_scores) / len(cbat_scores), 1) if cbat_scores else 0
        except Exception:
            n_cbat, n_subtests, cbat_avg = 0, 0, 0

        st.markdown(
            f'<div style="background:{card_bg};border:1px solid {card_bdr};border-left:4px solid #9b59b6;'
            f'border-radius:12px;padding:1rem 1.4rem;margin-bottom:1rem">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.5rem">'
            f'<div>'
            f'<div style="font-size:.75rem;color:#9b59b6;font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.2rem">🎯 CBAT Practice</div>'
            f'<div style="font-size:.9rem;color:{text_col}">{n_cbat} session(s) logged · {n_subtests}/23 subtests practiced'
            + (f' · avg {cbat_avg}/5' if cbat_avg else '')
            + f'</div>'
            f'<div style="font-size:.75rem;color:{sub_col}">Click CBAT Tracker above to log sessions and run AI coaching analysis</div>'
            f'</div></div></div>',
            unsafe_allow_html=True,
        )

        # Top-priority topics to improve (Tier 1, confidence < 3)
        st.markdown("### 🎯 Priority Topics to Bring to Confidence 3")
        tier1_lessons = RAF_CURRICULUM.get("Tier 1 — OASC Critical", {}).get("lessons", [])
        not_ready = [
            (l, progress.get(l["id"], {}).get("confidence", 0))
            for l in tier1_lessons
            if progress.get(l["id"], {}).get("confidence", 0) < 3
        ]
        not_ready.sort(key=lambda x: x[1])  # lowest confidence first

        if not not_ready:
            st.success("✅ All Tier 1 topics are at confidence 3 — interview-ready!")
        else:
            for lesson, conf in not_ready[:6]:
                conf_label, conf_color = CONFIDENCE_LABELS.get(conf, ("Not started", "#999"))
                tier_color = "#b71c1c"
                st.markdown(
                    f'<div style="background:{card_bg};border:1px solid {card_bdr};border-left:3px solid {tier_color};'
                    f'border-radius:8px;padding:.6rem 1rem;margin:.2rem 0;'
                    f'display:flex;justify-content:space-between;align-items:center">'
                    f'<div>'
                    f'<span style="font-size:.88rem;font-weight:600;color:{text_col}">{lesson["title"]}</span>'
                    f'<span style="font-size:.75rem;color:{sub_col}"> — {lesson.get("subtitle","")}</span>'
                    f'</div>'
                    f'<span style="font-size:.75rem;font-weight:600;color:{conf_color};white-space:nowrap;margin-left:.5rem">'
                    f'{conf_label}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            if len(not_ready) > 6:
                st.markdown(f"*…and {len(not_ready) - 6} more Tier 1 topics. Go to Curriculum to rate them all.*")

    # ─────────────────────────────────────────────────────────────────────────
    # VIEW: Curriculum (with confidence ratings)
    # ─────────────────────────────────────────────────────────────────────────
    elif view == "curriculum":
        st.markdown("### 📚 RAF Knowledge Curriculum")
        st.markdown(
            "*Rate your confidence on each topic: **1** = aware · **2** = can explain · **3** = interview-ready*"
        )
        st.markdown("<br>", unsafe_allow_html=True)

        for unit_name, unit_data in RAF_CURRICULUM.items():
            tier_num = unit_data.get("oasc_tier", 0)
            tier_label, tier_desc, tier_color = TIER_LABELS.get(tier_num, (unit_name, "", "#888"))
            lessons = unit_data["lessons"]
            confidences = [progress.get(l["id"], {}).get("confidence", 0) for l in lessons]
            at_3 = sum(1 for c in confidences if c == 3)
            avg_conf = round(sum(confidences) / len(lessons), 1) if lessons else 0

            with st.expander(
                f"**{tier_label}** — {unit_data['title']} | {at_3}/{len(lessons)} interview-ready",
                expanded=(tier_num == 1),
            ):
                st.markdown(
                    f'<div style="background:{card_bg};border-left:4px solid {tier_color};border-radius:0 8px 8px 0;'
                    f'padding:.5rem 1rem;margin-bottom:.8rem;font-size:.83rem;color:{sub_col}">'
                    f'<strong style="color:{tier_color}">{tier_desc}</strong> — {unit_data["description"]}'
                    f'</div>',
                    unsafe_allow_html=True,
                )

                for lesson in lessons:
                    lid = lesson["id"]
                    conf = progress.get(lid, {}).get("confidence", 0)
                    status = progress.get(lid, {}).get("status", "not_started")
                    conf_label, conf_color = CONFIDENCE_LABELS.get(conf, ("Not started", "#999"))

                    col_l, col_r = st.columns([4, 1])
                    with col_l:
                        status_icon = "✅" if status == "completed" else "▶️" if status == "in_progress" else "○"
                        st.markdown(
                            f'<div style="background:{card_bg};border:1px solid {card_bdr};border-left:3px solid {tier_color};'
                            f'border-radius:8px;padding:.55rem .9rem;margin:.2rem 0">'
                            f'<div style="display:flex;justify-content:space-between;align-items:center">'
                            f'<div>'
                            f'<span style="font-size:.78rem;color:{sub_col}">{status_icon} {lid}</span> '
                            f'<span style="font-size:.88rem;font-weight:600;color:{text_col}">{lesson["title"]}</span>'
                            f'<br><span style="font-size:.76rem;color:{sub_col}">{lesson.get("subtitle", "")}</span>'
                            f'</div>'
                            f'<span style="font-size:.75rem;font-weight:700;color:{conf_color};white-space:nowrap;margin-left:.5rem">'
                            f'{conf_label}</span>'
                            f'</div></div>',
                            unsafe_allow_html=True,
                        )
                        # Open lesson button
                        if st.button(f"Open {lid}", key=f"open_raf_{lid}", use_container_width=False):
                            st.session_state["R_active_lesson"] = lid
                            st.session_state["raf_view"] = "lesson"
                            st.rerun()

                    with col_r:
                        # Confidence selector
                        new_conf = st.selectbox(
                            "Confidence",
                            options=[0, 1, 2, 3],
                            index=conf,
                            format_func=lambda x: CONFIDENCE_LABELS[x][0],
                            key=f"conf_{lid}",
                            label_visibility="collapsed",
                        )
                        if new_conf != conf:
                            _save_confidence(lid, new_conf)
                            st.rerun()

    # ─────────────────────────────────────────────────────────────────────────
    # VIEW: Lesson Viewer
    # ─────────────────────────────────────────────────────────────────────────
    elif view == "lesson":
        try:
            from app import render_lesson_view
            from data.raf_curriculum import RAF_CURRICULUM
            active = st.session_state.get("R_active_lesson")
            if not active:
                st.info("Select a lesson from the Curriculum tab.")
                return

            lesson = None
            for unit_data in RAF_CURRICULUM.values():
                for l in unit_data["lessons"]:
                    if l["id"] == active:
                        lesson = l
                        break

            if not lesson:
                st.error(f"Lesson {active} not found.")
                return

            if st.button("← Back to Curriculum", key="raf_back"):
                st.session_state["raf_view"] = "curriculum"
                st.session_state.pop("R_active_lesson", None)
                st.rerun()

            render_lesson_view(
                lesson, progress.get(active, {}), active,
                lesson.get("unit", "Tier 1 — OASC Critical"),
                RAF_CURRICULUM.get(lesson.get("unit", "Tier 1 — OASC Critical"), {}).get("color", "#b71c1c"),
                RAF_CURRICULUM.get(lesson.get("unit", "Tier 1 — OASC Critical"), {}).get("level", ""),
            )
        except Exception as e:
            st.error(f"Error loading lesson viewer: {e}")
            st.info("Make sure render_lesson_view is exported from app.py.")

    # ─────────────────────────────────────────────────────────────────────────
    # VIEW: OASC AI Analysis
    # ─────────────────────────────────────────────────────────────────────────
    elif view == "analysis":
        dark2 = st.session_state.get("dark_mode", False)
        cb2 = "#161b22" if dark2 else "#ffffff"
        cd2 = "#30363d" if dark2 else "#e8e8f0"
        tc2 = "#e6edf3" if dark2 else "#1a1a2e"

        st.markdown("### 🤖 OASC Readiness Analysis")
        st.markdown(
            "Claude reads your confidence ratings across all RAF knowledge topics and gives you a frank "
            "assessment of your OASC readiness — what's strong, what's weak, and exactly what to study next."
        )

        from data.raf_curriculum import RAF_CURRICULUM, CONFIDENCE_LABELS
        t1_stats = get_tier1_readiness(progress)

        # Quick stats
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(
                f'<div style="background:{cb2};border:1px solid {cd2};border-radius:8px;padding:.7rem .9rem;text-align:center">'
                f'<div style="font-size:1.4rem;font-weight:700;color:#b71c1c">{t1_stats["ready_pct"]}%</div>'
                f'<div style="font-size:.72rem;color:{sub_col}">Tier 1 interview-ready</div></div>',
                unsafe_allow_html=True,
            )
        with c2:
            total_rated = sum(1 for l in [l for u in RAF_CURRICULUM.values() for l in u["lessons"]] if progress.get(l["id"], {}).get("confidence", 0) > 0)
            total_all = sum(len(u["lessons"]) for u in RAF_CURRICULUM.values())
            st.markdown(
                f'<div style="background:{cb2};border:1px solid {cd2};border-radius:8px;padding:.7rem .9rem;text-align:center">'
                f'<div style="font-size:1.4rem;font-weight:700;color:{tc2}">{total_rated}/{total_all}</div>'
                f'<div style="font-size:.72rem;color:{sub_col}">topics rated</div></div>',
                unsafe_allow_html=True,
            )
        with c3:
            t1_at0 = t1_stats["at_0"]
            st.markdown(
                f'<div style="background:{cb2};border:1px solid {cd2};border-radius:8px;padding:.7rem .9rem;text-align:center">'
                f'<div style="font-size:1.4rem;font-weight:700;color:{"#e74c3c" if t1_at0 > 0 else "#27ae60"}">{t1_at0}</div>'
                f'<div style="font-size:.72rem;color:{sub_col}">Tier 1 topics not started</div></div>',
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        if total_rated < 3:
            st.info("Rate at least a few topics on the Curriculum tab before running analysis — the more ratings, the better the coaching.")

        run = st.button("🔍 Run OASC Readiness Analysis", use_container_width=True)
        if run:
            with st.spinner("Claude is analysing your OASC readiness..."):
                analysis = generate_oasc_readiness_analysis(progress)
            st.session_state["_oasc_analysis"] = analysis
            st.session_state["_oasc_analysis_date"] = date.today().isoformat()

        if st.session_state.get("_oasc_analysis"):
            adate = st.session_state.get("_oasc_analysis_date", "")
            st.markdown(f"*Analysis generated: {adate}*")
            st.markdown(
                f'<div style="background:{cb2};border:1px solid {cd2};border-radius:12px;'
                f'padding:1.4rem 1.8rem;margin-top:.8rem;font-size:.92rem;line-height:1.8;color:{tc2}">'
                + st.session_state["_oasc_analysis"].replace("\n", "<br>")
                + "</div>",
                unsafe_allow_html=True,
            )
            if st.button("🗑 Clear analysis", key="clear_oasc_analysis"):
                st.session_state.pop("_oasc_analysis", None)
                st.rerun()
