"""
Peter's Study Tracker — Unified Dashboard
Three subjects: Korean Language, AQA Physics, RAF Application
"""

import streamlit as st
import hashlib
import os
from datetime import date, timedelta

st.set_page_config(
    page_title="Study Tracker",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Password ────────────────────────────────────────────────────────────────

def check_password():
    def _hash(pw): return hashlib.sha256(pw.encode()).hexdigest()
    stored = st.secrets.get("app_password_hash") or _hash(os.environ.get("TRACKER_PASSWORD","study2024"))
    if st.session_state.get("authenticated"): return True
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div style="text-align:center;padding:3rem 0 1.5rem">
            <span style="font-size:4rem">🎯</span>
            <h1 style="font-family:Georgia,serif;font-size:2rem;color:#1a1a2e;margin:.5rem 0">
                Study Tracker
            </h1>
            <p style="color:#666;font-size:.95rem">Korean · Physics · RAF Application</p>
        </div>""", unsafe_allow_html=True)
        with st.form("login"):
            pw = st.text_input("Password", type="password", placeholder="Enter password...", label_visibility="collapsed")
            if st.form_submit_button("→ Enter", use_container_width=True):
                if _hash(pw) == stored:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Incorrect password.")
    return False

# ─── CSS ─────────────────────────────────────────────────────────────────────

def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Playfair+Display:wght@600;700&display=swap');
    html,body,[class*="css"]{font-family:'Noto Sans KR',sans-serif;}
    #MainMenu,footer,.stDeployButton{visibility:hidden;display:none;}
    section[data-testid="stSidebar"]{background:linear-gradient(180deg,#0d1b2a 0%,#1b2838 60%,#1a3a5c 100%);border-right:1px solid #1e3a5f;}
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3{color:#e8eaf0!important;}
    section[data-testid="stSidebar"] .stButton button{background:rgba(255,255,255,.07);color:#e8eaf0;border:1px solid rgba(255,255,255,.12);border-radius:8px;width:100%;text-align:left;transition:all .2s;}
    section[data-testid="stSidebar"] .stButton button:hover{background:rgba(255,255,255,.15);}
    .stat-card{background:white;border-radius:16px;padding:1.4rem;box-shadow:0 2px 12px rgba(0,0,0,.06);border:1px solid #f0f0f8;text-align:center;}
    .stat-number{font-family:'Playfair Display',serif;font-size:2rem;font-weight:700;color:#1a1a2e;line-height:1;}
    .stat-label{color:#888;font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;margin-top:.3rem;}
    .subject-card{border-radius:16px;padding:1.5rem;margin-bottom:1rem;border:1px solid #eee;}
    .goal-card{background:#f8f9ff;border-radius:12px;padding:1.2rem 1.5rem;border-left:4px solid #3498db;margin-bottom:.8rem;}
    .lesson-card{background:white;border-radius:10px;padding:.9rem 1.1rem;margin-bottom:.5rem;border:1px solid #eee;border-left:4px solid #ddd;}
    .lesson-card.completed{border-left-color:#27ae60;background:#f8fff9;}
    .lesson-card.in_progress{border-left-color:#f39c12;background:#fffdf5;}
    .badge{display:inline-block;padding:.18rem .6rem;border-radius:999px;font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;}
    .badge-completed{background:#d4f5e2;color:#1a7a42;}
    .badge-in_progress{background:#fff3cd;color:#856404;}
    .badge-not_started{background:#f0f0f8;color:#888;}
    .progress-bar-container{background:#f0f0f8;border-radius:999px;height:8px;overflow:hidden;margin:.4rem 0;}
    .progress-bar-fill{height:100%;border-radius:999px;}
    .feynman-box{background:linear-gradient(135deg,#1a1a2e,#0f3460);border-radius:12px;padding:1.5rem;color:white;border-left:4px solid #e94560;}
    .recall-box{background:#fffbf0;border:1px solid #f0d060;border-radius:12px;padding:1.2rem 1.5rem;}
    .roadmap-step{background:white;border-radius:10px;padding:.9rem 1.2rem;margin-bottom:.5rem;border:1px solid #e8eaf0;border-left:4px solid #3498db;}
    .roadmap-step.done{border-left-color:#27ae60;background:#f8fff9;}
    .roadmap-step.current{border-left-color:#f39c12;background:#fffdf5;}

    /* ── Dark mode ── */
    body.dark-mode .main .block-container{background:#0d1117!important;}
    body.dark-mode .stat-card{background:#161b22!important;border-color:#30363d!important;}
    body.dark-mode .stat-number{color:#e6edf3!important;}
    body.dark-mode .lesson-card{background:#161b22!important;border-color:#30363d!important;color:#e6edf3!important;}
    body.dark-mode .lesson-card.completed{background:#0d2318!important;}
    body.dark-mode .lesson-card.in_progress{background:#1f1a0a!important;}
    body.dark-mode .roadmap-step{background:#161b22!important;border-color:#30363d!important;}
    body.dark-mode .roadmap-step.done{background:#0d2318!important;}
    body.dark-mode .roadmap-step.current{background:#1f1a0a!important;}
    body.dark-mode .recall-box{background:#1f1a00!important;border-color:#5a4a00!important;}
    body.dark-mode .progress-bar-container{background:#30363d!important;}

    /* ── Mobile ── */
    @media (max-width:768px){
        .block-container{padding:1rem .6rem!important;}
        .stat-card{padding:.8rem .4rem!important;}
        .stat-number{font-size:1.3rem!important;}
        .stat-label{font-size:.62rem!important;}
        .lesson-card{padding:.65rem .75rem!important;}
    }
    </style>""", unsafe_allow_html=True)

    # Dark mode JS toggle
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    dm_class = "dark-mode" if st.session_state.dark_mode else ""
    st.markdown(f'<script>window.parent.document.body.className=window.parent.document.body.className.replace(/\\bdark-mode\\b/,"").trim()+" {dm_class}".trim();</script>', unsafe_allow_html=True)

# ─── Store helpers ────────────────────────────────────────────────────────────

def _sb():
    if "supabase_client" not in st.session_state:
        try:
            from supabase import create_client
            url = st.secrets.get("SUPABASE_URL","")
            key = st.secrets.get("SUPABASE_KEY","")
            st.session_state["supabase_client"] = create_client(url,key) if url and key else None
        except Exception:
            st.session_state["supabase_client"] = None
    return st.session_state["supabase_client"]

def load_progress(prefix=""):
    sb = _sb()
    key = f"_progress_{prefix}"
    if sb:
        try:
            res = sb.table("progress").select("*").execute()
            all_rows = {row["lesson_id"]: row for row in res.data}
            if prefix:
                return {k:v for k,v in all_rows.items() if k.startswith(prefix)}
            return all_rows
        except Exception:
            pass
    return st.session_state.get(key, {})

def _upsert(lesson_id, fields):
    from datetime import datetime
    sb = _sb()
    fields["lesson_id"] = lesson_id
    fields["updated_at"] = datetime.now().isoformat()
    if sb:
        try: sb.table("progress").upsert(fields).execute()
        except Exception: pass
    prefix = lesson_id[:1] if lesson_id else ""
    key = f"_progress_{prefix}"
    prog = st.session_state.get(key, {})
    prog.setdefault(lesson_id, {}).update(fields)
    st.session_state[key] = prog
    # also update full cache
    full = st.session_state.get("_progress_", {})
    full.setdefault(lesson_id, {}).update(fields)
    st.session_state["_progress_"] = full

def mark_complete(lesson_id, score=None, time_spent=25):
    SR = {0:1,1:3,2:7,3:14,4:30,5:90}
    progress = load_progress()
    existing = progress.get(lesson_id, {})
    rc = existing.get("review_count", 0) + 1
    nr = (date.today() + timedelta(days=SR.get(min(rc,5),90))).isoformat()
    fields = {"status":"completed","completed_date":date.today().isoformat(),"score":score,
              "review_count":rc,"next_review":nr,"feynman_done":existing.get("feynman_done",False),
              "notes":existing.get("notes",""),"time_spent":time_spent}
    _upsert(lesson_id, fields)
    log_session(lesson_id, time_spent, "completed", f"Score:{score}")
    return fields

def unmark_complete(lesson_id):
    sb = _sb()
    fields = {"lesson_id": lesson_id, "status": "not_started", "completed_date": None,
              "score": None, "review_count": 0, "next_review": None, "feynman_done": False}
    if sb:
        try: sb.table("progress").upsert(fields).execute()
        except Exception: pass
    for key in [f"_progress_{lesson_id[:1]}", "_progress_"]:
        prog = st.session_state.get(key, {})
        prog[lesson_id] = fields
        st.session_state[key] = prog

def mark_in_progress(lesson_id):
    prog = load_progress()
    if prog.get(lesson_id,{}).get("status") != "completed":
        _upsert(lesson_id, {"status":"in_progress"})

def save_notes(lesson_id, notes):
    _upsert(lesson_id, {"notes":notes})

def mark_feynman(lesson_id):
    _upsert(lesson_id, {"feynman_done":True})

def get_due(prefix=""):
    prog = load_progress(prefix)
    today = date.today().isoformat()
    return [lid for lid,d in prog.items() if d.get("status")=="completed" and d.get("next_review","") <= today]

def log_session(lesson_id, duration, activity, notes=""):
    from datetime import datetime
    sb = _sb()
    row = {"lesson_id":lesson_id,"date":date.today().isoformat(),"time":datetime.now().strftime("%H:%M"),
           "duration":duration,"activity_type":activity}
    if sb:
        try: sb.table("sessions").insert(row).execute()
        except Exception: pass
    sessions = st.session_state.get("_sessions",[])
    sessions.append(row)
    st.session_state["_sessions"] = sessions

def load_sessions():
    sb = _sb()
    if sb:
        try: return sb.table("sessions").select("*").order("date",desc=True).execute().data
        except Exception: pass
    return st.session_state.get("_sessions",[])

def get_streak():
    sessions = load_sessions()
    if not sessions: return 0
    dates = sorted(set(s["date"] for s in sessions), reverse=True)
    today = date.today().isoformat()
    yesterday = (date.today()-timedelta(days=1)).isoformat()
    if dates[0] not in (today, yesterday): return 0
    streak = 0
    check = date.today() if dates[0]==today else date.today()-timedelta(days=1)
    for d in dates:
        if d==check.isoformat(): streak+=1; check-=timedelta(days=1)
        else: break
    return streak

def total_time():
    return sum(s.get("duration",0) for s in load_sessions())

# ─── Sidebar ──────────────────────────────────────────────────────────────────

def render_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style="text-align:center;padding:1rem 0 .5rem">
            <span style="font-size:2.5rem">🎯</span>
            <h2 style="color:white;font-family:Georgia,serif;font-size:1.2rem;margin:.3rem 0 0">Study Tracker</h2>
            <p style="color:#6a8ab0;font-size:.72rem;margin:0">Korean · Physics · RAF</p>
        </div>
        <hr style="border-color:#1e3a5f;margin:1rem 0">""", unsafe_allow_html=True)

        pages = {
            "🏠  Overview": "overview",
            "🇰🇷  Korean": "korean",
            "⚛️  Physics": "physics",
            "✈️  RAF Application": "raf",
        }
        if "current_page" not in st.session_state:
            st.session_state.current_page = "overview"

        for label, key in pages.items():
            if st.button(label, key=f"nav_{key}", use_container_width=True):
                st.session_state.current_page = key
                st.rerun()

        st.markdown('<hr style="border-color:#1e3a5f;margin:1.5rem 0 1rem">', unsafe_allow_html=True)

        all_prog = load_progress()
        completed = sum(1 for d in all_prog.values() if d.get("status")=="completed")
        hours = round(total_time()/60,1)
        streak = get_streak()
        k_due = len(get_due("U"))
        p_due = len(get_due("P"))
        r_due = len(get_due("R"))
        due_total = k_due + p_due + r_due

        st.markdown(f"""
        <div style="padding:0 .5rem;font-size:.84rem">
            <div style="color:#6a8ab0;font-size:.68rem;text-transform:uppercase;letter-spacing:.1em;margin-bottom:.7rem">Quick Stats</div>
            <div style="display:flex;justify-content:space-between;margin-bottom:.35rem">
                <span style="color:#ccc">🔥 Streak</span><span style="color:white;font-weight:600">{streak} days</span>
            </div>
            <div style="display:flex;justify-content:space-between;margin-bottom:.35rem">
                <span style="color:#ccc">✅ Completed</span><span style="color:white;font-weight:600">{completed}</span>
            </div>
            <div style="display:flex;justify-content:space-between;margin-bottom:.35rem">
                <span style="color:#ccc">🔄 Reviews Due</span>
                <span style="color:{'#ff6b6b' if due_total>0 else 'white'};font-weight:600">{due_total}</span>
            </div>
            <div style="display:flex;justify-content:space-between">
                <span style="color:#ccc">⏱ Total Time</span><span style="color:white;font-weight:600">{hours}h</span>
            </div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        dm_label = "☀️  Light Mode" if st.session_state.get("dark_mode") else "🌙  Dark Mode"
        if st.button(dm_label, use_container_width=True):
            st.session_state.dark_mode = not st.session_state.get("dark_mode", False)
            st.rerun()

        if st.button("🔒  Log Out", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()

# ─── Overview Page ────────────────────────────────────────────────────────────

def page_overview():
    from data.korean_curriculum import CURRICULUM as K_CUR
    from data.physics_curriculum import PHYSICS_CURRICULUM as P_CUR
    from data.raf_curriculum import RAF_CURRICULUM as R_CUR

    st.markdown("# 🎯 Overview")
    st.markdown(f"*{date.today().strftime('%A, %d %B %Y')}*")
    st.markdown("---")

    all_prog = load_progress()
    sessions = load_sessions()
    streak = get_streak()
    hours = round(total_time()/60,1)

    # ── Today's Goal Prompt ──
    today_name = date.today().strftime("%A")
    all_prog_early = load_progress()

    # Work out what to focus on for each subject today
    def next_lesson_id(prefix, curriculum):
        in_prog = [k for k,v in all_prog_early.items() if k.startswith(prefix) and v.get("status")=="in_progress"]
        if in_prog: return in_prog[0], "continue"
        due = get_due(prefix)
        if due: return due[0], "review"
        all_l = [l["id"] for u in curriculum.values() for l in u["lessons"]]
        not_started = [l for l in all_l if all_prog_early.get(l,{}).get("status","not_started")=="not_started"]
        if not_started: return not_started[0], "start"
        return None, "done"

    k_id, k_type = next_lesson_id("U", K_CUR)
    p_id, p_type = next_lesson_id("P", P_CUR)
    r_id, r_type = next_lesson_id("R", R_CUR)

    type_labels = {"continue":"▶️ Continue","review":"🔄 Review","start":"🆕 Start","done":"✅ All done"}
    type_colors = {"continue":"#f39c12","review":"#e74c3c","start":"#27ae60","done":"#888"}

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#0d1b2a,#1a3a5c);border-radius:16px;padding:1.4rem 1.8rem;
                margin-bottom:1.5rem;border:1px solid #1e3a5f;color:white">
        <div style="font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:#6a8ab0;margin-bottom:.6rem">
            🗓️ Today's Focus — {today_name}
        </div>
        <div style="display:flex;gap:1.5rem;flex-wrap:wrap">
            <div style="flex:1;min-width:160px">
                <span style="color:#aaa;font-size:.75rem">🇰🇷 KOREAN</span><br>
                <span style="color:{type_colors[k_type]};font-size:.82rem;font-weight:600">{type_labels[k_type]}</span>
                <span style="color:#ddd;font-size:.82rem"> {k_id or ''}</span>
            </div>
            <div style="flex:1;min-width:160px">
                <span style="color:#aaa;font-size:.75rem">⚛️ PHYSICS</span><br>
                <span style="color:{type_colors[p_type]};font-size:.82rem;font-weight:600">{type_labels[p_type]}</span>
                <span style="color:#ddd;font-size:.82rem"> {p_id or ''}</span>
            </div>
            <div style="flex:1;min-width:160px">
                <span style="color:#aaa;font-size:.75rem">✈️ RAF</span><br>
                <span style="color:{type_colors[r_type]};font-size:.82rem;font-weight:600">{type_labels[r_type]}</span>
                <span style="color:#ddd;font-size:.82rem"> {r_id or ''}</span>
            </div>
            <div style="flex:1;min-width:160px;border-left:1px solid #1e3a5f;padding-left:1.2rem">
                <span style="color:#aaa;font-size:.75rem">⏱ TARGET</span><br>
                <span style="color:white;font-size:.82rem;font-weight:600">3 × 25 min blocks</span><br>
                <span style="color:#6a8ab0;font-size:.75rem">~75 min total today</span>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    # Stats row
    k_lessons = sum(len(u["lessons"]) for u in K_CUR.values())
    p_lessons = sum(len(u["lessons"]) for u in P_CUR.values())
    r_lessons = sum(len(u["lessons"]) for u in R_CUR.values())
    total_lessons = k_lessons + p_lessons + r_lessons
    done = sum(1 for d in all_prog.values() if d.get("status")=="completed")

    c1,c2,c3,c4,c5 = st.columns(5)
    for col,num,label in [
        (c1,f"🔥 {streak}","Day Streak"),
        (c2,str(done),"Lessons Done"),
        (c3,str(total_lessons),"Total Lessons"),
        (c4,f"{hours}h","Study Time"),
        (c5,str(len(sessions)),"Sessions Logged"),
    ]:
        with col:
            st.markdown(f'<div class="stat-card"><div class="stat-number">{num}</div><div class="stat-label">{label}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Subject progress cards
    col_left, col_right = st.columns([3,2])

    with col_left:
        st.subheader("📊 Progress by Subject")

        subjects = [
            ("🇰🇷 Korean Language", K_CUR, "#e74c3c", "korean", "U"),
            ("⚛️ Physics (AQA GCSE)", P_CUR, "#3498db", "physics", "P"),
            ("✈️ RAF Application", R_CUR, "#1a3a6e", "raf", "R"),
        ]

        for name, curriculum, color, page_key, prefix in subjects:
            total = sum(len(u["lessons"]) for u in curriculum.values())
            done_s = sum(1 for k,d in all_prog.items() if k.startswith(prefix) and d.get("status")=="completed")
            pct = round(done_s/total*100) if total else 0
            due_count = len(get_due(prefix))

            st.markdown(f"""
            <div style="background:white;border-radius:14px;padding:1.2rem 1.5rem;margin-bottom:.8rem;
                        border:1px solid #eee;border-left:5px solid {color};">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:.5rem">
                    <span style="font-weight:700;font-size:1rem">{name}</span>
                    <span style="font-size:.82rem;color:#888">{done_s}/{total} lessons · {pct}%</span>
                </div>
                <div class="progress-bar-container">
                    <div class="progress-bar-fill" style="width:{pct}%;background:{color}"></div>
                </div>
                {'<span style="font-size:.75rem;color:#e74c3c;font-weight:600">🔄 ' + str(due_count) + ' review(s) due</span>' if due_count > 0 else '<span style="font-size:.75rem;color:#888">No reviews due</span>'}
            </div>""", unsafe_allow_html=True)

            if st.button(f"Go to {name.split()[1]} →", key=f"goto_{page_key}", use_container_width=False):
                st.session_state.current_page = page_key
                st.rerun()

    with col_right:
        st.subheader("🗓️ Today's Plan")
        st.markdown("""
        <div style="background:#f0f7ff;border-radius:12px;padding:1rem 1.2rem;font-size:.88rem;margin-bottom:1rem">
            <strong>Daily rhythm:</strong><br>
            🇰🇷 25 min Korean<br>
            ⚛️ 25 min Physics<br>
            ✈️ 25 min RAF prep<br>
            <span style="color:#888;font-size:.78rem">~75 min total · 3 focused blocks</span>
        </div>""", unsafe_allow_html=True)

        # What to do next per subject
        for name, prefix, page_key, icon in [
            ("Korean","U","korean","🇰🇷"),
            ("Physics","P","physics","⚛️"),
            ("RAF","R","raf","✈️"),
        ]:
            prog = {k:v for k,v in all_prog.items() if k.startswith(prefix)}
            in_prog = [k for k,v in prog.items() if v.get("status")=="in_progress"]
            if in_prog:
                lid = in_prog[0]
                st.markdown(f"""<div style="background:white;border-radius:8px;padding:.7rem 1rem;
                    margin-bottom:.4rem;border:1px solid #eee;border-left:3px solid #f39c12">
                    {icon} <strong>Continue:</strong> {lid}</div>""", unsafe_allow_html=True)
            else:
                due = get_due(prefix)
                if due:
                    st.markdown(f"""<div style="background:white;border-radius:8px;padding:.7rem 1rem;
                        margin-bottom:.4rem;border:1px solid #eee;border-left:3px solid #e74c3c">
                        {icon} <strong>Review due:</strong> {due[0]}</div>""", unsafe_allow_html=True)
                else:
                    st.markdown(f"""<div style="background:white;border-radius:8px;padding:.7rem 1rem;
                        margin-bottom:.4rem;border:1px solid #eee;border-left:3px solid #27ae60">
                        {icon} Start next lesson</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # ── End Goals & Roadmaps ──
    st.subheader("🚀 Your End Goals & Roadmaps")
    st.markdown("*The bigger picture — where all of this is heading*")
    st.markdown("<br>", unsafe_allow_html=True)

    goal_col1, goal_col2, goal_col3 = st.columns(3)

    with goal_col1:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#c0392b,#e74c3c);border-radius:16px;padding:1.5rem;color:white;text-align:center;margin-bottom:1rem">
            <div style="font-size:2.5rem">🇰🇷</div>
            <h3 style="margin:.5rem 0 .2rem;font-family:Georgia,serif">Korean Fluency</h3>
            <p style="font-size:.82rem;opacity:.85;margin:0">Conversational with her family</p>
        </div>""", unsafe_allow_html=True)

        with st.expander("📋 Step-by-step roadmap"):
            steps = [
                ("✅ Current", "Absolute beginner — starting HTSK Unit 0", "done"),
                ("🎯 Next", "Complete Hangul (Unit 0) — read Korean script", "current"),
                ("📍 3 months", "Finish Unit 1 — basic sentences and grammar", ""),
                ("📍 6 months", "Finish Unit 2 — hold simple conversations", ""),
                ("📍 12 months", "Unit 3-4 complete — discuss everyday topics", ""),
                ("📍 18 months", "Unit 5-6 — watch Korean TV without subtitles", ""),
                ("🏁 Goal", "Conversational with her family — Unit 7+ complete", ""),
            ]
            for label, desc, status in steps:
                cls = "done" if status=="done" else ("current" if status=="current" else "roadmap-step")
                st.markdown(f'<div class="roadmap-step {cls}" style="margin-bottom:.4rem"><strong>{label}:</strong> {desc}</div>', unsafe_allow_html=True)

    with goal_col2:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#1a3a6e,#2e4d9e);border-radius:16px;padding:1.5rem;color:white;text-align:center;margin-bottom:1rem">
            <div style="font-size:2.5rem">✈️</div>
            <h3 style="margin:.5rem 0 .2rem;font-family:Georgia,serif">RAF Pilot</h3>
            <p style="font-size:.82rem;opacity:.85;margin:0">Commission & earn your wings</p>
        </div>""", unsafe_allow_html=True)

        with st.expander("📋 Step-by-step roadmap"):
            steps = [
                ("✅ Done", "Initial application submitted", "done"),
                ("✅ Done", "DAA (Digital Aptitude Assessment)", "done"),
                ("✅ Done", "ID check at AFCO", "done"),
                ("🎯 Next", "Medical examination — pass all standards", "current"),
                ("📍 Soon", "CBAT — computer aptitude tests", ""),
                ("📍 Soon", "OASC — Officer & Aircrew Selection Centre", ""),
                ("📍 Pass", "IOT — Initial Officer Training, RAF Cranwell (30 wks)", ""),
                ("📍 Training", "EFTS — Elementary Flying (Grob Prefect)", ""),
                ("📍 Training", "BFJT/AFJT — Basic/Advanced Flying Training", ""),
                ("🏁 Goal", "Wings ceremony — front-line fast jet posting", ""),
            ]
            for label, desc, status in steps:
                cls = "done" if status=="done" else ("current" if status=="current" else "roadmap-step")
                st.markdown(f'<div class="roadmap-step {cls}" style="margin-bottom:.4rem"><strong>{label}:</strong> {desc}</div>', unsafe_allow_html=True)

    with goal_col3:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#145a32,#27ae60);border-radius:16px;padding:1.5rem;color:white;text-align:center;margin-bottom:1rem">
            <div style="font-size:2.5rem">⚛️</div>
            <h3 style="margin:.5rem 0 .2rem;font-family:Georgia,serif">Physics Mastery</h3>
            <p style="font-size:.82rem;opacity:.85;margin:0">GCSE → Aerospace depth</p>
        </div>""", unsafe_allow_html=True)

        with st.expander("📋 Step-by-step roadmap"):
            steps = [
                ("🎯 Now", "Topic 1 — Energy (foundations)", "current"),
                ("📍 Month 1", "Topics 1-2 complete — Energy & Electricity", ""),
                ("📍 Month 2", "Topics 3-4 — Particle Model & Radioactivity", ""),
                ("📍 Month 3", "Topic 5 — Forces (key for aviation)", ""),
                ("📍 Month 4", "Topics 6-7 — Waves & Electromagnetism", ""),
                ("📍 Month 5", "Topic 8 — Space Physics", ""),
                ("📍 Extension", "Aerospace physics: aerodynamics, propulsion, navigation", ""),
                ("🏁 Goal", "Confident physics foundation to support RAF training", ""),
            ]
            for label, desc, status in steps:
                cls = "done" if status=="done" else ("current" if status=="current" else "roadmap-step")
                st.markdown(f'<div class="roadmap-step {cls}" style="margin-bottom:.4rem"><strong>{label}:</strong> {desc}</div>', unsafe_allow_html=True)

# ─── Generic Lesson Viewer (shared by all subjects) ──────────────────────────

def render_lesson_viewer(lesson, unit_color, unit_level):
    lesson_id = lesson["id"]
    progress = load_progress()
    lesson_prog = progress.get(lesson_id, {})
    status = lesson_prog.get("status", "not_started")

    st.markdown(f"""
    <div style="background:{unit_color}18;border-left:5px solid {unit_color};border-radius:0 12px 12px 0;
                padding:1.4rem 2rem;margin-bottom:1.5rem">
        <div style="display:flex;justify-content:space-between;align-items:flex-start">
            <div>
                <span style="font-size:.7rem;color:#888;text-transform:uppercase;letter-spacing:.1em">
                    {lesson.get('unit','')} · {unit_level}
                </span>
                <h2 style="font-family:Georgia,serif;margin:.3rem 0;font-size:1.4rem;color:#1a1a2e">{lesson['title']}</h2>
                <p style="color:#666;margin:0;font-size:.88rem">{lesson.get('subtitle','')}</p>
            </div>
            <div style="text-align:right">
                <span class="badge badge-{status}">{status.replace('_',' ').title()}</span><br>
                <span style="font-size:.8rem;color:#888;display:block;margin-top:.3rem">⏱ {lesson['estimated_minutes']} min</span>
                <a href="{lesson['url']}" target="_blank" style="font-size:.76rem;color:#3a5bd9">↗ Open Resource</a>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    tab1,tab2,tab3,tab4,tab5 = st.tabs(["📋 Goals & Vocab","🧠 Active Recall","✍️ Feynman","📝 Notes","✅ Mark Complete"])

    with tab1:
        c1,c2 = st.columns([3,2])
        with c1:
            st.markdown("### 🎯 Learning Goals")
            for i,goal in enumerate(lesson["learning_goals"],1):
                st.markdown(f"""
                <div style="display:flex;gap:.75rem;align-items:flex-start;padding:.65rem;
                            background:#f8f9ff;border-radius:8px;margin-bottom:.4rem">
                    <span style="background:{unit_color};color:white;border-radius:50%;width:20px;height:20px;
                                 display:inline-flex;align-items:center;justify-content:center;font-size:.7rem;
                                 font-weight:700;flex-shrink:0">{i}</span>
                    <span style="font-size:.88rem">{goal}</span>
                </div>""", unsafe_allow_html=True)

            st.markdown("### 📖 Key Vocabulary")
            vocab_html = " ".join([
                f'<span style="background:#f0f4ff;border:1px solid #d0d8f8;border-radius:6px;'
                f'padding:.25rem .65rem;margin:.15rem;display:inline-block;font-size:.85rem">{v}</span>'
                for v in lesson.get("key_vocab",[])
            ])
            st.markdown(f"<div style='line-height:2.4'>{vocab_html}</div>", unsafe_allow_html=True)

        with c2:
            st.markdown("### 🛠️ Techniques")
            icons = {"Active Recall":"🧠","Spaced Repetition":"🔄","Feynman Technique":"✍️",
                     "Writing Practice":"📝","Pattern Recognition":"🔍","Sentence Building":"🔨"}
            for t in lesson.get("techniques",[]):
                st.markdown(f'<div style="background:white;border:1px solid #eee;border-radius:8px;padding:.45rem .85rem;margin-bottom:.3rem;font-size:.86rem">{icons.get(t,"💡")} {t}</div>', unsafe_allow_html=True)

            st.markdown("### 🔗 Resources")
            for r in lesson.get("resources",[]):
                st.markdown(f'<a href="{r["url"]}" target="_blank" style="display:inline-block;background:#f0f4ff;color:#3a5bd9;padding:.3rem .8rem;border-radius:999px;text-decoration:none;font-size:.8rem;border:1px solid #d0d8f8;margin:.15rem">↗ {r["name"]}</a>', unsafe_allow_html=True)

        if status == "not_started":
            st.markdown("<br>",unsafe_allow_html=True)
            if st.button("▶️ Start This Lesson", use_container_width=True, key=f"start_{lesson_id}"):
                mark_in_progress(lesson_id)
                st.success("Lesson started!")
                st.rerun()

    with tab2:
        st.markdown("### 🧠 Active Recall")
        st.markdown('<div style="background:#e8f4ff;border-left:4px solid #3a8fd9;border-radius:0 8px 8px 0;padding:.85rem 1.2rem;margin-bottom:1.4rem;font-size:.86rem"><strong>Protocol:</strong> Answer each question OUT LOUD or in writing <em>before</em> expanding. Struggling = learning.</div>', unsafe_allow_html=True)
        for i,q in enumerate(lesson.get("active_recall_questions",[]),1):
            st.markdown(f'<div class="recall-box" style="margin-bottom:.7rem"><strong>Q{i}.</strong> {q}</div>', unsafe_allow_html=True)
            with st.expander(f"→ Answer space for Q{i}"):
                st.text_area("Your answer:", key=f"ar_{lesson_id}_{i}", height=80, placeholder="Write before checking...")
                st.markdown(f'<a href="{lesson["url"]}" target="_blank" style="font-size:.82rem;color:#3a5bd9">↗ Verify in resource</a>', unsafe_allow_html=True)

    with tab3:
        st.markdown("### ✍️ Feynman Technique")
        st.markdown("""
        <div class="feynman-box" style="margin-bottom:1.4rem">
            <h4 style="color:#ff6b6b;margin:0 0 .5rem">The Feynman Method</h4>
            <ol style="margin:0;padding-left:1.2rem;line-height:1.8;font-size:.88rem">
                <li>Study the concept in the resource</li>
                <li>Close it — explain simply, as if teaching a 10-year-old</li>
                <li>Find where your explanation breaks down (that's your gap)</li>
                <li>Re-read only that part</li>
                <li>Re-explain until complete and clear</li>
            </ol>
        </div>""", unsafe_allow_html=True)
        st.markdown(f'<div style="background:#fff8f0;border:2px solid #e94560;border-radius:12px;padding:1.2rem 1.4rem;font-size:.93rem;margin-bottom:1rem"><strong>Your prompt:</strong><br><br>{lesson["feynman_prompt"]}</div>', unsafe_allow_html=True)
        feyn = st.text_area("Your explanation:", key=f"feyn_{lesson_id}", height=180, placeholder="Explain simply. Use examples. If you can't, you don't know it yet.")
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Save Feynman", use_container_width=True, key=f"feynsave_{lesson_id}"):
                if feyn.strip():
                    mark_feynman(lesson_id)
                    save_notes(lesson_id, f"[Feynman {date.today()}]\n{feyn}\n\n" + lesson_prog.get("notes",""))
                    st.success("Saved!")
                else:
                    st.warning("Write your explanation first.")
        with c2:
            if lesson_prog.get("feynman_done"):
                st.success("✅ Feynman completed")

    with tab4:
        st.markdown("### 📝 My Notes")
        notes = st.text_area("Notes:", value=lesson_prog.get("notes",""), key=f"notes_{lesson_id}", height=280,
                              placeholder="Write your own explanations, examples, connections...\nAvoid copying — process and rephrase.")
        if st.button("💾 Save Notes", use_container_width=True, key=f"savenotes_{lesson_id}"):
            save_notes(lesson_id, notes)
            st.success("Saved!")

    with tab5:
        st.markdown("### ✅ Mark Complete")
        if status == "completed":
            st.success(f"✅ Completed: {lesson_prog.get('completed_date','?')} | Next review: **{lesson_prog.get('next_review','?')}** | Reviews done: {lesson_prog.get('review_count',0)}")
        st.markdown('<div style="background:#f8f9ff;border:1px solid #d0d8f8;border-radius:12px;padding:1.2rem;margin-bottom:1rem"><strong>Before completing, confirm:</strong></div>', unsafe_allow_html=True)
        for item in ["Read/watched the full resource","Answered all active recall questions honestly","Completed the Feynman exercise","Can explain the key concepts without notes"]:
            st.checkbox(item, key=f"cc_{lesson_id}_{item[:12]}")
        c1,c2,c3 = st.columns(3)
        with c1: score = st.slider("Self-score:", 0, 100, 75, key=f"sc_{lesson_id}")
        with c2: t = st.number_input("Time (min):", 1, 120, value=lesson["estimated_minutes"], key=f"tm_{lesson_id}")
        with c3:
            st.markdown("<br>",unsafe_allow_html=True)
            btn = "✅ Mark Complete" if status != "completed" else "🔄 Log Review"
            if st.button(btn, use_container_width=True, key=f"mc_{lesson_id}"):
                result = mark_complete(lesson_id, score=score, time_spent=t)
                st.success(f"🎉 Done! Next review: **{result['next_review']}**")
                st.balloons()
                st.rerun()

        if status == "completed":
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("↩️ Unmark as Complete", key=f"unmark_{lesson_id}", use_container_width=True):
                unmark_complete(lesson_id)
                st.info("Lesson unmarked — back to not started.")
                st.rerun()

# ─── Generic Subject Page ─────────────────────────────────────────────────────

def render_subject_page(subject_name, curriculum, prefix, color, icon):
    progress = load_progress()
    due = get_due(prefix)

    # Sub-navigation
    if f"{prefix}_view" not in st.session_state:
        st.session_state[f"{prefix}_view"] = "curriculum"

    c1,c2,c3 = st.columns(3)
    with c1:
        if st.button("📚 Curriculum", use_container_width=True, key=f"{prefix}_nav_cur"):
            st.session_state[f"{prefix}_view"] = "curriculum"
    with c2:
        if st.button("📖 Lesson Viewer", use_container_width=True, key=f"{prefix}_nav_les"):
            st.session_state[f"{prefix}_view"] = "lesson"
    with c3:
        if st.button(f"🔄 Reviews ({len(due)})", use_container_width=True, key=f"{prefix}_nav_rev"):
            st.session_state[f"{prefix}_view"] = "review"

    st.markdown("---")
    view = st.session_state[f"{prefix}_view"]

    # Curriculum view
    if view == "curriculum":
        st.subheader(f"{icon} {subject_name} Curriculum")
        for unit_name, unit_data in curriculum.items():
            lessons = unit_data["lessons"]
            done = sum(1 for l in lessons if progress.get(l["id"],{}).get("status")=="completed")
            pct = round(done/len(lessons)*100) if lessons else 0
            with st.expander(f"**{unit_name} — {unit_data['title']}** | {done}/{len(lessons)} ({pct}%)", expanded=False):
                st.markdown(f'<div class="progress-bar-container"><div class="progress-bar-fill" style="width:{pct}%;background:{unit_data["color"]}"></div></div><p style="color:#888;font-size:.83rem;margin-top:.4rem">{unit_data["description"]}</p>', unsafe_allow_html=True)
                for lesson in lessons:
                    status = progress.get(lesson["id"],{}).get("status","not_started")
                    c_l, c_r = st.columns([8,1])
                    with c_l:
                        st.markdown(f"""
                        <div class="lesson-card {status}">
                            <div style="display:flex;justify-content:space-between;align-items:center">
                                <div>
                                    <strong>{lesson['id']} — {lesson['title']}</strong><br>
                                    <span style="color:#888;font-size:.78rem">{lesson.get('subtitle','')}</span>
                                </div>
                                <div style="text-align:right;min-width:110px">
                                    <span class="badge badge-{status}">{status.replace('_',' ').title()}</span><br>
                                    <span style="font-size:.72rem;color:#aaa">⏱ {lesson['estimated_minutes']} min</span>
                                </div>
                            </div>
                        </div>""", unsafe_allow_html=True)
                    with c_r:
                        st.markdown("<br>",unsafe_allow_html=True)
                        if st.button("📖", key=f"open_{lesson['id']}", help="Open lesson"):
                            st.session_state[f"{prefix}_active_lesson"] = lesson["id"]
                            st.session_state[f"{prefix}_view"] = "lesson"
                            st.rerun()

    # Lesson viewer
    elif view == "lesson":
        all_lessons = [l for u in curriculum.values() for l in u["lessons"]]
        options = {f"{l['id']} — {l['title']}": l["id"] for l in all_lessons}
        default_id = st.session_state.get(f"{prefix}_active_lesson", all_lessons[0]["id"])
        default_label = next((k for k,v in options.items() if v==default_id), list(options.keys())[0])
        selected = st.selectbox("Select Lesson", list(options.keys()), index=list(options.keys()).index(default_label), key=f"{prefix}_sel")
        lesson_id = options[selected]

        # Find lesson
        lesson = None
        for unit_name, unit_data in curriculum.items():
            for l in unit_data["lessons"]:
                if l["id"] == lesson_id:
                    lesson = dict(l)
                    lesson["unit"] = unit_name
                    unit_color = unit_data["color"]
                    unit_level = unit_data["level"]
                    break

        if lesson:
            render_lesson_viewer(lesson, unit_color, unit_level)

    # Review queue
    elif view == "review":
        st.subheader(f"🔄 {subject_name} Reviews Due")
        if not due:
            st.success("🎉 Nothing due today!")
        else:
            st.info(f"{len(due)} lesson(s) due for review. Test yourself before rating.")
            for lid in due:
                lesson = None
                for unit_name, unit_data in curriculum.items():
                    for l in unit_data["lessons"]:
                        if l["id"] == lid:
                            lesson = l
                            break
                if not lesson: continue
                with st.expander(f"🔄 {lid} — {lesson['title']}"):
                    st.markdown(f"**Feynman Prompt:** *{lesson['feynman_prompt']}*")
                    for q in lesson.get("active_recall_questions",[])[:2]:
                        st.markdown(f"- {q}")
                    st.text_area("Recall notes:", key=f"rn_{lid}", height=60)
                    r1,r2,r3 = st.columns(3)
                    with r1:
                        if st.button("😰 Hard", key=f"h_{lid}"):
                            r = mark_complete(lid, score=40, time_spent=10)
                            st.info(f"Next: {r['next_review']}")
                            st.rerun()
                    with r2:
                        if st.button("😐 Okay", key=f"o_{lid}"):
                            r = mark_complete(lid, score=70, time_spent=10)
                            st.success(f"Next: {r['next_review']}")
                            st.rerun()
                    with r3:
                        if st.button("😊 Easy", key=f"e_{lid}"):
                            r = mark_complete(lid, score=95, time_spent=5)
                            st.success(f"Next: {r['next_review']}")
                            st.rerun()

# ─── Subject Pages ────────────────────────────────────────────────────────────

def page_korean():
    from data.korean_curriculum import CURRICULUM
    st.markdown("# 🇰🇷 Korean Language")
    st.markdown("*Resource: [How to Study Korean](https://www.howtostudykorean.com) — work through every unit systematically*")
    render_subject_page("Korean", CURRICULUM, "U", "#e74c3c", "🇰🇷")

def page_physics():
    from data.physics_curriculum import PHYSICS_CURRICULUM
    st.markdown("# ⚛️ Physics — AQA GCSE")
    st.markdown("*Resource: [BBC Bitesize](https://www.bbc.co.uk/bitesize/examspecs/z8xtmnb) — focus on understanding over note-copying*")
    render_subject_page("Physics", PHYSICS_CURRICULUM, "P", "#3498db", "⚛️")

def page_raf():
    from data.raf_curriculum import RAF_CURRICULUM
    st.markdown("# ✈️ RAF Application")
    st.markdown("*Targeted prep for: Medical → CBAT → OASC → IOT*")
    render_subject_page("RAF", RAF_CURRICULUM, "R", "#1a3a6e", "✈️")

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    inject_css()
    if not check_password(): return
    render_sidebar()
    page = st.session_state.get("current_page","overview")
    if page == "overview": page_overview()
    elif page == "korean": page_korean()
    elif page == "physics": page_physics()
    elif page == "raf": page_raf()

if __name__ == "__main__":
    main()
