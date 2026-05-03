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

            {
                "id": "U1L4",
                "title": "Korean Adjectives ~ㄴ/은",
                "subtitle": "Describing nouns with adjectives, 많다, and particle ~도",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-4/",
                "estimated_minutes": 45,
                "split": True,
                "learning_goals": [
                    "Understand that adjectives have a stem (remove ~다) and can describe nouns by adding ~ㄴ (vowel stems) or ~은 (consonant stems)",
                    "Distinguish between an adjective predicating a sentence (음식은 비싸다) vs describing a noun (비싼 음식)",
                    "Know the ~있다 exception: adjectives ending in ~있다 use ~는 instead (재미있는, 맛있는)",
                    "Use 많다 both as a predicate (사람이 많다) and as a descriptor (많은 돈)",
                    "Use particle ~도 correctly to mean 'too/also', understanding it replaces 는/은 or 를/을 depending on what is being emphasised",
                ],
                "techniques": ["Active Recall", "Sentence Building", "Contrast Practice"],
                "key_vocab": [
                    "길=street", "거리=street/road", "손=hand", "영어=English", "택시=taxi",
                    "열차=train", "역=train/subway station", "버스 정류장=bus stop", "비행기=airplane",
                    "자전거=bicycle", "아내=wife", "아이=child", "아들=son", "딸=daughter",
                    "남편=husband", "아버지=father", "어머니=mother", "편지=letter", "맛=taste",
                    "식사=meal", "아침=morning", "아침식사=breakfast", "물=water", "사과=apple", "돈=money",
                    "오다=to come", "끝내다=to finish", "춤추다=to dance", "알다=to know",
                    "걷다=to walk", "배우다=to learn", "연습하다=to practice", "생각하다=to think", "살다=to live",
                    "위험하다=to be dangerous", "잘생기다=to be handsome", "못생기다=to be ugly",
                    "피곤하다=to be tired", "다르다=to be different", "슬프다=to be sad",
                    "맛있다=to be delicious", "재미있다=to be fun/funny", "많다=to be many/a lot",
                    "행복하다=to be happy", "거기=there", "저기=there(far)", "지금=now", "하지만=but",
                    "안녕히 가세요=goodbye(to someone leaving)",
                    "안녕히 계세요=goodbye(to someone staying)",
                    "만나서 반갑습니다=nice to meet you",
                    "실례합니다=excuse me", "죄송합니다=sorry",
                ],
                "feynman_prompt": (
                    "Without notes, explain the difference between 음식은 비싸다 and 비싼 음식. "
                    "Why is the second one not a complete sentence? Then write two sentences "
                    "that use 비싼 as a descriptor, with a verb predicating the sentence."
                ),
                "active_recall_questions": [
                    "What do you add to an adjective stem ending in a vowel to describe a noun?",
                    "What do you add to an adjective stem ending in a consonant to describe a noun?",
                    "Is 비싼 음식 a complete sentence? Why or why not?",
                    "Write 'I want a big boat' in Korean.",
                    "Write 'I go to the small house' in Korean.",
                    "How do you make 맛있다 describe a noun? What is the rule and why is it different?",
                    "Write 'I eat delicious food' using 맛있다 as a descriptor.",
                    "Write 'There are a lot of people' using 많다 as a predicate.",
                    "Write 'I have a lot of money' using 많다 as a descriptor.",
                    "What does ~도 mean, and what particles does it replace?",
                    "Write 'I speak Korean too' (emphasising that you also speak it, in addition to others).",
                    "Write 'I also speak Korean' (emphasising Korean in addition to other languages).",
                    "From U1L3: what is the difference between 좋다 and 좋아하다?",
                ],
                "resources": [
                    {"name": "HTSK Unit 1 Lesson 4", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-4/"},
                ],
                "topik_vocab_count": 38,
                "knowledge_bank": {
                    "summary": (
                        "To use an adjective to describe a noun (not predicate a sentence), remove ~다 to get the stem "
                        "and add ~ㄴ (vowel stems) or ~은 (consonant stems). "
                        "크다→큰, 비싸다→비싼, 작다→작은, 좋다→좋은, 많다→많은. "
                        "Key distinction: 음식은 비싸다 = the food is expensive (full sentence, predicate). "
                        "비싼 음식 = expensive food (descriptor only — NOT a sentence on its own). "
                        "Exception: adjectives ending in ~있다 use ~는 instead of ~ㄴ/은: "
                        "맛있다→맛있는, 재미있다→재미있는. "
                        "많다 as predicate: 사람이 많다 = there are a lot of people. "
                        "많다 as descriptor: 많은 돈 = a lot of money. "
                        "Particle ~도 means 'too/also/as well' and replaces ~는/은 (subject) or ~를/을 (object). "
                        "저도 한국어를 말하다 = I speak Korean too (emphasising the subject — I also do it). "
                        "저는 한국어도 말하다 = I speak Korean too (emphasising the object — Korean among other languages). "
                        "Whatever ~도 is attached to is the thing being expressed as 'too'."
                    ),
                    "facts": [
                        "To describe a noun: remove ~다, add ~ㄴ (vowel stem) or ~은 (consonant stem).",
                        "크다→큰(big), 비싸다→비싼(expensive), 싸다→싼(cheap).",
                        "작다→작은(small), 좋다→좋은(good), 많다→많은(many/a lot).",
                        "잘생기다→잘생긴(handsome), 뚱뚱하다→뚱뚱한(fat), 행복하다→행복한(happy).",
                        "Exception: ~있다 adjectives use ~는: 맛있다→맛있는, 재미있다→재미있는.",
                        "비싼 음식 = expensive food (NOT a sentence — needs a predicate verb or adjective).",
                        "나는 비싼 음식을 먹다 = I eat expensive food (verb 먹다 predicates the sentence).",
                        "비싼 음식은 맛있다 = Expensive food is delicious (adjective 맛있다 predicates).",
                        "많다 as predicate: 사람이 많다 = there are a lot of people (이/가 on subject).",
                        "많다 as descriptor: 많은 돈 = a lot of money, 많은 음식 = a lot of food.",
                        "~도 replaces ~는/은 or ~를/을 to mean 'too/also'.",
                        "저도 한국어를 말하다 = I speak Korean too (I, in addition to others).",
                        "저는 한국어도 말하다 = I speak Korean too (Korean, in addition to other languages).",
                        "나도 피곤하다 = I am tired too.",
                        "나의 딸도 행복하다 = My daughter is happy too.",
                        "행복한 여자는 작은 차 안에 있다 = The happy girl is inside the small car.",
                    ],
                    "grammar_rules": [
                        "RULE: adjective descriptor form = stem + ~ㄴ (if stem ends in vowel) or ~은 (if stem ends in consonant).",
                        "RULE: 크다 stem=크(vowel) → 큰. 비싸다 stem=비싸(vowel) → 비싼. 싸다 stem=싸(vowel) → 싼.",
                        "RULE: 작다 stem=작(consonant) → 작은. 좋다 stem=좋(consonant) → 좋은. 많다 stem=많(consonant) → 많은.",
                        "RULE: adjectives ending in ~있다 are an exception — always use ~는, never ~ㄴ/은. 맛있다→맛있는, 재미있다→재미있는.",
                        "RULE: 있다-ending adjectives NEVER take ~은 or ~ㄴ as a descriptor. 맛있은 and 맛있ㄴ are WRONG.",
                        "RULE: an adjective descriptor phrase (e.g. 큰 집) is NOT a complete sentence. A predicate verb or adjective must follow.",
                        "RULE: 많다 as predicate requires ~이/가 on the subject (사람이 많다), NOT ~는/은.",
                        "RULE: ~도 replaces ~는/은 when the subject is being marked as 'also'. It replaces ~를/을 when the object is being marked as 'also'.",
                        "RULE: ~도 cannot coexist with ~는/은 or ~를/을 on the same noun — it fully replaces them.",
                        "RULE: grammar conjugation taught in this lesson (U1L1–U1L4) uses dictionary/unconjugated verb forms only. Conjugation is taught in Lesson 5.",
                    ],
                    "example_sentences": [
                        {"korean": "나는 큰 배를 원하다", "english": "I want a big boat", "notes": "크다→큰 (vowel stem + ~ㄴ)"},
                        {"korean": "나는 작은 집에 가다", "english": "I go to the small house", "notes": "작다→작은 (consonant stem + ~은)"},
                        {"korean": "나는 잘생긴 남자를 만나다", "english": "I meet a handsome man", "notes": "잘생기다→잘생긴 (vowel stem + ~ㄴ)"},
                        {"korean": "나는 많은 돈이 있다", "english": "I have a lot of money", "notes": "많다→많은 as descriptor"},
                        {"korean": "사람이 많다", "english": "There are a lot of people", "notes": "많다 as predicate; subject takes ~이/가"},
                        {"korean": "음식이 많다", "english": "There is a lot of food", "notes": "많다 as predicate"},
                        {"korean": "나는 맛있는 음식을 먹다", "english": "I eat delicious food", "notes": "맛있다→맛있는 (~있다 exception: use ~는)"},
                        {"korean": "그 남자는 재미있는 남자이다", "english": "That man is a funny man", "notes": "재미있다→재미있는 (~있다 exception)"},
                        {"korean": "행복한 여자는 작은 차 안에 있다", "english": "The happy girl is inside the small car", "notes": "두 adjective descriptors in one sentence"},
                        {"korean": "저도 한국어를 말하다", "english": "I speak Korean too (I also do it)", "notes": "~도 on subject — emphasises that I too speak Korean"},
                        {"korean": "저는 한국어도 말하다", "english": "I speak Korean too (among other languages)", "notes": "~도 on object — emphasises Korean among other languages"},
                        {"korean": "나도 피곤하다", "english": "I am tired too", "notes": "~도 replaces ~는 on subject"},
                    ],
                    "common_mistakes": [
                        "Writing 맛있은 instead of 맛있는 — ~있다 adjectives always use ~는, never ~은.",
                        "Writing 재미있ㄴ instead of 재미있는 — same ~있다 exception applies.",
                        "Treating 큰 집 as a complete sentence — it is a noun phrase only; a predicate is required.",
                        "Using 사람은 많다 instead of 사람이 많다 — 많다 as predicate requires ~이/가 on the subject.",
                        "Writing 저도는 or 저는도 — ~도 fully replaces ~는/은; they cannot both appear on the same noun.",
                        "Using ~ㄴ on a consonant-ending stem: e.g. 작ㄴ — wrong, must be 작은.",
                        "Using ~은 on a vowel-ending stem: e.g. 크은 — wrong, must be 큰.",
                        "Confusing the predicate form (음식은 비싸다) with the descriptor form (비싼 음식) — they are structurally different.",
                    ],
                },
                "expected_answers": {
                    "What do you add to a vowel-ending stem to describe a noun?": "~ㄴ — e.g. 크다→큰.",
                    "What do you add to a consonant-ending stem to describe a noun?": "~은 — e.g. 작다→작은.",
                    "Is 비싼 음식 a complete sentence?": "No — it is a noun phrase (expensive food). It needs a predicate verb or adjective to be a sentence.",
                    "How do you make 맛있다 describe a noun?": "Use ~는 instead of ~ㄴ/은: 맛있는. This applies to all adjectives ending in ~있다.",
                    "Write 'there are a lot of people'.": "사람이 많다 (이/가 on subject, 많다 predicates).",
                    "Difference between 저도 한국어를 말하다 and 저는 한국어도 말하다?": "First: I also speak Korean (subject emphasised). Second: I speak Korean too, among other languages (object emphasised).",
                },
            },

            {
                "id": "U1L5",
                "title": "Korean Conjugation: Past, Present, Future",
                "subtitle": "Plain/diary form conjugation across all three tenses",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-5/",
                "estimated_minutes": 50,
                "split": True,
                "learning_goals": [
                    "Conjugate verbs to present tense (plain form): consonant stem + ~는다, vowel stem + ~ㄴ다",
                    "Conjugate verbs to past tense: apply ㅏ/ㅗ→았다, all else→었다, 하→했다; understand vowel merging",
                    "Conjugate verbs to future tense: add ~겠다 to stem regardless of vowel or consonant",
                    "Conjugate adjectives: present = unchanged dictionary form; past/future = same rules as verbs",
                    "Understand 있다 as an adjective (to have / to be at a location) needs no conjugation change in plain present",
                    "Know the difference between 나 (informal) and 저 (formal), and the 내가/제가 forms",
                    "Understand why 'you' is rarely used in Korean and what alternatives exist",
                ],
                "techniques": ["Active Recall", "Conjugation Tables", "Pattern Drilling"],
                "key_vocab": [
                    "동생=younger sibling", "남동생=younger brother", "여동생=younger sister",
                    "형=older brother(male speaker)", "오빠=older brother(female speaker)",
                    "누나=older sister(male speaker)", "언니=older sister(female speaker)",
                    "삼촌=uncle", "이모=aunt(mother's side)", "고모=aunt(father's side)",
                    "아저씨=older unrelated man", "아주머니=older unrelated woman",
                    "할아버지=grandfather", "할머니=grandmother", "친구=friend",
                    "사진=picture", "안경=glasses", "비밀=secret", "비=rain",
                    "가게=store/shop", "박물관=museum", "오리=duck", "꼬리=tail", "공=ball",
                    "기대하다=to expect", "건너다=to cross", "던지다=to throw",
                    "싫어하다=to not like", "떠나다=to leave", "농담하다=to joke", "공부하다=to study",
                    "지루하다=to be boring", "마르다=to be thin", "멀다=to be far",
                    "비슷하다=to be similar", "배고프다=to be hungry",
                    "오늘=today", "어제=yesterday", "내일=tomorrow", "모레=day after tomorrow",
                    "년=year", "일=day", "시간=time",
                    "월요일=Monday", "화요일=Tuesday", "수요일=Wednesday", "목요일=Thursday",
                    "금요일=Friday", "토요일=Saturday", "일요일=Sunday",
                ],
                "feynman_prompt": (
                    "Without notes, explain the vowel harmony rule for past tense conjugation. "
                    "Then conjugate 가다, 먹다, and 공부하다 into past tense plain form, "
                    "showing each step including any vowel merging."
                ),
                "active_recall_questions": [
                    "What do you add to a consonant-ending verb stem for present tense plain form?",
                    "What do you add to a vowel-ending verb stem for present tense plain form?",
                    "Conjugate 먹다 into present, past, and future plain form.",
                    "Conjugate 가다 into present, past, and future plain form.",
                    "Conjugate 공부하다 into present, past, and future plain form.",
                    "What is the vowel harmony rule for choosing 았다 vs 었다?",
                    "Why does 가다 past tense become 갔다 and not 가았다?",
                    "How do you conjugate an adjective in the present tense plain form?",
                    "Conjugate 비싸다 into past tense plain form.",
                    "Conjugate 길다 into past tense plain form.",
                    "What is 있다 in the plain present tense when meaning 'I have a pen'?",
                    "What is the difference between 나 and 저, and when does 나 change to 내?",
                    "Why is '너' rarely used in Korean? Give two alternatives.",
                    "From U1L4: write 'I eat a lot of food' using 많은 as a descriptor.",
                ],
                "resources": [
                    {"name": "HTSK Unit 1 Lesson 5", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-5/"},
                ],
                "topik_vocab_count": 42,
                "knowledge_bank": {
                    "summary": (
                        "Plain form (also called diary form) is used in diaries, books, newspapers and articles — "
                        "rarely in speech. It uses the informal 나. "
                        "VERB present tense: consonant stem + ~는다 (먹다→먹는다); vowel stem + ~ㄴ다 (가다→간다, 배우다→배운다). "
                        "VERB past tense: add ~았다 if last vowel is ㅏ or ㅗ; ~었다 for all others; ~했다 for 하다 verbs. "
                        "If the stem ends in a vowel, ~았/었다 merges: 가+았다=갔다, 오+았다=왔다, 배우+었다=배웠다. "
                        "VERB future tense: add ~겠다 to stem, no vowel/consonant distinction. "
                        "ADJECTIVE present tense: leave dictionary form unchanged (비싸다, 길다, 행복하다). "
                        "ADJECTIVE past/future: same vowel harmony rules as verbs. "
                        "있다 as adjective (to have / to be located) is already conjugated in plain present as-is. "
                        "나 = informal I; 저 = formal I. 나+가=내가; 저+가=제가. "
                        "너 = you (informal), but rarely used. Koreans use job titles, family terms (오빠, 형), "
                        "아저씨/아주머니 for strangers, or simply omit 'you' from the sentence."
                    ),
                    "facts": [
                        "Plain form is used in writing (diaries, books, news) — not normally in speech.",
                        "Verb present tense: consonant stem + ~는다 (먹다→먹는다, 닫다→닫는다).",
                        "Verb present tense: vowel stem + ~ㄴ다 (가다→간다, 배우다→배운다, 이해하다→이해한다).",
                        "Past tense rule: last vowel ㅏ or ㅗ → ~았다; anything else → ~었다; 하 → ~했다.",
                        "Vowel merging in past tense: 가→갔다, 오→왔다, 배우→배웠다, 던지→던졌다.",
                        "Future tense: add ~겠다 to any stem (먹겠다, 가겠다, 배우겠다).",
                        "Adjective present plain form = dictionary form unchanged (비싸다, 길다, 맛있다).",
                        "Adjective past: same vowel harmony rules — 비싸다→비쌌다, 길다→길었다.",
                        "있다 (to have / be located) is an adjective — plain present form is 있다 unchanged.",
                        "나 = informal I/me. 저 = formal I/me.",
                        "나+가 contracts to 내가. 저+가 contracts to 제가.",
                        "너 = informal 'you' — rarely used in Korean.",
                        "Alternatives to 너: job title (부장님), family term (오빠, 언니), 아저씨/아주머니, or omit entirely.",
                        "나는 친구를 만난다 = I meet a friend.",
                        "나는 박물관에 갔다 = I went to the museum.",
                        "나는 먹겠다 = I will eat.",
                        "그 길은 길다 = That street is long (adjective, plain present, unchanged).",
                        "그 길은 길었다 = That street was long (adjective past tense).",
                    ],
                    "grammar_rules": [
                        "RULE: verb present plain form — consonant stem → add ~는다. E.g. 먹다(먹+는다)→먹는다, 닫다→닫는다.",
                        "RULE: verb present plain form — vowel stem → add ~ㄴ to last syllable + 다. E.g. 가다(가+ㄴ다)→간다, 배우다→배운다.",
                        "RULE: past tense — last vowel of stem is ㅏ or ㅗ → add ~았다. E.g. 닫다→닫았다, 오다→왔다.",
                        "RULE: past tense — last vowel is anything other than ㅏ or ㅗ → add ~었다. E.g. 먹다→먹었다, 배우다→배웠다.",
                        "RULE: past tense — stem last syllable is 하 → add ~였다 which contracts to ~했다. E.g. 공부하다→공부했다.",
                        "RULE: vowel merging — when stem ends in a vowel, ~았/었 merges into the stem. 가+았=갔, 오+았=왔, 배우+었=배웠, 던지+었=던졌.",
                        "RULE: future tense — add ~겠다 to stem regardless of vowel or consonant. E.g. 먹겠다, 가겠다, 배우겠다.",
                        "RULE: adjective present plain form = leave dictionary form completely unchanged. 비싸다, 길다, 행복하다 are already correct.",
                        "RULE: adjective past/future tense uses the same vowel harmony rules as verbs. 비싸다→비쌌다(ㅏ), 길다→길었다(ㅣ).",
                        "RULE: 있다 as adjective (to have / be located) is already correct in plain present — do NOT add ~는다 or ~ㄴ다.",
                        "RULE: 나 is informal I — used with plain form. 저 is formal I. 나+가=내가, 저+가=제가.",
                        "SCOPE NOTE: this lesson teaches plain/diary form only. Speech level conjugations (아/어요, 습니다) are taught in Lesson 6.",
                    ],
                    "example_sentences": [
                        {"korean": "나는 밥을 먹는다", "english": "I eat rice", "notes": "먹다: consonant stem 먹 + ~는다"},
                        {"korean": "나는 집에 간다", "english": "I go home", "notes": "가다: vowel stem 가 + ~ㄴ다 → 간다"},
                        {"korean": "나는 한국어를 배운다", "english": "I learn Korean", "notes": "배우다: vowel stem 배우 + ~ㄴ다 → 배운다"},
                        {"korean": "나는 한국어를 공부한다", "english": "I study Korean", "notes": "공부하다: 하 stem + ~ㄴ다 → 공부한다"},
                        {"korean": "나는 밥을 먹었다", "english": "I ate rice", "notes": "먹다: last vowel ㅓ → ~었다"},
                        {"korean": "나는 박물관에 갔다", "english": "I went to the museum", "notes": "가다: last vowel ㅏ → ~았다, merged: 가+았=갔"},
                        {"korean": "삼촌은 가게에 왔다", "english": "My uncle came to the store", "notes": "오다: last vowel ㅗ → ~았다, merged: 오+았=왔"},
                        {"korean": "나는 한국어를 공부했다", "english": "I studied Korean", "notes": "공부하다: 하+였=했 (contraction)"},
                        {"korean": "나는 먹겠다", "english": "I will eat", "notes": "future tense: stem + ~겠다"},
                        {"korean": "그 길은 길다", "english": "That street is long", "notes": "adjective present plain = dictionary form unchanged"},
                        {"korean": "그 길은 길었다", "english": "That street was long", "notes": "adjective past: 길다 last vowel ㅣ → ~었다"},
                        {"korean": "나는 펜이 있다", "english": "I have a pen", "notes": "있다 as adjective — plain present = unchanged"},
                    ],
                    "common_mistakes": [
                        "Adding ~는다 to a vowel-ending verb stem: e.g. 가는다 — WRONG. Vowel stems take ~ㄴ다: 간다.",
                        "Adding ~ㄴ다 to a consonant-ending verb stem: e.g. 먹ㄴ다 — WRONG. Consonant stems take ~는다: 먹는다.",
                        "Choosing 었다 when last vowel is ㅏ: e.g. 닫었다 — WRONG. ㅏ/ㅗ take ~았다: 닫았다.",
                        "Choosing 았다 when last vowel is not ㅏ/ㅗ: e.g. 먹았다 — WRONG. Other vowels take ~었다: 먹었다.",
                        "Not merging ~았/었 when stem ends in a vowel: e.g. 가았다 — WRONG. Must merge: 갔다.",
                        "Conjugating an adjective in present plain form: e.g. 비싸는다 or 비싼다 — WRONG. Adjective present = unchanged: 비싸다.",
                        "Conjugating 있다 as a verb in plain present: e.g. 있는다 — WRONG when used as adjective (to have / be located).",
                        "Using 저 with plain/diary form — plain form is informal so 나 is used, not 저.",
                    ],
                },
                "expected_answers": {
                    "Conjugate 먹다 in present, past, future plain form.": "Present: 먹는다. Past: 먹었다. Future: 먹겠다.",
                    "Conjugate 가다 in present, past, future plain form.": "Present: 간다. Past: 갔다 (가+았다 merged). Future: 가겠다.",
                    "Conjugate 공부하다 in present, past, future plain form.": "Present: 공부한다. Past: 공부했다 (하→했). Future: 공부하겠다.",
                    "What is the vowel harmony rule?": "Last vowel ㅏ or ㅗ → add ~았다. Any other vowel → add ~었다. 하 stem → ~했다.",
                    "Why is 갔다 not 가았다?": "When the stem ends in a vowel, ~았/었다 merges with the final vowel syllable. 가+았=갔.",
                    "How do you conjugate an adjective in plain present?": "Leave the dictionary form unchanged — 비싸다, 길다, 행복하다 are already correct.",
                },
            },

            {
                "id": "U1L6",
                "title": "Korean Honorifics",
                "subtitle": "Informal low, informal high, and formal high conjugations",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-6/",
                "estimated_minutes": 45,
                "split": True,
                "learning_goals": [
                    "Understand why Korean speech levels exist and the social consequences of using the wrong one",
                    "Conjugate verbs and adjectives in informal low respect: add ~아/어 to stem",
                    "Conjugate verbs and adjectives in informal high respect: add ~아/어요",
                    "Conjugate verbs and adjectives in formal high respect: add ~ㅂ니다 (vowel stems) or ~습니다 (consonant stems)",
                    "Apply past and future tense across all three levels: 었어/었어요/었습니다 and 겠어/겠어요/겠습니다",
                    "Know when to use 나 vs 저 in correspondence with speech level",
                ],
                "techniques": ["Active Recall", "Conjugation Tables", "Contextual Drilling"],
                "key_vocab": [
                    "신발=shoe", "남방=shirt", "질문=question", "문제=question/problem",
                    "나이=age", "화장실=bathroom", "부장님=boss", "분위기=atmosphere",
                    "차=tea", "바지=pants", "교실=classroom", "급식=food at school",
                    "교감선생님=vice principal", "교장선생님=principal", "풀=glue",
                    "수도=capital city", "병=bottle", "병=disease/sickness",
                    "생선=fish", "야채=vegetable", "언덕=hill", "선물=present/gift",
                    "기타=guitar", "종이=paper", "우유=milk", "손목=wrist",
                    "시계=clock/watch", "손목시계=wristwatch", "영화=movie",
                    "노력하다=to try", "앉다=to sit", "만지다=to touch", "자다=to sleep",
                    "보다=to see", "기다리다=to wait", "청소하다=to clean",
                    "약속하다=to promise", "듣다=to hear", "운동하다=to exercise",
                    "빠르다=to be fast", "느리다=to be slow", "착하다=to be nice",
                    "곧=soon", "항상=always", "주=week", "아래=bottom",
                ],
                "feynman_prompt": (
                    "Without notes, produce a full conjugation table for 먹다 across all four forms "
                    "(plain, informal low, informal high, formal high) in past, present, and future. "
                    "Then explain when you would use each speech level."
                ),
                "active_recall_questions": [
                    "What are the three speech levels you are learning in this lesson?",
                    "What do you add to a stem for informal low respect present tense?",
                    "What do you add to a stem for informal high respect present tense?",
                    "What do you add to a vowel stem for formal high respect present tense?",
                    "What do you add to a consonant stem for formal high respect present tense?",
                    "Conjugate 먹다 in all three speech levels, present tense.",
                    "Conjugate 자다 in all three speech levels, present tense.",
                    "Conjugate 운동하다 in all three speech levels, past tense.",
                    "How do you say 'I ate' in informal high respect?",
                    "How do you say 'I will learn' in formal high respect?",
                    "Should you use 나 or 저 with informal low respect? With formal high respect?",
                    "What speech level would you use with your boss? With your best friend?",
                    "From U1L5: conjugate 가다 into past tense plain form.",
                ],
                "resources": [
                    {"name": "HTSK Unit 1 Lesson 6", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-6/"},
                ],
                "topik_vocab_count": 35,
                "knowledge_bank": {
                    "summary": (
                        "Korean has three speech levels for everyday use, plus the plain form from Lesson 5. "
                        "INFORMAL LOW (casual, friends/family/younger people): add ~아/어 to stem. Use 나. "
                        "INFORMAL HIGH (respectful, most everyday situations): add ~아/어요 to stem. Use 저. "
                        "FORMAL HIGH (high respect, bosses/officials/strangers deserving deference): "
                        "add ~ㅂ니다 (vowel stem) or ~습니다 (consonant stem). Use 저. "
                        "Vowel harmony applies: ㅏ/ㅗ stem → 아; all others → 어; 하 → 해. "
                        "Past tense across levels: 었어 / 었어요 / 었습니다. "
                        "Future tense across levels: 겠어 / 겠어요 / 겠습니다. "
                        "Adjectives conjugate exactly the same way as verbs for these three honorific levels. "
                        "The difference between informal high and formal high is not enormous — "
                        "either is acceptable in most respectful contexts."
                    ),
                    "facts": [
                        "Informal low: stem + ~아/어. Use 나. For friends, younger people, family.",
                        "Informal high: stem + ~아/어요. Use 저. Most common respectful spoken form.",
                        "Formal high: vowel stem + ~ㅂ니다; consonant stem + ~습니다. Use 저. High deference.",
                        "Vowel harmony: ㅏ or ㅗ → 아; anything else → 어; 하 stem → 해.",
                        "먹다: informal low = 먹어, informal high = 먹어요, formal high = 먹습니다.",
                        "자다: informal low = 자, informal high = 자요, formal high = 잡니다.",
                        "이해하다: informal low = 이해해, informal high = 이해해요, formal high = 이해합니다.",
                        "보다: informal low = 봐, informal high = 봐요, formal high = 봅니다.",
                        "Past tense: 먹었어 / 먹었어요 / 먹었습니다.",
                        "Future tense: 먹겠어 / 먹겠어요 / 먹겠습니다.",
                        "Adjectives follow identical rules: 비싸다→비싸/비싸요/비쌉니다.",
                        "길다→길어/길어요/깁니다 (note ㄹ irregular in formal high — covered in Lesson 7).",
                        "나 is used with informal low; 저 is used with informal high and formal high.",
                        "Never using honorifics correctly — even as a beginner — can cause serious offence.",
                        "저는 항상 저녁에 음식을 먹어요 = I always eat food in the evening (informal high).",
                        "저는 항상 아침에 운동합니다 = I always exercise in the morning (formal high).",
                    ],
                    "grammar_rules": [
                        "RULE: informal low present — add ~아/어 to stem. ㅏ/ㅗ last vowel → 아; all others → 어; 하 → 해.",
                        "RULE: informal high present — add ~아/어요. Same vowel harmony as informal low, just add 요.",
                        "RULE: formal high present — vowel stem + ~ㅂ니다; consonant stem + ~습니다.",
                        "RULE: vowel merging applies in informal low/high — same as plain form. 보다+아→봐, 오다+아→와.",
                        "RULE: informal low past — add ~았/었어 to stem (vowel harmony applies). 먹+었어=먹었어.",
                        "RULE: informal high past — add ~았/었어요. 먹+었어요=먹었어요.",
                        "RULE: formal high past — add ~았/었습니다. 먹+었습니다=먹었습니다.",
                        "RULE: informal low future — add ~겠어 to stem. 먹겠어.",
                        "RULE: informal high future — add ~겠어요. 먹겠어요.",
                        "RULE: formal high future — add ~겠습니다. 먹겠습니다.",
                        "RULE: adjectives conjugate identically to verbs for all three honorific levels.",
                        "RULE: 나 is used with informal low. 저 is used with informal high and formal high.",
                        "RULE: do NOT add ~는다/~ㄴ다 endings in any of these three speech levels — those are plain/diary form only.",
                        "SCOPE NOTE: ㄹ irregular in formal high (e.g. 깁니다 from 길다) is introduced in Lesson 7. Accept 길습니다 as an attempt even if technically irregular.",
                    ],
                    "example_sentences": [
                        {"korean": "나는 항상 저녁에 음식을 먹어", "english": "I always eat food in the evening", "notes": "informal low: 먹+어"},
                        {"korean": "저는 항상 저녁에 음식을 먹어요", "english": "I always eat food in the evening", "notes": "informal high: 먹+어요"},
                        {"korean": "저는 항상 저녁에 음식을 먹습니다", "english": "I always eat food in the evening", "notes": "formal high: 먹+습니다(consonant stem)"},
                        {"korean": "나는 저의 선생님을 항상 봐", "english": "I always see my teacher", "notes": "informal low: 보+아→봐(merged)"},
                        {"korean": "저는 저의 선생님을 항상 봐요", "english": "I always see my teacher", "notes": "informal high: 보+아요→봐요"},
                        {"korean": "저는 저의 선생님을 항상 봅니다", "english": "I always see my teacher", "notes": "formal high: 보+ㅂ니다(vowel stem)"},
                        {"korean": "나는 항상 아침에 운동해", "english": "I always exercise in the morning", "notes": "informal low: 운동하+여→운동해"},
                        {"korean": "저는 항상 아침에 운동해요", "english": "I always exercise in the morning", "notes": "informal high: 운동하+여요→운동해요"},
                        {"korean": "저는 항상 아침에 운동합니다", "english": "I always exercise in the morning", "notes": "formal high: 운동하+ㅂ니다→운동합니다"},
                        {"korean": "나는 먹었어", "english": "I ate", "notes": "informal low past: 먹+었어"},
                        {"korean": "저는 먹었어요", "english": "I ate", "notes": "informal high past: 먹+었어요"},
                        {"korean": "저는 먹었습니다", "english": "I ate", "notes": "formal high past: 먹+었습니다"},
                        {"korean": "저는 배우겠습니다", "english": "I will learn", "notes": "formal high future: 배우+겠습니다"},
                    ],
                    "common_mistakes": [
                        "Ending informal high sentences with ~다: e.g. 먹어요다 — WRONG. 먹어요 is the complete form.",
                        "Using formal high ~습니다 with 나: e.g. 나는 먹습니다 — WRONG. Formal high uses 저.",
                        "Using informal low ~어/아 with 저: e.g. 저는 먹어 — awkward/incorrect pairing. Informal low uses 나.",
                        "Adding ~는다 or ~ㄴ다 for informal/formal speech: e.g. 먹는다요 — WRONG. ~는다 is plain form only.",
                        "Using ~ㅂ니다 on a consonant stem: e.g. 먹ㅂ니다 — WRONG. Consonant stems take ~습니다: 먹습니다.",
                        "Using ~습니다 on a vowel stem: e.g. 가습니다 — WRONG. Vowel stems take ~ㅂ니다: 갑니다.",
                        "Forgetting vowel merging in informal forms: e.g. 보아요 — technically understandable but non-standard; 봐요 is preferred.",
                        "Using the wrong speech level for the context: informal low to a boss, or formal high to a friend.",
                    ],
                },
                "expected_answers": {
                    "Conjugate 먹다 in informal low, informal high, formal high (present).": "먹어 / 먹어요 / 먹습니다",
                    "Conjugate 자다 in informal low, informal high, formal high (present).": "자 / 자요 / 잡니다",
                    "How do you say 'I ate' in informal high respect?": "저는 먹었어요",
                    "How do you say 'I will learn' in formal high respect?": "저는 배우겠습니다",
                    "나 or 저 with informal low?": "나 — informal low goes with the informal first person pronoun.",
                    "나 or 저 with formal high?": "저 — formal speech always uses the polite first person pronoun.",
                },
            },

            {
                "id": "U1L7",
                "title": "Korean Irregulars",
                "subtitle": "ㅅ, ㄷ, ㅂ, ㅡ, 르, and ㄹ irregular conjugations",
                "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-7/",
                "estimated_minutes": 55,
                "split": True,
                "learning_goals": [
                    "Understand that most irregulars are triggered when adding a vowel (~아/어 and derivatives) to the stem",
                    "ㅅ irregular: ㅅ is dropped before a vowel (짓다→지어요); know exceptions: 웃다, 벗다, 씻다",
                    "ㄷ irregular: ㄷ changes to ㄹ before a vowel (걷다→걸어요); know exceptions: 받다, 닫다, 묻다",
                    "ㅂ irregular: ㅂ changes to 우 before a vowel (쉽다→쉬워요), except 돕다/곱다→오; applies to ~ㄴ/은 descriptor form too",
                    "ㅡ irregular: stem ending in ㅡ — look at second-last vowel for 아/어, then drop ㅡ and merge (바쁘다→바빠요, 예쁘다→예뻐요)",
                    "르 irregular: 르 stem + ~아/어 → insert ㄹ into preceding syllable + 라/러 (다르다→달라요, 빠르다→빨라요)",
                    "ㄹ irregular: ㄹ is dropped before ~ㄴ, ~ㅂ, ~ㄹ (길다→긴, 깁니다; 열다→연다, 엽니다) — the only irregular triggered by consonant additions",
                ],
                "techniques": ["Active Recall", "Conjugation Drills", "Contrastive Practice"],
                "key_vocab": [
                    "눈썹=eyebrow", "교사=teacher", "반=class of students", "직장=workplace",
                    "벽=wall", "털=body hair/fur", "머리카락=hair(on head)", "저녁=dinner/evening",
                    "점심=lunch", "옷=clothes", "오전=morning", "오후=afternoon",
                    "여름=summer", "가을=autumn", "겨울=winter", "봄=spring",
                    "찾다=to search/find", "가르치다=to teach", "일하다=to work",
                    "짓다=to build(ㅅ irregular)", "가지다=to own/possess",
                    "잠그다=to lock(ㅡ irregular)", "잊다=to forget",
                    "돕다=to help(ㅂ irregular, 오 form)", "주다=to give", "맞다=to be correct",
                    "쉽다=to be easy(ㅂ irregular)", "덥다=to be hot(ㅂ irregular)",
                    "귀엽다=to be cute(ㅂ irregular)", "춥다=to be cold(ㅂ irregular)",
                    "어렵다=to be difficult(ㅂ irregular)", "더럽다=to be dirty(ㅂ irregular)",
                    "바쁘다=to be busy(ㅡ irregular)", "예쁘다=to be pretty(ㅡ irregular)",
                    "부드럽다=to be soft(ㅂ irregular)", "안전하다=to be safe",
                    "같다=to be the same", "가능하다=to be possible",
                    "걷다=to walk(ㄷ irregular)", "열다=to open(ㄹ irregular)",
                    "길다=to be long(ㄹ irregular)", "멀다=to be far(ㄹ irregular)",
                    "만들다=to make(ㄹ irregular)",
                    "다르다=to be different(르 irregular)", "빠르다=to be fast(르 irregular)",
                    "매일=every day", "일찍=early",
                ],
                "feynman_prompt": (
                    "Without notes, explain the ㅂ irregular. What triggers it, what happens to ㅂ, "
                    "and what is the exception? Then conjugate 춥다, 쉽다, and 돕다 in informal high "
                    "respect present tense, showing your working."
                ),
                "active_recall_questions": [
                    "What type of addition triggers most Korean irregulars?",
                    "Conjugate 짓다 in informal high respect present and past tense.",
                    "Does the ㅅ irregular apply to 웃다? What is 웃다 in informal high present?",
                    "Conjugate 걷다 (to walk) in informal high respect present and past tense.",
                    "Does the ㄷ irregular apply to 받다? What is 받다 in informal high present?",
                    "Conjugate 쉽다 in informal high respect present tense.",
                    "Conjugate 춥다 in informal high respect present tense.",
                    "Conjugate 돕다 in informal high respect past tense. Why is it different from 쉽다?",
                    "How do you write 귀엽다 as a descriptor before a noun?",
                    "Conjugate 바쁘다 in informal high respect present tense. Show your steps.",
                    "Conjugate 예쁘다 in informal high respect present tense. Show your steps.",
                    "Conjugate 다르다 in informal high respect present tense.",
                    "Conjugate 빠르다 in informal high respect past tense.",
                    "What happens to 길다 in formal high respect present (습니다 form)?",
                    "What happens to 열다 in plain form present tense?",
                    "Which is the only irregular that applies when adding a consonant to a stem?",
                    "From U1L6: conjugate 먹다 in all three speech levels present tense.",
                ],
                "resources": [
                    {"name": "HTSK Unit 1 Lesson 7", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-7/"},
                    {"name": "HTSK Irregular Quick Reference", "url": "https://www.howtostudykorean.com/unit1/unit-1-lessons-1-8/unit-1-lesson-7/irregularquickreference/"},
                ],
                "topik_vocab_count": 40,
                "knowledge_bank": {
                    "summary": (
                        "Most irregulars fire when adding ~아/어 (or any derivative: ~았/었어, ~았/었어요, ~았/었습니다) to a stem. "
                        "ㅅ IRREGULAR: ㅅ is dropped before a vowel. 짓다→지어요, 짓다→지었어요. "
                        "Exceptions (regular): 웃다(웃어요), 벗다(벗어요), 씻다(씻어요). "
                        "ㄷ IRREGULAR (verbs only): ㄷ changes to ㄹ before a vowel. 걷다→걸어요. "
                        "Exceptions (regular): 받다(받아요), 닫다(닫아요), 묻다(묻어요). "
                        "ㅂ IRREGULAR (mostly adjectives): ㅂ changes to 우 before a vowel. 쉽다→쉬워요, 춥다→추워요, 귀엽다→귀여워요. "
                        "Exception: 돕다 and 곱다 → ㅂ changes to 오: 돕다→도와요. "
                        "Also applies when adding ~ㄴ/은 to describe a noun: 귀엽다→귀여운, 쉽다→쉬운, 춥다→추운. "
                        "Regular ㅂ words: 좁다(좁아요), 잡다(잡아요), 넓다(넓어요). "
                        "ㅡ IRREGULAR: stem ends in ㅡ — check second-last vowel for 아/어 choice, then drop ㅡ and merge. "
                        "바쁘다→바빠요(바+아), 예쁘다→예뻐요(예+어), 크다→커요(one syllable stem, default 어). "
                        "르 IRREGULAR: 르 stem + ~아/어 → insert ㄹ into preceding syllable + 라/러. "
                        "다르다→달라요, 빠르다→빨라요, 부르다→불렀어요. "
                        "ㄹ IRREGULAR (consonant additions): ㄹ is DROPPED before ~ㄴ, ~ㅂ, ~ㄹ. "
                        "길다→긴(~ㄴ/은), 깁니다(~ㅂ니다). 열다→연다(plain present), 엽니다(formal high). "
                        "만들다→만든다(plain), 만듭니다(formal high). "
                        "This is the ONLY irregular triggered by consonant additions."
                    ),
                    "facts": [
                        "Most irregulars fire when adding ~아/어 or its derivatives to a stem.",
                        "ㅅ irregular: ㅅ dropped before vowel. 짓다→지어요, 지었어요.",
                        "ㅅ irregular exceptions (regular): 웃다→웃어요, 벗다→벗어요, 씻다→씻어요.",
                        "ㄷ irregular (verbs): ㄷ→ㄹ before vowel. 걷다→걸어요, 걸었어요.",
                        "ㄷ irregular exceptions (regular): 받다→받아요, 닫다→닫아요, 묻다→묻어요.",
                        "ㅂ irregular: ㅂ→우 before vowel. 쉽다→쉬워요, 춥다→추워요, 어렵다→어려워요.",
                        "ㅂ irregular exception: 돕다→도와요(ㅂ→오), 곱다→고와요.",
                        "ㅂ irregular also applies to ~ㄴ/은 descriptor: 귀엽다→귀여운, 쉽다→쉬운, 부드럽다→부드러운.",
                        "ㅂ regular words: 좁다→좁아요, 잡다→잡아요, 넓다→넓어요.",
                        "ㅡ irregular: check second-last vowel for 아/어, drop ㅡ, merge. 바쁘다→바빠요, 예쁘다→예뻐요.",
                        "ㅡ irregular single-syllable stem: default to 어. 크다→커요.",
                        "르 irregular: insert ㄹ into preceding syllable + 라/러. 다르다→달라요, 빠르다→빨라요.",
                        "ㄹ irregular: ㄹ dropped before ~ㄴ, ~ㅂ, ~ㄹ (consonant additions).",
                        "길다: 긴(~ㄴ/은 descriptor), 깁니다(formal high), 길어요(informal high — no change).",
                        "열다: 연다(plain present), 엽니다(formal high), 열어요(informal high — no change).",
                        "만들다: 만든다(plain present), 만듭니다(formal high), 만들어요(informal high).",
                        "ㄹ irregular is the ONLY irregular triggered by consonant additions.",
                        "When 듣다 and 들다 are conjugated informally they can sound identical — context determines meaning.",
                    ],
                    "grammar_rules": [
                        "ㅅ IRREGULAR — trigger: adding ~아/어 (or any derivative). Action: drop ㅅ from stem before adding vowel.",
                        "ㅅ irregular applies to: 짓다(짓→지+어→지어요), 낫다, 잇다.",
                        "ㅅ irregular does NOT apply (regular) to: 웃다(웃어요), 벗다(벗어요), 씻다(씻어요).",
                        "ㄷ IRREGULAR — trigger: adding ~아/어. Action: ㄷ changes to ㄹ before the vowel. Verbs only.",
                        "ㄷ irregular applies to: 걷다(걷→걸+어→걸어요), 듣다(듣→들+어→들어요).",
                        "ㄷ irregular does NOT apply (regular) to: 받다(받아요), 닫다(닫아요), 묻다(묻어요).",
                        "ㅂ IRREGULAR — trigger: adding ~아/어. Action: ㅂ changes to 우 before the vowel.",
                        "ㅂ irregular applies to most adjectives ending in ㅂ: 쉽다→쉬워요, 춥다→추워요, 귀엽다→귀여워요, 어렵다→어려워요, 덥다→더워요, 더럽다→더러워요, 부드럽다→부드러워요.",
                        "ㅂ EXCEPTION: 돕다 and 곱다 — ㅂ changes to 오 (not 우): 돕다→도와요, 도왔어요.",
                        "ㅂ irregular also fires when adding ~ㄴ/은 as adjective descriptor: 쉽다→쉬운, 귀엽다→귀여운, 춥다→추운.",
                        "ㅂ regular (no irregular): 좁다→좁아요, 잡다→잡아요, 넓다→넓어요.",
                        "ㅡ IRREGULAR — trigger: adding ~아/어. Action: look at second-last vowel to decide 아/어, then drop ㅡ and merge.",
                        "ㅡ irregular: second-last vowel ㅏ or ㅗ → use 아. E.g. 바쁘다(바+아)→바빠요, 잠그다(잠+아)→잠가요.",
                        "ㅡ irregular: second-last vowel anything else → use 어. E.g. 예쁘다(예+어)→예뻐요, 슬프다(슬+어)→슬퍼요.",
                        "ㅡ irregular: single-syllable stem (e.g. 크다, stem=크) — no second-last syllable, default to 어: 크다→커요.",
                        "르 IRREGULAR — trigger: adding ~아/어. Action: insert ㄹ into preceding syllable as final consonant; 르→라 or 르→러.",
                        "르 irregular: 다르다→달라요(달랐어요), 빠르다→빨라요(빨랐어요), 부르다→불러요(불렀어요), 고르다→골라요.",
                        "르 irregular exceptions (regular): 따르다→따라요, 푸르다→푸러요.",
                        "ㄹ IRREGULAR — trigger: adding consonant additions ~ㄴ/은, ~ㅂ/습, ~ㄹ/을. Action: drop ㄹ from stem, then add ~ㄴ/~ㅂ/~ㄹ directly.",
                        "ㄹ irregular: ~ㄴ/은 descriptor → drop ㄹ + ~ㄴ. 길다→긴, 멀다→먼, 열다→연.",
                        "ㄹ irregular: formal high present → drop ㄹ + ~ㅂ니다. 길다→깁니다, 열다→엽니다, 만들다→만듭니다.",
                        "ㄹ irregular: plain present → drop ㄹ + ~ㄴ다. 열다→연다, 만들다→만든다.",
                        "ㄹ irregular does NOT fire when adding vowels: 길다→길어요, 열다→열어요 (no change to ㄹ).",
                        "ㄹ irregular is the ONLY irregular triggered by consonant additions — all others require a vowel addition.",
                    ],
                    "example_sentences": [
                        {"korean": "나는 집을 지어요", "english": "I build a house", "notes": "짓다: ㅅ irregular — ㅅ dropped, 짓+어→지어요"},
                        {"korean": "저는 집을 지었어요", "english": "I built a house", "notes": "짓다: ㅅ irregular past — 지었어요"},
                        {"korean": "저는 걸어요", "english": "I walk", "notes": "걷다: ㄷ irregular — ㄷ→ㄹ, 걷+어→걸어요"},
                        {"korean": "저는 걸었어요", "english": "I walked", "notes": "걷다: ㄷ irregular past — 걸었어요"},
                        {"korean": "그것은 쉬워요", "english": "That is easy", "notes": "쉽다: ㅂ irregular — ㅂ→우, 쉽+어→쉬워요"},
                        {"korean": "그것은 어려워요", "english": "That is difficult", "notes": "어렵다: ㅂ irregular — 어렵+어→어려워요"},
                        {"korean": "저는 저의 어머니를 도왔어요", "english": "I helped my mother", "notes": "돕다: ㅂ→오 exception — 돕+았→도왔어요"},
                        {"korean": "저는 귀여운 여자를 좋아해요", "english": "I like cute girls", "notes": "귀엽다: ㅂ irregular on ~ㄴ/은 form → 귀여운"},
                        {"korean": "저는 바빠요", "english": "I am busy", "notes": "바쁘다: ㅡ irregular — second-last ㅏ→아, drop ㅡ→바빠요"},
                        {"korean": "그 여자는 예뻐요", "english": "That girl is pretty", "notes": "예쁘다: ㅡ irregular — second-last not ㅏ/ㅗ→어, drop ㅡ→예뻐요"},
                        {"korean": "그 집은 커요", "english": "That house is big", "notes": "크다: ㅡ irregular single-syllable — default 어→커요"},
                        {"korean": "그것은 달라요", "english": "That thing is different", "notes": "다르다: 르 irregular — 다+ㄹ+라요→달라요"},
                        {"korean": "저는 긴 거리를 건넜어요", "english": "I crossed the long street", "notes": "길다: ㄹ irregular on ~ㄴ/은 → 긴"},
                        {"korean": "저는 문을 엽니다", "english": "I open the door", "notes": "열다: ㄹ irregular on formal high → 엽니다"},
                        {"korean": "저는 케이크를 만듭니다", "english": "I make a cake", "notes": "만들다: ㄹ irregular on formal high → 만듭니다"},
                    ],
                    "common_mistakes": [
                        "ㅅ irregular: writing 짓어요 — WRONG. ㅅ must be dropped: 지어요.",
                        "ㅅ regular confusion: writing 웃어요 and thinking it's wrong — it IS correct. 웃다 does not follow the ㅅ irregular.",
                        "ㄷ irregular: writing 걷어요 — WRONG. ㄷ→ㄹ before vowel: 걸어요.",
                        "ㄷ regular confusion: writing 받아요 and thinking ㄷ should change — it should NOT. 받다 is regular.",
                        "ㅂ irregular: writing 쉽어요 — WRONG. ㅂ→우: 쉬워요.",
                        "ㅂ irregular: writing 춥아요 — WRONG (wrong vowel choice too). ㅂ→우: 추워요.",
                        "ㅂ irregular on 돕다: writing 도워요 — WRONG. 돕다 uses 오 not 우: 도와요.",
                        "ㅂ irregular descriptor: writing 쉽은 — WRONG. ㅂ→우+ㄴ=운: 쉬운.",
                        "ㅡ irregular: writing 바쁘어요 — WRONG. Must drop ㅡ and merge: 바빠요.",
                        "ㅡ irregular: writing 예쁘아요 — WRONG (wrong vowel). Second-last vowel not ㅏ/ㅗ so use 어, drop ㅡ, merge: 예뻐요.",
                        "르 irregular: writing 다르아요 — WRONG. Insert ㄹ and change 르→라: 달라요.",
                        "ㄹ irregular: writing 길습니다 — WRONG. ㄹ dropped before ~ㅂ: 깁니다.",
                        "ㄹ irregular: writing 길는다 — WRONG for plain present. ㄹ dropped before ~ㄴ다: 긴다. Wait — 길다 is adjective so plain present = 길다 unchanged. Only verbs take ~ㄴ/는다.",
                        "ㄹ irregular: thinking ㄹ drops before vowels — WRONG. ㄹ only drops before consonant additions (~ㄴ, ~ㅂ, ~ㄹ). 길다→길어요 is correct (ㄹ stays).",
                    ],
                },
                "expected_answers": {
                    "Conjugate 짓다 in informal high present and past.": "Present: 지어요. Past: 지었어요. (ㅅ dropped before vowel)",
                    "Conjugate 걷다 in informal high present and past.": "Present: 걸어요. Past: 걸었어요. (ㄷ→ㄹ before vowel)",
                    "Conjugate 쉽다 in informal high present.": "쉬워요 (ㅂ→우 before vowel)",
                    "Conjugate 돕다 in informal high past.": "도왔어요 (ㅂ→오 for 돕다, then 오+았=왔)",
                    "Write 귀엽다 as a descriptor before a noun.": "귀여운 — ㅂ→우+ㄴ=운",
                    "Conjugate 바쁘다 in informal high present.": "바빠요 — second-last vowel is ㅏ, so add 아, drop ㅡ, merge: 바쁘+아=바빠",
                    "Conjugate 다르다 in informal high present.": "달라요 — 르 irregular: 다+ㄹ+라요",
                    "What happens to 길다 in formal high present?": "깁니다 — ㄹ dropped before ~ㅂ니다",
                    "Which irregular applies to consonant additions?": "ㄹ irregular only — all others require a vowel addition to trigger.",
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
