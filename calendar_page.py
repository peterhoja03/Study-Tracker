"""
calendar_page.py — Weekly Calendar with WPP integration
Time-grid layout: 24h axis, blocks positioned by time, height = duration.
Overlap handled by column-splitting within each day.
"""

import streamlit as st
from datetime import date, timedelta, datetime
import json

# ─── Supabase helper ──────────────────────────────────────────────────────────

def _sb():
    return st.session_state.get("supabase_client")

# ─── WPP Default blocks ───────────────────────────────────────────────────────

WPP_DEFAULTS = {
    0: [  # Monday
        {"title": "Anki — Korean",          "description": "10 min Korean — open app before coffee, without exception.", "block_type": "study",    "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast",              "description": "Hot food, sit down, no screens.",                           "block_type": "play",     "start_time": "08:15", "duration_minutes": 30},
        {"title": "Run 5k + Calisthenics",  "description": "~55 min fitness block.",                                    "block_type": "fitness",  "start_time": "08:45", "duration_minutes": 55},
        {"title": "Study Block 1",          "description": "25 min — one lesson from tracker. Mousetrap: open tracker, begin.", "block_type": "study", "start_time": "09:45", "duration_minutes": 25},
        {"title": "Get Ready + Admin",      "description": "Shower, pack, prep for the day.",                           "block_type": "personal", "start_time": "10:15", "duration_minutes": 40},
        {"title": "Amazon — Delivery Route","description": "W block. ~8h delivery shift.",                              "block_type": "work",     "start_time": "11:00", "duration_minutes": 480},
        {"title": "Home + Real Rest",       "description": "No study after work. Game, movie, recover. Non-negotiable.","block_type": "play",     "start_time": "19:00", "duration_minutes": 225},
        {"title": "Anki Wind-down",         "description": "10 min Korean before sleep.",                               "block_type": "study",    "start_time": "22:45", "duration_minutes": 10},
    ],
    1: [  # Tuesday
        {"title": "Anki — Korean",            "description": "10 min Korean.",                                                    "block_type": "study",    "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast",                "description": "30 min hot food.",                                                   "block_type": "play",     "start_time": "08:15", "duration_minutes": 30},
        {"title": "Study Block 1",            "description": "25 min — work through tracker.",                                    "block_type": "study",    "start_time": "08:45", "duration_minutes": 25},
        {"title": "Study Block 2",            "description": "25 min — second lesson or Feynman technique.",                      "block_type": "study",    "start_time": "09:20", "duration_minutes": 25},
        {"title": "Study Block 3 (Optional)", "description": "Only if genuinely sharp — stop at first sign of fatigue.",          "block_type": "study",    "start_time": "09:50", "duration_minutes": 25},
        {"title": "Free Time",                "description": "P block — game, rest, earned downtime.",                            "block_type": "play",     "start_time": "10:20", "duration_minutes": 430},
        {"title": "Get Ready for Hockey",     "description": "Kit, travel, warm up.",                                             "block_type": "personal", "start_time": "17:30", "duration_minutes": 90},
        {"title": "Hockey Training",          "description": "~2h — physical W block.",                                           "block_type": "fitness",  "start_time": "19:00", "duration_minutes": 120},
        {"title": "Anki + Sleep",             "description": "10 min Korean.",                                                    "block_type": "study",    "start_time": "22:45", "duration_minutes": 10},
    ],
    2: [  # Wednesday
        {"title": "Anki — Korean",          "description": "10 min Korean.",                          "block_type": "study",    "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast",              "description": "30 min hot food.",                         "block_type": "play",     "start_time": "08:15", "duration_minutes": 30},
        {"title": "Run 5k + Calisthenics",  "description": "~55 min fitness block.",                   "block_type": "fitness",  "start_time": "08:45", "duration_minutes": 55},
        {"title": "Study Block 1",          "description": "25 min — one lesson. Work-day target met.","block_type": "study",    "start_time": "09:45", "duration_minutes": 25},
        {"title": "Get Ready + Admin",      "description": "Shower, pack, prep.",                      "block_type": "personal", "start_time": "10:15", "duration_minutes": 45},
        {"title": "Amazon — Delivery Route","description": "Delivery route.",                          "block_type": "work",     "start_time": "11:00", "duration_minutes": 480},
        {"title": "Home + Real Rest",       "description": "No study. Game, watch, recover.",          "block_type": "play",     "start_time": "19:00", "duration_minutes": 225},
        {"title": "Anki Wind-down",         "description": "10 min Korean.",                          "block_type": "study",    "start_time": "22:45", "duration_minutes": 10},
    ],
    3: [  # Thursday
        {"title": "Anki — Korean",            "description": "10 min Korean.",                                           "block_type": "study", "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast",                "description": "30 min hot food.",                                          "block_type": "play",  "start_time": "08:15", "duration_minutes": 30},
        {"title": "Study Block 1",            "description": "25 min.",                                                   "block_type": "study", "start_time": "08:45", "duration_minutes": 25},
        {"title": "Study Block 2",            "description": "25 min.",                                                   "block_type": "study", "start_time": "09:20", "duration_minutes": 25},
        {"title": "Study Block 3",            "description": "25 min — or full review block.",                            "block_type": "study", "start_time": "09:50", "duration_minutes": 25},
        {"title": "Study Block 4 (Optional)", "description": "25 min — only if sharp. 3 is already a great day.",        "block_type": "study", "start_time": "10:20", "duration_minutes": 25},
        {"title": "Free Time",                "description": "P block — game, rest, recharge properly.",                  "block_type": "play",  "start_time": "11:00", "duration_minutes": 480},
        {"title": "Hockey Training",          "description": "~2h evening W block.",                                      "block_type": "fitness","start_time": "19:00", "duration_minutes": 120},
        {"title": "Anki + Sleep",             "description": "10 min Korean.",                                            "block_type": "study", "start_time": "22:45", "duration_minutes": 10},
    ],
    4: [  # Friday
        {"title": "Anki — Korean",          "description": "10 min Korean.",                              "block_type": "study",    "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast",              "description": "30 min hot food.",                             "block_type": "play",     "start_time": "08:15", "duration_minutes": 30},
        {"title": "Run 5k + Calisthenics",  "description": "~55 min.",                                    "block_type": "fitness",  "start_time": "08:45", "duration_minutes": 55},
        {"title": "Study Block 1",          "description": "25 min — one lesson. Friday target met.",     "block_type": "study",    "start_time": "09:45", "duration_minutes": 25},
        {"title": "Get Ready + Admin",      "description": "Shower, pack, prep.",                         "block_type": "personal", "start_time": "10:15", "duration_minutes": 45},
        {"title": "Amazon — Delivery Route","description": "Delivery route.",                             "block_type": "work",     "start_time": "11:00", "duration_minutes": 480},
        {"title": "Evening — Fully Free",   "description": "Social, gaming, movie. Friday is earned.",   "block_type": "play",     "start_time": "19:00", "duration_minutes": 225},
        {"title": "Anki Wind-down",         "description": "10 min Korean.",                              "block_type": "study",    "start_time": "22:45", "duration_minutes": 10},
    ],
    5: [  # Saturday
        {"title": "Anki — Korean",               "description": "10 min Korean — non-negotiable even on weekends.", "block_type": "study",    "start_time": "08:00", "duration_minutes": 10},
        {"title": "Breakfast",                   "description": "30 min — relaxed weekend pace.",                   "block_type": "play",     "start_time": "08:15", "duration_minutes": 30},
        {"title": "Study Block (Optional)",      "description": "25 min lighter topics. Skip freely.",              "block_type": "study",    "start_time": "08:45", "duration_minutes": 25},
        {"title": "Morning Free Time",           "description": "P block — relax, game, browse.",                   "block_type": "play",     "start_time": "09:15", "duration_minutes": 165},
        {"title": "GF Time",                     "description": "Morning into afternoon.",                          "block_type": "personal", "start_time": "12:00", "duration_minutes": 120},
        {"title": "Hockey Game",                 "description": "Travel + warm up + game.",                         "block_type": "fitness",  "start_time": "14:00", "duration_minutes": 210},
        {"title": "Post-Match + Evening with GF","description": "Team social then evening with GF.",                "block_type": "play",     "start_time": "17:30", "duration_minutes": 270},
    ],
    6: [  # Sunday
        {"title": "Wake (Natural)",       "description": "Weekend — no alarm.",                                     "block_type": "play",     "start_time": "08:00", "duration_minutes": 30},
        {"title": "Breakfast + Anki",     "description": "Stack Korean onto breakfast — 10 min while eating.",     "block_type": "study",    "start_time": "08:30", "duration_minutes": 40},
        {"title": "Morning with GF",      "description": "Breakfast together, plan the day.",                      "block_type": "personal", "start_time": "09:00", "duration_minutes": 60},
        {"title": "Out or At Home",       "description": "London trip, market — or staying in.",                   "block_type": "personal", "start_time": "10:00", "duration_minutes": 240},
        {"title": "Afternoon — Flexible", "description": "If home + she rests: 1-2 study blocks. Never forced.",  "block_type": "study",    "start_time": "14:00", "duration_minutes": 150},
        {"title": "Evening with GF",      "description": "Movie, dinner, quality time.",                           "block_type": "personal", "start_time": "16:30", "duration_minutes": 210},
        {"title": "Anki + Sleep Prep",    "description": "Final Korean. Earlier bed = better week.",               "block_type": "study",    "start_time": "22:00", "duration_minutes": 10},
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

PX_PER_HOUR  = 60
TOTAL_HOURS  = 24
TOTAL_HEIGHT = TOTAL_HOURS * PX_PER_HOUR
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
            rows.extend(cache.get((week_start + timedelta(days=d)).isoformat(), []))
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

def _time_to_min(t: str) -> int:
    try:
        h, m = t.strip().split(":")
        return int(h) * 60 + int(m)
    except Exception:
        return 0

def _min_to_px(m: int) -> int:
    return round(m * PX_PER_HOUR / 60)

def _dur_str(minutes: int) -> str:
    if minutes < 60:
        return f"{minutes}m"
    h, m = divmod(minutes, 60)
    return f"{h}h{m:02d}m" if m else f"{h}h"


# ─── Overlap layout ───────────────────────────────────────────────────────────

def _assign_columns(blocks: list) -> list:
    """
    Given a list of blocks sorted by start_time, assign each block a
    (col_index, total_cols) so overlapping blocks sit side-by-side.
    Returns list of (block, col_index, total_cols_in_group).
    """
    # Build intervals
    intervals = []
    for b in blocks:
        start = _time_to_min(b.get("start_time", "00:00"))
        end   = start + b.get("duration_minutes", 25)
        intervals.append((start, end, b))

    # Greedy column assignment
    col_ends = []   # tracks when each column becomes free
    assigned = []   # (block, col_index)
    for start, end, b in intervals:
        placed = False
        for ci, col_end in enumerate(col_ends):
            if start >= col_end:
                col_ends[ci] = end
                assigned.append((b, ci))
                placed = True
                break
        if not placed:
            assigned.append((b, len(col_ends)))
            col_ends.append(end)

    # Second pass: find max concurrent cols for each block's time window
    result = []
    for b, ci in assigned:
        start = _time_to_min(b.get("start_time", "00:00"))
        end   = start + b.get("duration_minutes", 25)
        # count how many blocks overlap with this one
        max_col = max(
            c for _, c in assigned
            if _time_to_min(bb.get("start_time", "00:00")) < end
            and _time_to_min(bb.get("start_time", "00:00")) + bb.get("duration_minutes", 25) > start
            for bb in [b2 for b2, c2 in assigned if c2 == c]
        ) if assigned else 0
        # simpler: total cols = max col index of any overlapping block + 1
        overlapping_cols = set()
        for b2, c2 in assigned:
            s2 = _time_to_min(b2.get("start_time", "00:00"))
            e2 = s2 + b2.get("duration_minutes", 25)
            if s2 < end and e2 > start:
                overlapping_cols.add(c2)
        total_cols = len(overlapping_cols)
        result.append((b, ci, total_cols))

    return result


# ─── Time-grid HTML ───────────────────────────────────────────────────────────

def _build_time_grid(blocks_by_date: dict, week_start: date, today: date, dark: bool) -> str:

    bg_grid   = "#161b22" if dark else "#ffffff"
    col_line  = "#30363d" if dark else "#e5e7eb"
    col_hour  = "#8b949e" if dark else "#9ca3af"
    col_hdr   = "#e6edf3" if dark else "#1a1a2e"
    col_sub   = "#8b949e" if dark else "#6b7280"
    today_hdr = "#1a2744" if dark else "#dbeafe"
    today_bdr = "#3b82f6"

    now      = datetime.now()
    now_top  = _min_to_px(now.hour * 60 + now.minute)
    show_now = (week_start <= today <= week_start + timedelta(days=6))
    today_col = today.weekday()

    # Hour labels + grid lines
    hour_labels = ""
    grid_lines  = ""
    for h in range(TOTAL_HOURS + 1):
        top = h * PX_PER_HOUR
        hour_labels += (
            f'<div style="position:absolute;top:{top}px;right:5px;font-size:.58rem;'
            f'color:{col_hour};transform:translateY(-50%);white-space:nowrap;line-height:1">'
            f'{h:02d}:00</div>'
        )
        grid_lines += (
            f'<div style="position:absolute;top:{top}px;left:0;right:0;'
            f'border-top:1px solid {col_line}"></div>'
        )
        if h < TOTAL_HOURS:
            half = top + PX_PER_HOUR // 2
            grid_lines += (
                f'<div style="position:absolute;top:{half}px;left:0;right:0;'
                f'border-top:1px dashed {col_line};opacity:.3"></div>'
            )

    # Day columns
    day_cols = ""
    for i in range(7):
        day_date   = week_start + timedelta(days=i)
        day_str    = day_date.isoformat()
        is_today   = (day_date == today)
        day_blocks = blocks_by_date.get(day_str, [])

        hdr_bg  = today_hdr if is_today else (bg_grid if dark else "#f9fafb")
        hdr_bdr = today_bdr if is_today else col_line
        dot = (f'<div style="width:5px;height:5px;background:{today_bdr};'
               f'border-radius:50%;margin:.12rem auto 0"></div>') if is_today else ""

        header = (
            f'<div style="position:sticky;top:0;z-index:10;background:{hdr_bg};'
            f'border-bottom:2px solid {hdr_bdr};padding:.3rem .1rem .22rem;'
            f'text-align:center;border-right:1px solid {col_line}">'
            f'<div style="font-size:.58rem;font-weight:700;text-transform:uppercase;'
            f'letter-spacing:.05em;color:{"#60a5fa" if is_today else col_sub}">'
            f'{DAY_SHORT[i]}</div>'
            f'<div style="font-size:.95rem;font-weight:700;line-height:1.1;'
            f'color:{"#3b82f6" if is_today else col_hdr}">'
            f'{day_date.strftime("%-d")}</div>{dot}'
            f'</div>'
        )

        now_line = ""
        if show_now and i == today_col:
            now_line = (
                f'<div style="position:absolute;top:{now_top}px;left:0;right:0;'
                f'border-top:2px solid #ef4444;z-index:6;pointer-events:none">'
                f'<div style="position:absolute;left:-3px;top:-4px;width:7px;height:7px;'
                f'background:#ef4444;border-radius:50%"></div></div>'
            )

        # Assign overlap columns
        layout = _assign_columns(day_blocks)

        blocks_html = ""
        for block, col_idx, total_cols in layout:
            top_px    = _min_to_px(_time_to_min(block.get("start_time", "00:00")))
            height_px = max(_min_to_px(block.get("duration_minutes", 25)), 18)
            btype     = block.get("block_type", "personal")
            palette   = BLOCK_COLOURS_DARK[btype] if dark else BLOCK_COLOURS[btype]
            icon      = TYPE_ICONS.get(btype, "📌")
            title     = block.get("title", "Untitled")
            is_def    = block.get("is_default", False)
            bid       = block.get("id", "")
            lock      = " 🔒" if is_def else ""

            # Width and left offset based on overlap column
            col_width_pct = 100 / total_cols
            left_pct      = col_idx * col_width_pct
            # Small gap between side-by-side blocks
            gap = 1
            left_pct_adj  = left_pct + gap / 2
            width_pct_adj = col_width_pct - gap

            if height_px >= 36:
                inner = (
                    f'<div style="font-size:.57rem;opacity:.75;margin-bottom:.06rem;'
                    f'white-space:nowrap;overflow:hidden">'
                    f'{block.get("start_time","")} · {_dur_str(block.get("duration_minutes",0))}'
                    f'</div>'
                    f'<div style="font-weight:600;font-size:.65rem;line-height:1.25;overflow:hidden;'
                    f'display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical">'
                    f'{icon} {title}{lock}</div>'
                )
            else:
                inner = (
                    f'<div style="font-weight:600;font-size:.62rem;white-space:nowrap;'
                    f'overflow:hidden;text-overflow:ellipsis">'
                    f'{icon} {title}{lock}</div>'
                )

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
                f'<div onclick="wppSelect(this)" data-block="{bdata}" '
                f'style="position:absolute;top:{top_px}px;'
                f'left:calc({left_pct_adj:.1f}% + 1px);'
                f'width:calc({width_pct_adj:.1f}% - 1px);'
                f'height:{height_px}px;'
                f'background:{palette["bg"]};border-left:3px solid {palette["border"]};'
                f'color:{palette["text"]};border-radius:3px;padding:.1rem .22rem;'
                f'overflow:hidden;cursor:pointer;z-index:4;box-sizing:border-box;'
                f'font-family:inherit;transition:filter .1s" '
                f'onmouseenter="this.style.filter=\'brightness(0.9)\'" '
                f'onmouseleave="this.style.filter=\'none\'">'
                f'{inner}</div>'
            )

        day_cols += (
            f'<div style="flex:1;min-width:0;position:relative;'
            f'border-right:1px solid {col_line}">'
            f'{header}'
            f'<div style="position:relative;height:{TOTAL_HEIGHT}px">'
            f'<div style="position:absolute;inset:0">{grid_lines}</div>'
            f'{now_line}{blocks_html}'
            f'</div></div>'
        )

    panel_bg  = "#1e293b" if dark else "#f8fafc"
    panel_bdr = "#334155" if dark else "#e2e8f0"

    return f"""
<style>
  .wpp-outer {{
    border:1px solid {col_line};border-radius:10px;
    overflow:hidden;background:{bg_grid};
    font-family:'Noto Sans KR',sans-serif;
  }}
  .wpp-scroll {{
    overflow-x:auto;overflow-y:auto;max-height:680px;
  }}
  .wpp-scroll::-webkit-scrollbar{{height:4px;width:4px}}
  .wpp-scroll::-webkit-scrollbar-thumb{{background:{col_line};border-radius:2px}}
  .wpp-inner {{display:flex;min-width:500px}}
  .wpp-tcol {{
    width:{TIME_COL_W}px;min-width:{TIME_COL_W}px;
    position:relative;background:{bg_grid};
    border-right:1px solid {col_line};flex-shrink:0;
  }}
  .wpp-tsticky {{
    position:sticky;top:0;z-index:11;
    background:{bg_grid};height:48px;
    border-bottom:2px solid {col_line};
  }}
  .wpp-tbody {{position:relative;height:{TOTAL_HEIGHT}px}}
  @media(max-width:600px){{.wpp-inner{{min-width:380px}}}}
</style>

<div class="wpp-outer">
  <div class="wpp-scroll" id="wppScroll">
    <div class="wpp-inner">
      <div class="wpp-tcol">
        <div class="wpp-tsticky"></div>
        <div class="wpp-tbody">{hour_labels}</div>
      </div>
      {day_cols}
    </div>
  </div>
</div>

<div id="wppPanel" style="display:none;margin-top:.7rem;padding:.85rem 1rem;
     background:{panel_bg};border:1px solid {panel_bdr};border-radius:10px;
     border-left:4px solid #3b82f6;font-family:inherit">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:.5rem">
    <div style="flex:1;min-width:0">
      <div id="wppPType" style="font-size:.65rem;text-transform:uppercase;
           letter-spacing:.08em;color:{col_sub};margin-bottom:.15rem"></div>
      <div id="wppPTitle" style="font-weight:700;font-size:.95rem;color:{col_hdr};margin-bottom:.12rem"></div>
      <div id="wppPTime"  style="font-size:.75rem;color:{col_sub};margin-bottom:.3rem"></div>
      <div id="wppPDesc"  style="font-size:.8rem;color:{col_hdr};line-height:1.55"></div>
    </div>
    <button onclick="document.getElementById('wppPanel').style.display='none'"
            style="background:none;border:none;cursor:pointer;font-size:1rem;
                   color:{col_sub};padding:.1rem .2rem;flex-shrink:0">✕</button>
  </div>
  <div style="margin-top:.6rem;font-size:.75rem;color:{col_sub}">
    To edit or delete this block, use the controls below the calendar.
  </div>
</div>

<script>
var _wppCur = null;
var _icons = {{"study":"📚","work":"💼","fitness":"🏃","personal":"👤","play":"🎮"}};

function wppSelect(el) {{
  _wppCur = JSON.parse(el.dataset.block.replace(/&quot;/g,'"'));
  var b = _wppCur;
  var dur = b.duration_minutes;
  var durStr = dur<60 ? dur+"m" : (dur%60===0 ? Math.floor(dur/60)+"h" : Math.floor(dur/60)+"h"+String(dur%60).padStart(2,"0")+"m");
  document.getElementById("wppPType").textContent  =
    (_icons[b.block_type]||"📌")+" "+b.block_type.charAt(0).toUpperCase()+b.block_type.slice(1)+(b.is_default?" · 🔒 WPP default":"");
  document.getElementById("wppPTitle").textContent = b.title;
  document.getElementById("wppPTime").textContent  = b.start_time+" · "+durStr;
  document.getElementById("wppPDesc").textContent  = b.description||"";
  var panel = document.getElementById("wppPanel");
  panel.style.display = "block";
  panel.scrollIntoView({{behavior:"smooth",block:"nearest"}});

  // Populate the Streamlit select + inputs below
  // Store selected block id in session for Streamlit buttons to act on
  document.getElementById("wppSelId").value  = b.id;
  document.getElementById("wppSelDay").value = b.day;
  // Trigger input event so Streamlit picks up change
  ["wppSelId","wppSelDay"].forEach(function(id){{
    var inp = document.getElementById(id);
    var ev = new Event("input",{{bubbles:true}});
    Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,"value")
      .set.call(inp, inp.value);
    inp.dispatchEvent(ev);
  }});
}}

(function(){{
  var el = document.getElementById("wppScroll");
  if(el) el.scrollTop = {_min_to_px(7*60+30)};
}})();
</script>

<!-- These two inputs are read by Streamlit for edit/delete — hidden via CSS -->
<style>
  #wppSelId, #wppSelDay {{
    position:absolute;opacity:0;pointer-events:none;height:0;padding:0;border:none;
  }}
</style>
<input id="wppSelId"  type="text" value="">
<input id="wppSelDay" type="text" value="">
"""


# ─── Add / Edit form ─────────────────────────────────────────────────────────

def render_block_form(day_str: str, existing_block: dict = None):
    is_edit = existing_block is not None
    eid     = existing_block["id"] if is_edit else "new"
    prefix  = f"cbf_{day_str}_{eid}"

    title = st.text_input("Title *",
                          value=existing_block.get("title", "") if is_edit else "",
                          key=f"{prefix}_t", placeholder="e.g. Study Block 2")
    desc  = st.text_area("Description",
                         value=existing_block.get("description", "") if is_edit else "",
                         key=f"{prefix}_d", height=68,
                         placeholder="Optional notes, reminders, context...")
    c1, c2 = st.columns(2)
    with c1:
        idx = BLOCK_TYPES.index(existing_block.get("block_type", "study")) if is_edit else 0
        btype = st.selectbox("Type", BLOCK_TYPES,
                             format_func=lambda t: f"{TYPE_ICONS[t]} {t.capitalize()}",
                             index=idx, key=f"{prefix}_bt")
    with c2:
        start = st.text_input("Start (HH:MM)",
                              value=existing_block.get("start_time", "") if is_edit else "",
                              key=f"{prefix}_s", placeholder="08:45")
    dur = st.number_input("Duration (min)", min_value=5, max_value=1440,
                          value=existing_block.get("duration_minutes", 25) if is_edit else 25,
                          step=5, key=f"{prefix}_dur")

    if st.button("💾 Save Changes" if is_edit else "➕ Add Block",
                 use_container_width=True, key=f"{prefix}_sub"):
        if not title.strip():
            st.error("Title is required.")
            return
        block = {
            "block_date": day_str, "title": title.strip(),
            "description": desc.strip(), "block_type": btype,
            "start_time": start.strip(), "duration_minutes": int(dur),
            "is_default": False,
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
    st.markdown("*Your WPP schedule — click any block to see details*")
    st.markdown("---")

    # Week nav
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

    # Load & seed
    blocks_by_date = load_blocks_for_week(week_start)
    seed_defaults_for_week(week_start, blocks_by_date)
    blocks_by_date = load_blocks_for_week(week_start)

    # Study summary bar
    total_study = sum(
        1 for i in range(7)
        for b in blocks_by_date.get((week_start + timedelta(days=i)).isoformat(), [])
        if b.get("block_type") == "study" and "Anki" not in b.get("title", "")
    )
    tmin, tmax = 8, 12
    bar_pct = min(100, round(total_study / tmax * 100))
    bar_col = "#22c55e" if total_study >= tmin else "#f59e0b" if total_study >= 4 else "#ef4444"
    st.markdown(f"""
    <div style="background:{'#161b22' if dark else '#f8fafc'};border:1px solid {card_bdr};
                border-radius:8px;padding:.55rem 1rem;margin:.4rem 0 .75rem;
                display:flex;align-items:center;gap:.9rem;flex-wrap:wrap">
      <span style="font-weight:700;font-size:.83rem;color:{text_col};white-space:nowrap">
        📊 {total_study} study sessions this week
      </span>
      <div style="flex:1;min-width:80px;background:{'#30363d' if dark else '#e5e7eb'};
                  border-radius:999px;height:6px">
        <div style="width:{bar_pct}%;height:100%;background:{bar_col};border-radius:999px"></div>
      </div>
      <span style="font-size:.73rem;color:{sub_col};white-space:nowrap">target {tmin}–{tmax}</span>
    </div>""", unsafe_allow_html=True)

    # Time grid
    st.markdown(_build_time_grid(blocks_by_date, week_start, today, dark),
                unsafe_allow_html=True)

    # ── Edit / Delete / Add controls ──────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='font-size:.78rem;color:{sub_col};margin-bottom:.5rem'>"
        f"Click a block to see its details above, then use the controls below to edit or delete it.</div>",
        unsafe_allow_html=True)

    # Build a flat list of all blocks this week for the selector
    all_blocks = []
    for i in range(7):
        d = (week_start + timedelta(days=i)).isoformat()
        for b in blocks_by_date.get(d, []):
            all_blocks.append(b)

    if all_blocks:
        block_labels = {
            f"{DAY_SHORT[date.fromisoformat(b['block_date']).weekday()]} {b.get('start_time','')} — {b['title']}": b
            for b in all_blocks
        }

        sel_col1, sel_col2, sel_col3 = st.columns([4, 1, 1])
        with sel_col1:
            selected_label = st.selectbox(
                "Select block:", list(block_labels.keys()),
                key="cal_block_sel",
                label_visibility="collapsed"
            )
        with sel_col2:
            if st.button("✏️ Edit", use_container_width=True, key="cal_edit_btn"):
                st.session_state["cal_edit_block"] = block_labels[selected_label]
                st.session_state.pop("cal_adding_day", None)
                st.rerun()
        with sel_col3:
            if st.button("🗑️ Delete", use_container_width=True, key="cal_del_btn"):
                b = block_labels[selected_label]
                delete_block(b["id"], b["block_date"])
                st.session_state.pop("cal_edit_block", None)
                st.rerun()

    # Add block
    st.markdown("<br>", unsafe_allow_html=True)
    a1, a2 = st.columns([3, 1])
    with a1:
        day_options = {
            f"{DAY_NAMES[i]}  {(week_start + timedelta(days=i)).strftime('%-d %b')}":
            (week_start + timedelta(days=i)).isoformat()
            for i in range(7)
        }
        sel_day = st.selectbox(
            "Day:", list(day_options.keys()),
            key="cal_add_day_sel",
            label_visibility="collapsed",
            index=min(today.weekday(), 6) if week_start <= today <= week_end else 0,
        )
    with a2:
        if st.button("➕ Add Block", use_container_width=True, key="cal_add_btn"):
            st.session_state["cal_adding_day"] = day_options[sel_day]
            st.session_state.pop("cal_edit_block", None)
            st.rerun()

    # Forms
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

    # Legend
    st.markdown("<br>", unsafe_allow_html=True)
    legend = "".join([
        f'<span style="background:{BLOCK_COLOURS[t]["bg"]};'
        f'border:1px solid {BLOCK_COLOURS[t]["border"]};border-radius:999px;'
        f'padding:.15rem .65rem;font-size:.71rem;color:{BLOCK_COLOURS[t]["text"]};'
        f'margin:.1rem;display:inline-block">{TYPE_ICONS[t]} {t.capitalize()}</span>'
        for t in BLOCK_TYPES
    ])
    st.markdown(
        f'<div><span style="font-size:.7rem;color:{sub_col};text-transform:uppercase;'
        f'letter-spacing:.08em">Legend: </span>{legend}'
        f'<span style="font-size:.7rem;color:{sub_col};margin-left:.4rem">🔒 = WPP default</span></div>',
        unsafe_allow_html=True)
