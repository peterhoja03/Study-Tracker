"""
AI Helper — shared Claude API module for Study Tracker.
All AI features import from here. Uses claude-haiku-4-5 by default.
"""

import json
import os
import streamlit as st


def _get_api_key() -> str:
    try:
        return st.secrets.get("ANTHROPIC_API_KEY", "") or os.environ.get("ANTHROPIC_API_KEY", "")
    except Exception:
        return os.environ.get("ANTHROPIC_API_KEY", "")


def ask_claude(system: str, user: str, model: str = "claude-haiku-4-5-20251001", max_tokens: int = 1024) -> str:
    """
    Send a single message to Claude and return the text response.
    Returns an error string on failure rather than raising.
    """
    api_key = _get_api_key()
    if not api_key:
        return "ERROR: No ANTHROPIC_API_KEY found in secrets."
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return message.content[0].text
    except Exception as e:
        return f"ERROR: {e}"


def ask_claude_json(system: str, user: str, model: str = "claude-haiku-4-5-20251001", max_tokens: int = 1024) -> dict:
    """
    Ask Claude and parse the response as JSON.
    Returns a dict. On failure returns {"error": "..."}.
    System prompt must instruct Claude to return only valid JSON.
    """
    raw = ask_claude(system, user, model, max_tokens)
    if raw.startswith("ERROR:"):
        return {"error": raw}
    try:
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("```")[1]
            if cleaned.startswith("json"):
                cleaned = cleaned[4:]
        return json.loads(cleaned.strip())
    except Exception as e:
        return {"error": f"JSON parse failed: {e}", "raw": raw}


# ─── Knowledge bank formatter ─────────────────────────────────────────────────

def format_knowledge_bank(lesson: dict) -> str:
    """
    Convert a lesson's knowledge_bank dict into a clean text block
    for use in Claude system prompts.
    """
    kb = lesson.get("knowledge_bank", {})
    if not kb:
        # Fallback: use existing lesson fields
        parts = []
        if lesson.get("learning_goals"):
            parts.append("Learning goals:\n" + "\n".join(f"- {g}" for g in lesson["learning_goals"]))
        if lesson.get("key_vocab"):
            parts.append("Key vocabulary: " + ", ".join(lesson["key_vocab"]))
        if lesson.get("active_recall_questions"):
            parts.append("Key questions:\n" + "\n".join(f"- {q}" for q in lesson["active_recall_questions"]))
        return "\n\n".join(parts)

    parts = []
    if kb.get("summary"):
        parts.append(f"Summary:\n{kb['summary']}")
    if kb.get("facts"):
        parts.append("Key facts:\n" + "\n".join(f"- {f}" for f in kb["facts"]))
    if kb.get("grammar_rules"):
        parts.append("Grammar rules:\n" + "\n".join(f"- {r}" for r in kb["grammar_rules"]))
    if kb.get("equations"):
        parts.append("Equations:\n" + "\n".join(f"- {e}" for e in kb["equations"]))
    if kb.get("vocabulary"):
        vocab_lines = []
        for v in kb["vocabulary"]:
            if isinstance(v, dict):
                vocab_lines.append(f"- {v.get('korean', v.get('term', ''))} = {v.get('english', v.get('definition', ''))}")
            else:
                vocab_lines.append(f"- {v}")
        parts.append("Vocabulary:\n" + "\n".join(vocab_lines))
    if kb.get("example_sentences"):
        ex_lines = []
        for s in kb["example_sentences"]:
            if isinstance(s, dict):
                line = f"- {s.get('korean', '')} ({s.get('english', '')})"
                if s.get("notes"):
                    line += f" — {s['notes']}"
                ex_lines.append(line)
            else:
                ex_lines.append(f"- {s}")
        parts.append("Example sentences:\n" + "\n".join(ex_lines))
    if kb.get("worked_example"):
        we = kb["worked_example"]
        if isinstance(we, dict):
            steps = "\n".join(f"  {i+1}. {s}" for i, s in enumerate(we.get("steps", [])))
            parts.append(f"Worked example:\nProblem: {we.get('problem', '')}\nSolution:\n{steps}")
    if kb.get("common_mistakes"):
        parts.append("Common mistakes to check for:\n" + "\n".join(f"- {m}" for m in kb["common_mistakes"]))
    if kb.get("spec_points"):
        parts.append("AQA spec points: " + ", ".join(kb["spec_points"]))
    if kb.get("competency"):
        parts.append(f"RAF competency being assessed: {kb['competency']}")
    if kb.get("grammar_pattern"):
        parts.append(f"Grammar pattern: {kb['grammar_pattern']}")
    return "\n\n".join(parts)


def format_expected_answers(lesson: dict) -> str:
    """Format expected_answers dict for use in Claude prompts."""
    ea = lesson.get("expected_answers", {})
    if not ea:
        return ""
    lines = ["Expected answers (for marking reference):"]
    for q, a in ea.items():
        lines.append(f"\nQ: {q}\nA: {a}")
    return "\n".join(lines)


# ─── Active Recall Marker ─────────────────────────────────────────────────────

def mark_active_recall(lesson: dict, question: str, student_answer: str) -> dict:
    """
    Mark a free-text answer against the lesson knowledge bank.
    Returns: {score, correct, gaps, focus, weakness_categories}
    """
    kb_text = format_knowledge_bank(lesson)
    ea_text = format_expected_answers(lesson)
    stream = lesson.get("id", "")[:1]
    stream_name = {"U": "Korean", "P": "Physics", "R": "RAF"}.get(stream, "General")

    system = f"""You are a strict but fair study examiner for {stream_name}.
Mark the student's answer using ONLY the knowledge bank provided below.
Do not use knowledge outside this material.

{kb_text}

{ea_text}

Return ONLY valid JSON with this exact structure:
{{
  "score": <integer 1-5>,
  "correct": "<one sentence: what was right>",
  "gaps": ["<specific gap 1>", "<specific gap 2>"],
  "focus": "<one sentence telling them exactly what to study next>",
  "weakness_categories": ["<category from: missing_fact, method_error, conceptual_confusion, aqa_language_gap, particle_error, word_order_error, conjugation_error, vocab_gap, star_gap, judgement_missing, competency_not_hit>"]
}}

Scoring: 5=complete and accurate, 4=mostly correct minor gap, 3=correct core missing details, 2=partial significant gaps, 1=major misunderstanding or mostly wrong."""

    user = f"Question: {question}\n\nStudent's answer: {student_answer}"
    return ask_claude_json(system, user, max_tokens=512)


# ─── Brain Dump Analyser ──────────────────────────────────────────────────────

def analyse_brain_dump(lesson: dict, brain_dump: str) -> dict:
    """
    Map a brain dump against the full knowledge bank.
    Returns: {covered, missing, score_pct, verdict}
    """
    kb_text = format_knowledge_bank(lesson)

    system = f"""You are analysing a student's brain dump after studying a topic.
Compare what they wrote against the knowledge bank below.
Use ONLY the knowledge bank as your reference — not general knowledge.

KNOWLEDGE BANK:
{kb_text}

Return ONLY valid JSON:
{{
  "covered": ["<item from knowledge bank they got right>"],
  "missing": ["<important item from knowledge bank they did not mention>"],
  "score_pct": <integer 0-100>,
  "verdict": "<2 sentences: overall assessment and most important gap to address>"
}}"""

    user = f"Student's brain dump:\n{brain_dump}"
    return ask_claude_json(system, user, max_tokens=768)


# ─── Feynman Explainer Check ──────────────────────────────────────────────────

def check_feynman(lesson: dict, explanation: str) -> dict:
    """
    Diagnose conceptual gaps in a Feynman-style explanation.
    Returns: {conceptual_gaps, surface_errors, verdict, weakness_categories}
    """
    kb_text = format_knowledge_bank(lesson)

    system = f"""You are checking a student's Feynman explanation for conceptual accuracy.
Your job is to find WHERE UNDERSTANDING BREAKS DOWN — not just missing facts.
A student can recite facts without understanding; the Feynman check catches this.

KNOWLEDGE BANK (source of truth):
{kb_text}

Return ONLY valid JSON:
{{
  "conceptual_gaps": ["<place where reasoning breaks down or shows misunderstanding>"],
  "surface_errors": ["<factual mistake or missing fact>"],
  "verdict": "<2 sentences: honest diagnosis of understanding level>",
  "weakness_categories": ["missing_fact", "conceptual_confusion"]
}}

Be specific. 'Vague explanation' is not useful. 'Said forces act in opposite directions but didn't mention they act on different objects' is useful."""

    user = f"Student's explanation:\n{explanation}"
    return ask_claude_json(system, user, max_tokens=512)


# ─── Show Your Working (Physics) ─────────────────────────────────────────────

def check_working(lesson: dict, working: str) -> dict:
    """
    Check physics calculation working step by step.
    Returns: {method_correct, answer_correct, errors, aqa_habits, verdict}
    """
    kb_text = format_knowledge_bank(lesson)

    system = f"""You are an AQA Physics examiner checking a student's written working.
Check METHOD as well as the final answer. Use only the knowledge bank provided.

KNOWLEDGE BANK:
{kb_text}

AQA mark scheme habits to check for:
- Equation written in symbol form before substitution
- Values substituted correctly
- Answer given with correct units
- Correct number of significant figures where relevant
- Word 'resultant' used where force is being calculated

Return ONLY valid JSON:
{{
  "method_correct": <true/false>,
  "answer_correct": <true/false>,
  "errors": ["<specific error in working>"],
  "aqa_habits": ["<AQA mark scheme habit missing or wrong>"],
  "verdict": "<2 sentences: what to fix>",
  "weakness_categories": ["method_error", "aqa_language_gap", "missing_fact"]
}}"""

    user = f"Student's working:\n{working}"
    return ask_claude_json(system, user, max_tokens=512)


# ─── Korean Writing Feedback ──────────────────────────────────────────────────

def check_korean_writing(lesson: dict, korean_text: str, english_prompt: str = "") -> dict:
    """
    Mark Korean writing against grammar rules and vocabulary.
    Returns: {corrected, errors, natural_alternatives, verdict, weakness_categories}
    """
    kb_text = format_knowledge_bank(lesson)

    system = f"""You are a Korean language teacher checking a student's written Korean.
The student is learning using How to Study Korean (HTSK).
Check ONLY against the grammar rules and vocabulary in the knowledge bank below.
Do not penalise for grammar not yet taught.

KNOWLEDGE BANK:
{kb_text}

Return ONLY valid JSON:
{{
  "corrected": "<corrected Korean sentence>",
  "errors": [{{"original": "<wrong part>", "correction": "<right part>", "rule": "<why>"}}],
  "natural_alternatives": ["<more natural phrasing if applicable>"],
  "verdict": "<2 sentences: what was good, what needs work>",
  "weakness_categories": ["particle_error", "conjugation_error", "word_order_error", "vocab_gap"]
}}

Only include weakness_categories that actually apply."""

    prompt = f"English prompt: {english_prompt}\n\nStudent's Korean: {korean_text}" if english_prompt else f"Student's Korean: {korean_text}"
    return ask_claude_json(system, prompt, max_tokens=512)


# ─── RAF Interview Practice ───────────────────────────────────────────────────

def mark_raf_answer(lesson: dict, question: str, answer: str) -> dict:
    """
    Score an RAF interview/competency answer against STAR framework.
    Returns: {scores, strengths, gaps, verdict, weakness_categories}
    """
    kb_text = format_knowledge_bank(lesson)

    system = f"""You are an RAF OASC assessor scoring a candidate's competency answer.
Score each STAR dimension 1-3 (1=weak/missing, 2=developing, 3=strong).

COMPETENCY CONTEXT:
{kb_text}

RAF Core Values to check for evidence of: Respect, Integrity, Service, Excellence.

Return ONLY valid JSON:
{{
  "scores": {{
    "situation": <1-3>,
    "task": <1-3>,
    "action": <1-3>,
    "result": <1-3>,
    "values": <1-3>
  }},
  "strengths": ["<what was done well>"],
  "gaps": ["<specific gap with actionable fix>"],
  "verdict": "<2 sentences: overall assessment and single most important improvement>",
  "weakness_categories": ["star_gap", "judgement_missing", "competency_not_hit"]
}}

The Action dimension is most important — did they explain HOW they decided and WHY, not just what happened?"""

    user = f"Question: {question}\n\nCandidate's answer: {answer}"
    return ask_claude_json(system, user, max_tokens=640)


# ─── Adaptive Review Question Generator ──────────────────────────────────────

def generate_review_questions(lesson: dict, weakness_log: list, n: int = 4) -> dict:
    """
    Generate fresh review questions weighted toward known weaknesses.
    weakness_log: list of past weakness_log rows for this lesson.
    Returns: {questions: [{question, type, targets_weakness}]}
    """
    kb_text = format_knowledge_bank(lesson)
    stream = lesson.get("id", "")[:1]
    stream_name = {"U": "Korean", "P": "Physics", "R": "RAF"}.get(stream, "General")

    # Summarise weaknesses for Claude
    weakness_summary = ""
    if weakness_log:
        all_gaps = []
        all_cats = []
        for row in weakness_log[-10:]:  # Last 10 attempts
            if isinstance(row.get("specific_gaps"), list):
                all_gaps.extend(row["specific_gaps"])
            if isinstance(row.get("weakness_categories"), list):
                all_cats.extend(row["weakness_categories"])
        if all_gaps:
            from collections import Counter
            top_gaps = [g for g, _ in Counter(all_gaps).most_common(5)]
            weakness_summary = f"Known weak areas from past attempts:\n" + "\n".join(f"- {g}" for g in top_gaps)
            if all_cats:
                top_cats = [c for c, _ in Counter(all_cats).most_common(3)]
                weakness_summary += f"\nWeakness types: {', '.join(top_cats)}"

    system = f"""You are generating review questions for a {stream_name} student.
Generate ONLY from the knowledge bank below — no outside knowledge.

KNOWLEDGE BANK:
{kb_text}

{weakness_summary}

Generate {n} questions. If weakness areas are known, 60% of questions should target those areas.
Vary question types: recall (state a fact), application (new scenario), misconception (spot the error), calculation (Physics only), translation (Korean only), feynman (explain it).

Return ONLY valid JSON:
{{
  "questions": [
    {{
      "question": "<the question text>",
      "type": "<recall|application|misconception|calculation|translation|feynman>",
      "targets_weakness": <true if targeting a known weak area, false if general>
    }}
  ]
}}"""

    user = "Generate the review questions now."
    return ask_claude_json(system, user, max_tokens=768)


# ─── Lesson Progress Analysis ─────────────────────────────────────────────────

def analyse_lesson_progress(lesson: dict, weakness_log: list) -> str:
    """
    Write a short analysis of the student's history on this specific lesson.
    Returns plain text (not JSON).
    """
    if not weakness_log:
        return "No AI-marked attempts yet for this lesson. Complete an active recall or brain dump to start building your history."

    kb_text = format_knowledge_bank(lesson)

    # Summarise the log
    attempts = len(weakness_log)
    scores = [r.get("score", 0) for r in weakness_log if r.get("score")]
    avg_score = round(sum(scores) / len(scores), 1) if scores else 0
    all_gaps = []
    for row in weakness_log:
        if isinstance(row.get("specific_gaps"), list):
            all_gaps.extend(row["specific_gaps"])

    from collections import Counter
    top_gaps = [g for g, c in Counter(all_gaps).most_common(3)] if all_gaps else []

    system = f"""You are writing a brief progress analysis for a student reviewing their history on one lesson.
Be direct and specific. 3-4 sentences maximum.

LESSON KNOWLEDGE BANK (for context):
{kb_text}"""

    summary = f"""Attempts: {attempts}
Scores: {scores if scores else 'none recorded'}
Average score: {avg_score}/5
Most frequent gaps: {top_gaps if top_gaps else 'none recorded yet'}"""

    user = f"Write a 3-4 sentence analysis of this student's progress. Be specific about what they keep missing and what they should focus on.\n\n{summary}"
    return ask_claude(system, user, max_tokens=256)


# ─── Weekly AI Analysis ───────────────────────────────────────────────────────

def generate_weekly_analysis(sessions: list, weakness_log: list, progress: dict) -> str:
    """
    Generate a frank written weekly analysis across all three streams.
    Returns plain text.
    """
    from datetime import date, timedelta
    from collections import Counter

    today = date.today()
    week_ago = (today - timedelta(days=7)).isoformat()

    # Sessions this week
    recent_sessions = [s for s in sessions if s.get("date", "") >= week_ago]
    session_count = len(recent_sessions)
    total_mins = sum(s.get("duration", 0) for s in recent_sessions)

    # Stream balance
    stream_mins = {"Korean": 0, "Physics": 0, "RAF": 0}
    for s in recent_sessions:
        lid = s.get("lesson_id", "")
        if lid.startswith("U"):
            stream_mins["Korean"] += s.get("duration", 0)
        elif lid.startswith("P"):
            stream_mins["Physics"] += s.get("duration", 0)
        elif lid.startswith("R"):
            stream_mins["RAF"] += s.get("duration", 0)

    # Weaknesses this week
    recent_weaknesses = [w for w in weakness_log if w.get("date", "") >= week_ago]
    all_gaps = []
    all_cats = []
    for w in recent_weaknesses:
        if isinstance(w.get("specific_gaps"), list):
            all_gaps.extend(w["specific_gaps"])
        if isinstance(w.get("weakness_categories"), list):
            all_cats.extend(w["weakness_categories"])

    top_gaps = [g for g, _ in Counter(all_gaps).most_common(5)] if all_gaps else []
    top_cats = [c for c, _ in Counter(all_cats).most_common(3)] if all_cats else []

    completed = sum(1 for d in progress.values() if d.get("status") == "completed")

    system = """You are a direct and honest study coach writing a weekly review for a student
studying Korean, AQA Physics, and preparing for RAF OASC selection.
Be frank, specific, and actionable. No fluff. 3-4 paragraphs.
End with exactly 3 concrete suggested sessions for tomorrow."""

    user = f"""Weekly data:
- Sessions completed: {session_count} (target: 15)
- Total study time: {total_mins} minutes
- Stream split: Korean {stream_mins['Korean']}min, Physics {stream_mins['Physics']}min, RAF {stream_mins['RAF']}min
- Target split: 40% RAF, 35% Physics, 25% Korean
- AI-marked attempts this week: {len(recent_weaknesses)}
- Most frequent gaps: {top_gaps}
- Most frequent weakness types: {top_cats}
- Total lessons completed to date: {completed}

Write the weekly analysis now."""

    return ask_claude(system, user, max_tokens=512)
