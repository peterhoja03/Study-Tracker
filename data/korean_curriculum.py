"""
How to Study Korean — Full Curriculum
Units 0–8 with lesson metadata, learning goals, techniques, and time estimates.
Lessons exceeding ~25 min are split into Part A / Part B.

TOPIK integration
─────────────────
Each lesson has a `topik_vocab_count` field — the approximate number of TOPIK I
vocabulary words introduced or reinforced in that lesson. Track cumulative vocab
learned against TOPIK_I_TARGET to get a second measurable progress axis alongside
the HTSK lesson number.

TOPIK_I_TARGET  : recommended word count to sit TOPIK I comfortably (Level 1–2)
TOPIK_I_FULL    : full official TOPIK I vocabulary list size

Lessons also carry `knowledge_bank` and `expected_answers` to enable AI marking,
exactly as in physics_curriculum.py.
"""

# ─── TOPIK constants ─────────────────────────────────────────────────────────
TOPIK_I_TARGET = 1200   # recommended comfortable threshold for TOPIK I exam
TOPIK_I_FULL   = 1671   # full official TOPIK I word list (Tammy Korean / NIIED)

CURRICULUM = {
    "Unit 0": {
        "title": "Learning How to Read (Hangul)",
        "level": "Absolute Beginner",
        "description": "Master the Korean alphabet (Hangul) before touching grammar.",
        "color": "#4A90D9",
        "url": "https://www.howtostudykorean.com/unit0/",
        "lessons": [
            {
                "id": "U0L1",
                "title": "The Korean Alphabet: Vowels",
                "subtitle": "ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ and more",
                "url": "https://www.howtostudykorean.com/unit0/unit0lesson1/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Recognise and write all 10 basic Korean vowels",
                    "Understand how vowels are formed with placeholder consonant ㅇ",
                    "Pronounce each vowel correctly using IPA guides",
                ],
                "techniques": ["Active Recall", "Spaced Repetition", "Writing Practice"],
                "key_vocab": ["아", "어", "오", "우", "으", "이", "애", "에", "외", "의"],
                "feynman_prompt": "Explain the difference between ㅏ and ㅓ as if teaching a 10-year-old. Use a sound analogy.",
                "active_recall_questions": [
                    "Without looking, write all 10 basic vowels from memory.",
                    "What does the placeholder consonant ㅇ do when it appears before a vowel?",
                    "Which vowel sounds like the 'a' in 'father'?",
                ],
                "resources": [
                    {"name": "HTSK Unit 0 Lesson 1", "url": "https://www.howtostudykorean.com/unit0/unit0lesson1/"},
                    {"name": "Naver Dictionary", "url": "https://dict.naver.com/"},
                ],
                "topik_vocab_count": 10,
                "knowledge_bank": {
                    "summary": (
                        "Korean has 10 basic vowels. Each is written by combining a vertical or "
                        "horizontal line with short strokes. Vowels cannot stand alone — they always "
                        "appear with the silent placeholder consonant ㅇ in front. "
                        "ㅏ = 'ah' (father), ㅓ = 'uh' (but), ㅗ = 'oh' (go), ㅜ = 'oo' (moon), "
                        "ㅡ = 'eu' (no English equivalent — flat lips), ㅣ = 'ee' (see), "
                        "ㅐ = 'eh' (bed), ㅔ = 'eh' (very similar to ㅐ), ㅚ = 'weh', ㅢ = 'ui'."
                    ),
                    "facts": [
                        "The 10 basic Korean vowels: ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ ㅐ ㅔ ㅚ ㅢ.",
                        "ㅇ is a silent placeholder used before vowels in syllable blocks.",
                        "ㅏ sounds like 'ah' as in 'father'.",
                        "ㅓ sounds like 'uh' as in 'but'.",
                        "ㅗ sounds like 'oh' as in 'go'.",
                        "ㅜ sounds like 'oo' as in 'moon'.",
                        "ㅡ has no direct English equivalent — produced with a flat, unrounded mouth.",
                        "ㅣ sounds like 'ee' as in 'see'.",
                        "ㅐ and ㅔ sound very similar — both close to 'eh' in 'bed'.",
                    ],
                },
                "expected_answers": {
                    "List all 10 basic Korean vowels.": "ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ ㅐ ㅔ ㅚ ㅢ",
                    "What does the silent consonant ㅇ do?": (
                        "It acts as a placeholder consonant when a syllable starts with a vowel. "
                        "It has no sound in this position."
                    ),
                    "How does ㅏ differ from ㅓ?": (
                        "ㅏ is a bright 'ah' sound (like 'father'). "
                        "ㅓ is a darker 'uh' sound (like 'but'). "
                        "ㅏ has the short stroke to the right; ㅓ has it to the left."
                    ),
                },
            },
            {
                "id": "U0L2",
                "title": "The Korean Alphabet: Consonants",
                "subtitle": "ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ",
                "url": "https://www.howtostudykorean.com/unit0/0-lesson-2/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Recognise and write all 14 basic Korean consonants",
                    "Understand aspirated vs. plain consonants",
                    "Combine consonants with vowels to form syllable blocks",
                ],
                "techniques": ["Active Recall", "Writing Practice", "Pattern Recognition"],
                "key_vocab": ["가", "나", "다", "라", "마", "바", "사", "자", "차", "카", "타", "파", "하"],
                "feynman_prompt": "Describe the difference between ㄱ and ㅋ — what makes ㅋ 'aspirated'?",
                "active_recall_questions": [
                    "Write all 14 basic consonants from memory.",
                    "How do you form the syllable block '나'?",
                    "Which consonant is silent at the start of a syllable?",
                ],
                "resources": [
                    {"name": "HTSK Unit 0 Lesson 2", "url": "https://www.howtostudykorean.com/unit0/0-lesson-2/"},
                    {"name": "Hangul Practice Sheets", "url": "https://www.google.com/search?q=hangul+practice+sheets+pdf+free"},
                ],
                "topik_vocab_count": 14,
                "knowledge_bank": {
                    "summary": (
                        "Korean has 14 basic consonants. Each has a plain, aspirated, or tense version. "
                        "Plain consonants: ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅈ ㅎ. "
                        "Aspirated (extra breath): ㅋ ㅌ ㅍ ㅊ. "
                        "Consonants combine with vowels to form syllable blocks. "
                        "ㅇ is silent at the start of a syllable but sounds like 'ng' when it appears as a final consonant."
                    ),
                    "facts": [
                        "14 basic consonants: ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ.",
                        "Aspirated consonants: ㅋ (k+h), ㅌ (t+h), ㅍ (p+h), ㅊ (ch+h).",
                        "ㅇ is silent at the start; sounds like 'ng' as a final consonant.",
                        "Syllable blocks are always C+V or C+V+C.",
                        "ㄹ sounds like a flap between 'r' and 'l'.",
                    ],
                },
                "expected_answers": {
                    "List all 14 basic Korean consonants.": "ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ",
                    "What makes an aspirated consonant different?": (
                        "Aspirated consonants (ㅋ ㅌ ㅍ ㅊ) are produced with a noticeable puff of air, "
                        "like placing a hand in front of your mouth and feeling breath. Their plain "
                        "counterparts (ㄱ ㄷ ㅂ ㅈ) have no such burst."
                    ),
                    "How is the syllable block '나' formed?": (
                        "ㄴ (consonant) + ㅏ (vowel) = 나. The consonant goes on the left, the vowel on the right."
                    ),
                },
            },
            {
                "id": "U0L3",
                "title": "Syllable Blocks & Final Consonants (받침)",
                "subtitle": "How syllables are stacked + reading flow",
                "url": "https://www.howtostudykorean.com/unit0/unit-0-lesson-3/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Understand how Korean syllables are structured as blocks",
                    "Read and write syllables with final consonants (받침)",
                    "Practice reading full words using blocks",
                ],
                "techniques": ["Active Recall", "Pattern Recognition", "Reading Practice"],
                "key_vocab": ["한", "국", "어", "학", "교", "선", "생", "님", "물", "밥"],
                "feynman_prompt": "Draw and explain the 3 possible syllable block structures (C+V, C+V+C, V only).",
                "active_recall_questions": [
                    "What are the 3 syllable block structures in Korean?",
                    "How is '학' broken down into its components?",
                    "Read aloud: 한국어 학교",
                ],
                "resources": [
                    {"name": "HTSK Unit 0 Lesson 3", "url": "https://www.howtostudykorean.com/unit0/unit-0-lesson-3/"},
                    {"name": "Pronunciation Tips", "url": "https://www.howtostudykorean.com/unit0/197-2/"},
                ],
                "topik_vocab_count": 20,
                "knowledge_bank": {
                    "summary": (
                        "Every Korean syllable is written as a block, not linearly. "
                        "Three block structures exist: (1) C+V — consonant left/top, vowel right/below; "
                        "(2) C+V+C — same but with a final consonant (받침) underneath; "
                        "(3) V only — vowel with silent ㅇ placeholder. "
                        "받침 is the term for the final consonant in a block."
                    ),
                    "facts": [
                        "Three syllable block structures: C+V, C+V+C, and vowel-only (ㅇ+V).",
                        "받침 = final consonant at the bottom of a syllable block.",
                        "한 = ㅎ + ㅏ + ㄴ (C+V+C structure).",
                        "아 = ㅇ + ㅏ (silent ㅇ + vowel).",
                        "Syllable blocks are always square in appearance — Korean is never written linearly.",
                    ],
                },
                "expected_answers": {
                    "What are the 3 syllable block structures in Korean?": (
                        "1. C+V (consonant + vowel, e.g. 나). "
                        "2. C+V+C (consonant + vowel + final consonant, e.g. 한). "
                        "3. V only — written as silent ㅇ + vowel (e.g. 아)."
                    ),
                    "How is '학' broken down?": (
                        "ㅎ (initial consonant) + ㅏ (vowel) + ㄱ (받침 / final consonant). "
                        "Structure: C+V+C."
                    ),
                    "What is 받침?": "받침 is the final consonant written at the bottom of a Korean syllable block.",
                },
            },
            {
                "id": "U0L4",
                "title": "Pronunciation Rules & Double Consonants",
                "subtitle": "ㄲ ㄸ ㅃ ㅆ ㅉ + key pronunciation shifts",
                "url": "https://www.howtostudykorean.com/unit0/197-2/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Learn the 5 double (tense) consonants",
                    "Understand 4 key pronunciation rules (linking, nasalisation, etc.)",
                    "Read any Hangul text confidently",
                ],
                "techniques": ["Active Recall", "Listening Practice", "Feynman Technique"],
                "key_vocab": ["까", "따", "빠", "싸", "짜", "있다", "없다", "닭", "국물"],
                "feynman_prompt": "Explain why '국민' is pronounced '궁민' — teach the nasalisation rule simply.",
                "active_recall_questions": [
                    "List the 5 tense consonants.",
                    "How does the pronunciation of ㄱ change before ㄴ or ㅁ?",
                    "Read this word: 읽다 — what sound does ㄺ make at the end?",
                ],
                "resources": [
                    {"name": "HTSK Pronunciation Tips", "url": "https://www.howtostudykorean.com/unit0/197-2/"},
                    {"name": "Quick Reference Chart", "url": "https://www.howtostudykorean.com/unit0/reading-quick-reference/"},
                ],
                "topik_vocab_count": 10,
                "knowledge_bank": {
                    "summary": (
                        "5 tense (doubled) consonants: ㄲ ㄸ ㅃ ㅆ ㅉ — produced with a tense throat, "
                        "no aspiration. Key pronunciation rules: "
                        "(1) Linking — a 받침 before a vowel moves to the next syllable (e.g. 한국어 → 한구거). "
                        "(2) Nasalisation — ㄱ/ㄷ/ㅂ before ㄴ/ㅁ become ㅇ/ㄴ/ㅁ (e.g. 국민 → 궁민). "
                        "(3) Aspiration — ㄱ/ㄷ/ㅂ/ㅈ + ㅎ merge into ㅋ/ㅌ/ㅍ/ㅊ. "
                        "(4) ㄹ assimilation — ㄹ next to ㄴ makes both ㄹ."
                    ),
                    "facts": [
                        "5 tense consonants: ㄲ ㄸ ㅃ ㅆ ㅉ.",
                        "Linking rule: 받침 + vowel → 받침 sound moves to next syllable.",
                        "Nasalisation: ㄱ→ㅇ, ㄷ→ㄴ, ㅂ→ㅁ before nasal consonants ㄴ/ㅁ.",
                        "국민 is pronounced 궁민 (nasalisation of ㄱ before ㅁ).",
                        "읽다 — the ㄺ cluster: the ㄱ is silent; pronounced 일다.",
                    ],
                },
                "expected_answers": {
                    "List the 5 tense consonants.": "ㄲ ㄸ ㅃ ㅆ ㅉ",
                    "Why is 국민 pronounced 궁민?": (
                        "Nasalisation rule: ㄱ before the nasal consonant ㅁ becomes ㅇ. "
                        "So 국 → 궁 in speech."
                    ),
                    "What is the linking rule in Korean pronunciation?": (
                        "When a syllable ends in a 받침 and the next syllable starts with the silent ㅇ, "
                        "the 받침 sound moves forward and is pronounced as the initial consonant of the next syllable. "
                        "Example: 한국어 → pronounced 한구거."
                    ),
                },
            },
        ],
    },

    "Unit 1": {
        "title": "Basic Korean Grammar",
        "level": "Beginner",
        "description": "Core sentence structure, particles, and fundamental verbs (Lessons 1–25).",
        "color": "#27AE60",
        "url": "https://www.howtostudykorean.com/unit1/",
        "lessons": [
            {
                "id": "U1L1",
                "title": "이다 — 'To Be' + Sentence Structure",
                "subtitle": "Subject + Object + Verb order; 이다 conjugation",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Understand Korean SOV sentence structure",
                    "Use 이다 (to be) in present tense formal/informal speech",
                    "Learn 20 core nouns from this lesson's vocabulary",
                ],
                "techniques": ["Active Recall", "Sentence Building", "Spaced Repetition"],
                "key_vocab": ["이다", "사람", "남자", "여자", "선생님", "학생", "친구", "나라", "한국", "영국"],
                "feynman_prompt": "Explain Korean sentence order to someone who only knows English. Use one example sentence.",
                "active_recall_questions": [
                    "Translate: 'I am a student' → Korean",
                    "What is the formal ending for 이다 in present tense?",
                    "What is the informal polite ending for 이다?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 1–8", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/"},
                    {"name": "Anki HTSK Deck", "url": "https://www.howtostudykorean.com/anki/"},
                ],
                "topik_vocab_count": 40,
                "knowledge_bank": {
                    "summary": (
                        "Korean sentence order is Subject–Object–Verb (SOV), opposite to English. "
                        "이다 means 'to be' and attaches directly to the noun. "
                        "Formal present: noun + 입니다. Informal polite: noun + 이에요 (after consonant) or 예요 (after vowel). "
                        "Example: 저는 학생이에요 = I am a student."
                    ),
                    "facts": [
                        "Korean sentence order: Subject → Object → Verb (SOV).",
                        "이다 = to be. Attaches to the preceding noun.",
                        "Formal present tense of 이다: 입니다.",
                        "Informal polite present: 이에요 (after consonant), 예요 (after vowel).",
                        "저 = I/me (formal/humble). 나 = I/me (casual).",
                        "학생 = student. 선생님 = teacher. 사람 = person.",
                        "한국 = Korea. 영국 = England.",
                    ],
                    "grammar_rules": [
                        "SOV order: 저는 밥을 먹어요 (I rice eat = I eat rice).",
                        "이다 after consonant: 학생이에요.",
                        "이다 after vowel: 의사예요.",
                    ],
                },
                "expected_answers": {
                    "Translate: 'I am a student.'": "저는 학생이에요. (informal polite) / 저는 학생입니다. (formal)",
                    "What is Korean sentence order?": "Subject – Object – Verb (SOV).",
                    "What is the informal polite ending for 이다 after a consonant?": "이에요",
                    "What is the informal polite ending for 이다 after a vowel?": "예요",
                },
            },
            {
                "id": "U1L2",
                "title": "Subject & Topic Particles: 이/가 and 은/는",
                "subtitle": "The difference that confuses every beginner",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Attach 이/가 (subject particle) correctly after vowels and consonants",
                    "Attach 은/는 (topic particle) correctly",
                    "Understand the conceptual difference between topic and subject",
                ],
                "techniques": ["Active Recall", "Contrast Drilling", "Feynman Technique"],
                "key_vocab": ["이/가", "은/는", "저", "나", "그것", "이것", "저것", "고양이", "개", "책"],
                "feynman_prompt": "Explain the difference between 이/가 and 은/는 using two sentences about the same object.",
                "active_recall_questions": [
                    "Add the correct particle: 나___ 학생이에요.",
                    "When do you use 이 vs 가?",
                    "Translate: 'As for me, I am Korean.'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 1–8", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/"},
                ],
                "topik_vocab_count": 30,
                "knowledge_bank": {
                    "summary": (
                        "이/가 = subject particle (marks the grammatical subject of the sentence). "
                        "은/는 = topic particle (marks what the sentence is *about*, often implying contrast or new topic). "
                        "이 and 은 are used after consonants; 가 and 는 after vowels. "
                        "은/는 often implies 'as for X' or subtle contrast. 이/가 is more neutral."
                    ),
                    "facts": [
                        "이/가 = subject particle. 이 after consonant, 가 after vowel.",
                        "은/는 = topic particle. 은 after consonant, 는 after vowel.",
                        "은/는 can imply contrast: 저는 한국 사람이에요 = As for me, I am Korean.",
                        "이/가 highlights new information; 은/는 marks established or contrasted topics.",
                        "저 ends in a vowel → 저는. 학생 ends in ㅇ (consonant) → 학생이.",
                    ],
                    "grammar_rules": [
                        "After consonant: 이 (subject), 은 (topic). E.g. 학생이, 학생은.",
                        "After vowel: 가 (subject), 는 (topic). E.g. 저가, 저는.",
                    ],
                },
                "expected_answers": {
                    "When do you use 이 vs 가?": (
                        "이 attaches to nouns ending in a consonant. 가 attaches to nouns ending in a vowel. "
                        "Both mark the grammatical subject."
                    ),
                    "What is the conceptual difference between 이/가 and 은/는?": (
                        "이/가 marks the subject of the action — neutral, introduces new info. "
                        "은/는 marks the topic of the sentence — implies contrast or 'as for X'."
                    ),
                    "Add the correct particle: 나___ 학생이에요.": "나는 학생이에요. (나 ends in vowel → 는)",
                },
            },
            {
                "id": "U1L3",
                "title": "Object Particle 을/를 & Negation with 안",
                "subtitle": "Direct objects + making sentences negative",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Attach 을/를 correctly to nouns",
                    "Negate verbs using 안",
                    "Build simple S+O+V sentences",
                ],
                "techniques": ["Sentence Building", "Active Recall", "Spaced Repetition"],
                "key_vocab": ["을/를", "안", "먹다", "마시다", "보다", "사다", "읽다", "쓰다", "물", "밥"],
                "feynman_prompt": "Give 3 example sentences showing 을/를, then negate each one with 안.",
                "active_recall_questions": [
                    "Add the correct particle: 밥___ 먹어요.",
                    "Negate: '물을 마셔요' using 안.",
                    "Translate: 'I don't read books.'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 1–8", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/"},
                ],
                "topik_vocab_count": 35,
                "knowledge_bank": {
                    "summary": (
                        "을/를 = object particle. Marks the direct object of a verb. "
                        "을 after consonant, 를 after vowel. "
                        "안 = negation prefix. Placed directly before the verb to negate it. "
                        "Structure: Subject + Object + 안 + Verb."
                    ),
                    "facts": [
                        "을/를 = object particle. 을 after consonant, 를 after vowel.",
                        "안 negates a verb: 먹어요 (eat) → 안 먹어요 (don't eat).",
                        "먹다 = to eat. 마시다 = to drink. 보다 = to see/watch. 읽다 = to read.",
                        "밥 = rice/meal. 물 = water. 책 = book.",
                    ],
                    "grammar_rules": [
                        "Object particle: 밥을 먹어요 (eat rice). 물을 마셔요 (drink water).",
                        "Negation: 안 + verb stem + conjugation. E.g. 안 먹어요.",
                    ],
                },
                "expected_answers": {
                    "Add the correct particle: 밥___ 먹어요.": "밥을 먹어요. (밥 ends in consonant → 을)",
                    "Negate: '물을 마셔요' using 안.": "물을 안 마셔요.",
                    "Translate: 'I don't read books.'": "저는 책을 안 읽어요.",
                },
            },
            {
                "id": "U1L4",
                "title": "Verbs: Present Tense Conjugation",
                "subtitle": "ㅏ/ㅗ → 아요 | all others → 어요",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Conjugate regular verbs into informal polite present tense",
                    "Apply the vowel harmony rule (아요 vs 어요)",
                    "Conjugate 하다 verbs using 해요",
                ],
                "techniques": ["Conjugation Drilling", "Active Recall", "Pattern Recognition"],
                "key_vocab": ["가다", "오다", "자다", "일하다", "공부하다", "좋아하다", "싫어하다", "알다", "모르다", "살다"],
                "feynman_prompt": "Explain the 아요/어요 rule. Why does 가다 become 가요 and 먹다 become 먹어요?",
                "active_recall_questions": [
                    "Conjugate: 가다 → ?",
                    "Conjugate: 먹다 → ?",
                    "Conjugate: 공부하다 → ?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 1–8", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/"},
                    {"name": "Korean Conjugation Reference", "url": "https://www.howtostudykorean.com/conjugation/purchase/"},
                ],
                "topik_vocab_count": 40,
                "knowledge_bank": {
                    "summary": (
                        "Informal polite present tense is formed by taking the verb stem and adding 아요 or 어요. "
                        "Vowel harmony rule: if the last vowel of the stem is ㅏ or ㅗ → add 아요. "
                        "All other stems → add 어요. "
                        "하다 verbs are irregular: 하다 → 해요 (not 하아요)."
                    ),
                    "facts": [
                        "Stem vowel ㅏ or ㅗ → add 아요. E.g. 가다 → 가요, 오다 → 와요.",
                        "All other stem vowels → add 어요. E.g. 먹다 → 먹어요.",
                        "하다 → 해요 (irregular — most common verb pattern).",
                        "공부하다 → 공부해요. 일하다 → 일해요. 좋아하다 → 좋아해요.",
                        "가다 = to go. 오다 = to come. 자다 = to sleep. 알다 = to know.",
                    ],
                    "grammar_rules": [
                        "Stem ends in ㅏ/ㅗ → 아요: 가 + 아요 = 가요 (ㅏ+ㅏ contract).",
                        "Other stems → 어요: 먹 + 어요 = 먹어요.",
                        "하다 → 해요 (always irregular).",
                    ],
                },
                "expected_answers": {
                    "Conjugate: 가다 → ?": "가요 (stem ㅏ → 아요, contracts to 가요)",
                    "Conjugate: 먹다 → ?": "먹어요 (stem ㅓ → 어요)",
                    "Conjugate: 공부하다 → ?": "공부해요 (하다 → 해요)",
                },
            },
            {
                "id": "U1L5",
                "title": "Past Tense + 있다/없다",
                "subtitle": "았/었어요 endings + existence verbs",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Form the informal polite past tense with 았/었어요",
                    "Use 있다 (to exist/have) and 없다 (to not exist/not have)",
                    "Distinguish 이다 past tense from regular verb past tense",
                ],
                "techniques": ["Active Recall", "Timeline Drilling", "Spaced Repetition"],
                "key_vocab": ["있다", "없다", "았어요", "었어요", "먹었어요", "갔어요", "했어요", "봤어요", "왔어요", "살았어요"],
                "feynman_prompt": "Explain past tense formation with two verbs: one with ㅏ/ㅗ stem, one without.",
                "active_recall_questions": [
                    "Convert to past tense: 가요 → ?",
                    "Convert to past tense: 먹어요 → ?",
                    "Translate: 'There is no water.' using 없다",
                ],
                "resources": [
                    {"name": "HTSK Lessons 1–8", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/"},
                ],
                "topik_vocab_count": 35,
                "knowledge_bank": {
                    "summary": (
                        "Past tense is formed by adding 았어요 (after ㅏ/ㅗ stems) or 었어요 (all other stems). "
                        "하다 → 했어요. "
                        "있다 = there is / to have. 없다 = there is not / to not have. "
                        "These are the most important existence verbs in Korean."
                    ),
                    "facts": [
                        "Past tense: stem ㅏ/ㅗ + 았어요. E.g. 가다 → 갔어요.",
                        "Past tense: other stems + 었어요. E.g. 먹다 → 먹었어요.",
                        "하다 → 했어요 (irregular past).",
                        "있다 = to exist / to have. 없다 = to not exist / to not have.",
                        "있어요 (present). 있었어요 (past). 없어요 (present). 없었어요 (past).",
                    ],
                    "grammar_rules": [
                        "Past: ㅏ/ㅗ stem + 았어요: 가 + 았어요 = 갔어요 (contraction).",
                        "Past: other stem + 었어요: 먹 + 었어요 = 먹었어요.",
                        "하다 past: 했어요.",
                    ],
                },
                "expected_answers": {
                    "Convert to past tense: 가요 → ?": "갔어요",
                    "Convert to past tense: 먹어요 → ?": "먹었어요",
                    "Translate: 'There is no water.'": "물이 없어요.",
                },
            },
            {
                "id": "U1L6",
                "title": "Location Particles: 에 and 에서",
                "subtitle": "Direction/existence vs. action location",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use 에 for location of existence and direction",
                    "Use 에서 for location where an action takes place",
                    "Combine location particles with 있다/없다 and action verbs",
                ],
                "techniques": ["Contrast Drilling", "Active Recall", "Sentence Building"],
                "key_vocab": ["에", "에서", "학교", "집", "공원", "도서관", "가게", "병원", "역", "카페"],
                "feynman_prompt": "Give two sentences — one using 에 and one using 에서 — about the same location. Explain the difference.",
                "active_recall_questions": [
                    "Translate: 'I study at the library.' (에 or 에서?)",
                    "Translate: 'I go to school.'",
                    "Translate: 'There is a cat in the house.'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 1–8", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/"},
                ],
                "topik_vocab_count": 30,
                "knowledge_bank": {
                    "summary": (
                        "에 and 에서 are both location particles but serve different purposes. "
                        "에 marks: (1) the location where something exists (있다/없다), "
                        "(2) the destination of movement verbs (가다, 오다). "
                        "에서 marks the location where an action actively takes place."
                    ),
                    "facts": [
                        "에 = location of existence or direction of movement.",
                        "에서 = location where an action takes place.",
                        "학교에 있어요 = I am at school (existence → 에).",
                        "학교에서 공부해요 = I study at school (action → 에서).",
                        "학교에 가요 = I go to school (movement/direction → 에).",
                    ],
                    "grammar_rules": [
                        "있다/없다 + 에: 집에 있어요 (I am at home).",
                        "Movement verbs + 에: 학교에 가요 (I go to school).",
                        "Action verbs + 에서: 카페에서 일해요 (I work at the café).",
                    ],
                },
                "expected_answers": {
                    "Translate: 'I study at the library.'": "도서관에서 공부해요. (action → 에서)",
                    "Translate: 'I go to school.'": "학교에 가요. (movement → 에)",
                    "Translate: 'There is a cat in the house.'": "집에 고양이가 있어요. (existence → 에)",
                },
            },
            {
                "id": "U1L7",
                "title": "와/과, 하고, (이)랑 — 'And' Particles",
                "subtitle": "Connecting nouns + and/with",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use 와/과 to connect nouns (formal)",
                    "Use 하고 to connect nouns (neutral)",
                    "Use (이)랑 to connect nouns (informal)",
                ],
                "techniques": ["Active Recall", "Register Awareness", "Sentence Building"],
                "key_vocab": ["와", "과", "하고", "이랑", "랑", "빵", "우유", "커피", "차", "과일"],
                "feynman_prompt": "Explain the 3 ways to say 'and' between nouns. Which is most common in daily speech?",
                "active_recall_questions": [
                    "Connect: '빵' and '우유' using all three connectors.",
                    "Which connector is most formal?",
                    "When do you use 이랑 vs 랑?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 1–8", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/"},
                ],
                "topik_vocab_count": 25,
                "knowledge_bank": {
                    "summary": (
                        "Korean has three ways to say 'and' between nouns, varying by formality. "
                        "와/과 = formal written. 하고 = neutral spoken. (이)랑 = informal/casual. "
                        "All three also mean 'with' in the sense of doing something together with someone."
                    ),
                    "facts": [
                        "와/과: 와 after vowel, 과 after consonant. Formal.",
                        "하고: neutral, common in speech. Same form regardless of final sound.",
                        "(이)랑: 랑 after vowel, 이랑 after consonant. Informal/casual.",
                        "빵하고 우유 = bread and milk (neutral). 빵이랑 우유 = bread and milk (casual).",
                    ],
                    "grammar_rules": [
                        "Formal: 빵과 우유 (빵 ends in consonant → 과).",
                        "Neutral: 빵하고 우유.",
                        "Casual: 빵이랑 우유 (빵 ends in consonant → 이랑).",
                    ],
                },
                "expected_answers": {
                    "Connect '빵' and '우유' using all three connectors.": (
                        "Formal: 빵과 우유. Neutral: 빵하고 우유. Casual: 빵이랑 우유."
                    ),
                    "Which connector is most formal?": "와/과",
                    "When do you use 이랑 vs 랑?": "이랑 after a consonant-ending noun; 랑 after a vowel-ending noun.",
                },
            },
            {
                "id": "U1L8",
                "title": "Possessive 의 + Numbers (Native & Sino-Korean)",
                "subtitle": "Two number systems used for different things",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Use 의 to show possession",
                    "Count 1–10 in both Native Korean and Sino-Korean",
                    "Know when to use each number system",
                ],
                "techniques": ["Spaced Repetition", "Active Recall", "Association"],
                "key_vocab": ["의", "하나", "둘", "셋", "일", "이", "삼", "사", "살", "번"],
                "feynman_prompt": "Explain why Korean has two number systems. Give one real-life example for each.",
                "active_recall_questions": [
                    "Count 1–5 in Sino-Korean.",
                    "Count 1–5 in Native Korean.",
                    "Which system is used for ages? Which for floors of a building?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 1–8", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/"},
                ],
                "topik_vocab_count": 40,
                "knowledge_bank": {
                    "summary": (
                        "의 = possessive particle ('s). Often dropped in casual speech. "
                        "Korean has two number systems: Native Korean (하나, 둘, 셋...) and Sino-Korean (일, 이, 삼...). "
                        "Native Korean: ages, hours, counting general items with counters. "
                        "Sino-Korean: dates, minutes, money, phone numbers, floors."
                    ),
                    "facts": [
                        "의 = possessive. 나의 책 = my book (often spoken as 내 책).",
                        "Native Korean 1–10: 하나 둘 셋 넷 다섯 여섯 일곱 여덟 아홉 열.",
                        "Sino-Korean 1–10: 일 이 삼 사 오 육 칠 팔 구 십.",
                        "Ages use Native Korean: 스물한 살 (21 years old).",
                        "Months use Sino-Korean: 삼월 = March (3rd month).",
                        "Hours use Native Korean: 세 시 = 3 o'clock.",
                        "Minutes use Sino-Korean: 삼십 분 = 30 minutes.",
                    ],
                },
                "expected_answers": {
                    "Count 1–5 in Sino-Korean.": "일, 이, 삼, 사, 오",
                    "Count 1–5 in Native Korean.": "하나, 둘, 셋, 넷, 다섯",
                    "Which number system is used for ages? Which for floors?": (
                        "Ages: Native Korean (스물 살 = 20 years old). "
                        "Floors: Sino-Korean (삼 층 = 3rd floor)."
                    ),
                },
            },
            # Lessons 9–16
            {
                "id": "U1L9",
                "title": "Counters + Telling the Time",
                "subtitle": "개, 명, 마리 + o'clock expressions",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Use common counters: 개 (things), 명 (people), 마리 (animals)",
                    "Tell the time using Native Korean hours + Sino-Korean minutes",
                    "Ask and answer 'What time is it?'",
                ],
                "techniques": ["Active Recall", "Real-life Application", "Spaced Repetition"],
                "key_vocab": ["개", "명", "마리", "시", "분", "시간", "지금", "몇", "오전", "오후"],
                "feynman_prompt": "Explain how to say '3:45 PM' in Korean step by step.",
                "active_recall_questions": [
                    "How do you say '5 animals'?",
                    "How do you say '2:30'?",
                    "Ask 'What time is it?' in Korean.",
                ],
                "resources": [
                    {"name": "HTSK Lessons 9–16", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/"},
                ],
                "topik_vocab_count": 35,
                "knowledge_bank": {
                    "summary": (
                        "Counters follow the number and specify what is being counted. "
                        "개 = general objects. 명 = people (neutral). 마리 = animals. 권 = books. 잔 = cups. "
                        "Telling the time: hours use Native Korean numbers + 시; "
                        "minutes use Sino-Korean numbers + 분."
                    ),
                    "facts": [
                        "개 = counter for general objects. 사과 세 개 = 3 apples.",
                        "명 = counter for people. 사람 두 명 = 2 people.",
                        "마리 = counter for animals. 고양이 한 마리 = 1 cat.",
                        "시 = o'clock (Native Korean hours). 세 시 = 3 o'clock.",
                        "분 = minutes (Sino-Korean). 삼십 분 = 30 minutes.",
                        "지금 몇 시예요? = What time is it now?",
                        "오전 = AM. 오후 = PM.",
                    ],
                },
                "expected_answers": {
                    "How do you say '5 animals'?": "동물 다섯 마리 (Native Korean 5 + animal counter 마리)",
                    "How do you say '2:30'?": "두 시 삼십 분 (Native Korean 2 + 시, Sino-Korean 30 + 분)",
                    "Ask 'What time is it?' in Korean.": "지금 몇 시예요?",
                },
            },
            {
                "id": "U1L10",
                "title": "Days, Months & Dates",
                "subtitle": "Days of the week, months, and saying dates",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Name all 7 days of the week",
                    "Name all 12 months using Sino-Korean numbers",
                    "State a full date in Korean",
                ],
                "techniques": ["Spaced Repetition", "Active Recall", "Chunking"],
                "key_vocab": ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일", "월", "일", "년"],
                "feynman_prompt": "State your birthday fully in Korean. Walk through the logic of each part.",
                "active_recall_questions": [
                    "What is 'Wednesday' in Korean?",
                    "How do you say 'March 15th'?",
                    "Translate: 'Today is Tuesday, April 14th.'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 9–16", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/"},
                ],
                "topik_vocab_count": 30,
                "knowledge_bank": {
                    "summary": (
                        "Days of the week follow a pattern based on the five elements + sun + moon. "
                        "Months are Sino-Korean numbers + 월. Dates are Sino-Korean numbers + 일. "
                        "Full date format: year 년 + month 월 + date 일 + day 요일."
                    ),
                    "facts": [
                        "월요일 Mon, 화요일 Tue, 수요일 Wed, 목요일 Thu, 금요일 Fri, 토요일 Sat, 일요일 Sun.",
                        "Months: 일월(Jan) 이월(Feb) 삼월(Mar) 사월(Apr) 오월(May) 유월(Jun) 칠월(Jul) 팔월(Aug) 구월(Sep) 시월(Oct) 십일월(Nov) 십이월(Dec).",
                        "Note: June = 유월 (not 육월), October = 시월 (not 십월) — irregular.",
                        "Date format: 이천이십육년 사월 이십일일 월요일.",
                    ],
                },
                "expected_answers": {
                    "What is 'Wednesday' in Korean?": "수요일",
                    "How do you say 'March 15th'?": "삼월 십오일",
                    "Translate: 'Today is Tuesday, April 14th.'": "오늘은 사월 십사일 화요일이에요.",
                },
            },
            {
                "id": "U1L11",
                "title": "Want To: ~고 싶다",
                "subtitle": "Expressing desires and wishes",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Attach ~고 싶다 to verb stems to express wanting",
                    "Use the ~고 싶어하다 form for third-person desires",
                    "Combine with vocabulary to make natural sentences",
                ],
                "techniques": ["Active Recall", "Sentence Building", "Feynman Technique"],
                "key_vocab": ["고 싶다", "고 싶어요", "먹고 싶어요", "가고 싶어요", "보고 싶어요", "하고 싶어요", "자고 싶어요", "사고 싶어요"],
                "feynman_prompt": "Explain how ~고 싶다 works using an analogy to an English structure.",
                "active_recall_questions": [
                    "Translate: 'I want to eat Korean food.'",
                    "Translate: 'She wants to go to Korea.' (use 싶어하다)",
                    "What is the past tense of 고 싶다?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 9–16", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/"},
                ],
                "topik_vocab_count": 20,
                "knowledge_bank": {
                    "summary": (
                        "~고 싶다 attaches to a verb stem to express wanting to do something. "
                        "For first/second person: verb stem + 고 싶어요. "
                        "For third person (he/she wants): verb stem + 고 싶어해요 (using 싶어하다). "
                        "Past: 고 싶었어요."
                    ),
                    "facts": [
                        "고 싶다 = want to do. Attaches to verb stem.",
                        "먹다 → 먹고 싶어요 (I want to eat).",
                        "가다 → 가고 싶어요 (I want to go).",
                        "Third person: 가고 싶어해요 (He/she wants to go).",
                        "Past: 먹고 싶었어요 (I wanted to eat).",
                    ],
                    "grammar_rules": [
                        "1st/2nd person: verb stem + 고 싶어요.",
                        "3rd person: verb stem + 고 싶어해요.",
                    ],
                },
                "expected_answers": {
                    "Translate: 'I want to eat Korean food.'": "한국 음식을 먹고 싶어요.",
                    "Translate: 'She wants to go to Korea.'": "그녀는 한국에 가고 싶어해요.",
                    "What is the past tense of 고 싶다?": "고 싶었어요 (e.g. 먹고 싶었어요 = I wanted to eat)",
                },
            },
            {
                "id": "U1L12",
                "title": "Can / Cannot: ~ㄹ/을 수 있다/없다",
                "subtitle": "Expressing ability and inability",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Form the ~ㄹ/을 수 있다 structure for ability",
                    "Use ~ㄹ/을 수 없다 for inability",
                    "Understand the rule: when to use ㄹ vs 을",
                ],
                "techniques": ["Pattern Drilling", "Active Recall", "Sentence Building"],
                "key_vocab": ["수 있다", "수 없다", "말하다", "운전하다", "수영하다", "요리하다", "노래하다", "춤추다"],
                "feynman_prompt": "Explain the ㄹ/을 수 있다 rule. Give an example with a vowel-stem verb and a consonant-stem verb.",
                "active_recall_questions": [
                    "Translate: 'I can speak Korean.'",
                    "Translate: 'He cannot drive.'",
                    "What changes between 먹다 and 가다 when using this pattern?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 9–16", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/"},
                ],
                "topik_vocab_count": 20,
                "knowledge_bank": {
                    "summary": (
                        "~ㄹ/을 수 있다 = can (ability). ~ㄹ/을 수 없다 = cannot. "
                        "Rule: if verb stem ends in a vowel → ㄹ 수 있다. "
                        "If verb stem ends in a consonant → 을 수 있다."
                    ),
                    "facts": [
                        "가다 (stem: 가, vowel) → 갈 수 있어요 (can go).",
                        "먹다 (stem: 먹, consonant) → 먹을 수 있어요 (can eat).",
                        "Can't: 갈 수 없어요 / 먹을 수 없어요.",
                        "말하다 = to speak. 운전하다 = to drive. 수영하다 = to swim.",
                    ],
                    "grammar_rules": [
                        "Vowel stem + ㄹ 수 있다: 가 + ㄹ 수 있어요 = 갈 수 있어요.",
                        "Consonant stem + 을 수 있다: 먹 + 을 수 있어요 = 먹을 수 있어요.",
                    ],
                },
                "expected_answers": {
                    "Translate: 'I can speak Korean.'": "한국어를 말할 수 있어요.",
                    "Translate: 'He cannot drive.'": "그는 운전할 수 없어요.",
                    "What changes between 먹다 and 가다 with this pattern?": (
                        "가다 has a vowel stem → ㄹ 수 있다. 먹다 has a consonant stem → 을 수 있다."
                    ),
                },
            },
            {
                "id": "U1L13",
                "title": "~아/어야 하다 — Must / Have To",
                "subtitle": "Obligation and necessity",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Form ~아/어야 하다 for obligation",
                    "Use ~아/어야 되다 as an alternative",
                    "Recognise the nuance between 하다 and 되다 forms",
                ],
                "techniques": ["Active Recall", "Contrast Drilling", "Spaced Repetition"],
                "key_vocab": ["아야 하다", "어야 하다", "아야 되다", "어야 되다", "가야 해요", "먹어야 해요", "해야 해요", "자야 해요"],
                "feynman_prompt": "Give a scenario (e.g., 'I have a test tomorrow') and explain obligation using ~야 하다.",
                "active_recall_questions": [
                    "Translate: 'I have to study.'",
                    "Translate: 'You must sleep early.'",
                    "Is there a difference between 해야 하다 and 해야 되다?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 9–16", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/"},
                ],
                "topik_vocab_count": 20,
                "knowledge_bank": {
                    "summary": (
                        "~아/어야 하다 expresses obligation ('must/have to'). "
                        "~아/어야 되다 is interchangeable and equally common. "
                        "Formation follows the same vowel harmony as 아요/어요 conjugation."
                    ),
                    "facts": [
                        "가야 해요 = I have to go (가 + 아야 하다).",
                        "먹어야 해요 = I have to eat (먹 + 어야 하다).",
                        "해야 해요 = I have to do it (하다 irregular).",
                        "되다 form: 가야 돼요 — equally natural.",
                    ],
                    "grammar_rules": [
                        "ㅏ/ㅗ stem + 아야 하다: 가 → 가야 해요.",
                        "Other stem + 어야 하다: 먹 → 먹어야 해요.",
                        "하다 → 해야 해요.",
                    ],
                },
                "expected_answers": {
                    "Translate: 'I have to study.'": "공부해야 해요. (or 공부해야 돼요)",
                    "Translate: 'You must sleep early.'": "일찍 자야 해요.",
                    "Is there a difference between 해야 하다 and 해야 되다?": (
                        "Functionally the same in most contexts. 하다 sounds slightly more formal/assertive; "
                        "되다 sounds slightly softer/more colloquial."
                    ),
                },
            },
            {
                "id": "U1L14",
                "title": "~지 않다 — Formal Negation",
                "subtitle": "More formal alternative to 안",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/",
                "estimated_minutes": 15,
                "split": False,
                "learning_goals": [
                    "Use ~지 않다 to negate verbs (formal style)",
                    "Compare ~지 않다 with 안 + verb",
                    "Apply to adjectives (descriptive verbs)",
                ],
                "techniques": ["Contrast Drilling", "Active Recall"],
                "key_vocab": ["지 않다", "지 않아요", "좋지 않아요", "크지 않아요", "먹지 않아요", "가지 않아요"],
                "feynman_prompt": "When would you choose 지 않다 over 안? Give a formal and informal context.",
                "active_recall_questions": [
                    "Negate formally: '먹어요' → ?",
                    "Negate formally: '좋아요' → ?",
                    "Translate: 'I do not go to school.' (formal negation)",
                ],
                "resources": [
                    {"name": "HTSK Lessons 9–16", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/"},
                ],
                "topik_vocab_count": 15,
                "knowledge_bank": {
                    "summary": (
                        "~지 않다 is the suffix-based negation, more formal than 안 + verb. "
                        "Formation: verb/adjective stem + 지 않아요. "
                        "Both forms are correct; 안 is more casual, ~지 않다 more polished."
                    ),
                    "facts": [
                        "먹지 않아요 = I don't eat (formal). 안 먹어요 = I don't eat (casual).",
                        "가지 않아요 = I don't go. 좋지 않아요 = It's not good.",
                        "Applies to both action verbs and descriptive verbs (adjectives).",
                    ],
                    "grammar_rules": [
                        "Stem + 지 않아요: 먹 + 지 않아요 = 먹지 않아요.",
                        "Past: stem + 지 않았어요: 먹지 않았어요.",
                    ],
                },
                "expected_answers": {
                    "Negate formally: '먹어요' → ?": "먹지 않아요",
                    "Negate formally: '좋아요' → ?": "좋지 않아요",
                    "Translate: 'I do not go to school.'": "학교에 가지 않아요.",
                },
            },
            {
                "id": "U1L15",
                "title": "~고 싶지 않다 + ~기 싫다",
                "subtitle": "Not wanting to do something",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/",
                "estimated_minutes": 15,
                "split": False,
                "learning_goals": [
                    "Combine negation with 고 싶다 to say 'don't want to'",
                    "Use ~기 싫다 as a stronger 'don't want'",
                    "Understand nuance between the two forms",
                ],
                "techniques": ["Nuance Awareness", "Active Recall", "Sentence Building"],
                "key_vocab": ["고 싶지 않다", "기 싫다", "하기 싫어요", "가기 싫어요", "먹기 싫어요"],
                "feynman_prompt": "Explain the feeling difference between '가고 싶지 않아요' and '가기 싫어요'.",
                "active_recall_questions": [
                    "Translate: 'I don't want to go.'",
                    "Translate: 'I really don't want to eat that.' (stronger)",
                    "Which is more emotional — 싶지 않다 or 기 싫다?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 9–16", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/"},
                ],
                "topik_vocab_count": 10,
                "knowledge_bank": {
                    "summary": (
                        "고 싶지 않아요 = polite 'I don't want to' (neutral/soft). "
                        "기 싫어요 = stronger emotional 'I don't want to / I hate doing'. "
                        "기 싫다 formation: verb stem + 기 싫다."
                    ),
                    "facts": [
                        "가고 싶지 않아요 = I don't want to go (mild/polite).",
                        "가기 싫어요 = I don't want to go / I hate going (stronger, emotional).",
                        "먹기 싫어요 = I don't feel like eating (strong aversion).",
                    ],
                },
                "expected_answers": {
                    "Translate: 'I don't want to go.'": "가고 싶지 않아요. (or 가기 싫어요 for stronger feeling)",
                    "Translate: 'I really don't want to eat that.'": "그거 먹기 싫어요.",
                    "Which is more emotional?": "기 싫다 — it implies stronger reluctance or aversion.",
                },
            },
            {
                "id": "U1L16",
                "title": "~는 것 — Nominalizing Verbs",
                "subtitle": "Turning verbs into nouns",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Use ~는 것 to turn a verb/clause into a noun",
                    "Understand the difference between ~는 것 (present) and ~ㄴ/은 것 (past/descriptive)",
                    "Use nominalized verbs as sentence subjects or objects",
                ],
                "techniques": ["Clause Building", "Active Recall", "Feynman Technique"],
                "key_vocab": ["는 것", "는 게", "공부하는 것", "먹는 것", "자는 것", "좋아하는 것", "싫어하는 것"],
                "feynman_prompt": "Explain ~는 것 using the English equivalent '-ing'. Show one sentence with it as subject and one as object.",
                "active_recall_questions": [
                    "Nominalize: '공부하다' → ?",
                    "Translate: 'Studying Korean is fun.'",
                    "Translate: 'I like eating.'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 9–16", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-9-16/"},
                ],
                "topik_vocab_count": 15,
                "knowledge_bank": {
                    "summary": (
                        "~는 것 turns a verb into a noun phrase (like English '-ing' or 'the act of'). "
                        "Present/action verbs: stem + 는 것. "
                        "는 게 is a contracted spoken form of 는 것이."
                    ),
                    "facts": [
                        "공부하는 것 = studying (the act of studying).",
                        "먹는 것 = eating.",
                        "공부하는 것이 재미있어요 = Studying is fun (subject).",
                        "먹는 것을 좋아해요 = I like eating (object).",
                        "는 게 = contracted 는 것이 — common in speech.",
                    ],
                    "grammar_rules": [
                        "Action verb stem + 는 것: 공부하 + 는 것 = 공부하는 것.",
                        "Descriptive verb + ㄴ/은 것: 좋 + 은 것 = 좋은 것.",
                    ],
                },
                "expected_answers": {
                    "Nominalize: '공부하다' → ?": "공부하는 것",
                    "Translate: 'Studying Korean is fun.'": "한국어를 공부하는 것이 재미있어요.",
                    "Translate: 'I like eating.'": "먹는 것을 좋아해요.",
                },
            },
            # Lessons 17–25
            {
                "id": "U1L17",
                "title": "Adjectives (Descriptive Verbs) + ~ㄴ/은",
                "subtitle": "Korean adjectives modify nouns differently to English",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Understand that Korean adjectives are conjugated verbs",
                    "Attach ~ㄴ/은 to adjective stems to modify nouns",
                    "Build adjective-noun phrases",
                ],
                "techniques": ["Pattern Recognition", "Active Recall", "Sentence Building"],
                "key_vocab": ["크다", "작다", "좋다", "나쁘다", "예쁘다", "멋있다", "맛있다", "맛없다", "재미있다", "재미없다"],
                "feynman_prompt": "Explain why '좋다' becomes '좋은' before a noun. Contrast with English adjectives.",
                "active_recall_questions": [
                    "Modify: '크다' + '집' → ?",
                    "Modify: '예쁘다' + '여자' → ?",
                    "Translate: 'a delicious meal'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 17–25", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/"},
                ],
                "topik_vocab_count": 30,
                "knowledge_bank": {
                    "summary": (
                        "Korean adjectives are descriptive verbs — they conjugate like verbs. "
                        "To modify a noun, add ~ㄴ after vowel stems or ~은 after consonant stems. "
                        "Example: 크다 (big) → 큰 집 (big house). 좋다 (good) → 좋은 사람 (good person)."
                    ),
                    "facts": [
                        "Korean adjectives conjugate — they are descriptive verbs.",
                        "To modify a noun: adj stem + ㄴ (after vowel) or 은 (after consonant).",
                        "크다 → 큰. 작다 → 작은. 좋다 → 좋은. 예쁘다 → 예쁜.",
                        "맛있다 → 맛있는 음식 (delicious food). 재미있다 → 재미있는 영화.",
                    ],
                    "grammar_rules": [
                        "Vowel stem + ㄴ: 크 + ㄴ = 큰.",
                        "Consonant stem + 은: 좋 + 은 = 좋은.",
                        "있다/없다 pattern: 있는, 없는 (uses ~는, not ~은).",
                    ],
                },
                "expected_answers": {
                    "Modify: '크다' + '집' → ?": "큰 집",
                    "Modify: '예쁘다' + '여자' → ?": "예쁜 여자",
                    "Translate: 'a delicious meal'": "맛있는 음식",
                },
            },
            {
                "id": "U1L18",
                "title": "Future Tense: ~ㄹ/을 것이다",
                "subtitle": "Expressing future intentions and predictions",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Form ~ㄹ/을 것이다 for future tense",
                    "Use ~ㄹ/을 거예요 in informal polite speech",
                    "Distinguish from ~겠다 (intention/guess)",
                ],
                "techniques": ["Pattern Drilling", "Active Recall", "Spaced Repetition"],
                "key_vocab": ["ㄹ 거예요", "을 거예요", "갈 거예요", "먹을 거예요", "할 거예요", "볼 거예요", "올 거예요"],
                "feynman_prompt": "Explain the future tense rule and when you'd use it vs. using present tense to imply future.",
                "active_recall_questions": [
                    "Translate: 'I will go to Korea.'",
                    "Translate: 'She will eat dinner.'",
                    "What is the vowel-stem vs consonant-stem rule here?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 17–25", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/"},
                ],
                "topik_vocab_count": 20,
                "knowledge_bank": {
                    "summary": (
                        "~ㄹ/을 것이다 expresses future tense. Spoken form: ~ㄹ/을 거예요. "
                        "Rule: vowel stem + ㄹ 거예요. Consonant stem + 을 거예요. "
                        "하다 → 할 거예요."
                    ),
                    "facts": [
                        "가다 → 갈 거예요 (will go). 먹다 → 먹을 거예요 (will eat).",
                        "할 거예요 = will do. 볼 거예요 = will watch/see.",
                        "갈 거예요 (neutral future). 가겠어요 (stronger intention/conjecture).",
                    ],
                    "grammar_rules": [
                        "Vowel stem + ㄹ 거예요: 가 + ㄹ 거예요 = 갈 거예요.",
                        "Consonant stem + 을 거예요: 먹 + 을 거예요 = 먹을 거예요.",
                    ],
                },
                "expected_answers": {
                    "Translate: 'I will go to Korea.'": "한국에 갈 거예요.",
                    "Translate: 'She will eat dinner.'": "그녀는 저녁을 먹을 거예요.",
                    "What is the vowel-stem vs consonant-stem rule?": (
                        "Vowel stem → ㄹ 거예요 (e.g. 가 → 갈). Consonant stem → 을 거예요 (e.g. 먹 → 먹을)."
                    ),
                },
            },
            {
                "id": "U1L19",
                "title": "~고 — Connecting Clauses (And Then)",
                "subtitle": "Chaining actions in sequence",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~고 to connect two actions sequentially",
                    "Understand tense handling with ~고 clauses",
                    "Build multi-clause sentences naturally",
                ],
                "techniques": ["Sentence Building", "Active Recall", "Narrative Practice"],
                "key_vocab": ["~고", "먹고", "가고", "공부하고", "자고", "일어나고", "씻고", "입고", "타고"],
                "feynman_prompt": "Describe your morning routine using ~고 to chain at least 4 actions.",
                "active_recall_questions": [
                    "Chain: 'I ate and went home.'",
                    "Chain: 'I studied and slept.'",
                    "Does tense go on the first clause or the last in a ~고 chain?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 17–25", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/"},
                ],
                "topik_vocab_count": 20,
                "knowledge_bank": {
                    "summary": (
                        "~고 connects two clauses sequentially ('and then'). "
                        "Tense only goes on the final verb — not on the 고 clause. "
                        "Suitable for listing actions in sequence or describing simultaneous states."
                    ),
                    "facts": [
                        "먹고 갔어요 = I ate and (then) went.",
                        "공부하고 잤어요 = I studied and slept.",
                        "Tense marker goes on the LAST verb only.",
                        "일어나고 씻고 먹어요 = I get up, wash, and eat (chained sequence).",
                    ],
                    "grammar_rules": ["Verb stem + 고 + next verb: 먹 + 고 + 갔어요 = 먹고 갔어요."],
                },
                "expected_answers": {
                    "Chain: 'I ate and went home.'": "밥을 먹고 집에 갔어요.",
                    "Chain: 'I studied and slept.'": "공부하고 잤어요.",
                    "Does tense go on the first clause?": "No — tense only goes on the final verb in the chain.",
                },
            },
            {
                "id": "U1L20",
                "title": "~지만 — But / However",
                "subtitle": "Contrasting two clauses",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/",
                "estimated_minutes": 15,
                "split": False,
                "learning_goals": [
                    "Use ~지만 to contrast two clauses",
                    "Apply to verbs and adjectives",
                    "Understand formality of 그렇지만 vs ~지만",
                ],
                "techniques": ["Contrast Drilling", "Active Recall"],
                "key_vocab": ["지만", "좋지만", "먹지만", "가지만", "그렇지만", "하지만"],
                "feynman_prompt": "Give two sentences using ~지만, one about preference and one about ability.",
                "active_recall_questions": [
                    "Translate: 'Korean is difficult, but interesting.'",
                    "Translate: 'I want to go, but I can't.'",
                    "What is the standalone word for 'but/however'?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 17–25", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/"},
                ],
                "topik_vocab_count": 15,
                "knowledge_bank": {
                    "summary": (
                        "~지만 connects two contrasting clauses ('but/however'). "
                        "Attaches directly to verb/adjective stem. "
                        "그렇지만 / 하지만 are standalone words meaning 'however/but' between sentences."
                    ),
                    "facts": [
                        "먹지만 = (I) eat, but... 좋지만 = (it's) good, but...",
                        "한국어가 어렵지만 재미있어요 = Korean is difficult but interesting.",
                        "그렇지만 / 하지만 = standalone 'however/but' (between sentences).",
                    ],
                    "grammar_rules": ["Verb/adj stem + 지만: 먹 + 지만 = 먹지만."],
                },
                "expected_answers": {
                    "Translate: 'Korean is difficult, but interesting.'": "한국어가 어렵지만 재미있어요.",
                    "Translate: 'I want to go, but I can't.'": "가고 싶지만 갈 수 없어요.",
                    "What is the standalone word for 'but/however'?": "그렇지만 or 하지만",
                },
            },
            {
                "id": "U1L21",
                "title": "~아/어서 — Because (Reason) & After Doing",
                "subtitle": "Dual-use connector: reason and sequential action",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Use ~아/어서 to express reason (because/so)",
                    "Use ~아/어서 to express sequential action (after doing, then...)",
                    "Recognise context clues for which meaning applies",
                ],
                "techniques": ["Dual Meaning Drilling", "Active Recall", "Feynman Technique"],
                "key_vocab": ["아서", "어서", "바빠서", "피곤해서", "만나서", "가서", "사서", "먹어서"],
                "feynman_prompt": "Create two sentences where ~아/어서 means 'because' and two where it means 'after doing'. Explain the difference.",
                "active_recall_questions": [
                    "Translate: 'I am tired so I will sleep.'",
                    "Translate: 'I went to the store and (then) bought food.'",
                    "Can you use tense with ~아/어서? Why not?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 17–25", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/"},
                ],
                "topik_vocab_count": 25,
                "knowledge_bank": {
                    "summary": (
                        "~아/어서 has two meanings depending on context: "
                        "(1) Reason: 'because/so' — 피곤해서 잘 거예요 (I'm tired so I'll sleep). "
                        "(2) Sequential action: 'after doing, then' — 가서 샀어요 (went and then bought). "
                        "Important: ~아/어서 clause cannot take tense — tense goes on the final verb only."
                    ),
                    "facts": [
                        "피곤해서 잘 거예요 = I'm tired so I'll sleep (reason).",
                        "가게에 가서 음식을 샀어요 = I went to the store and bought food (sequence).",
                        "You CANNOT say 갔어서 — no tense on the 아/어서 clause.",
                    ],
                    "grammar_rules": [
                        "ㅏ/ㅗ stem + 아서: 바쁘다 → 바빠서.",
                        "Other stem + 어서: 피곤하다 → 피곤해서.",
                        "No tense marker on ~아/어서 clause.",
                    ],
                },
                "expected_answers": {
                    "Translate: 'I am tired so I will sleep.'": "피곤해서 잘 거예요.",
                    "Translate: 'I went to the store and bought food.'": "가게에 가서 음식을 샀어요.",
                    "Can you use tense with ~아/어서?": "No — tense only goes on the final verb, never on the 아/어서 clause.",
                },
            },
            {
                "id": "U1L22",
                "title": "~(으)면 — If / When",
                "subtitle": "Conditional sentences",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Form conditional sentences with ~(으)면",
                    "Apply to verbs and adjectives",
                    "Understand the vowel-stem vs consonant-stem rule for 으",
                ],
                "techniques": ["If-Then Drilling", "Active Recall", "Spaced Repetition"],
                "key_vocab": ["으면", "면", "가면", "먹으면", "공부하면", "비가 오면", "있으면", "없으면", "좋으면"],
                "feynman_prompt": "Explain ~(으)면 with two real-life examples: one factual conditional and one hypothetical.",
                "active_recall_questions": [
                    "Translate: 'If you study, you will pass.'",
                    "Translate: 'When it rains, I stay home.'",
                    "Does tense affect the ~으면 clause?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 17–25", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/"},
                ],
                "topik_vocab_count": 20,
                "knowledge_bank": {
                    "summary": (
                        "~(으)면 = if/when (conditional). "
                        "Vowel stem → 면. Consonant stem → 으면. "
                        "Used for factual conditionals ('when X, Y') and hypotheticals ('if X, Y'). "
                        "No tense on the ~(으)면 clause."
                    ),
                    "facts": [
                        "가다 → 가면 (if/when you go).",
                        "먹다 → 먹으면 (if/when you eat).",
                        "공부하면 합격할 거예요 = If you study, you will pass.",
                        "비가 오면 집에 있어요 = When it rains, I stay home.",
                    ],
                    "grammar_rules": [
                        "Vowel stem + 면: 가 + 면 = 가면.",
                        "Consonant stem + 으면: 먹 + 으면 = 먹으면.",
                    ],
                },
                "expected_answers": {
                    "Translate: 'If you study, you will pass.'": "공부하면 합격할 거예요.",
                    "Translate: 'When it rains, I stay home.'": "비가 오면 집에 있어요.",
                    "Does tense affect the ~으면 clause?": "No — tense goes on the result clause (final verb) only.",
                },
            },
            {
                "id": "U1L23",
                "title": "~때 — When (Time Clauses)",
                "subtitle": "Expressing 'when X happens/happened'",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~(으)ㄹ 때 for 'when (future/hypothetical)'",
                    "Use ~ㄹ/을 때 with action verbs",
                    "Contrast with ~면 conditionals",
                ],
                "techniques": ["Time-Frame Drilling", "Active Recall"],
                "key_vocab": ["때", "공부할 때", "먹을 때", "어릴 때", "바쁠 때", "힘들 때", "어렸을 때"],
                "feynman_prompt": "Explain the difference between ~(으)면 and ~(으)ㄹ 때 using the same scenario.",
                "active_recall_questions": [
                    "Translate: 'When I study, I drink coffee.'",
                    "Translate: 'When I was young, I liked this.'",
                    "What is the form after a vowel-stem? After a consonant-stem?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 17–25", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/"},
                ],
                "topik_vocab_count": 20,
                "knowledge_bank": {
                    "summary": (
                        "때 = 'time / when'. "
                        "Present/future: verb stem + ㄹ/을 때. "
                        "Past (when I was doing): verb + 았/었을 때. "
                        "~면 = conditional 'if'. ~때 = time-reference 'when'."
                    ),
                    "facts": [
                        "공부할 때 커피를 마셔요 = When I study, I drink coffee.",
                        "어렸을 때 = when I was young (past).",
                        "바쁠 때 = when (I am) busy.",
                        "~(으)면 is conditional; ~ㄹ/을 때 is a time reference — not interchangeable.",
                    ],
                    "grammar_rules": [
                        "Vowel stem + ㄹ 때: 공부하 + ㄹ 때 = 공부할 때.",
                        "Consonant stem + 을 때: 먹 + 을 때 = 먹을 때.",
                        "Past time: 먹었을 때 (when I ate/was eating).",
                    ],
                },
                "expected_answers": {
                    "Translate: 'When I study, I drink coffee.'": "공부할 때 커피를 마셔요.",
                    "Translate: 'When I was young, I liked this.'": "어렸을 때 이걸 좋아했어요.",
                    "Form after vowel-stem / consonant-stem?": "Vowel stem + ㄹ 때 (공부할 때). Consonant stem + 을 때 (먹을 때).",
                },
            },
            {
                "id": "U1L24",
                "title": "~기 전에 / ~(으)ㄴ 후에 — Before & After",
                "subtitle": "Sequencing actions in time",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~기 전에 to express 'before doing'",
                    "Use ~(으)ㄴ 후에 or ~고 나서 for 'after doing'",
                    "Build complex time-ordered sentences",
                ],
                "techniques": ["Sequencing Drilling", "Active Recall", "Narrative Practice"],
                "key_vocab": ["기 전에", "ㄴ 후에", "고 나서", "자기 전에", "먹기 전에", "공부한 후에", "도착한 후에"],
                "feynman_prompt": "Describe a routine (e.g. bedtime) using both 전에 and 후에 in the same paragraph.",
                "active_recall_questions": [
                    "Translate: 'Before sleeping, I brush my teeth.'",
                    "Translate: 'After eating, I studied.'",
                    "Give the form of 전에 and 후에 with 먹다.",
                ],
                "resources": [
                    {"name": "HTSK Lessons 17–25", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-17-25-2/"},
                ],
                "topik_vocab_count": 20,
                "knowledge_bank": {
                    "summary": (
                        "기 전에 = before doing (verb stem + 기 전에). "
                        "~(으)ㄴ 후에 = after doing (verb past modifier + 후에). "
                        "~고 나서 = after doing (more casual alternative to 후에)."
                    ),
                    "facts": [
                        "자기 전에 이를 닦아요 = Before sleeping, I brush my teeth.",
                        "먹은 후에 공부했어요 = After eating, I studied.",
                        "먹고 나서 공부했어요 = After eating, I studied (고 나서 form).",
                        "전에 uses the verb in dictionary form + 기. 후에 uses past modifier + 후에.",
                    ],
                    "grammar_rules": [
                        "Before: verb stem + 기 전에: 자 + 기 전에 = 자기 전에.",
                        "After: past modifier + 후에: 먹 + 은 후에 = 먹은 후에.",
                        "After (casual): verb stem + 고 나서: 먹고 나서.",
                    ],
                },
                "expected_answers": {
                    "Translate: 'Before sleeping, I brush my teeth.'": "자기 전에 이를 닦아요.",
                    "Translate: 'After eating, I studied.'": "먹은 후에 공부했어요. (or 먹고 나서 공부했어요)",
                    "Form of 전에 and 후에 with 먹다.": "전에: 먹기 전에. 후에: 먹은 후에.",
                },
            },
            {
                "id": "U1L25",
                "title": "Unit 1 Review + Test Prep",
                "subtitle": "Consolidate all Unit 1 grammar and vocabulary",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-test/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Review all major grammar points from Unit 1",
                    "Self-test on vocabulary via active recall",
                    "Identify weak areas for spaced repetition focus",
                ],
                "techniques": ["Active Recall", "Spaced Repetition Review", "Feynman Self-Test"],
                "key_vocab": ["Review all Unit 1 grammar markers and 200 core vocab words"],
                "feynman_prompt": "Without notes, explain 5 grammar points from Unit 1 as if teaching a beginner. Note which ones felt shaky.",
                "active_recall_questions": [
                    "Write 10 sentences using 5 different grammar points from Unit 1.",
                    "List all particles learned. What does each one do?",
                    "What topics are you least confident on? Plan your Anki review.",
                ],
                "resources": [
                    {"name": "Unit 1 Test", "url": "https://www.howtostudykorean.com/unit1/unit-1-test/"},
                    {"name": "HTSK Anki Deck", "url": "https://www.howtostudykorean.com/anki/"},
                ],
                "topik_vocab_count": 50,
                "knowledge_bank": {
                    "summary": (
                        "Unit 1 covers 25 lessons of core Korean grammar. Key grammar points: "
                        "이다, particles (이/가, 은/는, 을/를, 에, 에서, 의), present/past/future tense, "
                        "negation (안, 지 않다), connectors (고, 지만, 아/어서, 으면, 때, 전에, 후에), "
                        "ability (ㄹ 수 있다), wanting (고 싶다), nominalisation (는 것). "
                        "Vocabulary target: ~400 words towards TOPIK I."
                    ),
                    "facts": [
                        "Particles: 이/가 (subject), 은/는 (topic), 을/를 (object), 에 (location/direction), 에서 (action location), 의 (possessive).",
                        "Tense: present (아/어요), past (았/었어요), future (ㄹ/을 거예요).",
                        "Negation: 안 + verb (casual), verb + 지 않아요 (formal).",
                        "Connectors covered: 고 (and then), 지만 (but), 아/어서 (because/after), 으면 (if/when), 때 (when), 기 전에 (before), 은 후에 (after).",
                    ],
                },
                "expected_answers": {
                    "List all particles from Unit 1 and what each does.": (
                        "이/가: subject. 은/는: topic. 을/를: object. 에: location/direction. "
                        "에서: action location. 의: possessive. 와/과/하고/이랑: 'and'."
                    ),
                    "Name 5 connectors from Unit 1.": "~고 (and then), ~지만 (but), ~아/어서 (because/after), ~(으)면 (if), ~때 (when).",
                    "What is the TOPIK vocab target for Unit 1?": "Approximately 400 words — roughly one third of the TOPIK I target.",
                },
            },
        ],
    },

    "Unit 2": {
        "title": "Lower-Intermediate Korean Grammar",
        "level": "Lower Intermediate",
        "description": "Expand sentence complexity with new verb endings, reported speech, and passive voice (Lessons 26–50).",
        "color": "#F39C12",
        "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/",
        "lessons": [
            {
                "id": "U2L26",
                "title": "~(으)ㄹ 수 있다/없다 Review + ~겠다",
                "subtitle": "Ability review + expressing conjecture/intention",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Solidify ~ㄹ/을 수 있다 ability pattern",
                    "Use ~겠다 for speaker's intention, conjecture, or softening",
                    "Distinguish 겠다 from ~ㄹ 거야 future",
                ],
                "techniques": ["Contrast Drilling", "Active Recall", "Spaced Repetition"],
                "key_vocab": ["겠다", "겠어요", "먹겠습니다", "알겠어요", "모르겠어요", "하겠습니다", "가겠습니다"],
                "feynman_prompt": "Explain three different uses of ~겠다 with one example each.",
                "active_recall_questions": [
                    "What does 알겠어요 mean?",
                    "Translate: 'I think it will be cold.' (using 겠다)",
                    "Difference between 갈 거예요 and 가겠어요?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 26–33", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/"},
                ],
            },
            {
                "id": "U2L27",
                "title": "~아/어 보다 — Trying Things",
                "subtitle": "'Try doing' + experience of having done",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~아/어 보다 to express trying/attempting something",
                    "Use ~아/어 봤다 for having experienced something",
                    "Combine with 적이 있다/없다 for life experience",
                ],
                "techniques": ["Active Recall", "Experience Narration"],
                "key_vocab": ["아 보다", "어 보다", "먹어 봤어요", "가 봤어요", "해 봤어요", "입어 봤어요", "적이 있다", "적이 없다"],
                "feynman_prompt": "Describe two things you've tried (식당, 음식) and one you haven't, using 아/어 봤어요 and 적이 없어요.",
                "active_recall_questions": [
                    "Translate: 'Have you tried Korean food?'",
                    "Translate: 'I've never been to Korea.'",
                    "What is the difference between 먹어 봐요 and 먹어 봤어요?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 26–33", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/"},
                ],
            },
            {
                "id": "U2L28",
                "title": "~아/어 주다 — Doing Favours",
                "subtitle": "Doing something for someone",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~아/어 주다 to express doing something for someone",
                    "Make polite requests using ~아/어 주세요",
                    "Use ~아/어 드리다 for respectful 'doing for'",
                ],
                "techniques": ["Politeness Register", "Active Recall", "Role-Play"],
                "key_vocab": ["아 주다", "어 주다", "해 주세요", "가르쳐 주세요", "도와주세요", "가져다주세요", "드리다"],
                "feynman_prompt": "Give a dialogue where someone asks for help using ~아/어 주세요 and someone responds.",
                "active_recall_questions": [
                    "Translate: 'Please help me.'",
                    "Translate: 'Can you teach me?' (polite)",
                    "When would you use 드리다 instead of 주다?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 26–33", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/"},
                ],
            },
            {
                "id": "U2L29",
                "title": "~(으)ㄹ게요 — I Will (Promise/Intention)",
                "subtitle": "First-person commitment to action",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/",
                "estimated_minutes": 15,
                "split": False,
                "learning_goals": [
                    "Use ~ㄹ게요 to make promises or state intentions to the listener",
                    "Understand it is only used in first-person",
                    "Contrast with 거예요 (neutral future) and 겠어요",
                ],
                "techniques": ["Context Drilling", "Active Recall"],
                "key_vocab": ["ㄹ게요", "을게요", "할게요", "갈게요", "먹을게요", "기다릴게요", "전화할게요"],
                "feynman_prompt": "Explain when 갈게요 is more natural than 갈 거예요. Create a mini-dialogue.",
                "active_recall_questions": [
                    "Translate: 'I'll call you later.' (promise)",
                    "Can you say '그가 갈게요'? Why not?",
                    "Translate: 'I'll wait for you.'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 26–33", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/"},
                ],
            },
            {
                "id": "U2L30",
                "title": "~(으)ㄹ까요? — Shall We? / I Wonder...",
                "subtitle": "Suggestions and rhetorical wondering",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~ㄹ까요 to make suggestions ('shall we?')",
                    "Use ~ㄹ까요 for wondering aloud",
                    "Contrast with ~ㄹ게요 and ~겠어요",
                ],
                "techniques": ["Suggestion Drilling", "Active Recall", "Context Awareness"],
                "key_vocab": ["ㄹ까요", "갈까요", "먹을까요", "할까요", "뭘 먹을까요", "어디 갈까요", "뭐가 좋을까요"],
                "feynman_prompt": "Give two dialogues: one where ~ㄹ까요 is a suggestion and one where it's internal wondering.",
                "active_recall_questions": [
                    "Suggest going to eat: '우리___'?",
                    "Express wondering: 'I wonder if she will come.'",
                    "What is the response if someone says 갈까요?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 26–33", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/"},
                ],
            },
            {
                "id": "U2L31",
                "title": "~는/(으)ㄴ/(으)ㄹ — Verb Modifiers (Relative Clauses)",
                "subtitle": "Using verbs to describe nouns — the core of Korean sentence complexity",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Use ~는 for present action modifying a noun",
                    "Use ~(으)ㄴ for past action or descriptive adjectives modifying a noun",
                    "Use ~(으)ㄹ for future/potential modifying a noun",
                ],
                "techniques": ["Pattern Recognition", "Active Recall", "Clause Stacking"],
                "key_vocab": ["먹는 사람", "먹은 음식", "먹을 것", "공부하는 학생", "예쁜 꽃", "갈 곳", "본 영화"],
                "feynman_prompt": "Explain all 3 verb modifier forms using ONE verb (e.g. 먹다) with three different nouns. What does each convey?",
                "active_recall_questions": [
                    "Translate: 'the person who is eating'",
                    "Translate: 'the food I ate yesterday'",
                    "Translate: 'the movie I will watch'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 26–33", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/"},
                ],
            },
            {
                "id": "U2L32",
                "title": "~이/가 아니다 — 'Is Not' + ~도 Particle",
                "subtitle": "Negating identity + 'also/too/even' particle",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use 이/가 아니다 to negate noun predicate sentences",
                    "Attach ~도 for 'also/too'",
                    "Use ~도 with negative to mean 'not...either'",
                ],
                "techniques": ["Negation Drilling", "Additive Drilling", "Active Recall"],
                "key_vocab": ["이 아니다", "가 아니다", "아니에요", "도", "나도", "그것도", "없어도", "안 해도"],
                "feynman_prompt": "Explain 아니다 vs 없다 vs 안 — three different negations. When is each used?",
                "active_recall_questions": [
                    "Translate: 'I am not a student.'",
                    "Translate: 'I also like this.'",
                    "Translate: 'He doesn't either.' (using 도 + negative)",
                ],
                "resources": [
                    {"name": "HTSK Lessons 26–33", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/"},
                ],
            },
            {
                "id": "U2L33",
                "title": "~만 (Only) + ~부터/까지 (From/Until)",
                "subtitle": "Limiting and range particles",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~만 to mean 'only'",
                    "Use 부터 for 'from (a time/place)'",
                    "Use 까지 for 'until/to (a time/place)'",
                ],
                "techniques": ["Range Expression", "Active Recall", "Sentence Building"],
                "key_vocab": ["만", "나만", "부터", "까지", "지금부터", "서울부터 부산까지", "월요일부터 금요일까지", "9시부터 5시까지"],
                "feynman_prompt": "Describe your study schedule using 부터, 까지, and 만 in three sentences.",
                "active_recall_questions": [
                    "Translate: 'Only I studied.'",
                    "Translate: 'From Monday to Friday'",
                    "Translate: 'From 9am until 6pm'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 26–33", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-26-33/"},
                ],
            },
            # Placeholder lessons 34–50 (representative structure)
            {
                "id": "U2L34",
                "title": "~아/어지다 — Becoming (Change of State)",
                "subtitle": "Describing how things change over time",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~아/어지다 to describe a gradual change of state",
                    "Apply to adjectives and intransitive verbs",
                    "Contrast with 되다 (to become)",
                ],
                "techniques": ["Change-State Drilling", "Active Recall", "Spaced Repetition"],
                "key_vocab": ["아지다", "어지다", "좋아지다", "나빠지다", "커지다", "작아지다", "더워지다", "추워지다", "익숙해지다"],
                "feynman_prompt": "Explain ~아지다 vs ~이/가 되다. When is one more natural?",
                "active_recall_questions": [
                    "Translate: 'The weather is getting colder.'",
                    "Translate: 'My Korean is improving.' (using 좋아지다)",
                    "Translate: 'He became a teacher.' (which verb do you use?)",
                ],
                "resources": [
                    {"name": "HTSK Lessons 34–41", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/"},
                ],
            },
            {
                "id": "U2L35",
                "title": "~(으)면서 — While Doing",
                "subtitle": "Two simultaneous actions by the same subject",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~(으)면서 to express two simultaneous actions",
                    "Apply the rule (vowel-stem: ~면서, consonant-stem: ~으면서)",
                    "Understand the same-subject constraint",
                ],
                "techniques": ["Simultaneous Action Drilling", "Active Recall"],
                "key_vocab": ["면서", "으면서", "먹으면서", "들으면서", "보면서", "걸으면서", "공부하면서", "이야기하면서"],
                "feynman_prompt": "Describe doing two things at once using ~면서. Then explain why it cannot be used with different subjects.",
                "active_recall_questions": [
                    "Translate: 'I listen to music while studying.'",
                    "Translate: 'She walks while talking on the phone.'",
                    "Is this correct? '나는 공부하면서 그는 잔다' — why or why not?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 34–41", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/"},
                ],
            },
            {
                "id": "U2L36",
                "title": "~(이)라서 / ~(이)기 때문에 — Because (Noun Reason)",
                "subtitle": "Expressing reason with noun subjects",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~(이)라서 to give a noun-based reason",
                    "Use ~기 때문에 with verb clauses",
                    "Distinguish from ~아/어서",
                ],
                "techniques": ["Reason-Clause Drilling", "Active Recall"],
                "key_vocab": ["이라서", "라서", "기 때문에", "학생이라서", "바쁘기 때문에", "비가 오기 때문에"],
                "feynman_prompt": "Show when you'd use ~아서, ~이라서, and ~기 때문에 for the same reason. What's the register difference?",
                "active_recall_questions": [
                    "Translate: 'Because I am a student, I study a lot.' (이라서)",
                    "Translate: 'Because I was busy, I couldn't come.' (기 때문에)",
                    "Can 기 때문에 be used in a command/request sentence?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 34–41", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/"},
                ],
            },
            {
                "id": "U2L37",
                "title": "~(으)ㄴ/는/(으)ㄹ 것 같다 — Seems Like",
                "subtitle": "Expressing conjecture and impression",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Form it-seems constructions using 것 같다",
                    "Apply the correct verb modifier for past/present/future",
                    "Understand the softening and speculation function",
                ],
                "techniques": ["Conjecture Drilling", "Active Recall", "Feynman Technique"],
                "key_vocab": ["것 같다", "인 것 같다", "는 것 같다", "ㄴ 것 같다", "ㄹ 것 같다", "바쁜 것 같다", "간 것 같다", "올 것 같다"],
                "feynman_prompt": "Use 것 같다 to speculate about 3 things: what happened, what is happening now, and what will happen.",
                "active_recall_questions": [
                    "Translate: 'It seems like she left.'",
                    "Translate: 'It looks like it will rain.'",
                    "Translate: 'I think he is busy.'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 34–41", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/"},
                ],
            },
            {
                "id": "U2L38",
                "title": "~(으)ㄹ 것이다 vs ~겠다 (Review) + Expressing Plans",
                "subtitle": "Nuance between future forms in context",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Consolidate understanding of all future forms",
                    "Choose the appropriate form based on context",
                    "Express travel or personal plans fluently",
                ],
                "techniques": ["Comparative Analysis", "Active Recall", "Production Practice"],
                "key_vocab": ["거예요", "겠어요", "ㄹ게요", "ㄹ까요", "계획이에요", "예정이에요"],
                "feynman_prompt": "Summarise all future forms: 거예요 / 겠어요 / ㄹ게요 / ㄹ까요. Give one natural example for each.",
                "active_recall_questions": [
                    "Which future form is used for promises to the listener?",
                    "Which future form is used for guesses/conjecture?",
                    "Translate: 'I plan to visit Korea next year.'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 34–41", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/"},
                ],
            },
            {
                "id": "U2L39",
                "title": "Passive Verbs: ~이/히/리/기 Passives",
                "subtitle": "How Korean creates passive voice",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Identify the 4 passive suffixes: 이, 히, 리, 기",
                    "Transform common active verbs into passive forms",
                    "Understand the agent marker 에게/에 의해",
                ],
                "techniques": ["Passive Transformation Drilling", "Active Recall", "Pattern Recognition"],
                "key_vocab": ["보이다", "들리다", "잡히다", "닫히다", "먹히다", "열리다", "팔리다", "쓰이다", "읽히다"],
                "feynman_prompt": "Explain why Korean uses passive verbs differently to English. Give 3 example sentences.",
                "active_recall_questions": [
                    "Passive of 보다 (to see)?",
                    "Translate: 'The door was opened.'",
                    "Translate: 'The book is being read.'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 34–41", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/"},
                ],
            },
            {
                "id": "U2L40",
                "title": "Causative Verbs: ~이/히/리/기/우/추 Causatives",
                "subtitle": "Making someone do something",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Identify causative suffixes and apply them",
                    "Distinguish passive vs causative forms",
                    "Use 시키다 as a productive causative",
                ],
                "techniques": ["Causative Drilling", "Active Recall", "Contrast with Passives"],
                "key_vocab": ["먹이다", "입히다", "울리다", "웃기다", "눕히다", "공부시키다", "청소시키다", "앉히다"],
                "feynman_prompt": "Explain causative vs passive using 먹이다 vs 먹히다. How are they structurally different?",
                "active_recall_questions": [
                    "Causative of 먹다?",
                    "Translate: 'The mother fed the baby.'",
                    "What is 공부시키다 and how is it different from 공부하게 하다?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 34–41", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/"},
                ],
            },
            {
                "id": "U2L41",
                "title": "~(으)ㄹ 뻔했다 + ~았/었으면 좋겠다",
                "subtitle": "Near misses and wishes",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~ㄹ 뻔했다 for 'almost did / nearly happened'",
                    "Use ~았/었으면 좋겠다 to express a wish",
                    "Understand the counter-factual nuance of the wish form",
                ],
                "techniques": ["Nuance Drilling", "Active Recall", "Creative Sentence Building"],
                "key_vocab": ["ㄹ 뻔했다", "을 뻔했다", "죽을 뻔했다", "넘어질 뻔했다", "았으면 좋겠다", "었으면 좋겠다", "비가 왔으면 좋겠다"],
                "feynman_prompt": "Tell a story: something that almost went wrong + something you wish were different now.",
                "active_recall_questions": [
                    "Translate: 'I almost fell.'",
                    "Translate: 'I wish it would rain.'",
                    "Translate: 'I almost missed the train.'",
                ],
                "resources": [
                    {"name": "HTSK Lessons 34–41", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-34-41/"},
                ],
            },
            {
                "id": "U2L42",
                "title": "~는/(으)ㄴ/(으)ㄹ 때문에 + ~덕분에",
                "subtitle": "Cause and gratitude connectors",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use 때문에 with full verb clauses",
                    "Use 덕분에 for positive outcomes ('thanks to')",
                    "Contrast 때문에 (neutral/negative) with 덕분에 (positive)",
                ],
                "techniques": ["Cause-Effect Drilling", "Contrast Drilling", "Active Recall"],
                "key_vocab": ["때문에", "덕분에", "비 때문에", "그 덕분에", "도움 덕분에", "당신 덕분에"],
                "feynman_prompt": "Use 때문에 and 덕분에 to describe the same outcome — what changes in feeling?",
                "active_recall_questions": [
                    "Translate: 'Because of the rain, I stayed home.'",
                    "Translate: 'Thanks to you, I passed.'",
                    "Can 덕분에 be used sarcastically? What might 네 덕분에 mean in context?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 42–50", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/"},
                ],
            },
            {
                "id": "U2L43",
                "title": "~(으)려고 / ~(으)려고 하다 — Intention / Plan",
                "subtitle": "Expressing intention to do something",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~(으)려고 to show purpose/intention before an action",
                    "Use ~(으)려고 하다 for 'be about to' or 'intend to'",
                    "Contrast with ~기 위해서 (for the purpose of)",
                ],
                "techniques": ["Intention Drilling", "Active Recall", "Purposive Clauses"],
                "key_vocab": ["려고", "으려고", "가려고", "먹으려고", "려고 하다", "려고 해요", "공부하려고 해요"],
                "feynman_prompt": "Explain the difference between ~려고, ~려고 하다, and ~기 위해서. When is each most natural?",
                "active_recall_questions": [
                    "Translate: 'I went to the library to study.'",
                    "Translate: 'I'm intending to go to Korea.'",
                    "Translate: 'I'm about to eat.' (려고 하다)",
                ],
                "resources": [
                    {"name": "HTSK Lessons 42–50", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/"},
                ],
            },
            {
                "id": "U2L44",
                "title": "Reported Speech: ~다고 하다 / ~(라)고 하다",
                "subtitle": "Quoting and reporting what someone said",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Report statements using ~다고 하다 (indirect speech)",
                    "Report questions using ~(으)냐고 하다",
                    "Report commands using ~(으)라고 하다",
                ],
                "techniques": ["Reported Speech Transformation", "Active Recall", "Dialogue Practice"],
                "key_vocab": ["다고 하다", "라고 하다", "냐고 하다", "자고 하다", "(으)라고 하다", "했대요", "간대요", "뭐라고 했어요"],
                "feynman_prompt": "Explain direct vs indirect speech in Korean. Transform 3 direct quotes into indirect reports.",
                "active_recall_questions": [
                    "Transform: '나는 학생이야' → reported speech",
                    "Transform: '밥 먹어!' (command) → reported speech",
                    "Transform: '어디 가?' (question) → reported speech",
                ],
                "resources": [
                    {"name": "HTSK Lessons 42–50", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/"},
                ],
            },
            {
                "id": "U2L45",
                "title": "~(이)라고 하다 + ~에 대해서 — About / Regarding",
                "subtitle": "Naming things and talking about topics",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~(이)라고 하다 to name or define something",
                    "Use 에 대해서 / 에 대한 to talk about a topic",
                    "Combine in academic and conversational contexts",
                ],
                "techniques": ["Definition Drilling", "Topic-Clause Practice", "Active Recall"],
                "key_vocab": ["이라고 하다", "라고 하다", "에 대해서", "에 대한", "한국에 대해서", "이 영화에 대한 생각"],
                "feynman_prompt": "Introduce a topic (e.g. Korean culture) using both ~라고 하다 and ~에 대해서.",
                "active_recall_questions": [
                    "How do you say 'This is called Hangul'?",
                    "Translate: 'I want to know about Korean culture.'",
                    "What is the difference between 에 대해서 (adverb) and 에 대한 (adjective)?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 42–50", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/"},
                ],
            },
            {
                "id": "U2L46",
                "title": "~(으)ㄴ/는지 — Whether / Question Embedding",
                "subtitle": "Embedding questions inside sentences",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Embed a question inside a sentence using ~(으)ㄴ/는지",
                    "Understand the tense/form rules for ~는지 vs ~ㄴ지",
                    "Use with verbs of knowing, wondering, asking",
                ],
                "techniques": ["Embedding Drilling", "Active Recall", "Question Transformation"],
                "key_vocab": ["는지", "ㄴ지", "인지", "어디에 있는지", "누군지", "뭔지", "알아요", "몰라요", "궁금해요"],
                "feynman_prompt": "Transform 3 direct questions into embedded questions and explain what changed grammatically.",
                "active_recall_questions": [
                    "Embed: '어디에 가요?' → 'I don't know where she's going.'",
                    "Embed: '뭐예요?' → 'I wonder what it is.'",
                    "What verb forms follow ~는지?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 42–50", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/"},
                ],
            },
            {
                "id": "U2L47",
                "title": "~게 하다 / ~게 되다 — Causing & Becoming",
                "subtitle": "Making someone do + coming to be in a state",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/",
                "estimated_minutes": 20,
                "split": False,
                "learning_goals": [
                    "Use ~게 하다 to make/allow someone to do something",
                    "Use ~게 되다 for a change or development that came about",
                    "Contrast ~게 되다 with ~아/어지다",
                ],
                "techniques": ["Causative/Resultant Drilling", "Active Recall"],
                "key_vocab": ["게 하다", "게 되다", "알게 되다", "좋아하게 되다", "공부하게 하다", "기다리게 하다"],
                "feynman_prompt": "Tell a learning story using ~게 되다: 'I came to like Korean because...'",
                "active_recall_questions": [
                    "Translate: 'He made me wait.'",
                    "Translate: 'I came to know Korean.'",
                    "Is ~게 되다 active or passive in feeling?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 42–50", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/"},
                ],
            },
            {
                "id": "U2L48",
                "title": "Formal Speech Level: ~ㅂ니다/습니다",
                "subtitle": "The formal (하십시오체) speech level",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Conjugate verbs into formal 합쇼체 (ㅂ니다/습니다) speech level",
                    "Use formal speech for formal questions (~ㅂ니까?)",
                    "Understand when this speech level is required",
                ],
                "techniques": ["Formality Drilling", "Active Recall", "Register Awareness"],
                "key_vocab": ["ㅂ니다", "습니다", "ㅂ니까", "습니까", "가겠습니다", "했습니다", "입니다", "아닙니다"],
                "feynman_prompt": "Imagine giving a formal presentation. Convert 5 everyday sentences into formal ~ㅂ니다 style.",
                "active_recall_questions": [
                    "Conjugate: 먹다 → formal present statement",
                    "Conjugate: 가다 → formal past question",
                    "In what situations in Korea would you use 합쇼체?",
                ],
                "resources": [
                    {"name": "HTSK Lessons 42–50", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/"},
                ],
            },
            {
                "id": "U2L49",
                "title": "Honorific Speech: ~(으)시 Honorific Infix",
                "subtitle": "Showing respect through verb conjugation",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Insert the honorific ~(으)시 into verbs",
                    "Use honorific forms for actions performed by respected people",
                    "Learn special honorific vocabulary (드시다, 주무시다, 돌아가시다)",
                ],
                "techniques": ["Honorific Drilling", "Active Recall", "Cultural Context"],
                "key_vocab": ["시다", "으시다", "가세요", "드세요", "주무세요", "계세요", "말씀하시다", "오세요"],
                "feynman_prompt": "Explain the difference between 먹어요, 드세요, and 드십니다. Describe the context for each.",
                "active_recall_questions": [
                    "Honorific of 가다 (present)?",
                    "What is the honorific of 먹다/마시다?",
                    "Translate: 'Please rest.' (to an elder)",
                ],
                "resources": [
                    {"name": "HTSK Lessons 42–50", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-lessons-42-50/"},
                ],
            },
            {
                "id": "U2L50",
                "title": "Unit 2 Review + Test Prep",
                "subtitle": "Consolidate lower-intermediate grammar",
                "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-test/",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Review all major Unit 2 grammar patterns",
                    "Self-assess via active recall and Feynman testing",
                    "Identify gaps for Anki/spaced repetition review",
                ],
                "techniques": ["Active Recall", "Spaced Repetition", "Self-Assessment"],
                "key_vocab": ["All Unit 2 grammar markers and extended vocabulary"],
                "feynman_prompt": "Pick your 3 weakest Unit 2 topics. Write a paragraph using each, then verify with the HTSK lesson.",
                "active_recall_questions": [
                    "List all sentence-ending patterns from Unit 2.",
                    "What are the 4 reported speech forms?",
                    "Explain passive and causative with examples.",
                ],
                "resources": [
                    {"name": "Unit 2 Test", "url": "https://www.howtostudykorean.com/unit-2-lower-intermediate-korean-grammar/unit-2-test/"},
                ],
            },
        ],
    },

    "Unit 3": {
        "title": "Intermediate Korean Grammar",
        "level": "Intermediate",
        "description": "Complex connectors, more nuanced expression, and expanded speech levels (Lessons 51–75).",
        "color": "#8E44AD",
        "url": "https://www.howtostudykorean.com/unit-3-intermediate-korean-grammar/",
        "lessons": [
            {
                "id": "U3_OVERVIEW",
                "title": "Unit 3: Intermediate Overview",
                "subtitle": "Lessons 51–75 — structure preview",
                "url": "https://www.howtostudykorean.com/unit-3-intermediate-korean-grammar/",
                "estimated_minutes": 15,
                "split": False,
                "learning_goals": [
                    "Survey the grammar covered in Unit 3",
                    "Set realistic goals for intermediate study",
                    "Review weak areas from Units 1–2 before progressing",
                ],
                "techniques": ["Goal Setting", "Spaced Repetition Review", "Active Recall"],
                "key_vocab": ["Review: all particles, endings, and connectors from Units 0–2"],
                "feynman_prompt": "Without notes, explain 10 grammar patterns from Units 1–2. Rate your confidence on each.",
                "active_recall_questions": [
                    "List all sentence-final endings you know.",
                    "What is the hardest concept from Unit 2 for you?",
                    "Set 3 specific goals for Unit 3.",
                ],
                "resources": [
                    {"name": "HTSK Unit 3", "url": "https://www.howtostudykorean.com/unit-3-intermediate-korean-grammar/"},
                    {"name": "HTSK Lessons 51–58", "url": "https://www.howtostudykorean.com/unit-3-intermediate-korean-grammar/unit-3-lessons-51-58/"},
                ],
            },
        ],
    },

    "Unit 4": {
        "title": "Upper-Intermediate Korean Grammar",
        "level": "Upper Intermediate",
        "description": "Advanced connectors, nuanced speech, expanded vocabulary (Lessons 76–100).",
        "color": "#E74C3C",
        "url": "https://www.howtostudykorean.com/upper-intermediate-korean-grammar/",
        "lessons": [
            {
                "id": "U4_OVERVIEW",
                "title": "Unit 4: Upper-Intermediate Overview",
                "subtitle": "Lessons 76–100 — structure preview",
                "url": "https://www.howtostudykorean.com/upper-intermediate-korean-grammar/",
                "estimated_minutes": 15,
                "split": False,
                "learning_goals": [
                    "Survey Unit 4 grammar scope",
                    "Assess readiness from Unit 3",
                    "Set spaced repetition review schedule",
                ],
                "techniques": ["Goal Setting", "Progress Review"],
                "key_vocab": ["Review units 1–3 vocabulary"],
                "feynman_prompt": "Summarise 5 key concepts from Unit 3 you feel confident about and 5 that need work.",
                "active_recall_questions": [
                    "What was the most useful grammar pattern from Unit 3?",
                    "What patterns do you still confuse?",
                    "Set 3 goals for Unit 4.",
                ],
                "resources": [
                    {"name": "HTSK Unit 4", "url": "https://www.howtostudykorean.com/upper-intermediate-korean-grammar/"},
                ],
            },
        ],
    },

    "Unit 5": {
        "title": "Lower-Advanced Korean Grammar",
        "level": "Lower Advanced",
        "description": "Near-natural speech patterns, complex sentence construction (Lessons 101–125).",
        "color": "#1ABC9C",
        "url": "https://www.howtostudykorean.com/unit-5/",
        "lessons": [
            {
                "id": "U5_OVERVIEW",
                "title": "Unit 5: Lower-Advanced Overview",
                "subtitle": "Lessons 101–125 — structure preview",
                "url": "https://www.howtostudykorean.com/unit-5/",
                "estimated_minutes": 15,
                "split": False,
                "learning_goals": [
                    "Survey Unit 5 grammar scope",
                    "Assess intermediate fluency",
                    "Plan immersion alongside structured study",
                ],
                "techniques": ["Goal Setting", "Immersion Planning"],
                "key_vocab": ["Review advanced connectors from Unit 4"],
                "feynman_prompt": "Describe a conversation you had in Korean (or imagined). What grammar did you use naturally?",
                "active_recall_questions": [
                    "List 5 grammar patterns that have become automatic.",
                    "List 3 patterns that still require conscious effort.",
                    "What immersion activities are you doing alongside study?",
                ],
                "resources": [
                    {"name": "HTSK Unit 5", "url": "https://www.howtostudykorean.com/unit-5/"},
                ],
            },
        ],
    },

    "Unit 6": {
        "title": "Advanced Korean Grammar",
        "level": "Advanced",
        "description": "Literary forms, advanced expression, and formal writing (Lessons 126–150).",
        "color": "#2C3E50",
        "url": "https://www.howtostudykorean.com/unit-6/",
        "lessons": [
            {
                "id": "U6_OVERVIEW",
                "title": "Unit 6: Advanced Overview",
                "subtitle": "Lessons 126–150",
                "url": "https://www.howtostudykorean.com/unit-6/",
                "estimated_minutes": 15,
                "split": False,
                "learning_goals": [
                    "Survey advanced grammar structures",
                    "Identify literary vs spoken registers",
                    "Plan reading-based immersion",
                ],
                "techniques": ["Register Analysis", "Goal Setting"],
                "key_vocab": ["Literary grammar markers overview"],
                "feynman_prompt": "What is the difference between written and spoken Korean grammar? Give two examples.",
                "active_recall_questions": [
                    "Name 3 grammar forms that are literary only.",
                    "What reading materials are you using for immersion?",
                    "Set 3 advanced goals.",
                ],
                "resources": [
                    {"name": "HTSK Unit 6", "url": "https://www.howtostudykorean.com/unit-6/"},
                ],
            },
        ],
    },

    "Unit 7": {
        "title": "Upper-Advanced Korean Grammar",
        "level": "Upper Advanced",
        "description": "Near-native complexity and nuance (Lessons 151–175).",
        "color": "#7F8C8D",
        "url": "https://www.howtostudykorean.com/unit-7/",
        "lessons": [
            {
                "id": "U7_OVERVIEW",
                "title": "Unit 7: Upper-Advanced Overview",
                "subtitle": "Lessons 151–175",
                "url": "https://www.howtostudykorean.com/unit-7/",
                "estimated_minutes": 15,
                "split": False,
                "learning_goals": [
                    "Assess near-native fluency gaps",
                    "Target nuance and register mastery",
                    "Engage in native media immersion",
                ],
                "techniques": ["Gap Analysis", "Immersion", "Native Media Engagement"],
                "key_vocab": ["Near-native vocabulary and idiomatic expressions"],
                "feynman_prompt": "Watch a Korean show without subtitles for 10 minutes. Note 5 phrases you didn't know. Look them up.",
                "active_recall_questions": [
                    "What idioms or proverbs have you learned?",
                    "Name 5 patterns from Unit 6 that were new to you.",
                    "What native Korean content are you consuming?",
                ],
                "resources": [
                    {"name": "HTSK Unit 7", "url": "https://www.howtostudykorean.com/unit-7/"},
                ],
            },
        ],
    },

    "Unit 8": {
        "title": "Near-Expert Korean Grammar",
        "level": "Near Expert",
        "description": "Expert-level expression and complete grammatical command (Lessons 176–200).",
        "color": "#C0392B",
        "url": "https://www.howtostudykorean.com/unit-8/",
        "lessons": [
            {
                "id": "U8_OVERVIEW",
                "title": "Unit 8: Near-Expert Overview",
                "subtitle": "Lessons 176–200",
                "url": "https://www.howtostudykorean.com/unit-8/",
                "estimated_minutes": 15,
                "split": False,
                "learning_goals": [
                    "Survey expert-level grammar structures",
                    "Commit to full immersion strategy",
                    "Plan TOPIK exam preparation if desired",
                ],
                "techniques": ["Expert Gap Analysis", "Immersion", "Exam Prep"],
                "key_vocab": ["Expert-level nuance markers and formal written forms"],
                "feynman_prompt": "Explain any 5 grammar points from Unit 7 with perfect precision. Note any you couldn't fully explain.",
                "active_recall_questions": [
                    "Can you write a formal email in Korean?",
                    "Can you hold a 5-minute conversation without switching to English?",
                    "What is your TOPIK goal?",
                ],
                "resources": [
                    {"name": "HTSK Unit 8", "url": "https://www.howtostudykorean.com/unit-8/"},
                    {"name": "TOPIK Info", "url": "https://www.topik.go.kr/"},
                ],
            },
        ],
    },
}

# Spaced repetition intervals (days)
SR_INTERVALS = {
    0: 1,   # New → review tomorrow
    1: 3,   # 2nd review → in 3 days
    2: 7,   # 3rd review → in 1 week
    3: 14,  # 4th review → in 2 weeks
    4: 30,  # 5th review → in 1 month
    5: 90,  # 6th review → in 3 months
}

def get_all_lessons():
    """Return a flat list of all lessons across all units."""
    lessons = []
    for unit_name, unit_data in CURRICULUM.items():
        for lesson in unit_data["lessons"]:
            lesson_copy = lesson.copy()
            lesson_copy["unit"] = unit_name
            lesson_copy["unit_title"] = unit_data["title"]
            lesson_copy["unit_color"] = unit_data["color"]
            lesson_copy["unit_level"] = unit_data["level"]
            lessons.append(lesson_copy)
    return lessons

def get_lesson_by_id(lesson_id):
    """Find a lesson by its ID."""
    for lesson in get_all_lessons():
        if lesson["id"] == lesson_id:
            return lesson
    return None

def get_unit_progress_summary(progress_data):
    """Calculate completion stats per unit."""
    summary = {}
    for unit_name, unit_data in CURRICULUM.items():
        total = len(unit_data["lessons"])
        completed = sum(
            1 for l in unit_data["lessons"]
            if progress_data.get(l["id"], {}).get("status") == "completed"
        )
        summary[unit_name] = {
            "total": total,
            "completed": completed,
            "percent": round((completed / total * 100) if total > 0 else 0, 1),
            "color": unit_data["color"],
            "title": unit_data["title"],
            "level": unit_data["level"],
        }
    return summary


# ─── TOPIK Progress Helpers ───────────────────────────────────────────────────

def get_topik_vocab_total(progress_data: dict) -> int:
    """
    Return the cumulative TOPIK I vocab count for all completed lessons.
    Uses `topik_vocab_count` field on each lesson (defaults to 0 if absent).
    Compare against TOPIK_I_TARGET (1200) to show measurable progress.
    """
    total = 0
    for unit_data in CURRICULUM.values():
        for lesson in unit_data["lessons"]:
            if progress_data.get(lesson["id"], {}).get("status") == "completed":
                total += lesson.get("topik_vocab_count", 0)
    return total


def get_topik_progress_summary(progress_data: dict) -> dict:
    """
    Return a dict with TOPIK vocab progress stats.
    {
        'words_known': int,
        'target': int (TOPIK_I_TARGET),
        'full': int (TOPIK_I_FULL),
        'percent_of_target': float,
        'percent_of_full': float,
        'ready_for_topik': bool,
    }
    """
    known = get_topik_vocab_total(progress_data)
    return {
        "words_known": known,
        "target": TOPIK_I_TARGET,
        "full": TOPIK_I_FULL,
        "percent_of_target": round(known / TOPIK_I_TARGET * 100, 1),
        "percent_of_full": round(known / TOPIK_I_FULL * 100, 1),
        "ready_for_topik": known >= TOPIK_I_TARGET,
    }
