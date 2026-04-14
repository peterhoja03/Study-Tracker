"""
Korean Study Tracker — Main App
================================
Password-protected Streamlit app for tracking progress through
How to Study Korean (howtostudykorean.com) + supplementary resources.

Run:  streamlit run app.py
"""

import streamlit as st
import hashlib
import os
from datetime import date, timedelta

# ─── Page Config ─────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="한국어 Study Tracker",
    page_icon="🇰🇷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Password Protection ──────────────────────────────────────────────────────

def check_password():
    def _hash(pw: str) -> str:
        return hashlib.sha256(pw.encode()).hexdigest()

    stored_hash = st.secrets.get("app_password_hash", None)
    if stored_hash is None:
        raw = os.environ.get("KOREAN_TRACKER_PASSWORD", "korean2024")
        stored_hash = _hash(raw)

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center; padding: 3rem 0 1rem;">
            <span style="font-size:4rem">🇰🇷</span>
            <h1 style="font-family: Georgia, serif; font-size: 2rem; color: #1a1a2e; margin: 0.5rem 0;">
                한국어 Study Tracker
            </h1>
            <p style="color: #555; font-size: 0.95rem;">Your personal Korean learning dashboard</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("login_form"):
            password = st.text_input("Password", type="password",
                                      placeholder="Enter your password...",
                                      label_visibility="collapsed")
            submitted = st.form_submit_button("→ Enter", use_container_width=True)

        if submitted:
            if _hash(password) == stored_hash:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password. Please try again.")

        st.markdown("""
        <p style="text-align:center; color:#aaa; font-size:0.8rem; margin-top:2rem;">
            Private study tracker — not publicly accessible
        </p>
        """, unsafe_allow_html=True)

    return False


# ─── Custom CSS ──────────────────────────────────────────────────────────────

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Playfair+Display:wght@600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
        border-right: 1px solid #2d2d4e;
    }
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #e8e8f0 !important;
    }
    section[data-testid="stSidebar"] label { color: #b8b8d0 !important; }
    section[data-testid="stSidebar"] .stButton button {
        background: rgba(255,255,255,0.08);
        color: #e8e8f0;
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 8px;
        width: 100%;
        text-align: left;
        transition: all 0.2s;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        background: rgba(255,255,255,0.15);
    }

    .stat-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        border: 1px solid #f0f0f8;
        text-align: center;
    }
    .stat-number {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a1a2e;
        line-height: 1;
    }
    .stat-label {
        color: #888;
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 0.4rem;
    }

    .lesson-card {
        background: white;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.6rem;
        border: 1px solid #eee;
        border-left: 4px solid #ddd;
    }
    .lesson-card.completed { border-left-color: #27AE60; background: #f8fff9; }
    .lesson-card.in_progress { border-left-color: #F39C12; background: #fffdf5; }

    .progress-bar-container {
        background: #f0f0f8;
        border-radius: 999px;
        height: 8px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    .progress-bar-fill { height: 100%; border-radius: 999px; }

    .badge {
        display: inline-block;
        padding: 0.2rem 0.65rem;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .badge-completed { background: #d4f5e2; color: #1a7a42; }
    .badge-in_progress { background: #fff3cd; color: #856404; }
    .badge-not_started { background: #f0f0f8; color: #888; }

    .feynman-box {
        background: linear-gradient(135deg, #1a1a2e, #0f3460);
        border-radius: 12px;
        padding: 1.5rem;
        color: white;
        border-left: 4px solid #e94560;
    }
    .recall-box {
        background: #fffbf0;
        border: 1px solid #f0d060;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
    }
    .review-due {
        background: linear-gradient(135deg, #fde8ff, #fff0f5);
        border: 1px solid #e8b4f8;
        border-radius: 12px;
        padding: 1rem 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)


# ─── Sidebar ──────────────────────────────────────────────────────────────────

def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center; padding: 1rem 0 0.5rem;">
            <span style="font-size:2.5rem">🇰🇷</span>
            <h2 style="color:white; font-family:Georgia,serif; font-size:1.3rem; margin:0.3rem 0 0;">
                한국어 Tracker
            </h2>
            <p style="color:#8888aa; font-size:0.75rem; margin:0;">Personal Study Dashboard</p>
        </div>
        <hr style="border-color:#2d2d4e; margin: 1rem 0;">
        """, unsafe_allow_html=True)

        pages = {
            "🏠  Dashboard": "dashboard",
            "📚  Curriculum": "curriculum",
            "📖  Lesson Viewer": "lesson",
            "🔄  Review Queue": "review",
            "📊  Progress": "progress",
            "⚙️  Settings": "settings",
        }

        if "current_page" not in st.session_state:
            st.session_state.current_page = "dashboard"

        for label, page_key in pages.items():
            if st.button(label, key=f"nav_{page_key}", use_container_width=True):
                st.session_state.current_page = page_key
                st.rerun()

        from data.store import get_dashboard_stats
        stats = get_dashboard_stats()

        st.markdown("""<hr style="border-color:#2d2d4e; margin: 1.5rem 0 1rem;">""", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="padding: 0 0.5rem; font-size:0.85rem;">
            <div style="color:#8888aa; font-size:0.7rem; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.75rem;">Quick Stats</div>
            <div style="display:flex; justify-content:space-between; margin-bottom:0.4rem;">
                <span style="color:#ccc;">🔥 Streak</span>
                <span style="color:white; font-weight:600;">{stats['streak']} days</span>
            </div>
            <div style="display:flex; justify-content:space-between; margin-bottom:0.4rem;">
                <span style="color:#ccc;">✅ Completed</span>
                <span style="color:white; font-weight:600;">{stats['total_completed']}</span>
            </div>
            <div style="display:flex; justify-content:space-between; margin-bottom:0.4rem;">
                <span style="color:#ccc;">🔄 Reviews Due</span>
                <span style="color:{'#ff6b6b' if stats['due_reviews'] > 0 else 'white'}; font-weight:600;">{stats['due_reviews']}</span>
            </div>
            <div style="display:flex; justify-content:space-between;">
                <span style="color:#ccc;">⏱ Total Time</span>
                <span style="color:white; font-weight:600;">{stats['total_study_hours']}h</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔒  Log Out", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()


# ─── Dashboard ────────────────────────────────────────────────────────────────

def page_dashboard():
    from data.store import get_dashboard_stats, get_due_reviews, load_progress
    from data.curriculum import CURRICULUM, get_unit_progress_summary, get_all_lessons, get_lesson_by_id

    st.markdown("# 🏠 Dashboard")
    st.markdown(f"*{date.today().strftime('%A, %d %B %Y')}*")
    st.markdown("---")

    stats = get_dashboard_stats()
    progress = load_progress()
    due = get_due_reviews()

    c1, c2, c3, c4, c5 = st.columns(5)
    for col, num, label in [
        (c1, f"🔥 {stats['streak']}", "Day Streak"),
        (c2, str(stats['total_completed']), "Lessons Done"),
        (c3, str(len(due)), "Reviews Due"),
        (c4, str(stats['total_in_progress']), "In Progress"),
        (c5, f"{stats['total_study_hours']}h", "Study Time"),
    ]:
        with col:
            st.markdown(f"""<div class="stat-card">
                <div class="stat-number">{num}</div>
                <div class="stat-label">{label}</div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("📚 Unit Progress")
        unit_summary = get_unit_progress_summary(progress)
        for unit_name, data in unit_summary.items():
            pct = data["percent"]
            st.markdown(f"""
            <div style="margin-bottom:1rem;">
                <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                    <span style="font-weight:600; font-size:0.9rem;">{unit_name}: {data['title']}</span>
                    <span style="font-size:0.8rem; color:#888;">{data['completed']}/{data['total']} · {pct}%</span>
                </div>
                <div class="progress-bar-container">
                    <div class="progress-bar-fill" style="width:{pct}%; background:{data['color']};"></div>
                </div>
                <span style="font-size:0.75rem; color:#aaa;">{data['level']}</span>
            </div>
            """, unsafe_allow_html=True)

    with col_right:
        if due:
            st.subheader(f"🔄 Reviews Due ({len(due)})")
            for lid in due[:4]:
                lesson = get_lesson_by_id(lid)
                if lesson:
                    st.markdown(f"""<div class="review-due" style="margin-bottom:0.5rem;">
                        <strong style="font-size:0.88rem;">{lesson['title']}</strong><br>
                        <span style="font-size:0.75rem; color:#888;">{lesson['unit']}</span>
                    </div>""", unsafe_allow_html=True)
            if st.button("→ Go to Review Queue", use_container_width=True):
                st.session_state.current_page = "review"
                st.rerun()
        else:
            st.subheader("✅ Reviews")
            st.success("No reviews due today!")

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("▶️ Continue Studying")
        in_prog = [(lid, d) for lid, d in progress.items() if d.get("status") == "in_progress"]
        all_lessons = get_all_lessons()

        if in_prog:
            lid, _ = in_prog[0]
            lesson = get_lesson_by_id(lid)
            if lesson:
                st.markdown(f"**{lesson['title']}**  \n*{lesson['unit']}*")
                if st.button("Continue →", use_container_width=True):
                    st.session_state.current_page = "lesson"
                    st.session_state.active_lesson_id = lid
                    st.rerun()
        else:
            not_started = [l for l in all_lessons
                           if progress.get(l["id"], {}).get("status", "not_started") == "not_started"]
            if not_started:
                nxt = not_started[0]
                st.markdown(f"**Next:** {nxt['title']}  \n*{nxt['unit']}*")
                if st.button(f"Start {nxt['id']} →", use_container_width=True):
                    st.session_state.current_page = "lesson"
                    st.session_state.active_lesson_id = nxt["id"]
                    st.rerun()


# ─── Curriculum ───────────────────────────────────────────────────────────────

def page_curriculum():
    from data.curriculum import CURRICULUM
    from data.store import load_progress

    st.markdown("# 📚 Curriculum")
    st.markdown("All units and lessons from [How to Study Korean](https://www.howtostudykorean.com)")
    st.markdown("---")

    progress = load_progress()

    for unit_name, unit_data in CURRICULUM.items():
        lessons = unit_data["lessons"]
        done = sum(1 for l in lessons if progress.get(l["id"], {}).get("status") == "completed")
        pct = round(done / len(lessons) * 100) if lessons else 0

        with st.expander(
            f"**{unit_name}** — {unit_data['title']} | {done}/{len(lessons)} ({pct}%)",
            expanded=(unit_name in ["Unit 0", "Unit 1"] and done < len(lessons))
        ):
            st.markdown(f"""
            <div class="progress-bar-container">
                <div class="progress-bar-fill" style="width:{pct}%; background:{unit_data['color']};"></div>
            </div>
            <p style="color:#888; font-size:0.85rem; margin-top:0.5rem;">{unit_data['description']}</p>
            """, unsafe_allow_html=True)

            for lesson in lessons:
                status = progress.get(lesson["id"], {}).get("status", "not_started")
                split_tag = " ✂️" if lesson.get("split") else ""

                col1, col2 = st.columns([8, 1])
                with col1:
                    st.markdown(f"""
                    <div class="lesson-card {status}">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <div>
                                <strong>{lesson['id']}{split_tag} — {lesson['title']}</strong><br>
                                <span style="color:#888; font-size:0.8rem;">{lesson.get('subtitle','')}</span>
                            </div>
                            <div style="text-align:right; min-width:120px;">
                                <span class="badge badge-{status}">{status.replace('_',' ').title()}</span><br>
                                <span style="font-size:0.75rem; color:#aaa;">⏱ {lesson['estimated_minutes']} min</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                with col2:
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("📖", key=f"c_{lesson['id']}", help="Open lesson"):
                        st.session_state.current_page = "lesson"
                        st.session_state.active_lesson_id = lesson["id"]
                        st.rerun()


# ─── Lesson Viewer ────────────────────────────────────────────────────────────

def page_lesson():
    from data.curriculum import get_all_lessons, get_lesson_by_id, CURRICULUM
    from data.store import (load_progress, mark_lesson_complete, mark_lesson_in_progress,
                              save_lesson_notes, mark_feynman_done, log_study_session)

    all_lessons = get_all_lessons()
    progress = load_progress()

    lesson_options = {f"{l['id']} — {l['title']} ({l['unit']})": l["id"] for l in all_lessons}
    default_id = st.session_state.get("active_lesson_id", all_lessons[0]["id"])
    default_label = next((k for k, v in lesson_options.items() if v == default_id),
                          list(lesson_options.keys())[0])

    selected_label = st.selectbox("Select Lesson", list(lesson_options.keys()),
                                   index=list(lesson_options.keys()).index(default_label))
    lesson_id = lesson_options[selected_label]
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        st.error("Lesson not found.")
        return

    status = progress.get(lesson_id, {}).get("status", "not_started")
    lesson_progress = progress.get(lesson_id, {})
    unit_data = CURRICULUM[lesson["unit"]]

    # Header
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,{unit_data['color']}22,{unit_data['color']}08);
                border-left:5px solid {unit_data['color']}; border-radius:0 12px 12px 0;
                padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
            <div>
                <span style="font-size:0.72rem; color:#888; text-transform:uppercase; letter-spacing:0.1em;">
                    {lesson['unit']} · {unit_data['level']}
                </span>
                <h2 style="font-family:Georgia,serif; margin:0.3rem 0; font-size:1.5rem; color:#1a1a2e;">
                    {lesson['title']}
                </h2>
                <p style="color:#666; margin:0; font-size:0.9rem;">{lesson.get('subtitle','')}</p>
            </div>
            <div style="text-align:right;">
                <span class="badge badge-{status}">{status.replace('_',' ').title()}</span><br>
                <span style="font-size:0.82rem; color:#888; display:block; margin-top:0.3rem;">
                    ⏱ {lesson['estimated_minutes']} min
                </span>
                <a href="{lesson['url']}" target="_blank" style="font-size:0.78rem; color:#3a5bd9;">↗ Open HTSK</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Goals & Vocab", "🧠 Active Recall", "✍️ Feynman", "📝 Notes", "✅ Mark Complete"
    ])

    with tab1:
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("### 🎯 Learning Goals")
            for i, goal in enumerate(lesson["learning_goals"], 1):
                st.markdown(f"""
                <div style="display:flex; gap:0.75rem; align-items:flex-start; padding:0.7rem;
                            background:#f8f9ff; border-radius:8px; margin-bottom:0.5rem;">
                    <span style="background:{unit_data['color']}; color:white; border-radius:50%;
                                 width:22px; height:22px; display:inline-flex; align-items:center;
                                 justify-content:center; font-size:0.72rem; font-weight:700; flex-shrink:0;">{i}</span>
                    <span style="font-size:0.9rem;">{goal}</span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("### 📖 Key Vocabulary")
            vocab_html = " ".join([
                f'<span style="background:#f0f4ff; border:1px solid #d0d8f8; border-radius:6px; '
                f'padding:0.3rem 0.7rem; margin:0.2rem; display:inline-block; '
                f'font-family:\'Noto Sans KR\',sans-serif;">{v}</span>'
                for v in lesson.get("key_vocab", [])
            ])
            st.markdown(f"<div style='line-height:2.4;'>{vocab_html}</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("### 🛠️ Techniques")
            icons = {"Active Recall":"🧠","Spaced Repetition":"🔄","Feynman Technique":"✍️",
                     "Writing Practice":"📝","Pattern Recognition":"🔍","Sentence Building":"🔨",
                     "Conjugation Drilling":"⚙️","Contrast Drilling":"⚖️","Listening Practice":"👂",
                     "Reading Practice":"📖","Role-Play":"🎭","Cultural Context":"🌏","Immersion":"🌊"}
            for tech in lesson.get("techniques", []):
                icon = icons.get(tech, "💡")
                st.markdown(f"""
                <div style="background:white; border:1px solid #eee; border-radius:8px;
                            padding:0.5rem 0.9rem; margin-bottom:0.35rem; font-size:0.88rem;">
                    {icon} {tech}
                </div>
                """, unsafe_allow_html=True)

            st.markdown("### 🔗 Resources")
            for res in lesson.get("resources", []):
                st.markdown(f'<a href="{res["url"]}" target="_blank" style="display:inline-block; '
                             f'background:#f0f4ff; color:#3a5bd9; padding:0.35rem 0.9rem; '
                             f'border-radius:999px; text-decoration:none; font-size:0.82rem; '
                             f'border:1px solid #d0d8f8; margin:0.2rem;">↗ {res["name"]}</a>',
                             unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(f"""
            <div style="background:#fff3cd; border:1px solid #ffc107; border-radius:8px; padding:0.9rem; font-size:0.83rem;">
                <strong>⏱ Time Budget:</strong> {lesson['estimated_minutes']} minutes<br>
                <span style="color:#888;">Keep sessions under 25 min for best retention</span>
            </div>
            """, unsafe_allow_html=True)

        if status == "not_started":
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("▶️ Start This Lesson", use_container_width=True):
                mark_lesson_in_progress(lesson_id)
                log_study_session(lesson_id, 0, "started")
                st.success("Lesson started! Work through the tabs above.")
                st.rerun()

    with tab2:
        st.markdown("### 🧠 Active Recall")
        st.markdown("""
        <div style="background:#e8f4ff; border-left:4px solid #3a8fd9; border-radius:0 8px 8px 0;
                    padding:0.9rem 1.3rem; margin-bottom:1.5rem; font-size:0.88rem;">
            <strong>Protocol:</strong> Answer each question OUT LOUD or in writing <em>before</em> checking. 
            Struggling is good — it forces your brain to work. Add hard items to Anki.
        </div>
        """, unsafe_allow_html=True)

        for i, q in enumerate(lesson.get("active_recall_questions", []), 1):
            st.markdown(f"""<div class="recall-box" style="margin-bottom:0.8rem;">
                <strong>Q{i}.</strong> {q}</div>""", unsafe_allow_html=True)
            with st.expander(f"→ Answer space for Q{i}"):
                st.text_area(f"Your answer:", key=f"ar_{lesson_id}_{i}", height=80,
                              placeholder="Write before looking...")
                st.markdown(f'<a href="{lesson["url"]}" target="_blank" style="font-size:0.83rem; color:#3a5bd9;">↗ Verify in HTSK</a>',
                             unsafe_allow_html=True)

    with tab3:
        st.markdown("### ✍️ Feynman Technique")
        st.markdown("""
        <div class="feynman-box" style="margin-bottom:1.5rem;">
            <h4 style="color:#ff6b6b; margin:0 0 0.5rem;">The Feynman Method</h4>
            <ol style="margin:0; padding-left:1.2rem; line-height:1.8; font-size:0.9rem;">
                <li>Study the concept in the HTSK lesson</li>
                <li>Close the lesson — explain it simply, as if teaching a 10-year-old</li>
                <li>Identify where your explanation breaks down (that's your gap)</li>
                <li>Go back and re-read only that part</li>
                <li>Re-explain until it's clear and complete</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background:#fff8f0; border:2px solid #e94560; border-radius:12px;
                    padding:1.3rem 1.5rem; font-size:0.95rem; color:#1a1a2e; margin-bottom:1rem;">
            <strong>Your prompt:</strong><br><br>{lesson['feynman_prompt']}
        </div>
        """, unsafe_allow_html=True)

        feynman_resp = st.text_area("Your explanation:", key=f"feyn_{lesson_id}", height=200,
                                     placeholder="Explain simply. Use examples. If you can't, you don't know it yet.")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Save Feynman Response", use_container_width=True):
                if feynman_resp.strip():
                    mark_feynman_done(lesson_id)
                    save_lesson_notes(lesson_id, f"[Feynman - {date.today()}]\n{feynman_resp}\n\n"
                                      + lesson_progress.get("notes", ""))
                    st.success("Saved!")
                else:
                    st.warning("Write your explanation first.")
        with col2:
            if lesson_progress.get("feynman_done"):
                st.success("✅ Feynman completed")

        for q in ["Could you explain this without notes?",
                   "Did you use an analogy or example?",
                   "Where did your explanation break down?",
                   "Did you go back and re-read those gaps?"]:
            st.checkbox(q, key=f"fc_{lesson_id}_{q[:15]}")

    with tab4:
        st.markdown("### 📝 My Notes")
        notes = st.text_area("Notes:", value=lesson_progress.get("notes", ""),
                              key=f"notes_{lesson_id}", height=300,
                              placeholder="Grammar rules, vocab examples, confusing points, connections...\nTip: Write examples in Korean!")
        if st.button("💾 Save Notes", use_container_width=True):
            save_lesson_notes(lesson_id, notes)
            st.success("Notes saved!")

    with tab5:
        st.markdown("### ✅ Mark Lesson Complete")

        if status == "completed":
            st.success(f"✅ Completed: {lesson_progress.get('completed_date', '?')} | "
                       f"Next review: **{lesson_progress.get('next_review', '?')}** | "
                       f"Reviews: {lesson_progress.get('review_count', 0)}")

        st.markdown("""
        <div style="background:#f8f9ff; border:1px solid #d0d8f8; border-radius:12px; padding:1.3rem; margin-bottom:1rem;">
            <strong>Before completing, confirm:</strong>
        </div>
        """, unsafe_allow_html=True)

        items = ["Read the full HTSK lesson",
                 "Answered all active recall questions honestly",
                 "Completed the Feynman exercise",
                 "Can make 3 sentences using today's grammar",
                 "Added weak items to Anki"]
        for item in items:
            st.checkbox(item, key=f"cc_{lesson_id}_{item[:15]}")

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            score = st.slider("Self-score (0–100):", 0, 100, 75, key=f"sc_{lesson_id}")
        with col2:
            time_spent = st.number_input("Time (min):", 1, 120,
                                          value=lesson["estimated_minutes"], key=f"tm_{lesson_id}")
        with col3:
            st.markdown("<br>", unsafe_allow_html=True)
            btn = "✅ Mark Complete" if status != "completed" else "🔄 Log Review"
            if st.button(btn, use_container_width=True):
                result = mark_lesson_complete(lesson_id, score=score, time_spent=time_spent)
                log_study_session(lesson_id, time_spent, "completed", f"Score: {score}")
                st.success(f"🎉 Done! Next review: **{result['next_review']}**")
                st.balloons()
                st.rerun()


# ─── Review Queue ─────────────────────────────────────────────────────────────

def page_review():
    from data.store import get_due_reviews, get_upcoming_reviews, mark_lesson_complete, log_study_session
    from data.curriculum import get_lesson_by_id

    st.markdown("# 🔄 Review Queue")
    st.markdown("*Spaced repetition keeps knowledge in long-term memory*")
    st.markdown("---")

    due = get_due_reviews()
    upcoming = get_upcoming_reviews(7)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader(f"🔴 Due Today ({len(due)})")
        if not due:
            st.success("🎉 Nothing due today!")
        else:
            st.info("For each review: test yourself FIRST (no looking), then verify, then rate.")
            for lid in due:
                lesson = get_lesson_by_id(lid)
                if not lesson:
                    continue
                with st.expander(f"🔄 {lid} — {lesson['title']}"):
                    st.markdown(f"**Feynman Prompt:** *{lesson['feynman_prompt']}*")
                    st.markdown("**Quick Recall:**")
                    for q in lesson.get("active_recall_questions", [])[:2]:
                        st.markdown(f"- {q}")
                    st.text_area("Recall notes:", key=f"rn_{lid}", height=60)
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        if st.button("😰 Hard", key=f"h_{lid}"):
                            r = mark_lesson_complete(lid, score=40, time_spent=10)
                            log_study_session(lid, 10, "review_hard")
                            st.info(f"Next: {r['next_review']}")
                            st.rerun()
                    with c2:
                        if st.button("😐 Okay", key=f"o_{lid}"):
                            r = mark_lesson_complete(lid, score=70, time_spent=10)
                            log_study_session(lid, 10, "review_okay")
                            st.success(f"Next: {r['next_review']}")
                            st.rerun()
                    with c3:
                        if st.button("😊 Easy", key=f"e_{lid}"):
                            r = mark_lesson_complete(lid, score=95, time_spent=5)
                            log_study_session(lid, 5, "review_easy")
                            st.success(f"Next: {r['next_review']}")
                            st.rerun()

    with col2:
        st.subheader("📅 Next 7 Days")
        if not upcoming:
            st.info("No upcoming reviews in 7 days.")
        else:
            for rev_date, ids in sorted(upcoming.items()):
                label = date.fromisoformat(rev_date).strftime("%a %d %b")
                st.markdown(f"**{label}** — {len(ids)} lesson(s)  \n*{', '.join(ids)}*")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        **Review intervals:**
        | Review # | Interval |
        |----------|----------|
        | 1st | 1 day |
        | 2nd | 3 days |
        | 3rd | 7 days |
        | 4th | 14 days |
        | 5th | 30 days |
        | 6th+ | 90 days |
        """)


# ─── Progress ─────────────────────────────────────────────────────────────────

def page_progress():
    import pandas as pd
    from data.store import load_progress, load_sessions, get_weekly_study_minutes
    from data.curriculum import get_unit_progress_summary

    st.markdown("# 📊 Progress & Analytics")
    st.markdown("---")

    progress = load_progress()
    sessions = load_sessions()

    st.subheader("📈 Study Time This Week (Minutes)")
    weekly = get_weekly_study_minutes()
    if any(v > 0 for v in weekly.values()):
        df = pd.DataFrame({
            "Day": [date.fromisoformat(d).strftime("%a %d") for d in weekly.keys()],
            "Minutes": list(weekly.values())
        })
        st.bar_chart(df.set_index("Day"))
    else:
        st.info("No sessions logged yet. Complete your first lesson!")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📚 Unit Completion")
        summary = get_unit_progress_summary(progress)
        df_u = pd.DataFrame([
            {"Unit": name, "Done": d["completed"], "Total": d["total"], "%": d["percent"]}
            for name, d in summary.items()
        ])
        st.dataframe(df_u, use_container_width=True, hide_index=True)

    with col2:
        if sessions:
            st.subheader("📋 Recent Sessions")
            df_s = pd.DataFrame(sessions[-10:][::-1])
            cols_show = [c for c in ["date", "lesson_id", "duration_min", "activity_type"] if c in df_s.columns]
            st.dataframe(df_s[cols_show], use_container_width=True, hide_index=True)


# ─── Settings ─────────────────────────────────────────────────────────────────

def page_settings():
    from data.store import load_goals, save_goals

    st.markdown("# ⚙️ Settings & Goals")
    st.markdown("---")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("🎯 Study Goals")
        goals = load_goals()
        weekly = st.number_input("Sessions per week:", 1, 14, value=goals.get("weekly_sessions", 3))
        mins = st.number_input("Minutes per session:", 10, 60, value=goals.get("daily_minutes", 25))
        motivation = st.text_area("My motivation:", value=goals.get("motivation", ""),
                                    placeholder="Why are you learning Korean?")
        if st.button("💾 Save Goals", use_container_width=True):
            save_goals({"weekly_sessions": weekly, "daily_minutes": mins, "motivation": motivation})
            st.success("Goals saved!")

    with col2:
        st.subheader("🔗 Free Resources")
        resources = [
            ("How to Study Korean", "https://www.howtostudykorean.com"),
            ("HTSK Anki Decks (free)", "https://www.howtostudykorean.com/anki/"),
            ("Naver Dictionary", "https://dict.naver.com"),
            ("Papago Translator", "https://papago.naver.com"),
            ("Talk To Me In Korean", "https://talktomeinkorean.com"),
            ("HelloTalk (language exchange)", "https://www.hellotalk.com"),
            ("HTSK YouTube", "https://www.youtube.com/c/howtostudykorean"),
        ]
        for name, url in resources:
            st.markdown(f"- [↗ {name}]({url})")

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("🔒 Change Password")
        st.markdown("""
        Edit `.streamlit/secrets.toml` and set:
        ```toml
        app_password_hash = "sha256_hash_of_your_password"
        ```
        Generate SHA-256: [sha256 tool](https://emn178.github.io/online-tools/sha256.html)
        """)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    inject_css()
    if not check_password():
        return
    render_sidebar()

    page = st.session_state.get("current_page", "dashboard")
    if page == "dashboard":
        page_dashboard()
    elif page == "curriculum":
        page_curriculum()
    elif page == "lesson":
        page_lesson()
    elif page == "review":
        page_review()
    elif page == "progress":
        page_progress()
    elif page == "settings":
        page_settings()


if __name__ == "__main__":
    main()
