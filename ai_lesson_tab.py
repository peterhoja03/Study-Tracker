"""
AI Lesson Tab — renders the AI tools section inside render_lesson_viewer.

USAGE: Add this import to app.py:
    from ai_lesson_tab import render_ai_lesson_tab

Then add one line at the bottom of render_lesson_viewer(), after the existing tabs:
    render_ai_lesson_tab(lesson, lesson_prog)
"""

import streamlit as st
from datetime import date
from ai_helper import (
    mark_active_recall,
    analyse_brain_dump,
    check_feynman,
    check_working,
    check_korean_writing,
    mark_raf_answer,
    generate_review_questions,
    analyse_lesson_progress,
)
from store_weakness import log_weakness, load_weakness_log, get_lesson_weakness_summary


def render_ai_lesson_tab(lesson: dict, lesson_prog: dict):
    """
    Renders the AI tools section below the existing lesson tabs.
    Paste one call to this function at the end of render_lesson_viewer().
    """
    lesson_id = lesson["id"]
    stream = lesson_id[:1]

    st.markdown("---")
    st.markdown(
        '<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">'
        '<span style="font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;'
        'color:#534AB7;background:#EEEDFE;padding:.2rem .7rem;border-radius:4px">🤖 AI tools for this lesson</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Build tab list based on stream
    tab_labels = ["🧠 Active recall", "🔍 Brain dump", "✍️ Feynman check", "📈 My progress"]
    if stream == "P":
        tab_labels.insert(3, "🔢 Show working")
    elif stream == "U":
        tab_labels.insert(3, "🇰🇷 Korean writing")
    elif stream == "R":
        tab_labels.insert(3, "🎖️ Interview practice")

    tabs = st.tabs(tab_labels)
    tab_idx = 0

    # ── Active Recall ──────────────────────────────────────────────────────────
    with tabs[tab_idx]:
        tab_idx += 1
        _render_active_recall(lesson, lesson_prog)

    # ── Brain Dump ─────────────────────────────────────────────────────────────
    with tabs[tab_idx]:
        tab_idx += 1
        _render_brain_dump(lesson)

    # ── Feynman Check ──────────────────────────────────────────────────────────
    with tabs[tab_idx]:
        tab_idx += 1
        _render_feynman_check(lesson)

    # ── Stream-specific tool ───────────────────────────────────────────────────
    with tabs[tab_idx]:
        tab_idx += 1
        if stream == "P":
            _render_show_working(lesson)
        elif stream == "U":
            _render_korean_writing(lesson)
        elif stream == "R":
            _render_raf_interview(lesson)

    # ── My Progress ───────────────────────────────────────────────────────────
    with tabs[tab_idx]:
        _render_lesson_progress(lesson)


# ─── Active Recall ─────────────────────────────────────────────────────────────

def _render_active_recall(lesson: dict, lesson_prog: dict):
    lesson_id = lesson["id"]
    st.markdown("Answer a question — Claude marks it against this lesson's knowledge bank.")

    # Check if we should use generated or fixed questions
    weakness_log = load_weakness_log(lesson_id=lesson_id)
    summary = get_lesson_weakness_summary(lesson_id)

    use_generated = st.checkbox(
        "Generate fresh question from knowledge bank",
        value=bool(lesson.get("knowledge_bank")),
        key=f"ai_gen_{lesson_id}",
    )

    if use_generated and lesson.get("knowledge_bank"):
        if st.button("Generate question", key=f"ai_genq_{lesson_id}"):
            with st.spinner("Generating..."):
                result = generate_review_questions(lesson, weakness_log, n=1)
            questions = result.get("questions", [])
            if questions:
                st.session_state[f"ai_q_{lesson_id}"] = questions[0]["question"]
                tw = questions[0].get("targets_weakness", False)
                if tw and summary["top_gaps"]:
                    st.caption(f"Targeting known gap: {summary['top_gaps'][0]}")

        question = st.session_state.get(f"ai_q_{lesson_id}", "")
        if question:
            st.markdown(f'<div style="background:#f8f9ff;border-left:3px solid #534AB7;border-radius:0 8px 8px 0;'
                        f'padding:.8rem 1rem;margin:.5rem 0;font-weight:500">{question}</div>',
                        unsafe_allow_html=True)
    else:
        # Use fixed recall questions from lesson
        questions_list = lesson.get("active_recall_questions", [])
        if not questions_list:
            st.info("No questions defined for this lesson yet.")
            return
        q_labels = [f"Q{i+1}: {q[:60]}..." if len(q) > 60 else f"Q{i+1}: {q}" for i, q in enumerate(questions_list)]
        selected_idx = st.selectbox("Select question:", range(len(q_labels)), format_func=lambda i: q_labels[i], key=f"ai_qsel_{lesson_id}")
        question = questions_list[selected_idx]
        st.markdown(f'<div style="background:#f8f9ff;border-left:3px solid #534AB7;border-radius:0 8px 8px 0;'
                    f'padding:.8rem 1rem;margin:.5rem 0;font-weight:500">{question}</div>',
                    unsafe_allow_html=True)

    answer = st.text_area("Your answer:", height=120, placeholder="Write your full answer...", key=f"ai_ans_{lesson_id}")

    if st.button("Mark my answer", use_container_width=True, key=f"ai_mark_{lesson_id}") and answer.strip():
        with st.spinner("Marking..."):
            result = mark_active_recall(lesson, question, answer)
        if result.get("error"):
            st.error(f"Could not mark: {result['error']}")
        else:
            _render_recall_result(result)
            # Save to weakness_log
            log_weakness(
                lesson_id=lesson["id"],
                score=result.get("score", 0),
                question_type="active_recall",
                weakness_categories=result.get("weakness_categories", []),
                specific_gaps=result.get("gaps", []),
                raw_answer=answer,
            )
            # Also update SRS score if score is high enough
            if result.get("score", 0) >= 4:
                st.success("Score 4+ saved to your progress record.")


def _render_recall_result(result: dict):
    score = result.get("score", 0)
    score_color = {5: "#27ae60", 4: "#2ecc71", 3: "#f39c12", 2: "#e67e22", 1: "#e74c3c"}.get(score, "#888")
    pips = "".join([
        f'<span style="display:inline-block;width:10px;height:10px;border-radius:50%;'
        f'background:{"' + score_color + '" if i < score else "#ddd"};margin:0 2px"></span>'
        for i in range(5)
    ])
    st.markdown(
        f'<div style="background:#f8f9ff;border:1px solid #e0e0f0;border-radius:10px;padding:1rem 1.2rem;margin-top:.8rem">'
        f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:.6rem">'
        f'{pips}<span style="font-weight:700;color:{score_color}">{score}/5</span></div>'
        f'<div style="font-size:.88rem;margin-bottom:.4rem"><strong>✓ Correct:</strong> {result.get("correct","")}</div>'
        + (f'<div style="font-size:.88rem;margin-bottom:.4rem"><strong>Gaps:</strong> ' +
           " · ".join(f'<span style="background:#fff3cd;border-radius:4px;padding:1px 6px">{g}</span>'
                      for g in result.get("gaps", [])) + "</div>" if result.get("gaps") else "")
        + f'<div style="font-size:.85rem;color:#555;border-top:1px solid #eee;padding-top:.6rem;margin-top:.4rem">'
          f'<strong>Focus:</strong> {result.get("focus","")}</div>'
          f'</div>',
        unsafe_allow_html=True,
    )


# ─── Brain Dump ────────────────────────────────────────────────────────────────

def _render_brain_dump(lesson: dict):
    lesson_id = lesson["id"]
    st.markdown("Close your notes and type everything you remember about this topic.")
    st.caption("Claude will map what you wrote against the full knowledge bank and show exactly what's missing.")

    dump = st.text_area("Everything you remember:", height=200,
                        placeholder="Write freely — don't look at notes. Include facts, equations, examples...",
                        key=f"ai_dump_{lesson_id}")

    if st.button("Analyse my brain dump", use_container_width=True, key=f"ai_bdump_{lesson_id}") and dump.strip():
        with st.spinner("Mapping against knowledge bank..."):
            result = analyse_brain_dump(lesson, dump)
        if result.get("error"):
            st.error(result["error"])
        else:
            covered = result.get("covered", [])
            missing = result.get("missing", [])
            pct = result.get("score_pct", 0)
            verdict = result.get("verdict", "")
            pct_color = "#27ae60" if pct >= 70 else "#f39c12" if pct >= 40 else "#e74c3c"
            st.markdown(
                f'<div style="background:#f8f9ff;border:1px solid #e0e0f0;border-radius:10px;padding:1rem 1.2rem;margin-top:.8rem">'
                f'<div style="font-size:1.4rem;font-weight:700;color:{pct_color};margin-bottom:.6rem">{pct}% covered</div>'
                + (f'<div style="font-size:.87rem;margin-bottom:.5rem"><strong>✓ Covered:</strong> ' +
                   ", ".join(covered) + "</div>" if covered else "")
                + (f'<div style="font-size:.87rem;margin-bottom:.5rem"><strong>Missing:</strong> ' +
                   "".join(f'<span style="background:#ffe0e0;border-radius:4px;padding:1px 6px;margin:2px">{m}</span> '
                            for m in missing) + "</div>" if missing else "")
                + f'<div style="font-size:.85rem;color:#555;border-top:1px solid #eee;padding-top:.6rem;margin-top:.4rem">'
                  f'{verdict}</div></div>',
                unsafe_allow_html=True,
            )
            # Log
            log_weakness(
                lesson_id=lesson["id"],
                score=round(pct / 20),  # Convert % to 1-5
                question_type="brain_dump",
                weakness_categories=["missing_fact"] if missing else [],
                specific_gaps=missing,
                raw_answer=dump,
            )


# ─── Feynman Check ─────────────────────────────────────────────────────────────

def _render_feynman_check(lesson: dict):
    lesson_id = lesson["id"]
    feynman_prompt = lesson.get("feynman_prompt", "Explain this topic as if teaching a 12-year-old.")
    st.markdown(f'<div style="background:#fff8f0;border-left:3px solid #f39c12;border-radius:0 8px 8px 0;'
                f'padding:.8rem 1rem;margin-bottom:.8rem"><strong>Prompt:</strong> {feynman_prompt}</div>',
                unsafe_allow_html=True)

    explanation = st.text_area("Your explanation:", height=180,
                               placeholder="Explain simply. Use examples. If you can't explain it simply, you don't understand it.",
                               key=f"ai_feyn_{lesson_id}")

    if st.button("Check my explanation", use_container_width=True, key=f"ai_feynchk_{lesson_id}") and explanation.strip():
        with st.spinner("Diagnosing..."):
            result = check_feynman(lesson, explanation)
        if result.get("error"):
            st.error(result["error"])
        else:
            conceptual = result.get("conceptual_gaps", [])
            surface = result.get("surface_errors", [])
            verdict = result.get("verdict", "")
            st.markdown(
                f'<div style="background:#f8f9ff;border:1px solid #e0e0f0;border-radius:10px;padding:1rem 1.2rem;margin-top:.8rem">'
                + (f'<div style="font-size:.87rem;margin-bottom:.5rem"><strong>Conceptual gaps (understanding):</strong><br>'
                   + "".join(f'<div style="background:#ffe0e0;border-radius:4px;padding:3px 8px;margin:3px 0">{g}</div>'
                              for g in conceptual) + "</div>" if conceptual else
                   '<div style="font-size:.87rem;color:#27ae60;margin-bottom:.5rem">✓ No major conceptual gaps found</div>')
                + (f'<div style="font-size:.87rem;margin-bottom:.5rem"><strong>Factual errors:</strong> '
                   + ", ".join(surface) + "</div>" if surface else "")
                + f'<div style="font-size:.85rem;color:#555;border-top:1px solid #eee;padding-top:.6rem;margin-top:.4rem">'
                  f'{verdict}</div></div>',
                unsafe_allow_html=True,
            )
            log_weakness(
                lesson_id=lesson["id"],
                score=3 if not conceptual else 2 if not surface else 1,
                question_type="feynman",
                weakness_categories=result.get("weakness_categories", []),
                specific_gaps=conceptual + surface,
                raw_answer=explanation,
            )


# ─── Show Your Working (Physics) ──────────────────────────────────────────────

def _render_show_working(lesson: dict):
    lesson_id = lesson["id"]
    st.markdown("Type your physics calculation step by step — Claude checks your method, not just the answer.")

    working = st.text_area("Your working:", height=160,
                            placeholder="E.g.\nF = ma\nm = 1200 kg, a = 3 m/s²\nF = 1200 × 3 = 3600 N",
                            key=f"ai_work_{lesson_id}")

    if st.button("Check my working", use_container_width=True, key=f"ai_workchk_{lesson_id}") and working.strip():
        with st.spinner("Checking..."):
            result = check_working(lesson, working)
        if result.get("error"):
            st.error(result["error"])
        else:
            mc = result.get("method_correct", False)
            ac = result.get("answer_correct", False)
            errors = result.get("errors", [])
            habits = result.get("aqa_habits", [])
            verdict = result.get("verdict", "")
            st.markdown(
                f'<div style="background:#f8f9ff;border:1px solid #e0e0f0;border-radius:10px;padding:1rem 1.2rem;margin-top:.8rem">'
                f'<div style="display:flex;gap:1rem;margin-bottom:.6rem">'
                f'<span style="color:{"#27ae60" if mc else "#e74c3c"}">{"✓" if mc else "✗"} Method</span>'
                f'<span style="color:{"#27ae60" if ac else "#e74c3c"}">{"✓" if ac else "✗"} Answer</span></div>'
                + (f'<div style="font-size:.87rem;margin-bottom:.4rem"><strong>Errors:</strong> '
                   + " · ".join(errors) + "</div>" if errors else "")
                + (f'<div style="font-size:.87rem;margin-bottom:.4rem"><strong>AQA habits to fix:</strong> '
                   + " · ".join(f'<span style="background:#fff3cd;border-radius:4px;padding:1px 6px">{h}</span>'
                                 for h in habits) + "</div>" if habits else "")
                + f'<div style="font-size:.85rem;color:#555;border-top:1px solid #eee;padding-top:.6rem;margin-top:.4rem">'
                  f'{verdict}</div></div>',
                unsafe_allow_html=True,
            )
            log_weakness(
                lesson_id=lesson["id"],
                score=5 if mc and ac and not habits else 4 if mc and ac else 3 if mc else 2,
                question_type="show_working",
                weakness_categories=result.get("weakness_categories", []),
                specific_gaps=errors + habits,
                raw_answer=working,
            )


# ─── Korean Writing ────────────────────────────────────────────────────────────

def _render_korean_writing(lesson: dict):
    lesson_id = lesson["id"]
    st.markdown("Write a Korean sentence — Claude checks grammar, particles, and register against this lesson's rules.")

    import streamlit.components.v1 as components

    english_prompt = st.text_input("English prompt (optional):", placeholder="e.g. I eat rice every day", key=f"ai_eng_{lesson_id}")

    # Embed Korean keyboard
    st.caption("Use the keyboard below or type if you have Korean input enabled:")
    kb_html = _get_keyboard_html()
    components.html(kb_html, height=210)

    korean_text = st.text_input("Korean:", placeholder="Type here or use keyboard above", key=f"ai_kor_{lesson_id}")

    if st.button("Get feedback", use_container_width=True, key=f"ai_korchk_{lesson_id}") and korean_text.strip():
        with st.spinner("Checking..."):
            result = check_korean_writing(lesson, korean_text, english_prompt)
        if result.get("error"):
            st.error(result["error"])
        else:
            corrected = result.get("corrected", "")
            errors = result.get("errors", [])
            alternatives = result.get("natural_alternatives", [])
            verdict = result.get("verdict", "")
            st.markdown(
                f'<div style="background:#f8f9ff;border:1px solid #e0e0f0;border-radius:10px;padding:1rem 1.2rem;margin-top:.8rem">'
                + (f'<div style="font-size:1rem;margin-bottom:.6rem"><strong>✓ Corrected:</strong> {corrected}</div>' if corrected else "")
                + (f'<div style="font-size:.87rem;margin-bottom:.5rem"><strong>Errors:</strong><br>'
                   + "".join(f'<div style="background:#ffe0e0;border-radius:4px;padding:3px 8px;margin:2px 0">'
                              f'<code>{e.get("original","")}</code> → <code>{e.get("correction","")}</code>'
                              f' — {e.get("rule","")}</div>'
                              for e in errors if isinstance(e, dict)) + "</div>" if errors else "")
                + (f'<div style="font-size:.87rem;margin-bottom:.4rem"><strong>More natural:</strong> '
                   + " / ".join(alternatives) + "</div>" if alternatives else "")
                + f'<div style="font-size:.85rem;color:#555;border-top:1px solid #eee;padding-top:.6rem;margin-top:.4rem">'
                  f'{verdict}</div></div>',
                unsafe_allow_html=True,
            )
            gap_list = [f"{e.get('original','')} should be {e.get('correction','')}" for e in errors if isinstance(e, dict)]
            log_weakness(
                lesson_id=lesson["id"],
                score=5 if not errors else 4 if len(errors) == 1 else 3 if len(errors) == 2 else 2,
                question_type="korean_writing",
                weakness_categories=result.get("weakness_categories", []),
                specific_gaps=gap_list,
                raw_answer=korean_text,
            )


# ─── RAF Interview Practice ────────────────────────────────────────────────────

def _render_raf_interview(lesson: dict):
    lesson_id = lesson["id"]
    competency = lesson.get("knowledge_bank", {}).get("competency", "general RAF competency")
    st.markdown(f"Practice a competency answer. Competency being assessed: **{competency}**")
    st.caption("Use the STAR framework: Situation → Task → Action (your decision + why) → Result")

    # Pull a question from the lesson or let user pick
    questions = lesson.get("active_recall_questions", [])
    if questions:
        q_idx = st.selectbox("Question:", range(len(questions)),
                              format_func=lambda i: questions[i],
                              key=f"ai_rafq_{lesson_id}")
        question = questions[q_idx]
    else:
        question = st.text_input("Question:", placeholder="e.g. Tell me about a time you led under pressure", key=f"ai_rafqin_{lesson_id}")

    answer = st.text_area("Your answer:", height=200,
                          placeholder="Use STAR format. Focus on what YOU decided and why — not just what happened.",
                          key=f"ai_rafans_{lesson_id}")

    if st.button("Score my answer", use_container_width=True, key=f"ai_rafchk_{lesson_id}") and answer.strip() and question:
        with st.spinner("Assessing..."):
            result = mark_raf_answer(lesson, question, answer)
        if result.get("error"):
            st.error(result["error"])
        else:
            scores = result.get("scores", {})
            strengths = result.get("strengths", [])
            gaps = result.get("gaps", [])
            verdict = result.get("verdict", "")
            dim_color = lambda s: "#27ae60" if s == 3 else "#f39c12" if s == 2 else "#e74c3c"
            dims_html = "".join(
                f'<div style="display:flex;justify-content:space-between;align-items:center;'
                f'padding:.3rem .5rem;margin:.2rem 0;background:#f8f8f8;border-radius:5px">'
                f'<span style="font-size:.85rem">{dim.title()}</span>'
                f'<span style="font-weight:700;color:{dim_color(val)}">{val}/3</span></div>'
                for dim, val in scores.items()
            )
            st.markdown(
                f'<div style="background:#f8f9ff;border:1px solid #e0e0f0;border-radius:10px;padding:1rem 1.2rem;margin-top:.8rem">'
                + dims_html
                + (f'<div style="font-size:.87rem;margin:.6rem 0 .3rem"><strong>✓ Strengths:</strong> '
                   + " · ".join(strengths) + "</div>" if strengths else "")
                + (f'<div style="font-size:.87rem;margin-bottom:.4rem"><strong>Gaps:</strong><br>'
                   + "".join(f'<div style="background:#ffe0e0;border-radius:4px;padding:2px 8px;margin:2px 0">{g}</div>'
                              for g in gaps) + "</div>" if gaps else "")
                + f'<div style="font-size:.85rem;color:#555;border-top:1px solid #eee;padding-top:.6rem;margin-top:.4rem">'
                  f'{verdict}</div></div>',
                unsafe_allow_html=True,
            )
            avg_score = round(sum(scores.values()) / len(scores)) if scores else 2
            log_weakness(
                lesson_id=lesson["id"],
                score=avg_score,
                question_type="raf_interview",
                weakness_categories=result.get("weakness_categories", []),
                specific_gaps=gaps,
                raw_answer=answer,
                competency_scores=scores,
            )


# ─── Lesson Progress ───────────────────────────────────────────────────────────

def _render_lesson_progress(lesson: dict):
    lesson_id = lesson["id"]
    st.markdown("Your AI-tracked history for this lesson.")

    summary = get_lesson_weakness_summary(lesson_id)
    weakness_log = load_weakness_log(lesson_id=lesson_id)

    if summary["attempts"] == 0:
        st.info("No AI-marked attempts yet. Use the other tabs to build your history.")
        return

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Attempts", summary["attempts"])
    with c2:
        st.metric("Avg score", f"{summary['avg_score']}/5")
    with c3:
        st.metric("Last attempt", summary["last_date"] or "—")

    if summary["top_gaps"]:
        st.markdown("**Persistent gaps:**")
        for g in summary["top_gaps"]:
            st.markdown(
                f'<span style="background:#ffe0e0;border-radius:4px;padding:2px 8px;'
                f'margin:2px;display:inline-block;font-size:.84rem">{g}</span>',
                unsafe_allow_html=True,
            )

    if st.button("Get AI analysis of my progress", key=f"ai_prog_{lesson_id}"):
        with st.spinner("Analysing..."):
            from ai_helper import analyse_lesson_progress
            analysis = analyse_lesson_progress(lesson, weakness_log)
        st.markdown(
            f'<div style="background:#f8f9ff;border:1px solid #e0e0f0;border-radius:10px;'
            f'padding:1rem 1.2rem;margin-top:.8rem;font-size:.9rem;line-height:1.7">'
            f'{analysis}</div>',
            unsafe_allow_html=True,
        )


# ─── Shared Korean keyboard HTML ───────────────────────────────────────────────

def _get_keyboard_html() -> str:
    return """
<style>
*{box-sizing:border-box;}
.kb-rows{display:flex;flex-direction:column;gap:3px;}
.kb-row{display:flex;gap:3px;justify-content:center;}
.key{background:#fff;border:1px solid #ced4da;border-radius:4px;cursor:pointer;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  width:48px;height:42px;transition:background 0.1s;flex-shrink:0;user-select:none;position:relative;}
.key:hover{background:#e9ecef;}.key:active{transform:scale(0.95);}
.key .ko-main{font-size:14px;color:#212529;}.key .ko-shift{font-size:9px;color:#8a6700;position:absolute;top:3px;right:5px;}
.key .en{font-size:9px;color:#6c757d;}
.key.sp{width:160px;}.key.fn{background:#e9ecef;}.key.fn .ko-main{font-size:10px;color:#495057;}
.acts{display:flex;gap:5px;margin-top:5px;}
.acts button{padding:3px 8px;font-size:11px;border:1px solid #ced4da;border-radius:3px;background:#fff;cursor:pointer;}
</style>
<div id="out" style="background:#f8f9fa;border:1px solid #dee2e6;border-radius:6px;padding:6px 10px;font-size:16px;min-height:40px;margin-bottom:6px;"></div>
<div class="kb-rows" id="kb"></div>
<div class="acts"><button onclick="bs()">←</button><button onclick="cl()">Clear</button><button id="sb" onclick="ts()">Shift</button><button onclick="cp()">Copy</button></div>
<script>
const NM={q:'ㅂ',w:'ㅈ',e:'ㄷ',r:'ㄱ',t:'ㅅ',y:'ㅛ',u:'ㅕ',i:'ㅑ',o:'ㅐ',p:'ㅔ',a:'ㅁ',s:'ㄴ',d:'ㅇ',f:'ㄹ',g:'ㅎ',h:'ㅗ',j:'ㅓ',k:'ㅏ',l:'ㅣ',z:'ㅋ',x:'ㅌ',c:'ㅊ',v:'ㅍ',b:'ㅠ',n:'ㅜ',m:'ㅡ'};
const SH={q:'ㅃ',w:'ㅉ',e:'ㄸ',r:'ㄲ',t:'ㅆ',o:'ㅒ',p:'ㅖ'};
const rows=[[{n:'ㅂ',s:'ㅃ',e:'q'},{n:'ㅈ',s:'ㅉ',e:'w'},{n:'ㄷ',s:'ㄸ',e:'e'},{n:'ㄱ',s:'ㄲ',e:'r'},{n:'ㅅ',s:'ㅆ',e:'t'},{n:'ㅛ',e:'y'},{n:'ㅕ',e:'u'},{n:'ㅑ',e:'i'},{n:'ㅐ',s:'ㅒ',e:'o'},{n:'ㅔ',s:'ㅖ',e:'p'}],[{n:'ㅁ',e:'a'},{n:'ㄴ',e:'s'},{n:'ㅇ',e:'d'},{n:'ㄹ',e:'f'},{n:'ㅎ',e:'g'},{n:'ㅗ',e:'h'},{n:'ㅓ',e:'j'},{n:'ㅏ',e:'k'},{n:'ㅣ',e:'l'}],[{n:'ㅋ',e:'z'},{n:'ㅌ',e:'x'},{n:'ㅊ',e:'c'},{n:'ㅍ',e:'v'},{n:'ㅠ',e:'b'},{n:'ㅜ',e:'n'},{n:'ㅡ',e:'m'}]];
const CH=['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'];
const JU=['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'];
const JO=['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'];
const CJ={'ㄱ+ㅅ':'ㄳ','ㄴ+ㅈ':'ㄵ','ㄴ+ㅎ':'ㄶ','ㄹ+ㄱ':'ㄺ','ㄹ+ㅁ':'ㄻ','ㄹ+ㅂ':'ㄼ','ㄹ+ㅅ':'ㄽ','ㄹ+ㅌ':'ㄾ','ㄹ+ㅍ':'ㄿ','ㄹ+ㅎ':'ㅀ','ㅂ+ㅅ':'ㅄ'};
const CV={'ㅗ+ㅏ':'ㅘ','ㅗ+ㅐ':'ㅙ','ㅗ+ㅣ':'ㅚ','ㅜ+ㅓ':'ㅝ','ㅜ+ㅔ':'ㅞ','ㅜ+ㅣ':'ㅟ','ㅡ+ㅣ':'ㅢ'};
function iV(c){return JU.includes(c);}function iC(c){return CH.includes(c);}
function cmp(a,b,c){const ci=CH.indexOf(a),vi=JU.indexOf(b),ji=JO.indexOf(c||'');if(ci<0||vi<0||ji<0)return(a||'')+(b||'')+(c||'');return String.fromCharCode(0xAC00+ci*21*28+vi*28+ji);}
let tx='',co=null,sh=false;
function ft(){return tx+(co?co.preview||'':'');}
function ud(){document.getElementById('out').textContent=ft()+'|';}
function ac(ch){
  if(sh&&!iV(ch))ss(false);
  if(!iV(ch)&&!iC(ch)){if(co){tx+=co.preview||'';co=null;}tx+=ch;ud();return;}
  if(!co){if(iC(ch))co={cho:ch,jung:null,jong:null,preview:ch};else tx+=ch;ud();return;}
  const c=co;
  if(c.cho&&!c.jung){if(iV(ch)){c.jung=CV[c.cho+'+'+ch]||ch;c.preview=cmp(c.cho,c.jung,'');ud();return;}tx+=c.cho;co={cho:ch,jung:null,jong:null,preview:ch};ud();return;}
  if(c.cho&&c.jung&&!c.jong){if(iC(ch)){c.jong=ch;c.preview=cmp(c.cho,c.jung,c.jong);ud();return;}if(iV(ch)){const cv=CV[c.jung+'+'+ch];if(cv){c.jung=cv;c.preview=cmp(c.cho,c.jung,'');ud();return;}tx+=cmp(c.cho,c.jung,'');co={cho:null,jung:ch,jong:null,preview:ch};ud();return;}}
  if(c.cho&&c.jung&&c.jong){if(iV(ch)){const ck=Object.entries(CJ).find(([k,v])=>v===c.jong);let sc=c.jong,rj='';if(ck){[sc,rj]=ck[0].split('+');}tx+=cmp(c.cho,c.jung,rj);co={cho:sc,jung:ch,jong:null,preview:cmp(sc,ch,'')};ud();return;}if(iC(ch)){const cv=CJ[c.jong+'+'+ch];if(cv){c.jong=cv;c.preview=cmp(c.cho,c.jung,c.jong);ud();return;}tx+=c.preview;co={cho:ch,jung:null,jong:null,preview:ch};ud();return;}}
  if(co){tx+=co.preview||'';co=null;}ac(ch);
}
function bs(){if(co){const c=co;if(c.jong){const ck=Object.entries(CJ).find(([k,v])=>v===c.jong);if(ck){c.jong=ck[0].split('+')[0];c.preview=cmp(c.cho,c.jung,c.jong);}else{c.jong=null;c.preview=cmp(c.cho,c.jung,'');}ud();return;}if(c.jung){const ck=Object.entries(CV).find(([k,v])=>v===c.jung);if(ck){c.jung=ck[0].split('+')[0];c.preview=c.cho?cmp(c.cho,c.jung,''):c.jung;ud();return;}c.jung=null;c.preview=c.cho||'';ud();return;}co=null;ud();return;}if(tx.length>0){tx=tx.slice(0,-1);ud();}}
function cl(){tx='';co=null;ss(false);ud();}
function cp(){navigator.clipboard.writeText(ft()).catch(()=>{});}
function ss(v){sh=v;document.getElementById('sb').style.background=v?'#ffc107':'';}
function ts(){ss(!sh);}
document.addEventListener('keydown',e=>{if(e.key==='Shift'){ss(true);return;}if(e.key==='Backspace'){e.preventDefault();bs();return;}if(e.key===' '){e.preventDefault();if(co){tx+=co.preview||'';co=null;}tx+=' ';ud();return;}const k=e.key.toLowerCase();const ch=sh?(SH[k]||NM[k]):NM[k];if(ch){e.preventDefault();ac(ch);}});
document.addEventListener('keyup',e=>{if(e.key==='Shift')ss(false);});
const kb=document.getElementById('kb');
rows.forEach((row,ri)=>{
  const re=document.createElement('div');re.className='kb-row';
  if(ri===2){const sk=document.createElement('div');sk.className='key fn';sk.style.width='54px';sk.innerHTML='<span class="ko-main">⇧</span>';sk.addEventListener('mousedown',e=>{e.preventDefault();ts();});re.appendChild(sk);}
  row.forEach(k=>{const key=document.createElement('div');key.className='key';key.innerHTML=`${k.s?`<span class="ko-shift">${k.s}</span>`:''}<span class="ko-main">${k.n}</span><span class="en">${k.e}</span>`;key.addEventListener('mousedown',e=>{e.preventDefault();const ch=sh&&k.s?k.s:k.n;ac(ch);if(sh)ss(false);});re.appendChild(key);});
  if(ri===1){const bk=document.createElement('div');bk.className='key fn';bk.style.width='60px';bk.innerHTML='<span class="ko-main">←del</span>';bk.addEventListener('mousedown',e=>{e.preventDefault();bs();});re.appendChild(bk);}
  if(ri===2){const sp=document.createElement('div');sp.className='key fn sp';sp.innerHTML='<span class="ko-main">space</span>';sp.addEventListener('mousedown',e=>{e.preventDefault();if(co){tx+=co.preview||'';co=null;}tx+=' ';ud();});re.appendChild(sp);}
  kb.appendChild(re);
});
ud();
</script>
"""
