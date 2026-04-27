"""
How to Study Korean — Full Curriculum
Built lesson-by-lesson from PDF screenshots of the HTSK website.

Each lesson contains:
  id                    : unique string e.g. "U0L1"
  title                 : lesson title
  subtitle              : one-line descriptor
  url                   : direct HTSK link
  estimated_minutes     : total reading/study time
  split                 : True if lesson should be spread across multiple blocks
  learning_goals        : list of specific measurable goals for THIS lesson
  techniques            : study techniques suited to this content
  key_vocab             : list of Korean words/forms introduced
  feynman_prompt        : one targeted Feynman-technique prompt
  active_recall_questions : list of questions (can reference prior lessons)
  resources             : list of {name, url} dicts
  topik_vocab_count     : approximate TOPIK I words introduced (int)
  knowledge_bank        : {summary: str, facts: [str]}
  expected_answers      : {question_str: answer_str}

Partial completion:
  completion_pct stored in Supabase (0-100).
  < 100 = in_progress. == 100 = completed.
"""

TOPIK_I_TARGET = 1200
TOPIK_I_FULL   = 1671

CURRICULUM = {

    "Unit 0": {
        "title": "Learning How to Read (Hangul)",
        "level": "Absolute Beginner",
        "description": "Master the Korean alphabet before touching grammar.",
        "color": "#4A90D9",
        "url": "https://www.howtostudykorean.com/unit0/",
        "lessons": [

            {
                "id": "U0L1",
                "title": "Korean Word Structure and Basic Letters",
                "subtitle": "9 consonants, 6 vowels, and how syllable blocks are built",
                "url": "https://www.howtostudykorean.com/unit0/unit0lesson1/",
                "estimated_minutes": 40,
                "split": True,
                "learning_goals": [
                    "Recognise and write the 9 basic consonants: ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅈ ㅎ",
                    "Recognise and write the 6 basic vowels: ㅣ ㅏ ㅓ ㅡ ㅜ ㅗ",
                    "Identify whether a vowel is vertically or horizontally drawn",
                    "Understand the 4 syllable block structures",
                    "Apply the rule: position 2 is always a vowel; positions 1 and 3 are always consonants",
                    "Build simple syllable blocks from consonants and vowels",
                ],
                "techniques": ["Writing Practice", "Active Recall", "Pattern Recognition"],
                "key_vocab": [
                    "ㄱ=k", "ㄴ=n", "ㄷ=d", "ㄹ=r/l", "ㅁ=m", "ㅂ=b", "ㅅ=s", "ㅈ=j", "ㅎ=h",
                    "ㅣ=i", "ㅏ=a", "ㅓ=eo", "ㅡ=eu", "ㅜ=u", "ㅗ=o",
                    "간", "법", "주", "호",
                ],
                "feynman_prompt": (
                    "Without notes, explain to an imaginary friend how to build a Korean syllable block. "
                    "Walk them through writing 법 step by step, explaining every decision."
                ),
                "active_recall_questions": [
                    "Write all 9 basic consonants and their approximate English sounds from memory.",
                    "Write all 6 basic vowels. Which three are vertical and which three are horizontal?",
                    "What are the four possible syllable block structures?",
                    "What is always in position 2 of a syllable block?",
                    "How do you write the syllable 주 (ju)? What block structure does it use?",
                    "How do you write the syllable 법 (beob)? Walk through each step.",
                    "Why is there no perfect English romanisation for Korean sounds?",
                ],
                "resources": [
                    {"name": "HTSK Unit 0 Lesson 1", "url": "https://www.howtostudykorean.com/unit0/unit0lesson1/"},
                    {"name": "Unit 0 Free PDF", "url": "https://www.howtostudykorean.com/unit0/"},
                ],
                "topik_vocab_count": 0,
                "knowledge_bank": {
                    "summary": (
                        "Korean has 9 basic consonants (ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅈ ㅎ) and 6 basic vowels "
                        "(ㅣ ㅏ ㅓ ㅡ ㅜ ㅗ). ㅣ ㅏ ㅓ are drawn vertically; ㅡ ㅜ ㅗ are drawn horizontally. "
                        "Korean is written in syllable blocks — one block = one syllable. "
                        "Position 2 is ALWAYS a vowel; positions 1 and 3 are ALWAYS consonants. "
                        "Four block shapes: vertical-no-final, vertical-with-final, "
                        "horizontal-no-final, horizontal-with-final. "
                        "There is no perfect English romanisation — the only way to learn correct "
                        "pronunciation is to listen to audio. ㄹ sounds halfway between R and L."
                    ),
                    "facts": [
                        "9 basic consonants: ㄱ(k) ㄴ(n) ㄷ(d) ㄹ(r/l) ㅁ(m) ㅂ(b) ㅅ(s) ㅈ(j) ㅎ(h).",
                        "6 basic vowels: ㅣ(i) ㅏ(a) ㅓ(eo) ㅡ(eu) ㅜ(u) ㅗ(o).",
                        "Vertical vowels: ㅣ ㅏ ㅓ. Horizontal vowels: ㅡ ㅜ ㅗ.",
                        "Position 2 in a syllable block is ALWAYS a vowel.",
                        "Positions 1 and 3 in a syllable block are ALWAYS consonants.",
                        "Vertical vowel blocks: consonant+vowel (side by side), or consonant+vowel+consonant.",
                        "Horizontal vowel blocks: consonant stacked above vowel, with or without final consonant below.",
                        "간 = ㄱ + ㅏ + ㄴ (vertical, with final consonant).",
                        "법 = ㅂ + ㅓ + ㅂ (vertical, with final consonant).",
                        "주 = ㅈ + ㅜ (horizontal, no final consonant).",
                        "호 = ㅎ + ㅗ (horizontal, no final consonant).",
                        "No perfect English romanisation exists — listening to audio is essential.",
                        "ㄹ sounds halfway between R and L — similar to 'dd' in the slang 'hadda'.",
                    ],
                },
                "expected_answers": {
                    "Write all 9 basic consonants and their sounds.": "ㄱ(k) ㄴ(n) ㄷ(d) ㄹ(r/l) ㅁ(m) ㅂ(b) ㅅ(s) ㅈ(j) ㅎ(h)",
                    "Which vowels are vertical and which are horizontal?": "Vertical: ㅣ ㅏ ㅓ. Horizontal: ㅡ ㅜ ㅗ.",
                    "What is always in position 2 of a syllable block?": "A vowel. Position 2 is always a vowel.",
                    "How do you build the syllable 법?": "ㅂ(b) + ㅓ(eo, vertical) + ㅂ(b) → consonant left, vowel right, final consonant below.",
                },
            },

            {
                "id": "U0L2",
                "title": "More Basic Korean Letters",
                "subtitle": "ㅇ (silent/ng), double consonants, and aspirated consonants",
                "url": "https://www.howtostudykorean.com/unit0/0-lesson-2/",
                "estimated_minutes": 35,
                "split": True,
                "learning_goals": [
                    "Understand ㅇ: silent in position 1, sounds 'ng' in position 3",
                    "Recognise the 5 double (tense) consonants: ㄲ ㅃ ㅉ ㄸ ㅆ",
                    "Recognise the 4 aspirated consonants: ㅋ ㅍ ㅊ ㅌ",
                    "Understand that double consonants are the base letter written twice and sound more forced",
                    "Build syllables using all new consonants with the 6 basic vowels from U0L1",
                ],
                "techniques": ["Writing Practice", "Active Recall", "Listening Practice"],
                "key_vocab": [
                    "ㅇ(silent/ng)", "ㄲ=kk", "ㅋ=k(aspirated)", "ㅃ=bb", "ㅍ=p",
                    "ㅉ=jj", "ㅊ=ch", "ㄸ=dd", "ㅌ=t", "ㅆ=ss",
                    "안=an", "운=un", "온=on", "업=eob",
                    "강=kang", "방=bang", "앙=ang", "땅=ddang", "통=tong",
                ],
                "feynman_prompt": (
                    "Explain the difference between ㄱ, ㄲ and ㅋ to someone who has never studied Korean. "
                    "Why are they hard to distinguish and what is the best way to learn them?"
                ),
                "active_recall_questions": [
                    "What two sounds does ㅇ make, and when does each apply?",
                    "Write the 5 double (tense) consonants and their romanisations.",
                    "Write the 4 aspirated consonants and their romanisations.",
                    "How is 앙 different from 강? What role does ㅇ play in each?",
                    "How is 땅 built? Walk through each letter.",
                    "From U0L1: what are the 6 basic vowels?",
                    "Why is it hard to distinguish ㄱ, ㄲ and ㅋ from each other?",
                ],
                "resources": [
                    {"name": "HTSK Unit 0 Lesson 2", "url": "https://www.howtostudykorean.com/unit0/0-lesson-2/"},
                    {"name": "Unit 0 Free PDF", "url": "https://www.howtostudykorean.com/unit0/"},
                ],
                "topik_vocab_count": 0,
                "knowledge_bank": {
                    "summary": (
                        "ㅇ in position 1 is completely silent (vowel sound leads: 안=an, 업=eob). "
                        "ㅇ in position 3 makes the 'ng' sound as in 'walking' (강=kang, 방=bang). "
                        "Both at once: 앙=ang. "
                        "Double (tense) consonants — written as two of the base letter, sound more forced: "
                        "ㄲ(kk), ㅃ(bb), ㅉ(jj), ㄸ(dd), ㅆ(ss). "
                        "Aspirated consonants — similar to base but with more air: ㅋ(k), ㅍ(p), ㅊ(ch), ㅌ(t). "
                        "Even experienced learners find ㄱ/ㄲ/ㅋ, ㅂ/ㅃ/ㅍ, ㅈ/ㅉ/ㅊ, ㄷ/ㄸ/ㅌ, ㅅ/ㅆ difficult. "
                        "Listening practice is essential."
                    ),
                    "facts": [
                        "ㅇ in position 1 is silent: 안=an, 운=un, 온=on, 업=eob.",
                        "ㅇ in position 3 sounds 'ng' (as in walking): 강=kang, 방=bang.",
                        "ㅇ can appear in both positions: 앙=ang.",
                        "Double consonants: ㄲ(kk), ㅃ(bb), ㅉ(jj), ㄸ(dd), ㅆ(ss).",
                        "Double consonants sound like their base but more tense/forced at the start.",
                        "Aspirated consonants: ㅋ(k), ㅍ(p), ㅊ(ch), ㅌ(t).",
                        "Aspirated consonants sound like their base but with a puff of air.",
                        "땅 = ㄸ + ㅏ + ㅇ (ddang).",
                        "통 = ㅌ + ㅗ + ㅇ (tong).",
                        "Distinguishing ㄱ, ㄲ and ㅋ is difficult even for advanced learners.",
                    ],
                },
                "expected_answers": {
                    "What two sounds does ㅇ make?": "In position 1 it is silent. In position 3 it makes the 'ng' sound as in 'walking'.",
                    "List the 5 double consonants.": "ㄲ(kk), ㅃ(bb), ㅉ(jj), ㄸ(dd), ㅆ(ss).",
                    "List the 4 aspirated consonants.": "ㅋ(k), ㅍ(p), ㅊ(ch), ㅌ(t).",
                    "How is 앙 built?": "ㅇ (silent, position 1) + ㅏ (vowel) + ㅇ (ng, position 3) = 앙.",
                },
            },

            {
                "id": "U0L3",
                "title": "Korean Diphthongs: Complex Vowels",
                "subtitle": "Y-vowels, compound vowels, 4-letter syllables, loanwords",
                "url": "https://www.howtostudykorean.com/unit0/unit-0-lesson-3/",
                "estimated_minutes": 35,
                "split": True,
                "learning_goals": [
                    "Recognise and use the 4 Y-vowels: ㅑ(ya) ㅕ(yeo) ㅠ(yu) ㅛ(yo)",
                    "Recognise ㅐ(ae) and ㅔ(e) and understand they sound identical in modern Korean",
                    "Recognise the compound vowels: ㅟ(wi) ㅝ(wo) ㅚ(oe) ㅘ(wa) ㅢ(ui) ㅖ(ye)",
                    "Recognise the rare vowels: ㅙ(wae) ㅒ(yae) ㅞ(we)",
                    "Understand 4-letter syllable blocks with double final consonants",
                    "Read simple Korean loanwords from English",
                ],
                "techniques": ["Reading Practice", "Active Recall", "Pattern Recognition"],
                "key_vocab": [
                    "ㅑ=ya", "ㅕ=yeo", "ㅠ=yu", "ㅛ=yo",
                    "ㅐ=ae", "ㅔ=e",
                    "ㅟ=wi", "ㅝ=wo", "ㅚ=oe(way)", "ㅘ=wa", "ㅢ=ui", "ㅖ=ye",
                    "ㅙ=wae", "ㅒ=yae", "ㅞ=we",
                    "닭=chicken", "앉다=to sit", "읽다=to read", "없다=to not have", "긁다=to scratch",
                    "호텔=hotel", "소파=sofa", "텔레비전=television", "라디오=radio",
                    "게임=game", "피자=pizza", "햄버거=hamburger", "택시=taxi", "샤워=shower", "카드=card",
                ],
                "feynman_prompt": (
                    "Without notes, explain how Y-vowels are formed and give one syllable example for each. "
                    "Then explain what a 4-letter syllable block is and give two examples from the lesson."
                ),
                "active_recall_questions": [
                    "How are the 4 Y-vowels formed? Write them with their romanisations.",
                    "Do ㅐ and ㅔ sound different in modern Korean? What do they both sound like?",
                    "Write the compound vowel formed from ㅜ + ㅣ. What does it sound like?",
                    "Write the compound vowel formed from ㅗ + ㅏ. Give an example syllable.",
                    "What is a 4-letter syllable? Give two examples.",
                    "From U0L2: what sound does ㅇ make in position 3?",
                    "Read this loanword: 텔레비전. What English word is it?",
                    "Read this loanword: 햄버거. What English word is it?",
                    "If you see the syllable 관, how many letters does it have? What are they?",
                ],
                "resources": [
                    {"name": "HTSK Unit 0 Lesson 3", "url": "https://www.howtostudykorean.com/unit0/unit-0-lesson-3/"},
                    {"name": "Unit 0 Free PDF", "url": "https://www.howtostudykorean.com/unit0/"},
                ],
                "topik_vocab_count": 5,
                "knowledge_bank": {
                    "summary": (
                        "Y-vowels add an extra line to basic vowels: ㅏ→ㅑ(ya), ㅓ→ㅕ(yeo), ㅜ→ㅠ(yu), ㅗ→ㅛ(yo). "
                        "ㅐ(ae) and ㅔ(e) look different but sound identical in modern Korean — both like 'ay' in 'weigh'. "
                        "Compound vowels combine two vowels: ㅜ+ㅣ=ㅟ(wi), ㅜ+ㅓ=ㅝ(wo), ㅗ+ㅣ=ㅚ(oe/way), "
                        "ㅗ+ㅏ=ㅘ(wa), ㅡ+ㅣ=ㅢ(ui), ㅕ+ㅣ=ㅖ(ye). "
                        "Rare vowels: ㅙ(wae), ㅒ(yae), ㅞ(we). "
                        "4-letter syllables have two final consonants: 닭(chicken), 앉다(to sit), 읽다(to read), "
                        "없다(to not have), 긁다(to scratch). "
                        "Compound vowels count as ONE letter (관 = ㄱ+ㅘ+ㄴ, three letters). "
                        "Double consonants count as ONE letter (있 = ㅇ+ㅣ+ㅆ, three letters). "
                        "Korean loanwords: 호텔(hotel), 소파(sofa — no f sound), 텔레비전(television), 피자(pizza), "
                        "햄버거(hamburger), 택시(taxi), 게임(game)."
                    ),
                    "facts": [
                        "Y-vowels: ㅑ(ya), ㅕ(yeo), ㅠ(yu), ㅛ(yo) — each formed by adding a line to ㅏ, ㅓ, ㅜ, ㅗ.",
                        "ㅐ and ㅔ sound identical in modern Korean — both like 'ay' in 'weigh'.",
                        "ㅜ+ㅣ=ㅟ(wi), ㅜ+ㅓ=ㅝ(wo), ㅗ+ㅣ=ㅚ(oe/way), ㅗ+ㅏ=ㅘ(wa), ㅡ+ㅣ=ㅢ(ui), ㅕ+ㅣ=ㅖ(ye).",
                        "Rare vowels: ㅙ(wae), ㅒ(yae), ㅞ(we).",
                        "4-letter syllables: one vowel and three consonants (two finals).",
                        "닭=chicken, 앉다=to sit, 읽다=to read, 없다=to not have, 긁다=to scratch.",
                        "Compound vowels count as one letter: 관 = ㄱ+ㅘ+ㄴ (three letters total).",
                        "Double consonants count as one letter: 있 = ㅇ+ㅣ+ㅆ (three letters total).",
                        "Loanwords: 호텔(hotel), 소파(sofa), 텔레비전(television), 피자(pizza), 햄버거(hamburger).",
                        "Korean has no 'f' sound — sofa becomes 소파.",
                    ],
                },
                "expected_answers": {
                    "How are Y-vowels formed?": "By adding one extra line: ㅏ→ㅑ(ya), ㅓ→ㅕ(yeo), ㅜ→ㅠ(yu), ㅗ→ㅛ(yo).",
                    "Do ㅐ and ㅔ sound different?": "No — in modern Korean they sound identical, both like 'ay' in 'weigh'.",
                    "What is ㅘ made from?": "ㅗ + ㅏ = ㅘ (wa). Example: 와.",
                    "How many letters in 관?": "Three: ㄱ + ㅘ + ㄴ. ㅘ is one letter even though it is made from two vowels.",
                },
            },

        ],
    },

    "Unit 1": {
        "title": "Basic Korean Grammar",
        "level": "Beginner",
        "description": "Core sentence structure, particles, verbs, adjectives and essential vocabulary.",
        "color": "#E74C3C",
        "url": "https://www.howtostudykorean.com/unit1/",
        "lessons": [

            {
                "id": "U1L1",
                "title": "Basic Korean Sentences",
                "subtitle": "이다, subject/object particles ~는/은 ~를/을, this/that, core vocab",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-1/",
                "estimated_minutes": 40,
                "split": True,
                "learning_goals": [
                    "Understand Korean sentence word order: Subject–Object–Verb / Subject–Adjective",
                    "Use subject particle ~는/은 and object particle ~를/을 correctly",
                    "Understand 이다 (to be) and how it attaches directly to a noun without a space",
                    "Know that 이다 is NOT used with adjectives",
                    "Know the difference between 이/그/저 (determiners) and 이것/그것/저것 (pronouns)",
                    "Know the difference between 나 (informal I) and 저 (formal I)",
                    "Memorise the core greeting words",
                    "Recognise the core vocabulary list for this lesson",
                ],
                "techniques": ["Active Recall", "Sentence Building", "Vocabulary Memorisation"],
                "key_vocab": [
                    "한국=Korea", "도시=city", "이름=name", "저=I(formal)", "나=I(informal)",
                    "남자=man", "여자=woman", "이=this(det)", "그=that(context)", "저=that(far)",
                    "것=thing", "이것=this thing", "그것=that thing", "저것=that thing",
                    "의자=chair", "탁자=table", "선생님=teacher", "침대=bed", "집=house",
                    "차=car", "사람=person", "책=book", "컴퓨터=computer", "나무=tree/wood",
                    "소파=sofa", "중국=China", "일본=Japan", "문=door", "의사=doctor", "학생=student",
                    "이다=to be", "네=yes", "아니=no",
                    "안녕하세요=hello", "감사합니다=thank you(formal)",
                    "감사해요=thank you", "고마워=thanks(informal)",
                    "잘 지내세요?=how are you?", "제발=please",
                ],
                "feynman_prompt": (
                    "Without notes, explain why 이다 is NOT used in 'I am pretty' in Korean "
                    "but IS used in 'I am a teacher'. Write one sentence of each type in Korean."
                ),
                "active_recall_questions": [
                    "What is the basic Korean sentence word order?",
                    "When do you use ~는 vs ~은 as the subject particle?",
                    "When do you use ~를 vs ~을 as the object particle?",
                    "Write 'I am a teacher' in Korean using 나.",
                    "Write 'That person is a doctor' in Korean.",
                    "Write 'This thing is a table' in Korean.",
                    "What is the difference between 그 사람 and 그것?",
                    "What is the difference between 그 and 저 when saying 'that'?",
                    "Why is 이다 NOT used in sentences like 나는 아름답다?",
                    "Does 이다 attach to a noun with or without a space?",
                    "What are the two ways to say 'I' in Korean, and when do you use each?",
                    "From U0L3: read the loanword 소파. What does it mean?",
                ],
                "resources": [
                    {"name": "HTSK Unit 1 Lesson 1", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-1/"},
                ],
                "topik_vocab_count": 32,
                "knowledge_bank": {
                    "summary": (
                        "Korean sentence order: Subject–Object–Verb or Subject–Adjective. "
                        "Every sentence must end in a verb, adjective, or 이다. "
                        "~는/은 marks the subject (는 after vowel, 은 after consonant). "
                        "~를/을 marks the object (를 after vowel, 을 after consonant). "
                        "이다 = 'to be', used when noun = noun. Attaches directly with NO space (남자이다). "
                        "이다 is NOT used with adjectives — 'is/am/are' is built into Korean adjectives. "
                        "이/그/저 are determiners before nouns (이 사람 = this person). "
                        "이것/그것/저것 are pronouns (this thing / that thing). "
                        "그 = 'that' from prior context. 저 = 'that' visible but out of reach. "
                        "나 = informal 'I'. 저 = formal 'I'. "
                        "Greetings: 안녕하세요(hello), 감사합니다(thank you), 잘 지내세요?(how are you?), 제발(please)."
                    ),
                    "facts": [
                        "Korean word order: Subject – Object – Verb (or Subject – Adjective).",
                        "Every Korean sentence must end in a verb, adjective, or 이다.",
                        "~는 after vowel-ending subjects; ~은 after consonant-ending subjects.",
                        "~를 after vowel-ending objects; ~을 after consonant-ending objects.",
                        "이다 = 'to be' — connects noun = noun.",
                        "이다 attaches directly to the noun with NO space: 남자이다, NOT 남자 이다.",
                        "이다 is NOT used with adjectives.",
                        "이 = this (within reach); 그 = that (from prior context); 저 = that (visible but far).",
                        "이것 = this thing; 그것 = that thing; 저것 = that thing (compound words, no space).",
                        "나 = informal I/me; 저 = formal I/me.",
                        "나는 남자이다 = I am a man.",
                        "그 사람은 의사이다 = That person is a doctor.",
                        "이것은 탁자이다 = This thing is a table.",
                        "저것은 침대이다 = That thing is a bed.",
                    ],
                },
                "expected_answers": {
                    "What is Korean word order?": "Subject – Object – Verb, or Subject – Adjective. Every sentence ends in a verb, adjective, or 이다.",
                    "When do you use ~는 vs ~은?": "~는 after a word ending in a vowel; ~은 after a word ending in a consonant.",
                    "Write 'I am a teacher' using 나.": "나는 선생님이다",
                    "Why is 이다 not used with adjectives?": "'Is/am/are' is already built into Korean adjectives. 이다 is only for noun = noun.",
                    "What is the difference between 그 and 저?": "그 = that (from prior context). 저 = that (visible but too far to touch).",
                },
            },

            {
                "id": "U1L2",
                "title": "Korean Particles 이/가",
                "subtitle": "있다 (to have/location), ~에 particle, position words, 이/가 vs 는/은",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-2/",
                "estimated_minutes": 40,
                "split": True,
                "learning_goals": [
                    "Use 있다 meaning 'to have' with ~이/가 on the possessed item (not ~을/를)",
                    "Use 있다 meaning 'to be at a location' with ~에 on the place",
                    "Use the ~에 particle to mark location",
                    "Use position words (안 위 밑 옆 뒤 앞) with ~에",
                    "Attach ~이/가 correctly: 이 after consonant, 가 after vowel",
                    "Understand the nuance difference between ~이/가 and ~는/은 as subject markers",
                    "Recognise the new vocabulary for this lesson",
                ],
                "techniques": ["Active Recall", "Sentence Building", "Pattern Comparison"],
                "key_vocab": [
                    "나라=country", "가방=bag/backpack", "창문=window", "잡지=magazine",
                    "방=room", "냉장고=refrigerator", "개=dog", "강아지=puppy",
                    "고양이=cat", "쥐=rat/mouse", "펜=pen", "전화기=phone",
                    "커피=coffee", "식당=restaurant", "건물=building", "텔레비전=television",
                    "미국=USA", "캐나다=Canada", "호텔=hotel", "학교=school", "은행=bank",
                    "안=inside", "위=on top", "밑=below", "옆=beside", "뒤=behind", "앞=in front", "여기=here",
                    "있다=to have / to be at a location",
                ],
                "feynman_prompt": (
                    "Without notes, explain why 나는 펜을 있다 is wrong and write the correct version. "
                    "Then explain the difference between 나는 학교가 있다 and 나는 학교에 있다."
                ),
                "active_recall_questions": [
                    "있다 has two meanings — what are they?",
                    "Write 'I have a pen' in Korean. Why 이/가 and not 을/를?",
                    "Write 'I am at school' in Korean.",
                    "What does the particle ~에 indicate?",
                    "Write 'The cat is under the chair' in Korean.",
                    "Write 'The restaurant is next to the bank' in Korean.",
                    "Write 'I am inside the bank' in Korean.",
                    "What is the nuance difference between ~는/은 and ~이/가 as subject markers?",
                    "When do you use ~이 vs ~가?",
                    "From U1L1: write 'That person is a doctor' in Korean.",
                    "Can ~에 appear twice in one sentence? Give an example of when this would happen.",
                ],
                "resources": [
                    {"name": "HTSK Unit 1 Lesson 2", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-2/"},
                ],
                "topik_vocab_count": 28,
                "knowledge_bank": {
                    "summary": (
                        "있다 has two usages. (1) To have (adjective): the possessed item takes ~이/가, "
                        "NOT ~을/를 — e.g. 나는 펜이 있다 = I have a pen. "
                        "(2) To be at a location (verb): place takes ~에 — e.g. 나는 학교에 있다 = I am at school. "
                        "~에 marks place or time. "
                        "Position words (안=inside, 위=on top, 밑=below, 옆=beside, 뒤=behind, 앞=in front) "
                        "follow a noun and take ~에: 학교 앞에 = in front of the school. "
                        "~이 after consonant-ending nouns; ~가 after vowel-ending nouns. "
                        "~이/가 and ~는/은 both mark the subject. "
                        "~는/은 implies comparison/contrast. ~이/가 states a neutral fact. "
                        "안 can be omitted when inside-ness is obvious: "
                        "커피가 냉장고에 있다 = the coffee is in the fridge."
                    ),
                    "facts": [
                        "있다 = to have (adjective) OR to be at a location (verb).",
                        "있다 'to have': possessed item takes ~이/가, NOT ~을/를.",
                        "나는 펜이 있다 = I have a pen.",
                        "나는 차가 있다 = I have a car.",
                        "있다 'to be at a location': place takes ~에.",
                        "나는 학교에 있다 = I am at school.",
                        "나는 캐나다에 있다 = I am in Canada.",
                        "~에 marks place or time.",
                        "Position words: 안(inside), 위(on top), 밑(below), 옆(beside), 뒤(behind), 앞(in front).",
                        "Position words follow a noun and take ~에: 학교 앞에 = in front of the school.",
                        "~이 after consonant; ~가 after vowel.",
                        "~는/은 = comparison/contrast implied. ~이/가 = neutral fact.",
                        "고양이는 집 뒤에 있다 = The cat is behind the house (comparison implied).",
                        "고양이가 집 뒤에 있다 = The cat is behind the house (neutral fact).",
                        "커피가 냉장고에 있다 = The coffee is in the fridge (안 omitted).",
                        "개는 집 안에 있다 = The dog is in the house.",
                        "식당은 은행 옆에 있다 = The restaurant is next to the bank.",
                    ],
                },
                "expected_answers": {
                    "Write 'I have a pen' in Korean.": "나는 펜이 있다 (이, not 을 — 있다 is an adjective and cannot take an object particle).",
                    "Write 'I am at school' in Korean.": "나는 학교에 있다",
                    "Write 'The dog is in the house'.": "개는 집 안에 있다",
                    "Nuance difference between ~는/은 and ~이/가?": "~는/은 implies comparison or contrast. ~이/가 states a neutral fact with no comparison.",
                    "When do you use ~이 vs ~가?": "~이 after a noun ending in a consonant; ~가 after a noun ending in a vowel.",
                },
            },

            {
                "id": "U1L3",
                "title": "Korean Verbs and Adjectives",
                "subtitle": "Verb/adjective rules, ~의 possessive, 좋다 vs 좋아하다, 우리",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-3/",
                "estimated_minutes": 40,
                "split": True,
                "learning_goals": [
                    "Know that every Korean verb and adjective ends in 다",
                    "Know that verbs ending in ~하다 can drop 하다 to form the noun",
                    "Build verb sentences: Subject~는/은 + Object~를/을 + Verb",
                    "Build adjective sentences: Subject~는/은 + Adjective (no object, no 이다)",
                    "Use ~의 as a possessive particle",
                    "Understand the difference between 좋다 (adjective: good) and 좋아하다 (verb: to like)",
                    "Use 우리 (we/us/our) correctly",
                    "Recognise the new vocabulary for this lesson",
                ],
                "techniques": ["Active Recall", "Sentence Building", "Contrast Practice"],
                "key_vocab": [
                    "음식=food", "케이크=cake", "공항=airport", "병원=hospital", "공원=park",
                    "한국어=Korean language", "머리=head", "다리=leg", "손가락=finger",
                    "귀=ear", "팔=arm", "눈=eye", "입=mouth/lips", "배=stomach", "버스=bus", "배=boat",
                    "우리=we/us/our",
                    "먹다=to eat", "가다=to go", "만나다=to meet", "닫다=to close", "열다=to open",
                    "원하다=to want", "만들다=to make", "하다=to do", "말하다=to speak",
                    "이해하다=to understand", "좋아하다=to like",
                    "크다=big", "작다=small", "새롭다=new", "낡다=old(not age)", "비싸다=expensive",
                    "싸다=cheap", "아름답다=beautiful", "뚱뚱하다=fat", "길다=long", "좋다=good",
                    "아주=very", "매우=very", "너무=too/very",
                ],
                "feynman_prompt": (
                    "Without notes, explain the difference between 좋다 and 좋아하다. "
                    "Write one correct sentence with each, showing why one takes an object and the other does not."
                ),
                "active_recall_questions": [
                    "What syllable does every Korean verb and adjective end in?",
                    "What do you get when you remove 하다 from 말하다? What does it mean?",
                    "Write 'I eat food' in Korean using correct particles.",
                    "Write 'I go to the park' — what particle does 공원 take?",
                    "Write 'This bus is big' in Korean. Does it use 이다?",
                    "Why do Korean adjective sentences not need 이다?",
                    "Write 'My book' in Korean using ~의.",
                    "Write 'The teacher's car' in Korean.",
                    "What is the difference between 좋다 and 좋아하다?",
                    "Write 'I like this food' using 좋아하다.",
                    "Write 'This food is good' using 좋다.",
                    "From U1L2: write 'I have a magazine' in Korean.",
                    "What does 우리 mean and does it change form between subject and object?",
                ],
                "resources": [
                    {"name": "HTSK Unit 1 Lesson 3", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-3/"},
                ],
                "topik_vocab_count": 35,
                "knowledge_bank": {
                    "summary": (
                        "Every Korean verb and adjective ends in 다 — 100% of the time. "
                        "Words ending in ~하다 are typically Chinese-origin. Removing 하다 gives the noun: "
                        "말하다→말(speech), 이해하다→이해(understanding). "
                        "Verb structure: Subject~는/은 + Object~를/을 + Verb. "
                        "Adjective structure: Subject~는/은 + Adjective. No object. No 이다. "
                        "'Is/am/are' is built into Korean adjectives — 나는 아름답다 = I am beautiful. "
                        "~의 is the possessive particle: 저의 책 = my book. Commonly omitted with 우리. "
                        "좋다 = adjective 'good' — cannot take an object. "
                        "좋아하다 = verb 'to like' — takes an object with ~을/를. "
                        "우리 = we/us/our — same form for subject and object. "
                        "Formal version of 우리 is 저희 but 우리 is acceptable even formally."
                    ),
                    "facts": [
                        "Every Korean verb and adjective ends in 다.",
                        "Removing 하다 from a ~하다 verb gives the noun form: 말하다→말, 이해하다→이해.",
                        "Verb sentence: Subject~는/은 + Object~를/을 + Verb.",
                        "Adjective sentence: Subject~는/은 + Adjective (no object, no 이다).",
                        "나는 아름답다 = I am beautiful (이다 NOT used).",
                        "이 버스는 크다 = This bus is big.",
                        "나는 공원에 가다 = I go to the park (가다 takes ~에).",
                        "나는 문을 닫다 = I close the door.",
                        "나는 창문을 열다 = I open the window.",
                        "나는 케이크를 만들다 = I make a cake.",
                        "~의 marks possession: 저의 책 = my book, 선생님의 차 = the teacher's car.",
                        "~의 is often omitted — especially with 우리: 우리 집 = our house.",
                        "좋다 = adjective 'good' (cannot act on an object).",
                        "좋아하다 = verb 'to like' (takes object with ~을/를).",
                        "이 음식은 좋다 = This food is good.",
                        "나는 이 음식을 좋아하다 = I like this food.",
                        "우리 = we/us/our — same form regardless of position in sentence.",
                        "우리 집은 크다 = Our house is big.",
                    ],
                },
                "expected_answers": {
                    "What does every verb and adjective end in?": "다 — 100% of the time.",
                    "Write 'I eat food' in Korean.": "저는 음식을 먹다",
                    "Write 'This bus is big' in Korean.": "이 버스는 크다 (no 이다 — not used with adjectives)",
                    "Difference between 좋다 and 좋아하다?": "좋다 is an adjective meaning 'good' — no object. 좋아하다 is a verb meaning 'to like' — takes ~을/를 object.",
                    "Write 'I like this food'.": "나는 이 음식을 좋아하다",
                    "Write 'my book' using ~의.": "저의 책",
                },
            },

        ],
    },
}

# ─── Spaced repetition intervals (days) ──────────────────────────────────────
SR_INTERVALS = {
    0: 1,
    1: 3,
    2: 7,
    3: 14,
    4: 30,
    5: 90,
}

# ─── Helpers ──────────────────────────────────────────────────────────────────

def get_all_lessons():
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
    for lesson in get_all_lessons():
        if lesson["id"] == lesson_id:
            return lesson
    return None


def get_unit_progress_summary(progress_data):
    summary = {}
    for unit_name, unit_data in CURRICULUM.items():
        total = len(unit_data["lessons"])
        completed = sum(
            1 for l in unit_data["lessons"]
            if progress_data.get(l["id"], {}).get("completion_pct", 0) == 100
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


def get_topik_vocab_total(progress_data: dict) -> int:
    total = 0
    for unit_data in CURRICULUM.values():
        for lesson in unit_data["lessons"]:
            if progress_data.get(lesson["id"], {}).get("completion_pct", 0) == 100:
                total += lesson.get("topik_vocab_count", 0)
    return total


def get_topik_progress_summary(progress_data: dict) -> dict:
    known = get_topik_vocab_total(progress_data)
    return {
        "words_known": known,
        "target": TOPIK_I_TARGET,
        "full": TOPIK_I_FULL,
        "percent_of_target": round(known / TOPIK_I_TARGET * 100, 1),
        "percent_of_full": round(known / TOPIK_I_FULL * 100, 1),
        "ready_for_topik": known >= TOPIK_I_TARGET,
    }
