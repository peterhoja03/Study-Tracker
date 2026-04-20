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

SESSION_DURATION_HOURS = 2
_SESSION_KEY = "tracker_session"

def _get_session_table():
    """Return a single-row 'sessions_auth' table value from Supabase, or None."""
    sb = _sb()
    if sb:
        try:
            res = sb.table("auth_session").select("*").eq("id", 1).execute()
            return res.data[0] if res.data else None
        except Exception:
            return None
    return None

def _save_session_to_db(login_time_iso):
    sb = _sb()
    if sb:
        try:
            sb.table("auth_session").upsert({"id": 1, "login_time": login_time_iso}).execute()
        except Exception:
            pass

def _clear_session_from_db():
    sb = _sb()
    if sb:
        try:
            sb.table("auth_session").delete().eq("id", 1).execute()
        except Exception:
            pass

def check_password():
    from datetime import datetime
    def _hash(pw): return hashlib.sha256(pw.encode()).hexdigest()
    stored = st.secrets.get("app_password_hash") or _hash(os.environ.get("TRACKER_PASSWORD","study2024"))

    # Check Supabase for a persisted login session
    if not st.session_state.get("authenticated"):
        row = _get_session_table()
        if row and row.get("login_time"):
            try:
                login_time = datetime.fromisoformat(row["login_time"])
                elapsed = (datetime.now() - login_time).total_seconds() / 3600
                if elapsed < SESSION_DURATION_HOURS:
                    st.session_state.authenticated = True
                    st.session_state.login_time = login_time
            except Exception:
                pass

    if st.session_state.get("authenticated"):
        login_time = st.session_state.get("login_time")
        if login_time:
            elapsed = (datetime.now() - login_time).total_seconds() / 3600
            if elapsed < SESSION_DURATION_HOURS:
                return True
        # Session expired
        st.session_state.authenticated = False
        st.session_state.pop("login_time", None)
        _clear_session_from_db()

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
                    now = datetime.now()
                    st.session_state.authenticated = True
                    st.session_state.login_time = now
                    _save_session_to_db(now.isoformat())
                    st.rerun()
                else:
                    st.error("Incorrect password.")
    return False

# ─── CSS ─────────────────────────────────────────────────────────────────────

def inject_css():
    dark = st.session_state.get("dark_mode", False)
    # ── Colour tokens ──────────────────────────────────────────────────────────
    bg           = "#0a0e14" if dark else "#f8f9fa"
    bg2          = "#0d1117" if dark else "#ffffff"
    card_bg      = "#161b22" if dark else "#ffffff"
    card_border  = "#30363d" if dark else "#e8e8f0"
    text_col     = "#e6edf3" if dark else "#1a1a2e"
    subtext      = "#8b949e" if dark else "#666"
    recall_bg    = "#1a1500" if dark else "#fffbf0"
    recall_border= "#5a4a00" if dark else "#f0d060"
    done_bg      = "#0d2318" if dark else "#f0fff5"
    prog_bg      = "#21262d" if dark else "#eeeeee"
    today_bg     = "#0d1f3c" if dark else "#f0f7ff"
    today_border = "#1e3a5f" if dark else "#c8deff"
    inprog_bg    = "#1a1400" if dark else "#fffdf0"
    input_bg     = "#0d1117" if dark else "#ffffff"
    tab_bg       = "#161b22" if dark else "#f0f2f6"
    expander_bg  = "#161b22" if dark else "#ffffff"
    dark_text_css = """
    h1,h2,h3,h4,h5,h6,p,span,div,label,li { color: #e6edf3 !important; }
    .stMarkdown, .stMarkdown p, .stMarkdown span { color: #e6edf3 !important; }
    """ if dark else ""
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Playfair+Display:wght@600;700&display=swap');

    /* ── Global reset ── */
    html, body, [class*="css"] {{
        font-family: 'Noto Sans KR', sans-serif !important;
    }}
    #MainMenu, footer, .stDeployButton {{ visibility:hidden; display:none; }}

    /* ── Main content area ── */
    .main, .main > div, .block-container,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewBlockContainer"],
    section.main > div {{
        background-color: {bg} !important;
    }}
    .block-container {{ transition: background .3s; }}
    {dark_text_css}

    /* ── Streamlit native elements ── */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div {{
        background-color: {input_bg} !important;
        color: {text_col} !important;
        border-color: {card_border} !important;
    }}
    .stButton > button {{
        background-color: {card_bg} !important;
        color: {text_col} !important;
        border-color: {card_border} !important;
    }}
    .stButton > button:hover {{
        border-color: #58a6ff !important;
        color: #58a6ff !important;
    }}

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {{
        background-color: {tab_bg} !important;
        border-radius: 8px;
    }}
    .stTabs [data-baseweb="tab"] {{
        background-color: transparent !important;
        color: {subtext} !important;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: {card_bg} !important;
        color: {text_col} !important;
    }}
    .stTabs [data-baseweb="tab-panel"] {{
        background-color: {bg} !important;
    }}

    /* ── Expanders ── */
    [data-testid="stExpander"] {{
        background-color: {expander_bg} !important;
        border-color: {card_border} !important;
    }}
    [data-testid="stExpander"] summary {{
        color: {text_col} !important;
    }}

    /* ── Sliders ── */
    [data-testid="stSlider"] label {{ color: {text_col} !important; }}

    /* ── Alerts / info boxes ── */
    [data-testid="stAlert"] {{
        background-color: {card_bg} !important;
        color: {text_col} !important;
    }}

    /* ── Checkboxes ── */
    .stCheckbox label {{ color: {text_col} !important; }}

    /* ── Metric ── */
    [data-testid="stMetric"] {{ background: {card_bg} !important; }}

    /* ── Custom cards ── */
    .stat-card {{
        background: {card_bg};
        border-radius: 16px;
        padding: 1.4rem;
        box-shadow: 0 2px 12px rgba(0,0,0,.15);
        border: 1px solid {card_border};
        text-align: center;
    }}
    .stat-number {{
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        color: {text_col} !important;
        line-height: 1;
    }}
    .stat-label {{
        color: {subtext} !important;
        font-size: .75rem;
        text-transform: uppercase;
        letter-spacing: .08em;
        margin-top: .3rem;
    }}
    .lesson-card {{
        background: {card_bg};
        border-radius: 10px;
        padding: .9rem 1.1rem;
        margin-bottom: .5rem;
        border: 1px solid {card_border};
        border-left: 4px solid #555;
        color: {text_col};
    }}
    .lesson-card.completed {{ border-left-color: #27ae60; background: {done_bg}; }}
    .lesson-card.in_progress {{ border-left-color: #f39c12; background: {inprog_bg}; }}
    .badge {{ display:inline-block; padding:.18rem .6rem; border-radius:999px; font-size:.7rem; font-weight:600; text-transform:uppercase; letter-spacing:.05em; }}
    .badge-completed {{ background:#1a4a2e; color:#5fdb8a; }}
    .badge-in_progress {{ background:#3d2e00; color:#f5c542; }}
    .badge-not_started {{ background:{prog_bg}; color:{subtext}; }}
    .progress-bar-container {{ background:{prog_bg}; border-radius:999px; height:8px; overflow:hidden; margin:.4rem 0; }}
    .progress-bar-fill {{ height:100%; border-radius:999px; }}
    .feynman-box {{ background:linear-gradient(135deg,#0d1b2a,#0f2d4a); border-radius:12px; padding:1.5rem; color:#e6edf3; border-left:4px solid #e94560; }}
    .recall-box {{ background:{recall_bg}; border:1px solid {recall_border}; border-radius:12px; padding:1.2rem 1.5rem; }}
    .roadmap-step {{ background:{card_bg}; border-radius:10px; padding:.9rem 1.2rem; margin-bottom:.5rem; border:1px solid {card_border}; border-left:4px solid #3498db; color:{text_col}; }}
    .roadmap-step.done {{ border-left-color:#27ae60; background:{done_bg}; }}
    .roadmap-step.current {{ border-left-color:#f39c12; background:{inprog_bg}; }}
    .today-card {{ background:{today_bg}; border:1px solid {today_border}; border-radius:12px; padding:1rem 1.2rem; font-size:.88rem; margin-bottom:1rem; color:{text_col}; }}
    .wpp-block {{ background:{card_bg}; border-radius:8px; padding:.7rem 1rem; margin-bottom:.4rem; border:1px solid {card_border}; color:{text_col}; }}

    /* ── Sidebar (always dark) ── */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg,#0d1b2a 0%,#1b2838 60%,#1a3a5c 100%) !important;
        border-right: 1px solid #1e3a5f;
    }}
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] div {{ color:#e8eaf0 !important; }}
    section[data-testid="stSidebar"] .stButton button {{
        background: rgba(255,255,255,.07) !important;
        color: #e8eaf0 !important;
        border: 1px solid rgba(255,255,255,.12) !important;
        border-radius: 8px;
        width: 100%;
        text-align: left;
        transition: all .2s;
    }}
    section[data-testid="stSidebar"] .stButton button:hover {{ background:rgba(255,255,255,.15) !important; }}

    /* ── Mobile ── */
    @media (max-width:768px) {{
        .block-container {{ padding:.8rem .4rem !important; }}
        .stat-card {{ padding:.7rem .3rem !important; }}
        .stat-number {{ font-size:1.2rem !important; }}
        .stat-label {{ font-size:.58rem !important; }}
        .lesson-card {{ padding:.6rem .7rem !important; font-size:.85rem; }}
        section[data-testid="stSidebar"] {{ display:none !important; }}
        .mobile-nav {{ display:flex !important; }}
        h1 {{ font-size:1.4rem !important; }}
    }}
    @media (min-width:769px) {{ .mobile-nav {{ display:none !important; }} }}
    .mobile-nav {{ display:none; gap:.4rem; margin-bottom:1.2rem; flex-wrap:wrap; padding:.5rem 0; }}
    .mobile-nav a {{ background:{card_bg}; color:{text_col}; border:1px solid {card_border}; border-radius:8px; padding:.5rem .9rem; text-decoration:none; font-size:.82rem; font-weight:600; }}
    </style>
    <div class="mobile-nav">
      <a href="?page=overview">🏠 Home</a>
      <a href="?page=korean">🇰🇷 Korean</a>
      <a href="?page=physics">⚛️ Physics</a>
      <a href="?page=raf">✈️ RAF</a>
    </div>
    """, unsafe_allow_html=True)


def _theme():
    dark = st.session_state.get("dark_mode", False)
    return {
        "card_bg":       "#161b22" if dark else "#ffffff",
        "card_border":   "#30363d" if dark else "#e8e8f0",
        "text":          "#e6edf3" if dark else "#1a1a2e",
        "subtext":       "#8b949e" if dark else "#666666",
        "done_bg":       "#0d2318" if dark else "#f0fff5",
        "done_border":   "#1a4a2e" if dark else "#c3e6cb",
        "done_text":     "#5fdb8a" if dark else "#276749",
        "info_bg":       "#0d1f3c" if dark else "#e8f4ff",
        "info_border":   "#1e3a5f" if dark else "#3a8fd9",
        "tag_bg":        "#21262d" if dark else "#f0f4ff",
        "tag_border":    "#30363d" if dark else "#d0d8f8",
        "tag_text":      "#58a6ff" if dark else "#3a5bd9",
        "feynman_bg":    "#0d1f3c" if dark else "#fff8f0",
        "recall_bg":     "#1a1500" if dark else "#f8f9ff",
        "recall_border": "#30363d" if dark else "#d0d8f8",
        "complete_bg":   "#0d1f3c" if dark else "#f8f9ff",
        "complete_bdr":  "#1e3a5f" if dark else "#d0d8f8",
        "review_ok_bg":  "#0d2318" if dark else "#f0fff4",
        "review_ok_bdr": "#1a4a2e" if dark else "#c3e6cb",
        "review_ok_txt": "#5fdb8a" if dark else "#276749",
    }

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
    # Fetch from Supabase once per session and cache locally
    if sb and "_progress_cache" not in st.session_state:
        try:
            res = sb.table("progress").select("*").execute()
            st.session_state["_progress_cache"] = {row["lesson_id"]: row for row in res.data}
        except Exception:
            st.session_state["_progress_cache"] = {}
    cache = st.session_state.get("_progress_cache", {})
    if prefix:
        return {k: v for k, v in cache.items() if k.startswith(prefix)}
    return cache

def _upsert(lesson_id, fields):
    from datetime import datetime
    sb = _sb()
    fields["lesson_id"] = lesson_id
    fields["updated_at"] = datetime.now().isoformat()
    if sb:
        try:
            sb.table("progress").upsert(fields).execute()
            # Invalidate cache so next load_progress re-fetches fresh from Supabase
            st.session_state.pop("_progress_cache", None)
        except Exception:
            # Write failed — update cache locally so session still reflects the change
            cache = st.session_state.get("_progress_cache", {})
            cache.setdefault(lesson_id, {}).update(fields)
            st.session_state["_progress_cache"] = cache
    else:
        # No Supabase — update cache locally
        cache = st.session_state.get("_progress_cache", {})
        cache.setdefault(lesson_id, {}).update(fields)
        st.session_state["_progress_cache"] = cache

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
            "📅  Calendar": "calendar",
            "🇰🇷  Korean": "korean",
            "⚛️  Physics": "physics",
            "✈️  RAF Application": "raf",
            "🎯  CBAT Tracker": "cbat",
            "🤖  AI Tools": "ai_tools",
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
            st.session_state.pop("login_time", None)
            _clear_session_from_db()
            st.rerun()

# ─── Reviews Panel ───────────────────────────────────────────────────────────

def _render_reviews_panel(all_prog, K_CUR, P_CUR, R_CUR):
    _t = _theme()
    from datetime import timedelta

    # Build a lookup: lesson_id -> (title, subject_name, subject_icon, page_key)
    lesson_meta = {}
    for cur, subj, icon, page_key in [
        (K_CUR, "Korean",  "🇰🇷", "korean"),
        (P_CUR, "Physics", "⚛️",  "physics"),
        (R_CUR, "RAF",     "✈️",  "raf"),
    ]:
        for unit_data in cur.values():
            for l in unit_data["lessons"]:
                lesson_meta[l["id"]] = (l["title"], subj, icon, page_key)

    today = date.today()
    today_str = today.isoformat()

    # Collect due today and upcoming (next 7 days)
    due_today = []
    upcoming = {}  # date_str -> list of lesson_ids
    for lid, data in all_prog.items():
        if data.get("status") != "completed":
            continue
        nr = data.get("next_review", "")
        if not nr:
            continue
        if nr <= today_str:
            due_today.append(lid)
        else:
            for i in range(1, 8):
                check = (today + timedelta(days=i)).isoformat()
                if nr == check:
                    upcoming.setdefault(check, []).append(lid)
                    break

    total_due = len(due_today)
    has_upcoming = any(upcoming.values())

    if total_due == 0 and not has_upcoming:
        return  # Nothing to show — keep overview clean

    subj_colors = {"Korean": "#e74c3c", "Physics": "#3498db", "RAF": "#1a3a6e"}

    st.markdown("### 🔄 Reviews")

    # ── Today's due ──
    if total_due > 0:
        st.markdown(
            f'<div style="display:flex;align-items:center;gap:.6rem;margin-bottom:.6rem">'
            f'<span style="background:#e74c3c;color:white;border-radius:999px;padding:.2rem .75rem;'
            f'font-size:.78rem;font-weight:700">{total_due} due today</span></div>',
            unsafe_allow_html=True,
        )
        cols = st.columns(min(total_due, 3)) if total_due <= 3 else st.columns(3)
        for i, lid in enumerate(due_today):
            meta = lesson_meta.get(lid, (lid, "Unknown", "📚", "overview"))
            title, subj, icon, page_key = meta
            rc = all_prog[lid].get("review_count", 0)
            color = subj_colors.get(subj, "#888")
            col = cols[i % 3]
            with col:
                st.markdown(
                    f'<div style="background:white;border-radius:10px;padding:.85rem 1rem;'
                    f'border:1px solid #eee;border-left:4px solid {color};margin-bottom:.5rem">'
                    f'<div style="font-size:.7rem;color:{color};font-weight:700;text-transform:uppercase;'
                    f'letter-spacing:.06em;margin-bottom:.2rem">{icon} {subj}</div>'
                    f'<div style="font-size:.88rem;font-weight:600;color:#1a1a2e;margin-bottom:.4rem">'
                    f'{lid} — {title}</div>'
                    f'<div style="font-size:.72rem;color:#aaa">Review #{rc + 1}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                if st.button(f"Start review →", key=f"ovw_rev_{lid}", use_container_width=True):
                    st.session_state.current_page = page_key
                    st.session_state[f"{page_key[0].upper()}_active_lesson"] = lid
                    st.session_state[f"{page_key[0].upper()}_view"] = "review"
                    st.rerun()
    else:
        st.markdown(
            f'<div style="background:{_t["review_ok_bg"]};border:1px solid {_t["review_ok_bdr"]};border-radius:10px;'
            f'padding:.7rem 1.1rem;font-size:.88rem;color:{_t["review_ok_txt"]};margin-bottom:.6rem">'
            '✅ No reviews due today — great work!</div>',
            unsafe_allow_html=True,
        )

    # ── Upcoming (next 7 days) ──
    if has_upcoming:
        with st.expander(f"📅 Upcoming reviews — next 7 days"):
            for i in range(1, 8):
                day_str = (today + timedelta(days=i)).isoformat()
                day_lessons = upcoming.get(day_str, [])
                if not day_lessons:
                    continue
                day_label = (today + timedelta(days=i)).strftime("%A %d %b")
                days_away = i
                pill_col = "#3498db" if days_away <= 3 else "#888"
                st.markdown(
                    f'<div style="display:flex;align-items:center;gap:.5rem;margin:.6rem 0 .3rem">'
                    f'<span style="background:{pill_col};color:white;border-radius:999px;'
                    f'padding:.15rem .65rem;font-size:.72rem;font-weight:700">{day_label}</span>'
                    f'<span style="font-size:.75rem;color:#aaa">in {days_away} day{"s" if days_away>1 else ""}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                for lid in day_lessons:
                    meta = lesson_meta.get(lid, (lid, "Unknown", "📚", "overview"))
                    title, subj, icon, page_key = meta
                    color = subj_colors.get(subj, "#888")
                    st.markdown(
                        f'<div style="background:white;border-radius:8px;padding:.55rem .9rem;'
                        f'border:1px solid #eee;border-left:3px solid {color};'
                        f'font-size:.84rem;margin-bottom:.3rem;color:#1a1a2e">'
                        f'{icon} <strong>{lid}</strong> — {title} '
                        f'<span style="color:#aaa;font-size:.75rem">({subj})</span></div>',
                        unsafe_allow_html=True,
                    )

    st.markdown("---")


# ─── Overview Page ────────────────────────────────────────────────────────────

def page_overview():
    _t = _theme()
    from data.korean_curriculum import CURRICULUM as K_CUR, get_topik_progress_summary, TOPIK_I_TARGET
    from data.physics_curriculum import PHYSICS_CURRICULUM as P_CUR
    from data.raf_curriculum import RAF_CURRICULUM as R_CUR, get_tier1_readiness, CONFIDENCE_LABELS

    dark = st.session_state.get("dark_mode", False)
    card_bg   = "#161b22" if dark else "#ffffff"
    card_bdr  = "#30363d" if dark else "#e8e8f0"
    text_col  = "#e6edf3" if dark else "#1a1a2e"
    sub_col   = "#8b949e" if dark else "#666"
    prog_bg   = "#21262d" if dark else "#eeeeee"

    st.markdown("# 🎯 Overview")
    st.markdown(f"*{date.today().strftime('%A, %d %B %Y')}*")
    st.markdown("---")

    all_prog = load_progress()
    sessions = load_sessions()
    streak = get_streak()
    hours = round(total_time() / 60, 1)

    # ── Next lesson per subject ───────────────────────────────────────────────
    today_name = date.today().strftime("%A")

    def next_lesson_id(prefix, curriculum):
        in_prog = [k for k, v in all_prog.items() if k.startswith(prefix) and v.get("status") == "in_progress"]
        if in_prog: return in_prog[0], "continue"
        due = get_due(prefix)
        if due: return due[0], "review"
        all_l = [l["id"] for u in curriculum.values() for l in u["lessons"]]
        not_started = [l for l in all_l if all_prog.get(l, {}).get("status", "not_started") == "not_started"]
        if not_started: return not_started[0], "start"
        return None, "done"

    k_id, k_type = next_lesson_id("U", K_CUR)
    p_id, p_type = next_lesson_id("P", P_CUR)
    r_id, r_type = next_lesson_id("R", R_CUR)

    type_labels = {"continue": "▶️ Continue", "review": "🔄 Review", "start": "🆕 Start", "done": "✅ All done"}
    type_colors = {"continue": "#f39c12", "review": "#e74c3c", "start": "#27ae60", "done": "#888"}

    schedule_notes = {
        "Monday":    ("🏃 Run + calisthenics", "Delivery morning — 1 study block after your workout."),
        "Tuesday":   ("🏑 Hockey tonight", "Study before hockey — aim for all 3 blocks this morning."),
        "Wednesday": ("🏃 Run + calisthenics", "Delivery morning — 1 study block."),
        "Thursday":  ("🏑 Hockey tonight", "Best study day — 3–4 blocks before hockey."),
        "Friday":    ("🏃 Run + calisthenics", "Delivery morning — 1 study block."),
        "Saturday":  ("🏑 Hockey this afternoon", "Study in the morning before hockey."),
        "Sunday":    ("Rest day", "Lighter day — even 1–2 blocks keeps the streak going."),
    }
    activity, advice = schedule_notes.get(today_name, ("", ""))

    # ── Today's focus banner ──────────────────────────────────────────────────
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#0d1b2a,#1a3a5c);border-radius:16px;padding:1.4rem 1.8rem;
                margin-bottom:1.2rem;border:1px solid #1e3a5f;color:white">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.4rem;margin-bottom:.4rem">
            <div style="font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;color:#6a8ab0">
                🗓️ Today — {today_name}
            </div>
            <div style="font-size:.78rem;color:#6a8ab0">{activity}</div>
        </div>
        <div style="font-size:.82rem;color:#a8c0d8;margin-bottom:1rem;font-style:italic">{advice}</div>
        <div style="display:flex;gap:1.5rem;flex-wrap:wrap">
            <div style="flex:1;min-width:130px">
                <div style="color:#aaa;font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.2rem">🇰🇷 Korean</div>
                <span style="color:{type_colors[k_type]};font-size:.82rem;font-weight:600">{type_labels[k_type]}</span>
                <span style="color:#ddd;font-size:.8rem"> {k_id or ''}</span>
            </div>
            <div style="flex:1;min-width:130px">
                <div style="color:#aaa;font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.2rem">⚛️ Physics</div>
                <span style="color:{type_colors[p_type]};font-size:.82rem;font-weight:600">{type_labels[p_type]}</span>
                <span style="color:#ddd;font-size:.8rem"> {p_id or ''}</span>
            </div>
            <div style="flex:1;min-width:130px">
                <div style="color:#aaa;font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.2rem">✈️ RAF</div>
                <span style="color:{type_colors[r_type]};font-size:.82rem;font-weight:600">{type_labels[r_type]}</span>
                <span style="color:#ddd;font-size:.8rem"> {r_id or ''}</span>
            </div>
            <div style="flex:1;min-width:130px;border-left:1px solid #1e3a5f;padding-left:1.2rem">
                <div style="color:#aaa;font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.2rem">⏱ Target</div>
                <span style="color:white;font-size:.82rem;font-weight:600">3 × 25 min blocks</span><br>
                <span style="color:#6a8ab0;font-size:.74rem">~75 min total</span>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    # ── Stats row ─────────────────────────────────────────────────────────────
    total_lessons = sum(len(u["lessons"]) for cur in [K_CUR, P_CUR, R_CUR] for u in cur.values())
    done = sum(1 for d in all_prog.values() if d.get("status") == "completed")

    c1, c2, c3, c4, c5 = st.columns(5)
    for col, num, label in [
        (c1, f"🔥 {streak}", "Day Streak"),
        (c2, str(done), "Lessons Done"),
        (c3, str(total_lessons), "Total Lessons"),
        (c4, f"{hours}h", "Study Time"),
        (c5, str(len(sessions)), "Sessions Logged"),
    ]:
        with col:
            st.markdown(
                f'<div class="stat-card"><div class="stat-number">{num}</div>'
                f'<div class="stat-label">{label}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Reviews panel ─────────────────────────────────────────────────────────
    _render_reviews_panel(all_prog, K_CUR, P_CUR, R_CUR)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── Subject progress + Today's plan ──────────────────────────────────────
    col_left, col_right = st.columns([3, 2])

    with col_left:
        st.subheader("📊 Progress by Subject")

        # ── Korean ──
        k_total = sum(len(u["lessons"]) for u in K_CUR.values())
        k_done  = sum(1 for k, d in all_prog.items() if k.startswith("U") and d.get("status") == "completed")
        k_pct   = round(k_done / k_total * 100) if k_total else 0
        k_due   = len(get_due("U"))
        topik   = get_topik_progress_summary(all_prog)
        vocab_pct = min(round(topik["words_known"] / TOPIK_I_TARGET * 100), 100)

        st.markdown(
            f'<div style="background:{card_bg};border-radius:14px;padding:1.1rem 1.4rem;margin-bottom:.7rem;'
            f'border:1px solid {card_bdr};border-left:5px solid #e74c3c">'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.5rem">'
            f'<span style="font-weight:700;font-size:.95rem;color:{text_col}">🇰🇷 Korean Language</span>'
            f'<span style="font-size:.78rem;color:{sub_col}">{k_done}/{k_total} lessons</span></div>'
            f'<div style="background:{prog_bg};border-radius:4px;height:6px;overflow:hidden;margin-bottom:.4rem">'
            f'<div style="width:{k_pct}%;height:100%;background:#e74c3c;border-radius:4px"></div></div>'
            f'<div style="display:flex;gap:1rem;font-size:.75rem;color:{sub_col}">'
            f'<span>Grammar: {k_pct}%</span>'
            f'<span>Vocab: {topik["words_known"]}/{TOPIK_I_TARGET} words ({vocab_pct}% to TOPIK I)</span>'
            + (f'<span style="color:#e74c3c;font-weight:600">🔄 {k_due} review(s) due</span>' if k_due else '')
            + f'</div></div>',
            unsafe_allow_html=True,
        )
        if st.button("Go to Korean →", key="goto_korean"):
            st.session_state.current_page = "korean"; st.rerun()

        # ── Physics ──
        p_total = sum(len(u["lessons"]) for u in P_CUR.values())
        p_done  = sum(1 for k, d in all_prog.items() if k.startswith("P") and d.get("status") == "completed")
        p_pct   = round(p_done / p_total * 100) if p_total else 0
        p_due   = len(get_due("P"))
        p_units = len(P_CUR)
        p_units_done = sum(
            1 for uname, ud in P_CUR.items()
            if all(all_prog.get(l["id"], {}).get("status") == "completed" for l in ud["lessons"])
        )

        st.markdown(
            f'<div style="background:{card_bg};border-radius:14px;padding:1.1rem 1.4rem;margin-bottom:.7rem;'
            f'border:1px solid {card_bdr};border-left:5px solid #3498db">'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.5rem">'
            f'<span style="font-weight:700;font-size:.95rem;color:{text_col}">⚛️ Physics — AQA GCSE</span>'
            f'<span style="font-size:.78rem;color:{sub_col}">{p_done}/{p_total} lessons</span></div>'
            f'<div style="background:{prog_bg};border-radius:4px;height:6px;overflow:hidden;margin-bottom:.4rem">'
            f'<div style="width:{p_pct}%;height:100%;background:#3498db;border-radius:4px"></div></div>'
            f'<div style="display:flex;gap:1rem;font-size:.75rem;color:{sub_col}">'
            f'<span>{p_pct}% complete · {p_units_done}/{p_units} topics finished</span>'
            + (f'<span style="color:#e74c3c;font-weight:600">🔄 {p_due} review(s) due</span>' if p_due else '')
            + f'</div></div>',
            unsafe_allow_html=True,
        )
        if st.button("Go to Physics →", key="goto_physics"):
            st.session_state.current_page = "physics"; st.rerun()

        # ── RAF ──
        r_total = sum(len(u["lessons"]) for u in R_CUR.values())
        r_done  = sum(1 for k, d in all_prog.items() if k.startswith("R") and d.get("status") == "completed")
        r_pct   = round(r_done / r_total * 100) if r_total else 0
        r_due   = len(get_due("R"))
        t1_stats = get_tier1_readiness(all_prog)
        ready_pct = t1_stats["ready_pct"]
        ready_color = "#27ae60" if ready_pct >= 75 else "#f39c12" if ready_pct >= 40 else "#e74c3c"

        try:
            from cbat_page import load_cbat_sessions
            cbat_n = len(load_cbat_sessions())
            cbat_subtests = len(set(s["subtest_id"] for s in load_cbat_sessions()))
        except Exception:
            cbat_n, cbat_subtests = 0, 0

        st.markdown(
            f'<div style="background:{card_bg};border-radius:14px;padding:1.1rem 1.4rem;margin-bottom:.7rem;'
            f'border:1px solid {card_bdr};border-left:5px solid #1a3a6e">'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.5rem">'
            f'<span style="font-weight:700;font-size:.95rem;color:{text_col}">✈️ RAF Application</span>'
            f'<span style="font-size:.78rem;color:{sub_col}">{r_done}/{r_total} lessons</span></div>'
            f'<div style="background:{prog_bg};border-radius:4px;height:6px;overflow:hidden;margin-bottom:.4rem">'
            f'<div style="width:{r_pct}%;height:100%;background:#1a3a6e;border-radius:4px"></div></div>'
            f'<div style="display:flex;gap:1rem;flex-wrap:wrap;font-size:.75rem;color:{sub_col}">'
            f'<span style="color:{ready_color};font-weight:600">🔴 Tier 1 OASC: {ready_pct}% interview-ready '
            f'({t1_stats["at_3"]}/{t1_stats["total"]})</span>'
            f'<span>🎯 CBAT: {cbat_n} session(s) · {cbat_subtests}/23 subtests</span>'
            + (f'<span style="color:#e74c3c;font-weight:600">🔄 {r_due} review(s) due</span>' if r_due else '')
            + f'</div></div>',
            unsafe_allow_html=True,
        )
        c_raf1, c_raf2 = st.columns(2)
        with c_raf1:
            if st.button("Go to RAF →", key="goto_raf"):
                st.session_state.current_page = "raf"; st.rerun()
        with c_raf2:
            if st.button("🎯 CBAT Tracker →", key="goto_cbat"):
                st.session_state.current_page = "cbat"; st.rerun()

    with col_right:
        st.subheader("🗓️ Today's Plan")
        day = date.today().weekday()
        wpp = {
            0: {"label": "Monday — Delivery + Fitness", "blocks": 1, "note": "1 block · Study after morning run", "color": "#e74c3c"},
            1: {"label": "Tuesday — Study Day",          "blocks": 3, "note": "2–3 blocks · Full morning available", "color": "#27ae60"},
            2: {"label": "Wednesday — Delivery + Fitness","blocks": 1, "note": "1 block · Morning only", "color": "#e74c3c"},
            3: {"label": "Thursday — Full Study Day",    "blocks": 4, "note": "3–4 blocks · Best day of the week", "color": "#27ae60"},
            4: {"label": "Friday — Delivery + Fitness",  "blocks": 1, "note": "1 block · Morning only", "color": "#e74c3c"},
            5: {"label": "Saturday — Optional",          "blocks": 1, "note": "1 optional block · Hockey this afternoon", "color": "#f39c12"},
            6: {"label": "Sunday — Flexible",            "blocks": 2, "note": "Anki + 1–2 blocks if natural", "color": "#8e44ad"},
        }
        tw = wpp[day]
        blocks = tw["blocks"]
        st.markdown(f"""
        <div class="today-card">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:.5rem">
                <strong>{tw['label']}</strong>
                <span style="background:{tw['color']};color:white;border-radius:999px;padding:.15rem .65rem;
                             font-size:.72rem;font-weight:700">{blocks} block{'s' if blocks > 1 else ''}</span>
            </div>
            <span style="font-size:.8rem;opacity:.8">{tw['note']}</span><br>
            <span style="font-size:.75rem;opacity:.6">🔑 Anki: 10 min Korean · Before coffee</span>
        </div>""", unsafe_allow_html=True)

        subject_order = [
            ("Korean", "U", "korean", "🇰🇷"),
            ("Physics", "P", "physics", "⚛️"),
            ("RAF",     "R", "raf",     "✈️"),
        ]
        shown = 0
        for sname, prefix, page_key, icon in subject_order:
            if shown >= blocks and blocks < 3:
                break
            in_prog  = [k for k, v in all_prog.items() if k.startswith(prefix) and v.get("status") == "in_progress"]
            due_items = get_due(prefix)
            if in_prog:
                label = f"Continue: {in_prog[0]}"
                border_col = "#f39c12"
            elif due_items:
                label = f"Review due: {due_items[0]}"
                border_col = "#e74c3c"
            else:
                label = "Start next lesson"
                border_col = "#27ae60"
            st.markdown(
                f'<div class="wpp-block" style="border-left:3px solid {border_col}">'
                f'{icon} <strong>{sname}</strong> · <span style="font-size:.82rem">{label}</span></div>',
                unsafe_allow_html=True,
            )
            shown += 1

        # RAF quick status
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="background:{card_bg};border:1px solid {card_bdr};border-left:3px solid #1a3a6e;'
            f'border-radius:8px;padding:.7rem 1rem;font-size:.8rem">'
            f'<div style="font-weight:700;color:{text_col};margin-bottom:.3rem">✈️ RAF Application Status</div>'
            f'<div style="color:{sub_col}">✅ Application · ✅ DAA · ✅ ID check</div>'
            f'<div style="color:#f39c12;font-weight:600;margin-top:.2rem">🎯 Next: Medical examination</div>'
            f'<div style="color:{sub_col};margin-top:.2rem">Then: CBAT → OASC</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── End Goals & Roadmaps ─────────────────────────────────────────────────
    st.subheader("🚀 End Goals & Roadmaps")
    st.markdown("*The bigger picture — where all of this is heading*")
    st.markdown("<br>", unsafe_allow_html=True)

    goal_col1, goal_col2, goal_col3 = st.columns(3)

    with goal_col1:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#c0392b,#e74c3c);border-radius:16px;padding:1.5rem;
                    color:white;text-align:center;margin-bottom:1rem">
            <div style="font-size:2.5rem">🇰🇷</div>
            <h3 style="margin:.5rem 0 .2rem;font-family:Georgia,serif">Korean Fluency</h3>
            <p style="font-size:.82rem;opacity:.85;margin:0">Conversational with her family</p>
        </div>""", unsafe_allow_html=True)
        with st.expander("📋 Roadmap"):
            for label, desc, s in [
                ("🎯 Now",      "HTSK Unit 0 — Hangul & pronunciation",           "current"),
                ("📍 Month 1",  "Unit 0 complete — reading Korean script",         ""),
                ("📍 Month 3",  "Unit 1 complete — basic sentences & grammar",     ""),
                ("📍 Month 6",  "Unit 2 — hold simple conversations",              ""),
                ("📍 Month 12", "Units 3-4 — discuss everyday topics",             ""),
                ("📍 Month 18", "Units 5-6 — TV without subtitles",                ""),
                ("🏁 Goal",     "Conversational with her family — Unit 7+",        ""),
            ]:
                cls = "done" if s == "done" else ("current" if s == "current" else "roadmap-step")
                st.markdown(f'<div class="roadmap-step {cls}" style="margin-bottom:.4rem"><strong>{label}:</strong> {desc}</div>', unsafe_allow_html=True)

    with goal_col2:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#1a3a6e,#2e4d9e);border-radius:16px;padding:1.5rem;
                    color:white;text-align:center;margin-bottom:1rem">
            <div style="font-size:2.5rem">✈️</div>
            <h3 style="margin:.5rem 0 .2rem;font-family:Georgia,serif">RAF Pilot</h3>
            <p style="font-size:.82rem;opacity:.85;margin:0">Commission & earn your wings</p>
        </div>""", unsafe_allow_html=True)
        with st.expander("📋 Roadmap"):
            for label, desc, s in [
                ("✅ Done",      "Application submitted",                           "done"),
                ("✅ Done",      "DAA — Digital Aptitude Assessment",               "done"),
                ("✅ Done",      "ID check at AFCO",                                "done"),
                ("🎯 Next",      "Medical examination",                             "current"),
                ("📍 Soon",      "CBAT — 23 computer aptitude tests at Cranwell",   ""),
                ("📍 Soon",      "OASC — Officer & Aircrew Selection Centre",       ""),
                ("📍 Pass",      "IOT — Initial Officer Training (24 weeks)",       ""),
                ("📍 Training",  "EFTS — Elementary Flying (Grob Prefect)",         ""),
                ("📍 Training",  "BFJT → AFJT — Basic & Advanced Flying Training", ""),
                ("🏁 Goal",      "Wings ceremony — front-line fast jet posting",    ""),
            ]:
                cls = "done" if s == "done" else ("current" if s == "current" else "roadmap-step")
                st.markdown(f'<div class="roadmap-step {cls}" style="margin-bottom:.4rem"><strong>{label}:</strong> {desc}</div>', unsafe_allow_html=True)

    with goal_col3:
        st.markdown("""
        <div style="background:linear-gradient(135deg,#145a32,#27ae60);border-radius:16px;padding:1.5rem;
                    color:white;text-align:center;margin-bottom:1rem">
            <div style="font-size:2.5rem">⚛️</div>
            <h3 style="margin:.5rem 0 .2rem;font-family:Georgia,serif">Physics Mastery</h3>
            <p style="font-size:.82rem;opacity:.85;margin:0">GCSE → Aerospace depth</p>
        </div>""", unsafe_allow_html=True)
        with st.expander("📋 Roadmap"):
            for label, desc, s in [
                ("🎯 Now",      "Topic 1 — Energy (AQA foundations)",              "current"),
                ("📍 Month 1",  "Topics 1-2 — Energy & Electricity done",          ""),
                ("📍 Month 2",  "Topics 3-4 — Particle Model & Radioactivity",     ""),
                ("📍 Month 3",  "Topic 5 — Forces (critical for aviation)",        ""),
                ("📍 Month 4",  "Topics 6-7 — Waves & Electromagnetism",           ""),
                ("📍 Month 5",  "Topic 8 — Space Physics",                         ""),
                ("📍 Extension","Aerospace: aerodynamics, propulsion, navigation", ""),
                ("🏁 Goal",     "Solid physics foundation for RAF training",        ""),
            ]:
                cls = "done" if s == "done" else ("current" if s == "current" else "roadmap-step")
                st.markdown(f'<div class="roadmap-step {cls}" style="margin-bottom:.4rem"><strong>{label}:</strong> {desc}</div>', unsafe_allow_html=True)

# ─── Generic Lesson Viewer (shared by all subjects) ──────────────────────────

def render_lesson_viewer(lesson, unit_color, unit_level):
    _t = _theme()
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

    tab1, tab2, tab3 = st.tabs(["📋 Goals & Vocab", "📝 Notes", "✅ Mark Complete"])

    with tab1:
        c1, c2 = st.columns([3, 2])
        with c1:
            st.markdown("### 🎯 Learning Goals")
            for i, goal in enumerate(lesson["learning_goals"], 1):
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
                for v in lesson.get("key_vocab", [])
            ])
            st.markdown(f"<div style='line-height:2.4'>{vocab_html}</div>", unsafe_allow_html=True)

        with c2:
            st.markdown("### 🔗 Resources")
            for r in lesson.get("resources", []):
                st.markdown(
                    f'<a href="{r["url"]}" target="_blank" style="display:inline-block;background:#f0f4ff;'
                    f'color:#3a5bd9;padding:.3rem .8rem;border-radius:999px;text-decoration:none;'
                    f'font-size:.8rem;border:1px solid #d0d8f8;margin:.15rem">↗ {r["name"]}</a>',
                    unsafe_allow_html=True,
                )

        if status == "not_started":
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("▶️ Start This Lesson", use_container_width=True, key=f"start_{lesson_id}"):
                mark_in_progress(lesson_id)
                st.success("Lesson started!")
                st.rerun()

    with tab2:
        st.markdown("### 📝 My Notes")
        notes = st.text_area(
            "Notes:",
            value=lesson_prog.get("notes", ""),
            key=f"notes_{lesson_id}",
            height=280,
            placeholder="Write your own explanations, examples, connections...\nAvoid copying — process and rephrase.",
        )
        if st.button("💾 Save Notes", use_container_width=True, key=f"savenotes_{lesson_id}"):
            save_notes(lesson_id, notes)
            st.success("Saved!")

    with tab3:
        st.markdown("### ✅ Mark Complete")
        if status == "completed":
            st.success(
                f"✅ Completed: {lesson_prog.get('completed_date','?')} | "
                f"Next review: **{lesson_prog.get('next_review','?')}** | "
                f"Reviews done: {lesson_prog.get('review_count', 0)}"
            )
        st.markdown(
            f'<div style="background:{_t["complete_bg"]};border:1px solid {_t["complete_bdr"]};'
            f'border-radius:12px;padding:1.2rem;margin-bottom:1rem;color:{_t["text"]}">'
            f'<strong>Before completing, confirm:</strong></div>',
            unsafe_allow_html=True,
        )
        for item in [
            "Read/watched the full resource",
            "Completed at least one AI active recall attempt",
            "Can explain the key concepts without notes",
        ]:
            st.checkbox(item, key=f"cc_{lesson_id}_{item[:12]}")
        c1, c2, c3 = st.columns(3)
        with c1:
            score = st.slider("Self-score:", 0, 100, 75, key=f"sc_{lesson_id}")
        with c2:
            t = st.number_input("Time (min):", 1, 120, value=lesson["estimated_minutes"], key=f"tm_{lesson_id}")
        with c3:
            st.markdown("<br>", unsafe_allow_html=True)
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

    # ── AI Tools ──────────────────────────────────────────────────────────────
    from ai_lesson_tab import render_ai_lesson_tab
    render_ai_lesson_tab(lesson, lesson_prog)

# ─── Subject Reviews Summary ─────────────────────────────────────────────────

def _render_subject_reviews(progress, curriculum, prefix, color, icon):
    _t = _theme()
    from datetime import timedelta
    today = date.today()
    today_str = today.isoformat()
    lesson_meta = {l["id"]: l for u in curriculum.values() for l in u["lessons"]}
    due_today = []
    upcoming = {}
    for lid, data in progress.items():
        if not lid.startswith(prefix): continue
        if data.get("status") != "completed": continue
        nr = data.get("next_review", "")
        if not nr: continue
        if nr <= today_str:
            due_today.append(lid)
        else:
            for i in range(1, 8):
                check = (today + timedelta(days=i)).isoformat()
                if nr == check:
                    upcoming.setdefault(check, []).append(lid)
                    break
    if not due_today and not upcoming:
        return
    dark = st.session_state.get("dark_mode", False)
    card_bg = "#161b22" if dark else "#ffffff"
    card_border = "#30363d" if dark else "#e8e8f0"
    text_col = "#e6edf3" if dark else "#1a1a2e"
    st.markdown("### 🔄 Your Reviews")
    if due_today:
        st.markdown(
            f'<span style="background:#e74c3c;color:white;border-radius:999px;'
            f'padding:.2rem .75rem;font-size:.78rem;font-weight:700">'
            f'{len(due_today)} due today</span>',
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        cols = st.columns(min(len(due_today), 3))
        for i, lid in enumerate(due_today):
            lesson = lesson_meta.get(lid, {})
            rc = progress[lid].get("review_count", 0)
            with cols[i % 3]:
                st.markdown(
                    f'<div style="background:{card_bg};border-radius:10px;padding:.85rem 1rem;'
                    f'border:1px solid {card_border};border-left:4px solid {color};margin-bottom:.5rem">'
                    f'<div style="font-size:.7rem;color:{color};font-weight:700;text-transform:uppercase;'
                    f'letter-spacing:.06em;margin-bottom:.2rem">{icon} Review #{rc}</div>'
                    f'<div style="font-size:.88rem;font-weight:600;color:{text_col};margin-bottom:.3rem">'
                    f'{lid} — {lesson.get("title","")}</div>'
                    f'<div style="font-size:.72rem;color:#aaa">{lesson.get("subtitle","")}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                if st.button("Start review →", key=f"subj_rev_{lid}", use_container_width=True):
                    st.session_state[f"{prefix}_active_lesson"] = lid
                    st.session_state[f"{prefix}_view"] = "review"
                    st.rerun()
    else:
        st.markdown(
            f'<div style="background:{"#0d2318" if dark else "#f0fff5"};border:1px solid '
            f'{"#1a4a2e" if dark else "#c3e6cb"};border-radius:10px;padding:.6rem 1rem;'
            f'font-size:.86rem;color:{"#5fdb8a" if dark else "#276749"};margin-bottom:.5rem">'
            f'✅ No reviews due today</div>',
            unsafe_allow_html=True,
        )
    if upcoming:
        with st.expander("📅 Upcoming — next 7 days"):
            for i in range(1, 8):
                day_str = (today + timedelta(days=i)).isoformat()
                day_lessons = upcoming.get(day_str, [])
                if not day_lessons: continue
                day_label = (today + timedelta(days=i)).strftime("%A %d %b")
                pill_col = "#3498db" if i <= 3 else "#555"
                st.markdown(
                    f'<div style="display:flex;align-items:center;gap:.5rem;margin:.5rem 0 .2rem">'
                    f'<span style="background:{pill_col};color:white;border-radius:999px;'
                    f'padding:.15rem .65rem;font-size:.72rem;font-weight:700">{day_label}</span>'
                    f'<span style="font-size:.75rem;color:#aaa">in {i} day{"s" if i>1 else ""}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                for lid in day_lessons:
                    lesson = lesson_meta.get(lid, {})
                    st.markdown(
                        f'<div style="background:{card_bg};border-radius:8px;padding:.5rem .9rem;'
                        f'border:1px solid {card_border};border-left:3px solid {color};'
                        f'font-size:.84rem;margin-bottom:.3rem;color:{text_col}">'
                        f'<strong>{lid}</strong> — {lesson.get("title","")}</div>',
                        unsafe_allow_html=True,
                    )
    st.markdown("---")


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

    # ── Subject-level reviews summary ──────────────────────────────────────────
    _render_subject_reviews(progress, curriculum, prefix, color, icon)

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
                    # Pre-review briefing from weakness log
                    from store_weakness import get_lesson_weakness_summary, load_weakness_log
                    summary = get_lesson_weakness_summary(lid)
                    if summary["attempts"] > 0:
                        st.markdown(
                            f'<div style="background:#f0f7ff;border-left:3px solid #3498db;'
                            f'border-radius:0 8px 8px 0;padding:.7rem 1rem;margin-bottom:.8rem;font-size:.86rem">'
                            f'<strong>Your history:</strong> {summary["attempts"]} attempt(s) · '
                            f'Avg score {summary["avg_score"]}/5'
                            + (f' · Top gap: <em>{summary["top_gaps"][0]}</em>' if summary["top_gaps"] else '')
                            + f'</div>',
                            unsafe_allow_html=True,
                        )

                    # AI-generated questions
                    from ai_helper import generate_review_questions
                    weakness_log = load_weakness_log(lesson_id=lid)
                    if st.button(f"Generate smart review questions", key=f"genrev_{lid}"):
                        with st.spinner("Generating targeted questions..."):
                            result = generate_review_questions(lesson, weakness_log, n=3)
                        st.session_state[f"rev_qs_{lid}"] = result.get("questions", [])

                    qs = st.session_state.get(f"rev_qs_{lid}", [])
                    if qs:
                        for i, q in enumerate(qs):
                            tw = q.get("targets_weakness", False)
                            badge = (' <span style="font-size:.72rem;background:#ffe0e0;border-radius:3px;'
                                     'padding:1px 5px">targets weak area</span>') if tw else ""
                            st.markdown(
                                f'<div style="background:#f8f9ff;border-left:2px solid #534AB7;'
                                f'padding:.6rem .9rem;margin:.3rem 0;font-size:.88rem">'
                                f'Q{i+1}: {q["question"]}{badge}</div>',
                                unsafe_allow_html=True,
                            )
                            st.text_area("Your answer:", key=f"rev_ans_{lid}_{i}", height=70)
                    else:
                        st.info(
                            "Click 'Generate smart review questions' above to get AI questions "
                            "targeted at your known weak areas for this lesson."
                        )

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
    from data.korean_curriculum import CURRICULUM, get_topik_progress_summary, TOPIK_I_TARGET
    _t = _theme()
    dark = st.session_state.get("dark_mode", False)

    st.markdown("# 🇰🇷 Korean Language")
    st.markdown("*Resource: [How to Study Korean](https://www.howtostudykorean.com) · Benchmark: TOPIK I vocabulary*")

    # ── TOPIK progress panel ──────────────────────────────────────────────────
    progress = load_progress()
    topik = get_topik_progress_summary(progress)

    # Lesson progress (Unit 0 + Unit 1 = 29 lessons, the measurable core)
    u0u1_lessons = [l for u, ud in CURRICULUM.items() for l in ud["lessons"] if l["id"].startswith(("U0", "U1"))]
    u0u1_total = len(u0u1_lessons)
    u0u1_done = sum(1 for l in u0u1_lessons if progress.get(l["id"], {}).get("status") == "completed")
    lesson_pct = round(u0u1_done / u0u1_total * 100) if u0u1_total else 0

    vocab_pct = min(round(topik["words_known"] / TOPIK_I_TARGET * 100), 100)
    ready_label = "✅ TOPIK I ready" if topik["ready_for_topik"] else f"{TOPIK_I_TARGET - topik['words_known']} words to go"
    ready_color = "#27ae60" if topik["ready_for_topik"] else "#e74c3c"

    card_bg   = "#161b22" if dark else "#ffffff"
    card_bdr  = "#30363d" if dark else "#e8e8f0"
    text_col  = "#e6edf3" if dark else "#1a1a2e"
    sub_col   = "#8b949e" if dark else "#666"
    prog_bg   = "#21262d" if dark else "#eeeeee"

    st.markdown(f"""
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:1.2rem">

      <div style="background:{card_bg};border:1px solid {card_bdr};border-left:4px solid #e74c3c;
                  border-radius:12px;padding:1rem 1.2rem">
        <div style="font-size:.72rem;color:{sub_col};text-transform:uppercase;letter-spacing:.08em;margin-bottom:.4rem">
          Grammar track — HTSK
        </div>
        <div style="font-size:1.5rem;font-weight:600;color:{text_col};margin-bottom:.3rem">
          {u0u1_done} / {u0u1_total}
          <span style="font-size:.8rem;font-weight:400;color:{sub_col}">lessons</span>
        </div>
        <div style="background:{prog_bg};border-radius:4px;height:6px;overflow:hidden;margin-bottom:.3rem">
          <div style="width:{lesson_pct}%;height:100%;background:#e74c3c;border-radius:4px"></div>
        </div>
        <div style="font-size:.75rem;color:{sub_col}">Units 0–1 · {lesson_pct}% complete</div>
      </div>

      <div style="background:{card_bg};border:1px solid {card_bdr};border-left:4px solid #27ae60;
                  border-radius:12px;padding:1rem 1.2rem">
        <div style="font-size:.72rem;color:{sub_col};text-transform:uppercase;letter-spacing:.08em;margin-bottom:.4rem">
          Vocabulary track — TOPIK I
        </div>
        <div style="font-size:1.5rem;font-weight:600;color:{text_col};margin-bottom:.3rem">
          {topik['words_known']} / {TOPIK_I_TARGET}
          <span style="font-size:.8rem;font-weight:400;color:{sub_col}">words</span>
        </div>
        <div style="background:{prog_bg};border-radius:4px;height:6px;overflow:hidden;margin-bottom:.3rem">
          <div style="width:{vocab_pct}%;height:100%;background:#27ae60;border-radius:4px"></div>
        </div>
        <div style="font-size:.75rem;color:{ready_color};font-weight:600">{ready_label}</div>
      </div>

      <div style="background:{card_bg};border:1px solid {card_bdr};border-left:4px solid #3498db;
                  border-radius:12px;padding:1rem 1.2rem">
        <div style="font-size:.72rem;color:{sub_col};text-transform:uppercase;letter-spacing:.08em;margin-bottom:.4rem">
          Next milestone
        </div>
        <div style="font-size:.88rem;font-weight:600;color:{text_col};margin-bottom:.3rem">HTSK Unit 1 Test</div>
        <div style="font-size:.78rem;color:{sub_col};margin-bottom:.5rem">Complete all 25 lessons in Unit 1</div>
        <div style="font-size:.72rem;color:{sub_col}">Then: TOPIK I exam (book when vocab ≥ 1,200)</div>
      </div>

    </div>
    """, unsafe_allow_html=True)

    render_subject_page("Korean", CURRICULUM, "U", "#e74c3c", "🇰🇷")

def page_physics():
    from data.physics_curriculum import PHYSICS_CURRICULUM
    st.markdown("# ⚛️ Physics — AQA GCSE")
    st.markdown("*Resource: [BBC Bitesize](https://www.bbc.co.uk/bitesize/examspecs/z8xtmnb) — focus on understanding over note-copying*")
    render_subject_page("Physics", PHYSICS_CURRICULUM, "P", "#3498db", "⚛️")

def page_raf():
    from raf_page import page_raf as _raf_page
    _raf_page()

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
         inject_css()
         if not check_password(): return
         render_sidebar()
         page = st.session_state.get("current_page","overview")
         if page == "overview": page_overview()
         elif page == "calendar":
             from calendar_page import page_calendar
             page_calendar()
         elif page == "korean": page_korean()
         elif page == "physics": page_physics()
         elif page == "raf": page_raf()
         elif page == "cbat":
             from cbat_page import page_cbat
             page_cbat()
         elif page == "ai_tools":
             from ai_tools import page_ai_tools
             page_ai_tools()



if __name__ == "__main__":
    main()
