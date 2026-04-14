"""
calendar_page.py — Weekly Calendar with WPP integration
Add this file to your project root, then wire it into app.py (see instructions).
"""

import streamlit as st
from datetime import date, timedelta, datetime


# ─── Supabase helper (mirrors app.py pattern) ────────────────────────────────

def _sb():
    return st.session_state.get("supabase_client")


# ─── WPP Default blocks ───────────────────────────────────────────────────────
# Seeded from your WPP planner. These are templates applied per weekday.
# is_default=True blocks show with a lock icon and can still be edited/deleted.

WPP_DEFAULTS = {
    0: [  # Monday — Work + Fitness
        {"title": "Anki — Korean", "description": "10 min Korean — open app before coffee, without exception.", "block_type": "study", "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast", "description": "Hot food, sit down, no screens.", "block_type": "play", "start_time": "08:15", "duration_minutes": 30},
        {"title": "Run 5k + Calisthenics", "description": "~55 min fitness block.", "block_type": "fitness", "start_time": "08:45", "duration_minutes": 55},
        {"title": "Study Block 1", "description": "25 min — one lesson from tracker. Mousetrap: open tracker, begin.", "block_type": "study", "start_time": "09:45", "duration_minutes": 25},
        {"title": "Get Ready + Admin", "description": "Shower, pack, prep for the day.", "block_type": "personal", "start_time": "10:15", "duration_minutes": 40},
        {"title": "Amazon — Delivery Route", "description": "W block. ~8h delivery shift.", "block_type": "work", "start_time": "11:00", "duration_minutes": 480},
        {"title": "Home + Real Rest", "description": "No study after work. Game, movie, recover. Non-negotiable.", "block_type": "play", "start_time": "19:00", "duration_minutes": 225},
        {"title": "Anki Wind-down", "description": "10 min Korean before sleep.", "block_type": "study", "start_time": "22:45", "duration_minutes": 10},
    ],
    1: [  # Tuesday — Study + Hockey
        {"title": "Anki — Korean", "description": "10 min Korean.", "block_type": "study", "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast", "description": "30 min hot food.", "block_type": "play", "start_time": "08:15", "duration_minutes": 30},
        {"title": "Study Block 1", "description": "25 min — work through tracker.", "block_type": "study", "start_time": "08:45", "duration_minutes": 25},
        {"title": "Study Block 2", "description": "25 min — second lesson or Feynman technique.", "block_type": "study", "start_time": "09:20", "duration_minutes": 25},
        {"title": "Study Block 3 (Optional)", "description": "Only if genuinely sharp — stop at first sign of fatigue.", "block_type": "study", "start_time": "09:50", "duration_minutes": 25},
        {"title": "Free Time", "description": "P block — game, rest, earned downtime.", "block_type": "play", "start_time": "10:20", "duration_minutes": 430},
        {"title": "Get Ready for Hockey", "description": "Kit, travel, warm up.", "block_type": "personal", "start_time": "17:30", "duration_minutes": 90},
        {"title": "Hockey Training", "description": "~2h — physical W block.", "block_type": "fitness", "start_time": "19:00", "duration_minutes": 120},
        {"title": "Anki + Sleep", "description": "10 min Korean.", "block_type": "study", "start_time": "22:45", "duration_minutes": 10},
    ],
    2: [  # Wednesday — Work + Fitness
        {"title": "Anki — Korean", "description": "10 min Korean.", "block_type": "study", "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast", "description": "30 min hot food.", "block_type": "play", "start_time": "08:15", "duration_minutes": 30},
        {"title": "Run 5k + Calisthenics", "description": "~55 min fitness block.", "block_type": "fitness", "start_time": "08:45", "duration_minutes": 55},
        {"title": "Study Block 1", "description": "25 min — one lesson. Work-day target met.", "block_type": "study", "start_time": "09:45", "duration_minutes": 25},
        {"title": "Get Ready + Admin", "description": "Shower, pack, prep.", "block_type": "personal", "start_time": "10:15", "duration_minutes": 45},
        {"title": "Amazon — Delivery Route", "description": "Delivery route.", "block_type": "work", "start_time": "11:00", "duration_minutes": 480},
        {"title": "Home + Real Rest", "description": "No study. Game, watch, recover.", "block_type": "play", "start_time": "19:00", "duration_minutes": 225},
        {"title": "Anki Wind-down", "description": "10 min Korean.", "block_type": "study", "start_time": "22:45", "duration_minutes": 10},
    ],
    3: [  # Thursday — Full Study Day
        {"title": "Anki — Korean", "description": "10 min Korean.", "block_type": "study", "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast", "description": "30 min hot food.", "block_type": "play", "start_time": "08:15", "duration_minutes": 30},
        {"title": "Study Block 1", "description": "25 min.", "block_type": "study", "start_time": "08:45", "duration_minutes": 25},
        {"title": "Study Block 2", "description": "25 min.", "block_type": "study", "start_time": "09:20", "duration_minutes": 25},
        {"title": "Study Block 3", "description": "25 min — or full review block.", "block_type": "study", "start_time": "09:50", "duration_minutes": 25},
        {"title": "Study Block 4 (Optional)", "description": "25 min — only if sharp. 3 is already a great day.", "block_type": "study", "start_time": "10:20", "duration_minutes": 25},
        {"title": "Free Time", "description": "P block — game, rest, recharge properly.", "block_type": "play", "start_time": "11:00", "duration_minutes": 480},
        {"title": "Hockey Training", "description": "~2h evening W block.", "block_type": "fitness", "start_time": "19:00", "duration_minutes": 120},
        {"title": "Anki + Sleep", "description": "10 min Korean.", "block_type": "study", "start_time": "22:45", "duration_minutes": 10},
    ],
    4: [  # Friday — Work + Fitness
        {"title": "Anki — Korean", "description": "10 min Korean.", "block_type": "study", "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast", "description": "30 min hot food.", "block_type": "play", "start_time": "08:15", "duration_minutes": 30},
        {"title": "Run 5k + Calisthenics", "description": "~55 min.", "block_type": "fitness", "start_time": "08:45", "duration_minutes": 55},
        {"title": "Study Block 1", "description": "25 min — one lesson. Friday target met.", "block_type": "study", "start_time": "09:45", "duration_minutes": 25},
        {"title": "Get Ready + Admin", "description": "Shower, pack, prep.", "block_type": "personal", "start_time": "10:15", "duration_minutes": 45},
        {"title": "Amazon — Delivery Route", "description": "Delivery route.", "block_type": "work", "start_time": "11:00", "duration_minutes": 480},
        {"title": "Evening — Fully Free", "description": "Social, gaming, movie. Friday is earned.", "block_type": "play", "start_time": "19:00", "duration_minutes": 225},
        {"title": "Anki Wind-down", "description": "10 min Korean.", "block_type": "study", "start_time": "22:45", "duration_minutes": 10},
    ],
    5: [  # Saturday — Hockey + GF
        {"title": "Anki — Korean", "description": "10 min Korean — non-negotiable even on weekends.", "block_type": "study", "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast", "description": "30 min — relaxed weekend pace.", "block_type": "play", "start_time": "08:15", "duration_minutes": 30},
        {"title": "Study Block (Optional)", "description": "25 min lighter topics. Skip freely — this is a rest day.", "block_type": "study", "start_time": "08:45", "duration_minutes": 25},
        {"title": "Morning Free Time", "description": "P block — relax, game, browse.", "block_type": "play", "start_time": "09:15", "duration_minutes": 165},
        {"title": "GF Time", "description": "Morning into afternoon.", "block_type": "personal", "start_time": "12:00", "duration_minutes": 120},
        {"title": "Hockey Game", "description": "Travel + warm up + game.", "block_type": "fitness", "start_time": "14:00", "duration_minutes": 210},
        {"title": "Post-Match + Evening with GF", "description": "Team social then evening with GF.", "block_type": "play", "start_time": "17:30", "duration_minutes": 270},
    ],
    6: [  # Sunday — GF Day
        {"title": "Wake (Natural)", "description": "Weekend — no alarm.", "block_type": "play", "start_time": "08:00", "duration_minutes": 30},
        {"title": "Breakfast + Anki", "description": "Stack Korean onto breakfast — 10 min while eating.", "block_type": "study", "start_time": "08:30", "duration_minutes": 40},
        {"title": "Morning with GF", "description": "Breakfast together, plan the day.", "block_type": "personal", "start_time": "09:00", "duration_minutes": 60},
        {"title": "Out or At Home", "description": "London trip, market — or staying in.", "block_type": "personal", "start_time": "10:00", "duration_minutes": 240},
        {"title": "Afternoon — Flexible", "description": "If home + she rests: 1–2 study blocks. Never forced.", "block_type": "study", "start_time": "14:00", "duration_minutes": 150},
        {"title": "Evening with GF", "description": "Movie, dinner, quality time.", "block_type": "personal", "start_time": "16:30", "duration_minutes": 210},
        {"title": "Anki + Sleep Prep", "description": "Final Korean. Earlier bed = better week.", "block_type": "study", "start_time": "22:00", "duration_minutes": 10},
    ],
}

BLOCK_COLOURS = {
    "study":    {"bg": "#dbeafe", "border": "#3b82f6", "text": "#1e3a5f", "badge": "#3b82f6"},
    "work":     {"bg": "#fee2e2", "border": "#ef4444", "text": "#7f1d1d", "badge": "#ef4444"},
    "fitness":  {"bg": "#dcfce7", "border": "#22c55e", "text": "#14532d", "badge": "#22c55e"},
    "personal": {"bg": "#fef9c3", "border": "#eab308", "text": "#713f12", "badge": "#eab308"},
    "play":     {"bg": "#f3e8ff", "border": "#a855f7", "text": "#3b0764", "badge": "#a855f7"},
}

BLOCK_TYPES = ["study", "work", "fitness", "personal", "play"]
TYPE_ICONS  = {"study": "📚", "work": "💼", "fitness": "🏃", "personal": "👤", "play": "🎮"}
DAY_NAMES   = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


# ─── Supabase CRUD ────────────────────────────────────────────────────────────

def load_blocks_for_week(week_start: date) -> dict:
    """Return {date_str: [block, ...]} for the 7 days of the week."""
    week_end = week_start + timedelta(days=6)
    sb = _sb()
    rows = []
    if sb:
        try:
            res = (sb.table("calendar_blocks")
                     .select("*")
                     .gte("block_date", week_start.isoformat())
                     .lte("block_date", week_end.isoformat())
                     .order("start_time")
                     .execute())
            rows = res.data
        except Exception:
            pass
    # fall back to session state
    if not rows:
        cache = st.session_state.get("_calendar_blocks", {})
        for d in range(7):
            day = (week_start + timedelta(days=d)).isoformat()
            rows.extend(cache.get(day, []))

    by_date = {}
    for r in rows:
        by_date.setdefault(r["block_date"], []).append(r)
    # sort each day by start_time
    for d in by_date:
        by_date[d].sort(key=lambda x: x.get("start_time") or "")
    return by_date


def save_block(block: dict) -> dict:
    """Insert or upsert a block. Returns the saved block (with id)."""
    sb = _sb()
    block.setdefault("is_default", False)
    if sb:
        try:
            if block.get("id"):
                res = sb.table("calendar_blocks").upsert(block).execute()
            else:
                res = sb.table("calendar_blocks").insert(block).execute()
            if res.data:
                saved = res.data[0]
                _update_session_cache(saved)
                return saved
        except Exception:
            pass
    # session state fallback
    if not block.get("id"):
        import uuid
        block["id"] = str(uuid.uuid4())
    _update_session_cache(block)
    return block


def delete_block(block_id: str, block_date: str):
    sb = _sb()
    if sb:
        try:
            sb.table("calendar_blocks").delete().eq("id", block_id).execute()
        except Exception:
            pass
    cache = st.session_state.get("_calendar_blocks", {})
    cache[block_date] = [b for b in cache.get(block_date, []) if b.get("id") != block_id]
    st.session_state["_calendar_blocks"] = cache


def _update_session_cache(block: dict):
    cache = st.session_state.get("_calendar_blocks", {})
    d = block["block_date"]
    existing = cache.get(d, [])
    ids = [b["id"] for b in existing]
    if block["id"] in ids:
        cache[d] = [block if b["id"] == block["id"] else b for b in existing]
    else:
        cache[d] = existing + [block]
    st.session_state["_calendar_blocks"] = cache


def seed_defaults_for_week(week_start: date, existing: dict):
    """For any day in the week that has NO blocks yet, seed WPP defaults."""
    for i in range(7):
        day = week_start + timedelta(days=i)
        day_str = day.isoformat()
        if day_str not in existing:
            weekday = day.weekday()
            for tmpl in WPP_DEFAULTS.get(weekday, []):
                block = {**tmpl, "block_date": day_str, "is_default": True}
                save_block(block)


# ─── UI helpers ───────────────────────────────────────────────────────────────

def _block_card_html(block: dict, dark: bool) -> str:
    btype  = block.get("block_type", "personal")
    cols   = BLOCK_COLOURS.get(btype, BLOCK_COLOURS["personal"])
    icon   = TYPE_ICONS.get(btype, "📌")
    title  = block.get("title", "Untitled")
    desc   = block.get("description", "")
    start  = block.get("start_time", "")
    dur    = block.get("duration_minutes", 0)
    is_def = block.get("is_default", False)

    if dark:
        bg     = cols["bg"].replace("#", "#22") if len(cols["bg"]) == 7 else cols["bg"]
        bg     = "#1e293b"
        text   = "#e2e8f0"
        sub    = "#94a3b8"
    else:
        bg     = cols["bg"]
        text   = cols["text"]
        sub    = "#64748b"

    lock = " 🔒" if is_def else ""
    dur_str = f"{dur}m" if dur < 60 else f"{dur//60}h{dur%60:02d}m" if dur % 60 else f"{dur//60}h"

    return f"""
    <div style="background:{bg};border-left:3px solid {cols['border']};border-radius:6px;
                padding:.45rem .65rem;margin-bottom:.3rem;font-size:.8rem;">
        <div style="display:flex;justify-content:space-between;align-items:center;">
            <span style="font-weight:600;color:{text}">{icon} {title}{lock}</span>
            <span style="font-size:.7rem;color:{sub};white-space:nowrap;margin-left:.4rem">{start} · {dur_str}</span>
        </div>
        {f'<div style="color:{sub};font-size:.72rem;margin-top:.15rem;line-height:1.3">{desc[:80]}{"…" if len(desc)>80 else ""}</div>' if desc else ''}
    </div>"""


def _week_start_for(d: date) -> date:
    return d - timedelta(days=d.weekday())


# ─── Add / Edit form ─────────────────────────────────────────────────────────

def render_block_form(day_str: str, existing_block: dict = None):
    """Renders the add/edit form in a sidebar or expander context."""
    is_edit = existing_block is not None
    prefix  = f"form_{day_str}_{existing_block['id'] if is_edit else 'new'}"

    title = st.text_input("Title *", value=existing_block.get("title", "") if is_edit else "",
                          key=f"{prefix}_title", placeholder="e.g. Study Block 2")
    desc  = st.text_area("Description", value=existing_block.get("description", "") if is_edit else "",
                         key=f"{prefix}_desc", height=70,
                         placeholder="Optional notes, reminders, context…")

    c1, c2 = st.columns(2)
    with c1:
        btype_idx = BLOCK_TYPES.index(existing_block.get("block_type", "study")) if is_edit else 0
        btype = st.selectbox("Type", BLOCK_TYPES,
                             format_func=lambda t: f"{TYPE_ICONS[t]} {t.capitalize()}",
                             index=btype_idx, key=f"{prefix}_type")
    with c2:
        start = st.text_input("Start time", value=existing_block.get("start_time", "") if is_edit else "",
                              key=f"{prefix}_start", placeholder="08:45")

    dur = st.number_input("Duration (minutes)", min_value=5, max_value=480,
                          value=existing_block.get("duration_minutes", 25) if is_edit else 25,
                          step=5, key=f"{prefix}_dur")

    btn_label = "💾 Save Changes" if is_edit else "➕ Add Block"
    if st.button(btn_label, use_container_width=True, key=f"{prefix}_submit"):
        if not title.strip():
            st.error("Title is required.")
            return
        block = {
            "block_date":        day_str,
            "title":             title.strip(),
            "description":       desc.strip(),
            "block_type":        btype,
            "start_time":        start.strip(),
            "duration_minutes":  int(dur),
            "is_default":        False,
        }
        if is_edit:
            block["id"] = existing_block["id"]
        save_block(block)
        st.success("Saved!" if is_edit else "Block added!")
        # Clear edit state
        st.session_state.pop(f"editing_{existing_block['id']}", None)
        st.rerun()


# ─── Main page ────────────────────────────────────────────────────────────────

def page_calendar():
    dark = st.session_state.get("dark_mode", False)
    text_col = "#e6edf3" if dark else "#1a1a2e"
    sub_col  = "#8b949e" if dark else "#6b7280"
    card_bg  = "#161b22" if dark else "white"
    card_bdr = "#30363d" if dark else "#e5e7eb"

    st.markdown("# 📅 Weekly Calendar")
    st.markdown("*Your WPP schedule — view, edit, and customise any block*")
    st.markdown("---")

    # ── Week navigation ──
    if "cal_week_offset" not in st.session_state:
        st.session_state["cal_week_offset"] = 0

    offset     = st.session_state["cal_week_offset"]
    today      = date.today()
    week_start = _week_start_for(today) + timedelta(weeks=offset)
    week_end   = week_start + timedelta(days=6)

    nav1, nav2, nav3, nav4 = st.columns([1, 2, 1, 1])
    with nav1:
        if st.button("◀ Prev week", use_container_width=True):
            st.session_state["cal_week_offset"] -= 1
            st.rerun()
    with nav2:
        week_label = f"{week_start.strftime('%d %b')} – {week_end.strftime('%d %b %Y')}"
        st.markdown(f"<div style='text-align:center;font-weight:700;font-size:1.05rem;padding:.35rem 0;color:{text_col}'>{week_label}</div>",
                    unsafe_allow_html=True)
    with nav3:
        if st.button("Next week ▶", use_container_width=True):
            st.session_state["cal_week_offset"] += 1
            st.rerun()
    with nav4:
        if st.button("Today", use_container_width=True):
            st.session_state["cal_week_offset"] = 0
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Load & seed ──
    blocks_by_date = load_blocks_for_week(week_start)
    seed_defaults_for_week(week_start, blocks_by_date)
    # Reload after seeding so new defaults appear
    blocks_by_date = load_blocks_for_week(week_start)

    # ── Week summary strip ──
    study_counts = {}
    for i in range(7):
        d = (week_start + timedelta(days=i)).isoformat()
        day_blocks = blocks_by_date.get(d, [])
        study_counts[d] = sum(1 for b in day_blocks if b.get("block_type") == "study"
                              and "Anki" not in b.get("title", ""))

    total_study = sum(study_counts.values())
    target_min, target_max = 8, 12
    bar_pct = min(100, round(total_study / target_max * 100))
    bar_col = "#22c55e" if total_study >= target_min else "#f59e0b" if total_study >= target_min // 2 else "#ef4444"

    st.markdown(f"""
    <div style="background:{'#161b22' if dark else '#f8fafc'};border:1px solid {card_bdr};border-radius:12px;
                padding:1rem 1.4rem;margin-bottom:1.2rem">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:.5rem">
            <span style="font-weight:700;color:{text_col}">📊 Week at a glance</span>
            <span style="font-size:.82rem;color:{sub_col}">Target: {target_min}–{target_max} study sessions</span>
        </div>
        <div style="background:{'#30363d' if dark else '#e5e7eb'};border-radius:999px;height:8px;margin-bottom:.5rem">
            <div style="width:{bar_pct}%;height:100%;background:{bar_col};border-radius:999px"></div>
        </div>
        <span style="font-size:.82rem;color:{sub_col}">{total_study} study sessions this week</span>
    </div>""", unsafe_allow_html=True)

    # ── Day columns ──
    cols = st.columns(7)

    for i, col in enumerate(cols):
        day_date  = week_start + timedelta(days=i)
        day_str   = day_date.isoformat()
        day_label = DAY_NAMES[i]
        is_today  = (day_date == today)
        day_blocks = blocks_by_date.get(day_str, [])

        header_bg  = ("#1a2744" if dark else "#eff6ff") if is_today else (card_bg)
        header_bdr = "#3b82f6" if is_today else card_bdr
        date_num   = day_date.strftime("%-d")

        with col:
            # Day header
            st.markdown(f"""
            <div style="background:{header_bg};border:1px solid {header_bdr};border-radius:10px 10px 0 0;
                        padding:.5rem .6rem;text-align:center;margin-bottom:0">
                <div style="font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;
                            color:{'#60a5fa' if is_today else sub_col};font-weight:600">{day_label[:3]}</div>
                <div style="font-size:1.3rem;font-weight:700;color:{'#3b82f6' if is_today else text_col};line-height:1.1">{date_num}</div>
                {'<div style="width:6px;height:6px;background:#3b82f6;border-radius:50%;margin:.1rem auto 0"></div>' if is_today else ''}
            </div>""", unsafe_allow_html=True)

            # Blocks
            st.markdown(f"""
            <div style="background:{card_bg};border:1px solid {card_bdr};border-top:none;
                        border-radius:0 0 10px 10px;padding:.5rem .4rem;min-height:120px">""",
                        unsafe_allow_html=True)

            for block in day_blocks:
                bid = block.get("id", "")
                st.markdown(_block_card_html(block, dark), unsafe_allow_html=True)

                # Edit / Delete buttons (tiny, inline)
                b1, b2 = st.columns([1, 1])
                with b1:
                    if st.button("✏️", key=f"edit_{bid}", help="Edit block"):
                        st.session_state[f"editing_{bid}"] = True
                        st.session_state["edit_day"] = day_str
                        st.session_state["edit_block"] = block
                with b2:
                    if st.button("🗑️", key=f"del_{bid}", help="Delete block"):
                        delete_block(bid, day_str)
                        st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

            # Add block button
            if st.button("＋", key=f"add_{day_str}", help=f"Add block to {day_label}",
                         use_container_width=True):
                st.session_state["adding_day"] = day_str

    # ── Add block panel ──
    adding_day = st.session_state.get("adding_day")
    editing_block = st.session_state.get("edit_block")
    editing_id = st.session_state.get("editing_" + (editing_block.get("id","") if editing_block else ""), False)

    if adding_day or (editing_block and editing_id):
        st.markdown("---")
        target_day = adding_day or st.session_state.get("edit_day", "")
        day_name_label = DAY_NAMES[date.fromisoformat(target_day).weekday()] if target_day else ""

        if editing_block and editing_id:
            st.subheader(f"✏️ Edit block — {day_name_label}")
            with st.container():
                render_block_form(target_day, existing_block=editing_block)
                if st.button("✖ Cancel", key="cancel_edit"):
                    st.session_state.pop("edit_block", None)
                    st.session_state.pop("edit_day", None)
                    for k in list(st.session_state.keys()):
                        if k.startswith("editing_"):
                            del st.session_state[k]
                    st.rerun()
        else:
            st.subheader(f"➕ Add block — {day_name_label} ({target_day})")
            with st.container():
                render_block_form(target_day)
                if st.button("✖ Cancel", key="cancel_add"):
                    st.session_state.pop("adding_day", None)
                    st.rerun()

    # ── Legend ──
    st.markdown("<br>", unsafe_allow_html=True)
    legend_items = "".join([
        f'<span style="background:{BLOCK_COLOURS[t]["bg"]};border:1px solid {BLOCK_COLOURS[t]["border"]};'
        f'border-radius:999px;padding:.2rem .75rem;font-size:.75rem;color:{BLOCK_COLOURS[t]["text"]};'
        f'margin:.15rem;display:inline-block">{TYPE_ICONS[t]} {t.capitalize()}</span>'
        for t in BLOCK_TYPES
    ])
    st.markdown(f"""
    <div style="margin-top:.5rem">
        <span style="font-size:.72rem;color:{sub_col};text-transform:uppercase;letter-spacing:.08em">Legend: </span>
        {legend_items}
        <span style="font-size:.72rem;color:{sub_col};margin-left:.5rem">🔒 = WPP default block</span>
    </div>""", unsafe_allow_html=True)
