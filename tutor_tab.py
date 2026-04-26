"""
tutor_tab.py — AI Tutor Chat Tab

A persistent, per-lesson conversational tutor. Chat history is stored
in Supabase (tutor_chats table) so it survives page reloads.

Knowledge priority:
  1. Current lesson knowledge_bank
  2. Completed prior lessons' knowledge_banks (passed in as context)
  3. General Korean language knowledge (flagged to user when used)

The tutor explains concepts, answers "why" questions, gives extra
examples, and connects ideas across lessons. Practice sentence
generation is available but secondary to explanation.
"""

import streamlit as st
import json
import requests
from datetime import datetime
from db import _sb


# ─── Supabase helpers ─────────────────────────────────────────────────────────

def _load_chat(lesson_id: str) -> list:
    """Load chat history for this lesson from Supabase."""
    sb = _sb()
    if not sb:
        return st.session_state.get(f"tutor_chat_{lesson_id}", [])
    try:
        res = (
            sb.table("tutor_chats")
            .select("role, content")
            .eq("lesson_id", lesson_id)
            .order("created_at", desc=False)
            .execute()
        )
        return [{"role": r["role"], "content": r["content"]} for r in res.data]
    except Exception:
        return st.session_state.get(f"tutor_chat_{lesson_id}", [])


def _save_message(lesson_id: str, role: str, content: str):
    """Persist a single message to Supabase."""
    sb = _sb()
    if sb:
        try:
            sb.table("tutor_chats").insert({
                "lesson_id": lesson_id,
                "role": role,
                "content": content,
            }).execute()
        except Exception:
            pass
    # Also keep in session state as fallback
    key = f"tutor_chat_{lesson_id}"
    msgs = st.session_state.get(key, [])
    msgs.append({"role": role, "content": content})
    st.session_state[key] = msgs


def _clear_chat(lesson_id: str):
    """Delete all chat messages for this lesson."""
    sb = _sb()
    if sb:
        try:
            sb.table("tutor_chats").delete().eq("lesson_id", lesson_id).execute()
        except Exception:
            pass
    st.session_state.pop(f"tutor_chat_{lesson_id}", None)


# ─── Context builder ──────────────────────────────────────────────────────────

def _build_system_prompt(lesson: dict, completed_lessons: list) -> str:
    """
    Build the tutor system prompt with lesson knowledge injected.
    completed_lessons: list of lesson dicts that have been fully completed,
                       in order from earliest to most recent.
    """
    lesson_id = lesson["id"]
    lesson_title = lesson.get("title", lesson_id)

    # Current lesson knowledge
    kb = lesson.get("knowledge_bank", {})
    summary = kb.get("summary", "No summary available.")
    facts = kb.get("facts", [])
    facts_text = "\n".join(f"- {f}" for f in facts) if facts else "No specific facts listed."

    learning_goals = lesson.get("learning_goals", [])
    goals_text = "\n".join(f"- {g}" for g in learning_goals) if learning_goals else ""

    key_vocab = lesson.get("key_vocab", [])
    vocab_text = ", ".join(key_vocab) if key_vocab else "None listed."

    # Prior completed lessons summary
    prior_context = ""
    if completed_lessons:
        prior_parts = []
        for pl in completed_lessons[-10:]:  # cap at last 10 to manage token use
            pl_id = pl.get("id", "")
            pl_title = pl.get("title", pl_id)
            pl_kb = pl.get("knowledge_bank", {})
            pl_summary = pl_kb.get("summary", "")
            pl_facts = pl_kb.get("facts", [])
            if pl_summary or pl_facts:
                facts_snippet = " | ".join(pl_facts[:5]) if pl_facts else ""
                prior_parts.append(
                    f"[{pl_id}: {pl_title}]\n"
                    f"Summary: {pl_summary}\n"
                    f"Key facts: {facts_snippet}"
                )
        if prior_parts:
            prior_context = (
                "\n\n--- PREVIOUSLY COMPLETED LESSONS ---\n"
                + "\n\n".join(prior_parts)
            )

    return f"""You are a patient, clear Korean language tutor helping a student understand the content of their current lesson.

CURRENT LESSON: {lesson_id} — {lesson_title}

LESSON SUMMARY:
{summary}

KEY FACTS FROM THIS LESSON:
{facts_text}

LEARNING GOALS:
{goals_text}

KEY VOCABULARY/GRAMMAR IN THIS LESSON:
{vocab_text}
{prior_context}

--- YOUR ROLE AND RULES ---

1. KNOWLEDGE PRIORITY: Always draw first from the current lesson content above. Second, draw from the prior completed lessons listed above. Only use your general Korean language knowledge as a last resort — and when you do, clearly say something like "This goes slightly beyond what the lesson covers, but..." so the student knows.

2. MAIN PURPOSE: Help the student UNDERSTAND concepts. Explain things in different ways, use analogies, give extra examples. Be conversational and encouraging.

3. TONE: Patient, clear, friendly. Like a knowledgeable tutor sitting next to them. Not robotic. Not a wall of text — keep responses focused and digestible.

4. PRACTICE SENTENCES: You can generate practice sentences using only vocabulary the student has been exposed to (from completed lessons + current lesson). But only do this when it genuinely helps explain a concept, not as a default. If asked directly, do it — keep sentences simple and always explain them.

5. AHEAD OF LEVEL: If a student asks about something beyond their current lessons, answer briefly and flag it: "You'll cover this properly in a later lesson, but here's the short version..." Don't overwhelm them with advanced grammar they haven't reached.

6. MISCONCEPTIONS: If you spot a misunderstanding in what the student writes, gently correct it with a clear explanation of why.

7. LENGTH: Keep responses concise. One clear concept at a time. Use short paragraphs or brief bullet points only when listing things. Never write essays.

8. KOREAN SCRIPT: Use Korean characters (Hangul) where helpful — the student can read Korean from Unit 0. Always provide the English meaning alongside Korean examples.

You are not a general chatbot. Stay focused on Korean language learning within the scope of what this student has studied."""


# ─── API call ─────────────────────────────────────────────────────────────────

def _call_tutor(system_prompt: str, messages: list) -> str:
    """Call the Anthropic API and return the assistant response text."""
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={"Content-Type": "application/json"},
            json={
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 1000,
                "system": system_prompt,
                "messages": messages,
            },
        )
        data = response.json()
        if "content" in data and data["content"]:
            return data["content"][0].get("text", "Sorry, I couldn't generate a response.")
        elif "error" in data:
            return f"API error: {data['error'].get('message', 'Unknown error')}"
        return "Sorry, something went wrong. Please try again."
    except Exception as e:
        return f"Connection error: {str(e)}"


# ─── Main render function ─────────────────────────────────────────────────────

def render_tutor_tab(lesson: dict, completed_lessons: list = None):
    """
    Render the AI tutor chat tab.

    Args:
        lesson: the current lesson dict (must have knowledge_bank)
        completed_lessons: list of fully completed lesson dicts in order,
                           used to give the tutor context of prior learning.
    """
    if completed_lessons is None:
        completed_lessons = []

    lesson_id = lesson["id"]
    dark = st.session_state.get("dark_mode", False)

    # Colours
    user_bg    = "#3a5bd9" if not dark else "#3a5bd9"
    user_text  = "#ffffff"
    bot_bg     = "#f0f4ff" if not dark else "#1e2330"
    bot_border = "#d0d8f8" if not dark else "#2d3550"
    bot_text   = "#1a1a2e" if not dark else "#e6edf3"
    input_bg   = "#ffffff" if not dark else "#161b22"
    card_bg    = "#f8f9ff" if not dark else "#161b22"

    # ── Header ────────────────────────────────────────────────────────────────
    col_title, col_btn = st.columns([4, 1])
    with col_title:
        st.markdown(
            '<p style="font-size:.85rem;color:#666;margin:0 0 .5rem 0">'
            'Ask me anything about this lesson. I\'ll explain, give examples, '
            'and connect ideas to what you\'ve already covered.</p>',
            unsafe_allow_html=True,
        )
    with col_btn:
        if st.button("🗑 New chat", key=f"tutor_clear_{lesson_id}", use_container_width=True):
            st.session_state[f"tutor_confirm_clear_{lesson_id}"] = True

    # Confirm clear dialog
    if st.session_state.get(f"tutor_confirm_clear_{lesson_id}"):
        st.warning("Clear the entire chat history for this lesson?")
        cc1, cc2 = st.columns(2)
        with cc1:
            if st.button("Yes, clear it", key=f"tutor_yes_{lesson_id}", use_container_width=True):
                _clear_chat(lesson_id)
                st.session_state.pop(f"tutor_confirm_clear_{lesson_id}", None)
                st.rerun()
        with cc2:
            if st.button("Cancel", key=f"tutor_no_{lesson_id}", use_container_width=True):
                st.session_state.pop(f"tutor_confirm_clear_{lesson_id}", None)
                st.rerun()
        return

    # ── Load history ──────────────────────────────────────────────────────────
    history = _load_chat(lesson_id)

    # ── Render chat messages ──────────────────────────────────────────────────
    chat_container = st.container()
    with chat_container:
        if not history:
            st.markdown(
                f'<div style="background:{card_bg};border-radius:12px;padding:1.2rem;'
                f'text-align:center;color:#888;font-size:.88rem;margin:.5rem 0 1rem 0">'
                f'No messages yet. Ask me anything about this lesson!</div>',
                unsafe_allow_html=True,
            )
        else:
            for msg in history:
                role = msg["role"]
                content = msg["content"]
                # Escape HTML in content for safe rendering
                safe_content = (
                    content
                    .replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\n", "<br>")
                )
                if role == "user":
                    st.markdown(
                        f'<div style="display:flex;justify-content:flex-end;margin:.4rem 0">'
                        f'<div style="background:{user_bg};color:{user_text};border-radius:16px 16px 4px 16px;'
                        f'padding:.65rem 1rem;max-width:80%;font-size:.88rem;line-height:1.5">'
                        f'{safe_content}</div></div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f'<div style="display:flex;justify-content:flex-start;margin:.4rem 0">'
                        f'<div style="background:{bot_bg};color:{bot_text};border:1px solid {bot_border};'
                        f'border-radius:16px 16px 16px 4px;padding:.65rem 1rem;max-width:85%;'
                        f'font-size:.88rem;line-height:1.6">'
                        f'<span style="font-size:.7rem;font-weight:700;color:#534AB7;'
                        f'text-transform:uppercase;letter-spacing:.06em;display:block;margin-bottom:.3rem">'
                        f'Tutor</span>{safe_content}</div></div>',
                        unsafe_allow_html=True,
                    )

    # ── Suggested prompts (only shown when chat is empty) ─────────────────────
    if not history:
        st.markdown(
            '<p style="font-size:.75rem;color:#888;margin:.8rem 0 .4rem 0">'
            'Try asking:</p>',
            unsafe_allow_html=True,
        )
        suggestions = _get_suggestions(lesson)
        cols = st.columns(len(suggestions))
        for i, (col, suggestion) in enumerate(zip(cols, suggestions)):
            with col:
                if st.button(
                    suggestion,
                    key=f"tutor_sugg_{lesson_id}_{i}",
                    use_container_width=True,
                ):
                    st.session_state[f"tutor_prefill_{lesson_id}"] = suggestion

    # ── Input ─────────────────────────────────────────────────────────────────
    prefill = st.session_state.pop(f"tutor_prefill_{lesson_id}", "")

    with st.form(key=f"tutor_form_{lesson_id}", clear_on_submit=True):
        user_input = st.text_area(
            "Your question:",
            value=prefill,
            placeholder="e.g. Why does ㅇ make no sound at the start of a syllable?",
            height=80,
            label_visibility="collapsed",
            key=f"tutor_input_{lesson_id}",
        )
        submitted = st.form_submit_button(
            "Send →",
            use_container_width=True,
        )

    if submitted and user_input.strip():
        question = user_input.strip()

        # Save user message
        _save_message(lesson_id, "user", question)

        # Build API messages from full history + new question
        fresh_history = _load_chat(lesson_id)
        api_messages = [
            {"role": m["role"], "content": m["content"]}
            for m in fresh_history
        ]

        # Call API
        system_prompt = _build_system_prompt(lesson, completed_lessons)
        with st.spinner("Tutor is thinking..."):
            reply = _call_tutor(system_prompt, api_messages)

        # Save assistant reply
        _save_message(lesson_id, "assistant", reply)
        st.rerun()


# ─── Suggested starter prompts ────────────────────────────────────────────────

def _get_suggestions(lesson: dict) -> list:
    """Return 3 short suggested questions based on lesson content."""
    lesson_id = lesson.get("id", "")
    goals = lesson.get("learning_goals", [])

    # Generic fallbacks
    defaults = [
        "Can you explain this in simpler terms?",
        "Can you give me more examples?",
        "How does this connect to what I've already learned?",
    ]

    # Lesson-specific suggestions based on ID prefix
    if lesson_id.startswith("U0"):
        return [
            "Why do vowels need ㅇ in front of them?",
            "Can you show me how to build a syllable block step by step?",
            "What's the difference between horizontal and vertical vowels?",
        ]
    elif lesson_id.startswith("U1L1"):
        return [
            "Why does 이다 attach directly to the noun?",
            "What's the difference between 이것, 그것 and 저것?",
            "When do I use 나 vs 저?",
        ]
    elif lesson_id.startswith("U1L2"):
        return [
            "When should I use 이/가 instead of 는/은?",
            "Why does 있다 use 이/가 instead of 을/를?",
            "Can you show me more examples with position words?",
        ]
    elif lesson_id.startswith("U1L3"):
        return [
            "What's the difference between 좋다 and 좋아하다?",
            "Why don't Korean adjectives need 이다?",
            "How does 의 work as a possessive?",
        ]
    elif goals:
        # Use first learning goal to generate a relevant suggestion
        return [
            f"Can you explain: {goals[0][:50]}?",
            "Can you give me more examples of this?",
            "How does this connect to what I've already learned?",
        ]

    return defaults
