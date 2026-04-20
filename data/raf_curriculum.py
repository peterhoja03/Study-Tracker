"""
RAF Application Study Curriculum
Restructured with OASC priority tiers:
  - Tier 1: OASC-Critical (interview-ready, can articulate cold)
  - Tier 2: Good to know, likely to come up
  - Tier 3: Post-offer / background (lower priority)
CBAT is handled separately in cbat_page.py (session logging, not lesson-based)
"""

RAF_CURRICULUM = {

    # ─────────────────────────────────────────────────────────────────────────
    # TIER 1 — OASC-CRITICAL
    # Must be articulable cold under interview pressure.
    # ─────────────────────────────────────────────────────────────────────────

    "Tier 1 — OASC Critical": {
        "title": "OASC-Critical Knowledge",
        "color": "#b71c1c",
        "level": "Tier 1 — Must Know Cold",
        "oasc_tier": 1,
        "description": "Topics you must be able to articulate fluently under interview pressure at OASC. "
                       "These will be tested — directly or indirectly — in the interview, group exercises, "
                       "and candidate presentation. Confidence rating 3 = interview-ready.",
        "lessons": [
            {
                "id": "R1L1", "title": "RAF Core Values — RISE", "unit": "Tier 1 — OASC Critical",
                "subtitle": "Respect, Integrity, Service, Excellence — with your own examples",
                "url": "https://www.raf.mod.uk/our-organisation/raf-ethos-core-values-and-standards/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 1,
                "confidence": 0,
                "learning_goals": [
                    "State all four RAF core values without prompting",
                    "Explain what each value means in practice as an officer",
                    "Give a genuine personal example for each value from your own life",
                    "Understand why these values matter operationally and ethically"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["Respect", "Integrity", "Service", "Excellence", "RISE", "ethos", "values", "standards", "Service Test"],
                "feynman_prompt": "Pick one RAF core value and explain a real situation from your own life where you demonstrated it. Be specific, honest, and reflective. Then do all four.",
                "active_recall_questions": [
                    "State the 4 RAF core values from memory — no prompts",
                    "Give a personal example that demonstrates Integrity under pressure",
                    "What does 'Service before self' mean in practice for an RAF officer?",
                    "How would you demonstrate Excellence in a non-military context?"
                ],
                "knowledge_bank": {
                    "summary": "The RAF core values are RISE: Respect, Integrity, Service, Excellence. "
                               "These are not just words — at OASC you'll be assessed on whether you embody them.",
                    "facts": [
                        "Respect: treating every person with dignity regardless of rank or background",
                        "Integrity: doing the right thing even when no one is watching",
                        "Service: putting mission and team before personal interest",
                        "Excellence: striving for the highest standard in everything you do",
                        "The Service Test: 'Have your actions or behaviour brought, or are likely to bring, the Service into disrepute?'",
                        "Values apply equally to a junior officer and the Chief of the Air Staff",
                    ],
                    "competency": "RAF RISE values — interview and leadership tasks",
                },
                "resources": [
                    {"name": "RAF Values & Standards", "url": "https://www.raf.mod.uk/our-organisation/raf-ethos-core-values-and-standards/"}
                ]
            },
            {
                "id": "R1L2", "title": "Why RAF, Why Pilot — Your Personal Narrative", "unit": "Tier 1 — OASC Critical",
                "subtitle": "Your motivations, rehearsed but genuine",
                "url": "https://www.raf.mod.uk/recruitment/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 1,
                "confidence": 0,
                "learning_goals": [
                    "Articulate convincingly why you want to be an RAF pilot (not commercial)",
                    "Connect your personal background to the RAF's values and requirements",
                    "Prepare specific answers to 'tell me about yourself' style questions",
                    "Know your own application and CV inside out — no surprises"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["motivation", "personal statement", "STAR technique", "Situation", "Task", "Action", "Result", "self-awareness", "career goals"],
                "feynman_prompt": "Give your 2-minute answer to 'Why do you want to be an RAF pilot?' out loud. Be specific, genuine, and link it to your actual experiences. Time yourself.",
                "active_recall_questions": [
                    "Why do you want to be an RAF pilot specifically, not a commercial pilot?",
                    "What experiences in your life have prepared you for a military career?",
                    "What would you say is your biggest weakness and how are you actively addressing it?",
                    "Why the RAF over the Army or Royal Navy?"
                ],
                "knowledge_bank": {
                    "summary": "Your 'why' narrative is one of the most important things you'll say at OASC. "
                               "It needs to be genuine, specific to the RAF, and link to your real history.",
                    "facts": [
                        "Interviewers look for genuine motivation, not a rehearsed script",
                        "The RAF vs commercial pilot distinction matters — they want to know you want military service, not just to fly",
                        "STAR: Situation, Task, Action, Result — use this for all competency examples",
                        "Knowing your own application in detail is essential — you'll be asked about anything you've written",
                        "Weakness questions are a test of self-awareness, not a trap",
                    ],
                    "competency": "Motivation, self-awareness, OASC interview",
                },
                "resources": [
                    {"name": "STAR Technique", "url": "https://www.prospects.ac.uk/careers-advice/interview-tips/competency-based-interview-questions"}
                ]
            },
            {
                "id": "R1L3", "title": "Current RAF Aircraft & Roles", "unit": "Tier 1 — OASC Critical",
                "subtitle": "Front-line fleet, what each aircraft does, where it's deployed",
                "url": "https://www.raf.mod.uk/aircraft/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 1,
                "confidence": 0,
                "learning_goals": [
                    "Name all current front-line RAF aircraft and their primary roles",
                    "Distinguish fast jet, multi-engine, and rotary platforms",
                    "Know which aircraft perform Quick Reaction Alert (QRA)",
                    "Know where key aircraft are based and what operations they support"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["Typhoon", "F-35B", "Voyager", "Atlas", "Poseidon", "Wildcat", "Chinook", "Merlin", "Reaper", "Shadow", "Quick Reaction Alert", "QRA"],
                "feynman_prompt": "You're asked in the interview: 'What do you know about current RAF aircraft and how they're used?' Give a confident 2-minute answer covering the main platforms.",
                "active_recall_questions": [
                    "Name the RAF's current fast jet aircraft and their primary roles",
                    "What is Quick Reaction Alert (QRA) and which aircraft perform it?",
                    "What is the F-35B and how does it differ from the Typhoon in role and capability?",
                    "Name two current RAF multi-engine platforms and what they do"
                ],
                "knowledge_bank": {
                    "summary": "The RAF operates a range of fast jet, multi-engine, and rotary aircraft. "
                               "As a pilot candidate you're expected to know the current fleet fluently.",
                    "facts": [
                        "Typhoon FGR4: primary fast jet, multirole (air defence + ground attack), based at Coningsby and Lossiemouth",
                        "F-35B Lightning II: 5th generation stealth, short takeoff/vertical landing, based at Marham, operates from HMS Queen Elizabeth",
                        "Voyager: air-to-air refuelling and strategic transport, RAF Brize Norton",
                        "Atlas C1 (A400M): tactical and strategic transport, Brize Norton",
                        "Poseidon MRA1: maritime patrol and anti-submarine, RAF Lossiemouth",
                        "Reaper: remotely piloted air system (RPAS), intelligence and strike",
                        "Shadow R1: intelligence, surveillance and reconnaissance (ISR)",
                        "Quick Reaction Alert (QRA): Typhoons on permanent 24/7 readiness to intercept unidentified aircraft over UK airspace",
                        "Chinook: heavy lift helicopter, RAF Odiham",
                        "Merlin HC4/HM2: medium lift helicopter (RAF/RN shared)",
                    ],
                    "competency": "RAF knowledge — aircraft and operations (OASC interview)",
                },
                "resources": [
                    {"name": "RAF Aircraft", "url": "https://www.raf.mod.uk/aircraft/"},
                    {"name": "RAF News", "url": "https://www.raf.mod.uk/news/"}
                ]
            },
            {
                "id": "R1L4", "title": "Current RAF Operations & NATO Role", "unit": "Tier 1 — OASC Critical",
                "subtitle": "What the RAF is actually doing right now, and where",
                "url": "https://www.raf.mod.uk/operations/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 1,
                "confidence": 0,
                "learning_goals": [
                    "Name current RAF operations and the RAF's role in each",
                    "Explain the RAF's role within NATO and UK defence",
                    "Know recent significant RAF deployments or exercises",
                    "Understand how UK defence posture has changed since 2022"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["NATO", "Air Policing", "Operation Shader", "Baltic Air Policing", "UK defence", "ISTAR", "QRA", "Falkland Islands", "Cyprus", "Joint Expeditionary Force"],
                "feynman_prompt": "Explain the RAF's current operational commitments to someone who doesn't follow defence news. What is the RAF actually doing, and why does it matter?",
                "active_recall_questions": [
                    "What is Operation Shader and what is the RAF's current involvement?",
                    "What NATO air policing commitments does the RAF hold?",
                    "How has the UK's defence posture shifted since Russia's invasion of Ukraine in 2022?",
                    "Where are RAF aircraft permanently based overseas?"
                ],
                "knowledge_bank": {
                    "summary": "Knowing current RAF operations is essential for OASC. Candidates are expected "
                               "to follow defence news and understand the operational context they're joining.",
                    "facts": [
                        "Operation Shader: UK contribution to the defeat of Daesh (ISIS) in Iraq and Syria — RAF Reaper, Tornado (now retired), Typhoon involvement",
                        "NATO Baltic Air Policing: Typhoons deployed to Baltic states to police NATO airspace",
                        "QRA: Typhoons on 24/7 alert at Coningsby and Lossiemouth to intercept aircraft approaching UK airspace",
                        "Falkland Islands: permanent RAF presence, Typhoons on QRA (FIG — Falkland Islands Government)",
                        "Cyprus: RAF Akrotiri — forward operating base for Middle East operations",
                        "Russia's 2022 invasion of Ukraine significantly increased NATO's eastern flank deployments",
                        "Joint Expeditionary Force (JEF): UK-led grouping of northern European nations, RAF contributes air assets",
                        "ISTAR: Intelligence, Surveillance, Target Acquisition and Reconnaissance — Shadow, Sentinel, Rivet Joint",
                    ],
                    "competency": "Current affairs, RAF knowledge, strategic awareness (OASC interview)",
                },
                "resources": [
                    {"name": "RAF Operations", "url": "https://www.raf.mod.uk/operations/"},
                    {"name": "UK Defence Journal", "url": "https://ukdefencejournal.org.uk/"}
                ]
            },
            {
                "id": "R1L5", "title": "RAF Structure & Officer Ranks", "unit": "Tier 1 — OASC Critical",
                "subtitle": "Commands, rank structure, how the RAF is organised",
                "url": "https://www.raf.mod.uk/our-organisation/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 1,
                "confidence": 0,
                "learning_goals": [
                    "Describe the RAF's command structure",
                    "Name the officer ranks from Pilot Officer to Air Chief Marshal",
                    "Know the difference between commissioned and non-commissioned officers",
                    "Know which rank you'll enter at and your immediate career path"
                ],
                "techniques": ["Active Recall"],
                "key_vocab": ["Air Command", "Strike Command", "No. 1 Group", "No. 11 Group", "No. 22 Group", "Pilot Officer", "Flying Officer", "Flight Lieutenant", "Squadron Leader", "Wing Commander", "Group Captain", "Air Commodore", "Air Vice-Marshal", "Air Marshal", "Air Chief Marshal"],
                "feynman_prompt": "Explain the RAF's rank structure and organisational hierarchy to a civilian friend. Walk them from Pilot Officer to Air Chief Marshal and explain what each level commands.",
                "active_recall_questions": [
                    "List all RAF officer ranks from Pilot Officer to Air Chief Marshal",
                    "What rank does a newly commissioned officer enter at?",
                    "What is Air Command and what does it encompass?",
                    "What is the difference between a commissioned and non-commissioned officer?"
                ],
                "knowledge_bank": {
                    "summary": "The RAF is organised under Air Command, with numbered Groups responsible for different capabilities. "
                               "Officer ranks run from Pilot Officer (OF-1) to Air Chief Marshal (OF-9).",
                    "facts": [
                        "Officer ranks ascending: Pilot Officer → Flying Officer → Flight Lieutenant → Squadron Leader → Wing Commander → Group Captain → Air Commodore → Air Vice-Marshal → Air Marshal → Air Chief Marshal",
                        "New commissioned officers enter at Pilot Officer",
                        "Air Command: headquarters at RAF High Wycombe, commands all RAF flying and non-flying units",
                        "No. 1 Group: fast jet and attack aircraft",
                        "No. 11 Group: air defence and QRA",
                        "No. 22 Group: training and education",
                        "NCO ranks: Aircraftman, Leading Aircraftman, Senior Aircraftman, Corporal, Sergeant, Flight Sergeant, Warrant Officer",
                        "The Chief of the Air Staff (CAS) is the professional head of the RAF, typically an Air Chief Marshal",
                    ],
                    "competency": "RAF knowledge, structure and organisation (OASC interview)",
                },
                "resources": [
                    {"name": "RAF Organisation", "url": "https://www.raf.mod.uk/our-organisation/"}
                ]
            },
            {
                "id": "R1L6", "title": "Basic Aviation Knowledge", "unit": "Tier 1 — OASC Critical",
                "subtitle": "Four forces, how flight works, instruments — pilot candidate basics",
                "url": "https://www.skybrary.aero/articles/four-forces-flight",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 1,
                "confidence": 0,
                "learning_goals": [
                    "Explain the four forces of flight and how they interact",
                    "Describe how a wing generates lift",
                    "Explain what a stall is and why it matters",
                    "Describe the three axes of movement and the control surfaces for each"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["lift", "drag", "thrust", "weight", "Bernoulli", "angle of attack", "stall", "aerofoil", "roll", "pitch", "yaw", "aileron", "elevator", "rudder", "attitude indicator", "altimeter", "airspeed indicator"],
                "feynman_prompt": "Explain to a non-pilot how an aircraft flies. Cover the four forces, how lift is generated, and what happens when the aircraft stalls. Use plain language.",
                "active_recall_questions": [
                    "Name the four forces acting on an aircraft in straight and level flight",
                    "What is angle of attack and how does it relate to lift generation?",
                    "What is a stall — what causes it and how is it recovered?",
                    "Name the three axes of aircraft movement and which control surface controls each"
                ],
                "knowledge_bank": {
                    "summary": "As a pilot candidate you're expected to understand the basics of how aircraft fly. "
                               "This is Tier 1 because aviation questions are common in OASC pilot interviews.",
                    "facts": [
                        "Four forces: Lift (up), Weight/Gravity (down), Thrust (forward), Drag (backward)",
                        "Lift is generated by the aerofoil shape — faster airflow over the top creates lower pressure (Bernoulli's principle)",
                        "Angle of attack: the angle between the wing chord and the oncoming airflow",
                        "Stall: occurs when the critical angle of attack is exceeded — airflow separates from the wing, lift collapses",
                        "Stall recovery: reduce angle of attack (push forward), apply power",
                        "Roll axis (longitudinal): controlled by ailerons",
                        "Pitch axis (lateral): controlled by elevator/horizontal stabiliser",
                        "Yaw axis (vertical): controlled by rudder",
                        "Attitude indicator: shows pitch and roll relative to the horizon",
                        "Altimeter: shows altitude above mean sea level",
                        "Airspeed indicator (ASI): shows speed through the air",
                    ],
                    "competency": "Aviation knowledge — pilot interview (OASC)",
                },
                "resources": [
                    {"name": "SKYbrary — Four Forces", "url": "https://www.skybrary.aero/articles/four-forces-flight"},
                    {"name": "NASA Aerodynamics", "url": "https://www.grc.nasa.gov/www/k-12/airplane/bga.html"}
                ]
            },
            {
                "id": "R1L7", "title": "Leadership & Group Exercises", "unit": "Tier 1 — OASC Critical",
                "subtitle": "How to lead, how to contribute, what assessors actually look for",
                "url": "https://www.how2become.com/free-resources/raf-oasc/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 1,
                "confidence": 0,
                "learning_goals": [
                    "Understand what assessors look for in group and leaderless exercises",
                    "Know how to lead effectively without dominating",
                    "Know how to contribute as a team member when not the designated leader",
                    "Develop a decision-making framework for under-pressure scenarios"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["leadership", "delegation", "situational awareness", "decision making", "communication", "assertiveness", "active listening", "team dynamics", "leaderless exercise", "planning exercise"],
                "feynman_prompt": "Describe how you'd approach a leaderless exercise where the group is going in the wrong direction. How do you assert your view without alienating others?",
                "active_recall_questions": [
                    "What is the difference between assertive and aggressive in a group exercise?",
                    "How do you demonstrate leadership when you're not the designated leader?",
                    "Name 3 behaviours that immediately impress OASC assessors in group exercises",
                    "Name 3 behaviours that immediately count against candidates"
                ],
                "knowledge_bank": {
                    "summary": "OASC group exercises assess officer qualities — not just who talks most, but who leads effectively, "
                               "listens actively, and makes good decisions under pressure.",
                    "facts": [
                        "Assessors look for: initiative, clear communication, listening, composure under pressure, constructive contribution",
                        "Impresses: bringing quieter members in, changing your mind when shown to be wrong, clear rationale for decisions",
                        "Counts against: dominating without listening, ignoring the task, sycophancy, freezing under pressure",
                        "Leaderless exercises: no designated leader — everyone is assessed on whether they lead when needed and follow when appropriate",
                        "Planning exercises: you'll be given a scenario, resource constraints, and a time limit — allocate resources logically",
                        "Physical command tasks (at OASC): teamwork, communication, practical leadership under mild stress",
                    ],
                    "competency": "Leadership, teamwork, officer qualities (OASC group exercises)",
                },
                "resources": [
                    {"name": "OASC Guide", "url": "https://www.how2become.com/free-resources/raf-oasc/"}
                ]
            },
            {
                "id": "R1L8", "title": "UK Defence & Geopolitical Context", "unit": "Tier 1 — OASC Critical",
                "subtitle": "How the RAF fits into UK defence, NATO, and the current global picture",
                "url": "https://ukdefencejournal.org.uk/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 1,
                "confidence": 0,
                "learning_goals": [
                    "Explain how the RAF sits within UK defence alongside the Army and Royal Navy",
                    "Describe the UK's role in NATO and what Article 5 means",
                    "Know the major geopolitical threats driving UK defence priorities",
                    "Be able to discuss why defence spending and the RAF matter right now"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["NATO", "Article 5", "collective defence", "Integrated Review", "SDSR", "Ministry of Defence", "Chief of Defence Staff", "peer adversary", "Russia", "China", "cyber threat", "grey zone"],
                "feynman_prompt": "Explain to a sceptical civilian why the UK needs a large, capable air force in 2025. What threats justify the investment and what does the RAF uniquely provide?",
                "active_recall_questions": [
                    "What is NATO Article 5 and why does it matter to the RAF?",
                    "How has Russia's invasion of Ukraine changed UK/NATO defence posture?",
                    "What does the Integrated Review say about UK defence priorities?",
                    "How does the RAF's role differ from the Royal Navy's and Army's in UK defence?"
                ],
                "knowledge_bank": {
                    "summary": "OASC candidates are expected to understand the strategic context of the job they're applying for. "
                               "Current affairs and defence awareness will come up in the interview.",
                    "facts": [
                        "NATO Article 5: an attack on one member is an attack on all — the cornerstone of collective defence",
                        "UK's 2023 Integrated Review Refresh: identified Russia as the most acute threat, China as the systemic challenge",
                        "Russia's 2022 Ukraine invasion triggered increased NATO eastern flank deployments and defence spending commitments",
                        "UK defence budget: one of the largest in NATO, commitment to reach 2.5% GDP",
                        "Joint Chiefs: Chief of Defence Staff (CDS) is professional head of UK armed forces, above individual service chiefs",
                        "RAF's unique contribution: air sovereignty, strategic airlift, ISR, precision strike — capabilities Army/Navy can't replicate",
                        "Grey zone warfare: activity below the threshold of conventional conflict — cyber, disinformation, hybrid threats",
                    ],
                    "competency": "Strategic awareness, current affairs, motivation (OASC interview)",
                },
                "resources": [
                    {"name": "UK Defence Journal", "url": "https://ukdefencejournal.org.uk/"},
                    {"name": "RUSI", "url": "https://rusi.org/"}
                ]
            },
        ]
    },

    # ─────────────────────────────────────────────────────────────────────────
    # TIER 2 — GOOD TO KNOW
    # Likely to come up at OASC; not guaranteed but gives depth and confidence.
    # ─────────────────────────────────────────────────────────────────────────

    "Tier 2 — Good to Know": {
        "title": "Good to Know — Depth & Context",
        "color": "#e65100",
        "level": "Tier 2 — Good to Know",
        "oasc_tier": 2,
        "description": "Likely to come up at OASC, and knowing these gives you depth and confidence. "
                       "Study after all Tier 1 topics reach confidence 3.",
        "lessons": [
            {
                "id": "R2L1", "title": "RAF History & Heritage", "unit": "Tier 2 — Good to Know",
                "subtitle": "Battle of Britain, Cold War, modern era — the story of the RAF",
                "url": "https://www.raf.mod.uk/our-organisation/history/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 2,
                "confidence": 0,
                "learning_goals": [
                    "Describe key milestones in RAF history from 1918 to present",
                    "Explain the significance of the Battle of Britain",
                    "Know famous RAF figures and their contributions",
                    "Understand how the RAF's role has evolved"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["Battle of Britain", "Spitfire", "Hurricane", "Dambusters", "Cold War", "Falklands", "Gulf War", "Hugh Dowding", "Douglas Bader", "RAF Centenary"],
                "feynman_prompt": "Explain why the Battle of Britain is considered the RAF's defining moment. What were the stakes, what tactics were used, and why did the RAF prevail?",
                "active_recall_questions": [
                    "When was the RAF founded and from what predecessor service?",
                    "Describe the tactical situation during the Battle of Britain in summer 1940",
                    "What was Operation Chastise (the Dambusters raid) and what aircraft was used?",
                    "Name two significant RAF operations since 2000"
                ],
                "knowledge_bank": {
                    "facts": [
                        "RAF founded 1 April 1918, from Royal Flying Corps (RFC) and Royal Naval Air Service (RNAS)",
                        "Battle of Britain (July–October 1940): RAF Fighter Command defeated the Luftwaffe's attempt to gain air superiority over Britain",
                        "Hugh Dowding: Commander-in-Chief Fighter Command during Battle of Britain — credited with the victory through his radar and sector control system",
                        "Douglas Bader: famous for flying with two prosthetic legs, leading wing formations in the Battle of Britain",
                        "Dambusters (Operation Chastise, May 1943): 617 Squadron, Lancaster bombers with Barnes Wallis's bouncing bomb, breached Ruhr dams",
                        "Cold War: V-Bombers (Vulcan, Victor, Valiant) carried UK nuclear deterrent",
                        "Falklands 1982: Vulcan Black Buck raids, longest bombing raid in history at the time",
                        "Gulf War 1991, Iraq 2003, Libya 2011, Syria/Iraq 2014–present",
                        "RAF Centenary: 2018",
                    ],
                },
                "resources": [
                    {"name": "RAF History", "url": "https://www.raf.mod.uk/our-organisation/history/"}
                ]
            },
            {
                "id": "R2L2", "title": "Current Affairs — Defence & Geopolitics", "unit": "Tier 2 — Good to Know",
                "subtitle": "Stay informed on the world your RAF career will operate in",
                "url": "https://ukdefencejournal.org.uk/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 2,
                "confidence": 0,
                "learning_goals": [
                    "Follow defence and international news relevant to the RAF's role",
                    "Be able to discuss a recent defence story confidently",
                    "Understand the major global flashpoints the RAF might respond to",
                    "Show awareness that you're joining during a period of elevated threat"
                ],
                "techniques": ["Active Recall"],
                "key_vocab": ["Ukraine", "Russia", "NATO enlargement", "Indo-Pacific", "China", "cyber warfare", "hypersonic weapons", "drone warfare", "air defence"],
                "feynman_prompt": "Describe one significant defence story from the last 3 months and explain what it means for the RAF specifically.",
                "active_recall_questions": [
                    "Name one significant defence story from the last 3 months",
                    "What is the current status of the Ukraine conflict and what UK/NATO support has been given?",
                    "How has drone warfare in Ukraine changed how militaries think about air defence?",
                    "What is the Indo-Pacific tilt and does it affect the RAF?"
                ],
                "knowledge_bank": {
                    "facts": [
                        "Read UK Defence Journal (ukdefencejournal.org.uk) weekly as minimum prep",
                        "Ukraine war: ongoing since Feb 2022, NATO providing air defence systems, training, intelligence",
                        "Sweden and Finland joined NATO (2023/2024) — significant shift in European security",
                        "Drone warfare: Ukraine has demonstrated cheap drones can threaten expensive platforms — changing air defence doctrine",
                        "UK AUKUS: trilateral security pact (UK, US, Australia) — nuclear submarine technology sharing, RAF implications for ISR",
                        "Defence spending: UK committed to 2.5% GDP, one of highest in NATO",
                    ],
                },
                "resources": [
                    {"name": "UK Defence Journal", "url": "https://ukdefencejournal.org.uk/"},
                    {"name": "BBC Defence", "url": "https://www.bbc.co.uk/news/defence"}
                ]
            },
            {
                "id": "R2L3", "title": "OASC Process — What to Expect", "unit": "Tier 2 — Good to Know",
                "subtitle": "Full schedule, what each element assesses, how to stand out",
                "url": "https://www.raf.mod.uk/recruitment/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 2,
                "confidence": 0,
                "learning_goals": [
                    "Know the full OASC schedule and what each element assesses",
                    "Understand the officer qualities the selectors look for",
                    "Know what preparation is most valuable for each element",
                    "Know what makes candidates stand out vs fail"
                ],
                "techniques": ["Active Recall"],
                "key_vocab": ["OASC", "officer qualities", "leadership", "initiative", "resilience", "situational judgement", "leaderless exercise", "planning exercise", "command tasks", "presentation"],
                "feynman_prompt": "Explain what OASC is assessing at its core. It's not just about being smart — what human qualities are they really looking for, and why do those qualities matter in the RAF?",
                "active_recall_questions": [
                    "Name the main elements of the OASC selection process",
                    "What are the key officer qualities the RAF looks for at OASC?",
                    "What is a leaderless group exercise and what does it specifically test?",
                    "What are the most common reasons candidates fail OASC?"
                ],
                "knowledge_bank": {
                    "facts": [
                        "OASC elements: written tests, interview, group discussion, planning exercise, individual command task, physical command tasks",
                        "Candidate presentation: brief talk on a topic — assessed on communication, structure, confidence",
                        "Interview panel: typically 2-3 officers, covers motivation, values, current affairs, aviation knowledge",
                        "Group exercises: leaderless and designated leader formats — both used",
                        "Physical command tasks: team-based obstacles requiring communication and leadership",
                        "Common failure reasons: poor motivation narrative, inability to give STAR examples, weak current affairs, poor leadership in group exercises",
                        "Officer qualities: leadership potential, personal effectiveness, intellectual ability, effective communication",
                    ],
                },
                "resources": [
                    {"name": "OASC Guide — How2Become", "url": "https://www.how2become.com/free-resources/raf-oasc/"}
                ]
            },
            {
                "id": "R2L4", "title": "RAF Fitness Standards", "unit": "Tier 2 — Good to Know",
                "subtitle": "Exact requirements, where you are, your gap plan",
                "url": "https://www.raf.mod.uk/recruitment/life-in-the-raf/fitness/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 2,
                "confidence": 0,
                "learning_goals": [
                    "Know the exact fitness standards for RAF officer entry",
                    "Know the bleep test level required and your current level",
                    "Know the press-up and sit-up requirements for your age group",
                    "Have a concrete plan to meet and exceed minimum standards"
                ],
                "techniques": ["Active Recall"],
                "key_vocab": ["bleep test", "multi-stage fitness test", "MSFT", "VO2 max", "press-ups", "sit-ups", "RAF fitness test", "officer fitness"],
                "feynman_prompt": "State the exact RAF fitness test requirements for pilot entry. Then honestly assess where you are versus where you need to be and what your training plan is.",
                "active_recall_questions": [
                    "What is the minimum bleep test level required for RAF officer entry?",
                    "What are the press-up and sit-up requirements for your age group?",
                    "What level are you currently at and what is your gap to the standard?",
                    "What training approach will get you from your current level to standard before OASC?"
                ],
                "knowledge_bank": {
                    "facts": [
                        "RAF bleep test minimum: Level 9 Shuttle 10 for officer entry (check current standards — may vary by role)",
                        "Press-ups and sit-ups: 2-minute tests, standards vary by age and gender",
                        "Fitness test taken at the Medical (PMC) and again at OASC",
                        "Pilot candidates should aim to exceed minimums — being borderline fit sends a bad signal",
                        "Running 5k regularly plus calisthenics is solid baseline — add interval training to improve bleep test score",
                    ],
                },
                "resources": [
                    {"name": "RAF Fitness", "url": "https://www.raf.mod.uk/recruitment/life-in-the-raf/fitness/"}
                ]
            },
        ]
    },

    # ─────────────────────────────────────────────────────────────────────────
    # TIER 3 — POST-OFFER / BACKGROUND
    # Lower priority — study after Tier 1 and 2 are solid.
    # ─────────────────────────────────────────────────────────────────────────

    "Tier 3 — Post-Offer": {
        "title": "Post-Offer / Background Knowledge",
        "color": "#1565c0",
        "level": "Tier 3 — Background",
        "oasc_tier": 3,
        "description": "Good to know eventually, but not critical for OASC. "
                       "Study these once Tier 1 and 2 are at confidence 3.",
        "lessons": [
            {
                "id": "R3L1", "title": "RAF Pilot Training Pipeline", "unit": "Tier 3 — Post-Offer",
                "subtitle": "IOT, EFTS, BFJT, AFJT — the full route to wings",
                "url": "https://www.raf.mod.uk/recruitment/roles/pilot/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 3,
                "confidence": 0,
                "learning_goals": [
                    "Describe every stage of RAF pilot training from IOT to wings",
                    "Know the aircraft used at each stage of training",
                    "Understand the selection points within training where people wash out",
                    "Know the approximate timeline from OASC to first front-line posting"
                ],
                "techniques": ["Active Recall"],
                "key_vocab": ["IOT", "EFTS", "BFJT", "AFJT", "Grob Prefect", "Texan T6", "Hawk T2", "wings", "fast jet", "multi-engine", "rotary", "Cranwell", "Valley"],
                "feynman_prompt": "Walk through the complete RAF pilot training pipeline from day one at Cranwell to receiving your wings. Aircraft at each stage, what you're learning, timeline.",
                "active_recall_questions": [
                    "What does IOT stand for and how long does it last?",
                    "What aircraft is used for Elementary Flying Training?",
                    "At what stage do pilots split into fast jet, multi-engine, and rotary streams?",
                    "Approximately how long from starting IOT to reaching a front-line squadron?"
                ],
                "knowledge_bank": {
                    "facts": [
                        "Initial Officer Training (IOT): 24 weeks at RAF Cranwell — military officer foundation",
                        "Elementary Flying Training (EFTS): Grob Prefect at RAF Cranwell",
                        "Basic Fast Jet Training (BFJT): Texan T6 — primary fast jet selection",
                        "Advanced Fast Jet Training (AFJT): Hawk T2 at RAF Valley",
                        "Streaming: after EFTS, pilots are streamed to fast jet, multi-engine (King Air/Shadow), or rotary (Juno/Jupiter)",
                        "OCU (Operational Conversion Unit): type-specific training on front-line aircraft",
                        "Total pipeline: approximately 4-5 years from IOT to front-line for fast jet",
                    ],
                },
                "resources": [
                    {"name": "RAF Pilot Role", "url": "https://www.raf.mod.uk/recruitment/roles/pilot/"}
                ]
            },
            {
                "id": "R3L2", "title": "Life as an RAF Officer", "unit": "Tier 3 — Post-Offer",
                "subtitle": "Mess life, postings, pay, career progression",
                "url": "https://www.raf.mod.uk/recruitment/life-in-the-raf/",
                "estimated_minutes": 25, "split": False,
                "oasc_tier": 3,
                "confidence": 0,
                "learning_goals": [
                    "Understand the practicalities of life as a new RAF officer",
                    "Know officer pay bands and progression",
                    "Understand how postings work and what affects where you're sent",
                    "Know the commitment period on joining"
                ],
                "techniques": ["Active Recall"],
                "key_vocab": ["officers' mess", "posting", "detachment", "commission", "return of service", "RAF pay", "accommodation", "service family accommodation"],
                "feynman_prompt": "Describe what the first 2 years of life as a newly commissioned RAF officer pilot actually looks like — practically, day to day.",
                "active_recall_questions": [
                    "What is the initial commission period (return of service) for an RAF pilot?",
                    "What accommodation are new officers entitled to?",
                    "How does the RAF posting system work?",
                    "What is the officers' mess and what is expected of you there?"
                ],
                "knowledge_bank": {
                    "facts": [
                        "Initial return of service for pilots: approximately 12 years from award of wings",
                        "New officers live in the officers' mess — subsidised accommodation on base",
                        "Mess life: formal dining-in nights, informal socialising — integral to officer culture",
                        "Postings: typically every 2-3 years, preference taken into account but operational need takes priority",
                        "Pay: officers start at Flying Officer pay band, increments for time served and promotion",
                        "Detachments: periods away from home station on operations or exercises — part of the job",
                    ],
                },
                "resources": [
                    {"name": "Life in the RAF", "url": "https://www.raf.mod.uk/recruitment/life-in-the-raf/"}
                ]
            },
        ]
    },
}

SR_INTERVALS = {0: 1, 1: 3, 2: 7, 3: 14, 4: 30, 5: 90}

TIER_LABELS = {
    1: ("🔴 Tier 1", "OASC-Critical — must be articulable cold", "#b71c1c"),
    2: ("🟠 Tier 2", "Good to know — likely to come up", "#e65100"),
    3: ("🔵 Tier 3", "Background — study after Tier 1 & 2 are solid", "#1565c0"),
}

CONFIDENCE_LABELS = {
    0: ("Not started", "#999"),
    1: ("Aware", "#e67e22"),
    2: ("Can explain", "#3498db"),
    3: ("Interview-ready", "#27ae60"),
}


def get_all_raf_lessons():
    lessons = []
    for unit_data in RAF_CURRICULUM.values():
        for lesson in unit_data["lessons"]:
            lesson["unit_title"] = unit_data["title"]
        lessons.extend(unit_data["lessons"])
    return lessons


def get_raf_lesson_by_id(lesson_id: str):
    for unit_name, unit_data in RAF_CURRICULUM.items():
        for lesson in unit_data["lessons"]:
            if lesson["id"] == lesson_id:
                lesson["unit"] = unit_name
                lesson["unit_title"] = unit_data["title"]
                return lesson
    return None


def get_raf_unit_progress_summary(progress_data: dict):
    summary = {}
    for unit_name, unit_data in RAF_CURRICULUM.items():
        lessons = unit_data["lessons"]
        completed = sum(1 for l in lessons if progress_data.get(l["id"], {}).get("status") == "completed")
        avg_confidence = 0
        conf_lessons = [l for l in lessons if progress_data.get(l["id"], {}).get("confidence", 0) > 0]
        if conf_lessons:
            avg_confidence = round(
                sum(progress_data[l["id"]].get("confidence", 0) for l in conf_lessons) / len(conf_lessons), 1
            )
        summary[unit_name] = {
            "title": unit_data["title"],
            "completed": completed,
            "total": len(lessons),
            "percent": round(completed / len(lessons) * 100) if lessons else 0,
            "avg_confidence": avg_confidence,
            "color": unit_data["color"],
            "level": unit_data["level"],
            "oasc_tier": unit_data.get("oasc_tier", 0),
        }
    return summary


def get_tier1_readiness(progress_data: dict) -> dict:
    """
    Returns readiness stats for Tier 1 (OASC-critical) topics.
    {total, at_3, at_2, at_1, at_0, avg_confidence, ready_pct}
    """
    tier1_lessons = RAF_CURRICULUM.get("Tier 1 — OASC Critical", {}).get("lessons", [])
    confidences = [progress_data.get(l["id"], {}).get("confidence", 0) for l in tier1_lessons]
    total = len(tier1_lessons)
    at_3 = sum(1 for c in confidences if c == 3)
    at_2 = sum(1 for c in confidences if c == 2)
    at_1 = sum(1 for c in confidences if c == 1)
    at_0 = sum(1 for c in confidences if c == 0)
    avg = round(sum(confidences) / total, 2) if total else 0
    return {
        "total": total,
        "at_3": at_3,
        "at_2": at_2,
        "at_1": at_1,
        "at_0": at_0,
        "avg_confidence": avg,
        "ready_pct": round(at_3 / total * 100) if total else 0,
    }
