"""
How to Study Korean - Full Curriculum
Units 0-8 with lesson metadata, learning goals, techniques, and time estimates.
Lessons exceeding ~25 min are split into Part A / Part B.
"""

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
