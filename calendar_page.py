"""
calendar_page.py — Weekly Calendar with WPP integration
Time-grid layout: 24h axis on left, blocks positioned by start time, height = duration.
"""

import streamlit as st
from datetime import date, timedelta, datetime
import json

# ─── Supabase helper ──────────────────────────────────────────────────────────

def _sb():
    return st.session_state.get("supabase_client")

# ─── WPP Default blocks ───────────────────────────────────────────────────────

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
        {"title": "Afternoon — Flexible", "description": "If home + she rests: 1-2 study blocks. Never forced.", "block_type": "study", "start_time": "14:00", "duration_minutes": 150},
        {"title": "Evening with GF", "description": "Movie, dinner, quality time.", "block_type": "personal", "start_time": "16:30", "duration_minutes": 210},
        {"title": "Anki + Sleep Prep", "description": "Final Korean. Earlier bed = better week.", "block_type": "study", "start_time": "22:00", "duration_minutes": 10},
    ],
}

BLOCK_COLOURS = {
    "study":    {"bg": "#dbeafe", "border": "#3b82f6", "text": "#1e3a5f"},
    "work":     {"bg": "#fee2e2", "border": "#ef4444", "text": "#7f1d1d"},
    "fitness":  {"bg": "#dcfce7", "border": "#22c55e", "text": "#14532d"},
    "personal": {"bg": "#fef9c3", "border": "#eab308", "text": "#713f12"},
    "play":     {"bg": "#f3e8ff", "border": "#a855f7", "text": "#3b0764"},
}
BLOCK_COLOURS_DARK = {
    "study":    {"bg": "#1e3a5f", "border": "#3b82f6", "text": "#bfdbfe"},
    "work":     {"bg": "#450a0a", "border": "#ef4444", "text": "#fecaca"},
    "fitness":  {"bg": "#052e16", "border": "#22c55e", "text": "#bbf7d0"},
    "personal": {"bg": "#422006", "border": "#eab308", "text": "#fef08a"},
    "play":     {"bg": "#3b0764", "border": "#a855f7", "text": "#e9d5ff"},
}

BLOCK_TYPES = ["study", "work", "fitness", "personal", "play"]
TYPE_ICONS  = {"study": "📚", "work": "💼", "fitness": "🏃", "personal": "👤", "play": "🎮"}
DAY_NAMES   = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
DAY_SHORT   = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

# Grid constants — 1px per minute, 60px per hour
PX_PER_HOUR  = 60
TOTAL_HOURS  = 24
TOTAL_HEIGHT = TOTAL_HOURS * PX_PER_HOUR   # 1440px
TIME_COL_W   = 44


# ─── Supabase CRUD ────────────────────────────────────────────────────────────

def load_blocks_for_week(week_start: date) -> dict:
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
    if not rows:
        cache = st.session_state.get("_calendar_blocks", {})
        for d in range(7):
            day = (week_start + timedelta(days=d)).isoformat()
            rows.extend(cache.get(day, []))
    by_date = {}
    for r in rows:
        by_date.setdefault(r["block_date"], []).append(r)
    for d in by_date:
        by_date[d].sort(key=lambda x: x.get("start_time") or "")
    return by_date


def save_block(block: dict) -> dict:
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
    for i in range(7):
        day = week_start + timedelta(days=i)
        day_str = day.isoformat()
        if day_str not in existing:
            for tmpl in WPP_DEFAULTS.get(day.weekday(), []):
                save_block({**tmpl, "block_date": day_str, "is_default": True})


def _week_start_for(d: date) -> date:
    return d - timedelta(days=d.weekday())


# ─── Time helpers ─────────────────────────────────────────────────────────────

def _time_to_px(t: str) -> int:
    """'HH:MM' -> pixel offset from top of grid (1px per minute)."""
    try:
        h, m = t.strip().split(":")
        return int(h) * PX_PER_HOUR + round(int(m) * PX_PER_HOUR / 60)
    except Exception:
        return 0


def _dur_to_px(minutes: int) -> int:
    return max(round(minutes * PX_PER_HOUR / 60), 18)


def _dur_str(minutes: int) -> str:
    if minutes < 60:
        return f"{minutes}m"
    h, m = divmod(minutes, 60)
    return f"{h}h{m:02d}m" if m else f"{h}h"


# ─── Time-grid HTML ───────────────────────────────────────────────────────────

def _build_time_grid(blocks_by_date: dict, week_start: date, today: date, dark: bool) -> str:

    bg_grid   = "#161b22"   if dark else "#ffffff"
    col_line  = "#30363d"   if dark else "#e5e7eb"
    col_hour  = "#8b949e"   if dark else "#9ca3af"
    col_hdr   = "#e6edf3"   if dark else "#1a1a2e"
    col_sub   = "#8b949e"   if dark else "#6b7280"
    today_hdr = "#1a2744"   if dark else "#dbeafe"
    today_bdr = "#3b82f6"

    # Current-time marker
    now       = datetime.now()
    now_top   = now.hour * PX_PER_HOUR + round(now.minute * PX_PER_HOUR / 60)
    show_now  = (week_start <= today <= week_start + timedelta(days=6))
    today_col = today.weekday()

    # ── Hour labels & horizontal lines ──
    hour_labels = ""
    grid_lines  = ""
    for h in range(TOTAL_HOURS + 1):
        top = h * PX_PER_HOUR
        if h <= TOTAL_HOURS:
            hour_labels += (
                f'<div style="position:absolute;top:{top}px;right:5px;'
                f'font-size:.58rem;color:{col_hour};transform:translateY(-50%);'
                f'white-space:nowrap;line-height:1">{h:02d}:00</div>'
            )
        grid_lines += (
            f'<div style="position:absolute;top:{top}px;left:0;right:0;'
            f'border-top:1px solid {col_line}"></div>'
        )
        if h < TOTAL_HOURS:
            half = top + PX_PER_HOUR // 2
            grid_lines += (
                f'<div style="position:absolute;top:{half}px;left:0;right:0;'
                f'border-top:1px dashed {col_line};opacity:.35"></div>'
            )

    # ── Day columns ──
    day_cols = ""
    for i in range(7):
        day_date   = week_start + timedelta(days=i)
        day_str    = day_date.isoformat()
        is_today   = (day_date == today)
        day_blocks = blocks_by_date.get(day_str, [])

        hdr_bg  = today_hdr if is_today else (bg_grid if dark else "#f9fafb")
        hdr_bdr = today_bdr if is_today else col_line
        dot     = (f'<div style="width:5px;height:5px;background:{today_bdr};'
                   f'border-radius:50%;margin:.15rem auto 0"></div>') if is_today else ""

        header = (
            f'<div style="position:sticky;top:0;z-index:10;background:{hdr_bg};'
            f'border-bottom:2px solid {hdr_bdr};padding:.3rem .15rem .25rem;'
            f'text-align:center;border-right:1px solid {col_line};">'
            f'<div style="font-size:.58rem;font-weight:700;text-transform:uppercase;'
            f'letter-spacing:.06em;color:{"#60a5fa" if is_today else col_sub}">'
            f'{DAY_SHORT[i]}</div>'
            f'<div style="font-size:.95rem;font-weight:700;line-height:1.1;'
            f'color:{"#3b82f6" if is_today else col_hdr}">'
            f'{day_date.strftime("%-d")}</div>'
            f'{dot}'
            f'</div>'
        )

        # Now-line (today only)
        now_line = ""
        if show_now and i == today_col:
            now_line = (
                f'<div style="position:absolute;top:{now_top}px;left:0;right:0;'
                f'border-top:2px solid #ef4444;z-index:6;pointer-events:none">'
                f'<div style="position:absolute;left:-3px;top:-4px;width:7px;height:7px;'
                f'background:#ef4444;border-radius:50%"></div>'
                f'</div>'
            )

        # Blocks
        blocks_html = ""
        for block in day_blocks:
            top_px    = _time_to_px(block.get("start_time", "00:00"))
            height_px = _dur_to_px(block.get("duration_minutes", 25))
            btype     = block.get("block_type", "personal")
            palette   = BLOCK_COLOURS_DARK[btype] if dark else BLOCK_COLOURS[btype]
            icon      = TYPE_ICONS.get(btype, "📌")
            title     = block.get("title", "Untitled")
            is_def    = block.get("is_default", False)
            bid       = block.get("id", "")
            lock      = " 🔒" if is_def else ""

            if height_px >= 38:
                inner = (
                    f'<div style="font-size:.58rem;opacity:.75;margin-bottom:.08rem;'
                    f'white-space:nowrap;overflow:hidden">'
                    f'{block.get("start_time","")} · {_dur_str(block.get("duration_minutes",0))}</div>'
                    f'<div style="font-weight:600;font-size:.67rem;line-height:1.25;overflow:hidden;'
                    f'display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical">'
                    f'{icon} {title}{lock}</div>'
                )
            else:
                inner = (
                    f'<div style="font-weight:600;font-size:.63rem;white-space:nowrap;'
                    f'overflow:hidden;text-overflow:ellipsis">'
                    f'{icon} {title}{lock}</div>'
                )

            # JSON data encoded into data attribute for click handler
            bdata = json.dumps({
                "id": bid, "day": day_str,
                "title": title,
                "description": block.get("description", ""),
                "block_type": btype,
                "start_time": block.get("start_time", ""),
                "duration_minutes": block.get("duration_minutes", 25),
                "is_default": is_def,
            }).replace('"', "&quot;")

            blocks_html += (
                f'<div onclick="selectBlock(this)" data-block="{bdata}" '
                f'style="position:absolute;top:{top_px}px;left:1px;right:1px;'
                f'height:{height_px}px;background:{palette["bg"]};'
                f'border-left:3px solid {palette["border"]};color:{palette["text"]};'
                f'border-radius:3px;padding:.12rem .25rem;overflow:hidden;'
                f'cursor:pointer;z-index:4;box-sizing:border-box;font-family:inherit;'
                f'transition:filter .12s" '
                f'onmouseenter="this.style.filter=\'brightness(0.92)\'" '
                f'onmouseleave="this.style.filter=\'none\'">'
                f'{inner}'
                f'</div>'
            )

        day_cols += (
            f'<div style="flex:1;min-width:0;position:relative;'
            f'border-right:1px solid {col_line}">'
            f'{header}'
            f'<div style="position:relative;height:{TOTAL_HEIGHT}px;">'
            f'<div style="position:absolute;inset:0">{grid_lines}</div>'
            f'{now_line}'
            f'{blocks_html}'
            f'</div>'
            f'</div>'
        )

    # ── Info panel colours ──
    panel_bg  = "#1e293b" if dark else "#f8fafc"
    panel_bdr = "#30363d" if dark else "#e2e8f0"

    return f"""
<style>
  .wpp-cal-outer {{
    border: 1px solid {col_line};
    border-radius: 10px;
    overflow: hidden;
    background: {bg_grid};
    font-family: 'Noto Sans KR', sans-serif;
  }}
  .wpp-cal-scroll {{
    overflow-x: auto;
    overflow-y: auto;
    max-height: 680px;
  }}
  .wpp-cal-scroll::-webkit-scrollbar {{ height: 4px; width: 4px; }}
  .wpp-cal-scroll::-webkit-scrollbar-thumb {{
    background: {col_line}; border-radius: 2px;
  }}
  .wpp-cal-inner {{
    display: flex;
    min-width: 500px;
  }}
  .wpp-time-col {{
    width: {TIME_COL_W}px;
    min-width: {TIME_COL_W}px;
    position: relative;
    background: {bg_grid};
    border-right: 1px solid {col_line};
    flex-shrink: 0;
  }}
  .wpp-time-sticky {{
    position: sticky;
    top: 0;
    z-index: 11;
    background: {bg_grid};
    height: 48px;
    border-bottom: 2px solid {col_line};
  }}
  .wpp-time-body {{
    position: relative;
    height: {TOTAL_HEIGHT}px;
  }}
  @media (max-width: 600px) {{
    .wpp-cal-inner {{ min-width: 380px; }}
  }}
</style>

<div class="wpp-cal-outer">
  <div class="wpp-cal-scroll" id="wppCalScroll">
    <div class="wpp-cal-inner">
      <div class="wpp-time-col">
        <div class="wpp-time-sticky"></div>
        <div class="wpp-time-body">{hour_labels}</div>
      </div>
      {day_cols}
    </div>
  </div>
</div>

<!-- Block detail panel -->
<div id="wppBlockPanel" style="display:none;margin-top:.75rem;padding:.9rem 1.1rem;
     background:{panel_bg};border:1px solid {panel_bdr};border-radius:10px;
     border-left:4px solid #3b82f6;font-family:inherit">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:.5rem">
    <div style="flex:1;min-width:0">
      <div id="wppBpType" style="font-size:.66rem;text-transform:uppercase;
           letter-spacing:.08em;color:{col_sub};margin-bottom:.18rem"></div>
      <div id="wppBpTitle" style="font-weight:700;font-size:.95rem;
           color:{col_hdr};margin-bottom:.15rem"></div>
      <div id="wppBpTime"  style="font-size:.76rem;color:{col_sub};
           margin-bottom:.35rem"></div>
      <div id="wppBpDesc"  style="font-size:.82rem;color:{col_hdr};
           line-height:1.55;white-space:pre-wrap"></div>
    </div>
    <button onclick="document.getElementById('wppBlockPanel').style.display='none'"
            style="background:none;border:none;cursor:pointer;font-size:1rem;
                   color:{col_sub};flex-shrink:0;padding:.1rem .25rem">✕</button>
  </div>
  <div style="display:flex;gap:.45rem;margin-top:.7rem;flex-wrap:wrap">
    <button id="wppBpEditBtn" onclick="wppTriggerEdit()"
            style="background:#3b82f6;color:white;border:none;border-radius:6px;
                   padding:.28rem .8rem;font-size:.78rem;cursor:pointer">✏️ Edit</button>
    <button id="wppBpDelBtn" onclick="wppTriggerDelete()"
            style="background:#ef4444;color:white;border:none;border-radius:6px;
                   padding:.28rem .8rem;font-size:.78rem;cursor:pointer">🗑️ Delete</button>
  </div>
</div>

<script>
var _wppBlock = null;
var _icons = {{"study":"📚","work":"💼","fitness":"🏃","personal":"👤","play":"🎮"}};

function selectBlock(el) {{
  _wppBlock = JSON.parse(el.dataset.block.replace(/&quot;/g, '"'));
  var b = _wppBlock;
  document.getElementById("wppBpType").textContent =
    (_icons[b.block_type]||"📌") + " " +
    b.block_type.charAt(0).toUpperCase() + b.block_type.slice(1) +
    (b.is_default ? " · 🔒 WPP default" : "");
  document.getElementById("wppBpTitle").textContent = b.title;
  document.getElementById("wppBpTime").textContent =
    b.start_time + " · " + wppDurStr(b.duration_minutes);
  document.getElementById("wppBpDesc").textContent = b.description || "";
  var panel = document.getElementById("wppBlockPanel");
  panel.style.display = "block";
  panel.scrollIntoView({{behavior:"smooth", block:"nearest"}});
}}

function wppDurStr(m) {{
  if (m < 60) return m + "m";
  var h = Math.floor(m/60), r = m%60;
  return r ? h + "h" + String(r).padStart(2,"0") + "m" : h + "h";
}}

function wppTriggerEdit() {{
  if (!_wppBlock) return;
  var inp = window.parent.document.querySelector('[data-testid="stTextInput"] input[aria-label="wpp_edit_trigger"]');
  // Use Streamlit component value trick via postMessage
  window.parent.postMessage({{
    type: "streamlit:setComponentValue",
    value: JSON.stringify(_wppBlock)
  }}, "*");
  // Fallback: write to a visible input Streamlit can read
  var inputs = document.querySelectorAll('input[type="text"]');
  inputs.forEach(function(inp) {{
    if (inp.placeholder === "__wpp_edit__") {{
      var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
      nativeInputValueSetter.call(inp, JSON.stringify(_wppBlock));
      inp.dispatchEvent(new Event('input', {{ bubbles: true }}));
    }}
  }});
}}

function wppTriggerDelete() {{
  if (!_wppBlock) return;
  if (!confirm('Delete "' + _wppBlock.title + '"?')) return;
  var inputs = document.querySelectorAll('input[type="text"]');
  inputs.forEach(function(inp) {{
    if (inp.placeholder === "__wpp_del_id__") {{
      var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
      setter.call(inp, _wppBlock.id + "|" + _wppBlock.day);
      inp.dispatchEvent(new Event('input', {{ bubbles: true }}));
    }}
  }});
}}

// Auto-scroll to 07:30 on load
(function() {{
  var el = document.getElementById("wppCalScroll");
  if (el) el.scrollTop = {_time_to_px("07:30")};
}})();
</script>
"""


# ─── Add / Edit form ─────────────────────────────────────────────────────────

def render_block_form(day_str: str, existing_block: dict = None):
    is_edit = existing_block is not None
    prefix  = f"form_{day_str}_{existing_block['id'] if is_edit else 'new'}"

    title = st.text_input("Title *",
                          value=existing_block.get("title", "") if is_edit else "",
                          key=f"{prefix}_title", placeholder="e.g. Study Block 2")
    desc  = st.text_area("Description",
                         value=existing_block.get("description", "") if is_edit else "",
                         key=f"{prefix}_desc", height=70,
                         placeholder="Optional notes, reminders, context...")
    c1, c2 = st.columns(2)
    with c1:
        btype_idx = BLOCK_TYPES.index(existing_block.get("block_type", "study")) if is_edit else 0
        btype = st.selectbox("Type", BLOCK_TYPES,
                             format_func=lambda t: f"{TYPE_ICONS[t]} {t.capitalize()}",
                             index=btype_idx, key=f"{prefix}_type")
    with c2:
        start = st.text_input("Start time (HH:MM)",
                              value=existing_block.get("start_time", "") if is_edit else "",
                              key=f"{prefix}_start", placeholder="08:45")
    dur = st.number_input("Duration (minutes)", min_value=5, max_value=1440,
                          value=existing_block.get("duration_minutes", 25) if is_edit else 25,
                          step=5, key=f"{prefix}_dur")

    if st.button("💾 Save Changes" if is_edit else "➕ Add Block",
                 use_container_width=True, key=f"{prefix}_submit"):
        if not title.strip():
            st.error("Title is required.")
            return
        block = {
            "block_date":       day_str,
            "title":            title.strip(),
            "description":      desc.strip(),
            "block_type":       btype,
            "start_time":       start.strip(),
            "duration_minutes": int(dur),
            "is_default":       False,
        }
        if is_edit:
            block["id"] = existing_block["id"]
        save_block(block)
        st.success("Saved!")
        st.session_state.pop("cal_edit_block", None)
        st.session_state.pop("cal_adding_day", None)
        st.rerun()


# ─── Main page ────────────────────────────────────────────────────────────────

def page_calendar():
    dark     = st.session_state.get("dark_mode", False)
    text_col = "#e6edf3" if dark else "#1a1a2e"
    sub_col  = "#8b949e" if dark else "#6b7280"
    card_bdr = "#30363d" if dark else "#e5e7eb"

    st.markdown("# 📅 Weekly Calendar")
    st.markdown("*Your WPP schedule — click any block to view details, edit or delete*")
    st.markdown("---")

    # ── Week navigation ──
    if "cal_week_offset" not in st.session_state:
        st.session_state["cal_week_offset"] = 0

    offset     = st.session_state["cal_week_offset"]
    today      = date.today()
    week_start = _week_start_for(today) + timedelta(weeks=offset)
    week_end   = week_start + timedelta(days=6)

    n1, n2, n3, n4 = st.columns([1, 2, 1, 1])
    with n1:
        if st.button("◀ Prev", use_container_width=True, key="cal_prev"):
            st.session_state["cal_week_offset"] -= 1
            st.rerun()
    with n2:
        st.markdown(
            f"<div style='text-align:center;font-weight:700;font-size:1rem;"
            f"padding:.38rem 0;color:{text_col}'>"
            f"{week_start.strftime('%d %b')} – {week_end.strftime('%d %b %Y')}</div>",
            unsafe_allow_html=True)
    with n3:
        if st.button("Next ▶", use_container_width=True, key="cal_next"):
            st.session_state["cal_week_offset"] += 1
            st.rerun()
    with n4:
        if st.button("Today", use_container_width=True, key="cal_today"):
            st.session_state["cal_week_offset"] = 0
            st.rerun()

    # ── Load & seed ──
    blocks_by_date = load_blocks_for_week(week_start)
    seed_defaults_for_week(week_start, blocks_by_date)
    blocks_by_date = load_blocks_for_week(week_start)

    # ── Study session summary ──
    total_study = sum(
        1 for i in range(7)
        for b in blocks_by_date.get((week_start + timedelta(days=i)).isoformat(), [])
        if b.get("block_type") == "study" and "Anki" not in b.get("title", "")
    )
    target_min, target_max = 8, 12
    bar_pct = min(100, round(total_study / target_max * 100))
    bar_col = "#22c55e" if total_study >= target_min else "#f59e0b" if total_study >= 4 else "#ef4444"

    st.markdown(f"""
    <div style="background:{'#161b22' if dark else '#f8fafc'};border:1px solid {card_bdr};
                border-radius:8px;padding:.6rem 1.1rem;margin:.5rem 0 .8rem;
                display:flex;align-items:center;gap:.9rem;flex-wrap:wrap">
      <span style="font-weight:700;font-size:.84rem;color:{text_col};white-space:nowrap">
        📊 {total_study} study sessions this week
      </span>
      <div style="flex:1;min-width:100px;background:{'#30363d' if dark else '#e5e7eb'};
                  border-radius:999px;height:6px">
        <div style="width:{bar_pct}%;height:100%;background:{bar_col};border-radius:999px"></div>
      </div>
      <span style="font-size:.74rem;color:{sub_col};white-space:nowrap">
        target {target_min}–{target_max}
      </span>
    </div>""", unsafe_allow_html=True)

    # ── Time grid ──
    st.markdown(_build_time_grid(blocks_by_date, week_start, today, dark),
                unsafe_allow_html=True)

    # ── Hidden inputs for JS→Streamlit communication ──
    # These are read after the grid renders
    edit_raw = st.text_input("", key="cal_edit_input",
                             label_visibility="collapsed",
                             placeholder="__wpp_edit__")
    del_raw  = st.text_input("", key="cal_del_input",
                             label_visibility="collapsed",
                             placeholder="__wpp_del_id__")

    # Handle delete (format: "block_id|date_str")
    if del_raw and "|" in del_raw:
        bid, bday = del_raw.split("|", 1)
        delete_block(bid.strip(), bday.strip())
        st.session_state["cal_del_input"] = ""
        st.rerun()

    # Handle edit
    if edit_raw:
        try:
            eb = json.loads(edit_raw)
            st.session_state["cal_edit_block"] = eb
            st.session_state.pop("cal_adding_day", None)
            st.session_state["cal_edit_input"] = ""
        except Exception:
            pass

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Add block row ──
    a1, a2 = st.columns([3, 1])
    with a1:
        day_options = {
            DAY_NAMES[i] + "  " + (week_start + timedelta(days=i)).strftime("%-d %b"):
            (week_start + timedelta(days=i)).isoformat()
            for i in range(7)
        }
        sel_label = st.selectbox(
            "Add block to day:", list(day_options.keys()),
            key="cal_add_day_sel",
            index=min(today.weekday(), 6) if week_start <= today <= week_end else 0,
            label_visibility="collapsed"
        )
    with a2:
        if st.button("➕ Add Block", use_container_width=True, key="cal_open_add"):
            st.session_state["cal_adding_day"] = day_options[sel_label]
            st.session_state.pop("cal_edit_block", None)

    # ── Edit / Add forms ──
    edit_block = st.session_state.get("cal_edit_block")
    adding_day = st.session_state.get("cal_adding_day")

    if edit_block:
        dn = DAY_NAMES[date.fromisoformat(edit_block["day"]).weekday()]
        with st.expander(f"✏️ Editing: **{edit_block['title']}** — {dn}", expanded=True):
            render_block_form(edit_block["day"], existing_block=edit_block)
            if st.button("✖ Cancel", key="cal_cancel_edit"):
                st.session_state.pop("cal_edit_block", None)
                st.rerun()

    elif adding_day:
        dn = DAY_NAMES[date.fromisoformat(adding_day).weekday()]
        with st.expander(f"➕ New block — {dn} ({adding_day})", expanded=True):
            render_block_form(adding_day)
            if st.button("✖ Cancel", key="cal_cancel_add"):
                st.session_state.pop("cal_adding_day", None)
                st.rerun()

    # ── Legend ──
    st.markdown("<br>", unsafe_allow_html=True)
    legend = "".join([
        f'<span style="background:{BLOCK_COLOURS[t]["bg"]};'
        f'border:1px solid {BLOCK_COLOURS[t]["border"]};border-radius:999px;'
        f'padding:.16rem .65rem;font-size:.72rem;color:{BLOCK_COLOURS[t]["text"]};'
        f'margin:.12rem;display:inline-block">{TYPE_ICONS[t]} {t.capitalize()}</span>'
        for t in BLOCK_TYPES
    ])
    st.markdown(
        f'<div><span style="font-size:.7rem;color:{sub_col};text-transform:uppercase;'
        f'letter-spacing:.08em">Legend: </span>{legend}'
        f'<span style="font-size:.7rem;color:{sub_col};margin-left:.4rem">'
        f'🔒 = WPP default</span></div>',
        unsafe_allow_html=True)
