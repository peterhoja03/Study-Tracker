"""
RAF Application Study Curriculum
Tailored for: Post-DAA, ID check done, medical upcoming, targeting CBAT + OASC
Covers: Aptitude prep, officer knowledge, fitness, interview & board preparation
"""

RAF_CURRICULUM = {
    "Phase 1": {
        "title": "CBAT Aptitude Preparation",
        "color": "#1a3a6e",
        "level": "Immediate Priority",
        "description": "Computer-Based Aptitude Tests — verbal, numerical, spatial reasoning, and aviation-specific tests.",
        "lessons": [
            {
                "id": "R1L1", "title": "Understanding the CBAT", "unit": "Phase 1",
                "subtitle": "What to expect, test types, scoring, and strategy",
                "url": "https://www.raf.mod.uk/recruitment/roles/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Know exactly which CBAT tests apply to officer and pilot roles",
                    "Understand how each test is scored and what scores are needed",
                    "Identify your weakest areas to prioritise practice",
                    "Build a daily 25-min CBAT practice routine"
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "key_vocab": ["CBAT", "aptitude test", "verbal reasoning", "numerical reasoning", "spatial reasoning", "working memory", "processing speed", "RAF pilot aptitude"],
                "feynman_prompt": "Explain to a friend what the CBAT tests and why it's hard to prepare for in the traditional sense. What kinds of practice actually help?",
                "active_recall_questions": [
                    "Name the main test batteries included in the RAF CBAT",
                    "What is the key difference between practicing for aptitude tests vs knowledge exams?",
                    "Which test areas tend to be hardest for people with a humanities background?",
                    "What daily practice schedule would best improve your CBAT performance?"
                ],
                "resources": [
                    {"name": "RAF Official Site", "url": "https://www.raf.mod.uk/recruitment/"},
                    {"name": "Practice Aptitude Tests", "url": "https://www.practiceaptitudetests.com"},
                    {"name": "RAF Aptitude Guide", "url": "https://www.how2become.com/free-aptitude-tests/raf-aptitude-test/"}
                ]
            },
            {
                "id": "R1L2", "title": "Numerical Reasoning", "unit": "Phase 1",
                "subtitle": "Speed, accuracy, and confidence with numbers under pressure",
                "url": "https://www.practiceaptitudetests.com/numerical-reasoning-tests/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Solve percentage, ratio, and rate problems quickly and accurately",
                    "Interpret tables and graphs to extract numerical information",
                    "Apply mental arithmetic shortcuts to save time",
                    "Complete a timed 20-question numerical test with 80%+ accuracy"
                ],
                "techniques": ["Active Recall", "Pattern Recognition", "Writing Practice"],
                "key_vocab": ["percentage", "ratio", "rate", "mean", "average", "data interpretation", "mental arithmetic", "speed accuracy trade-off"],
                "feynman_prompt": "Walk through your mental process for solving a percentage increase question under timed conditions. What shortcuts do you use and where do errors creep in?",
                "active_recall_questions": [
                    "What is 15% of 340? (solve without a calculator)",
                    "A jet travels 480km in 40 minutes. What is its speed in km/h?",
                    "If fuel costs £1.80/litre and a tank holds 60 litres, what is the total cost?",
                    "What strategies help you stay accurate when working under time pressure?"
                ],
                "resources": [
                    {"name": "Practice Tests", "url": "https://www.practiceaptitudetests.com/numerical-reasoning-tests/"},
                    {"name": "JobTestPrep RAF", "url": "https://www.jobtestprep.co.uk/raf-tests"}
                ]
            },
            {
                "id": "R1L3", "title": "Verbal Reasoning", "unit": "Phase 1",
                "subtitle": "Reading comprehension, logic, and deductive reasoning at speed",
                "url": "https://www.practiceaptitudetests.com/verbal-reasoning-tests/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Identify the main point and implied meaning in dense passages",
                    "Apply true/false/cannot say logic consistently and quickly",
                    "Improve reading speed without sacrificing comprehension",
                    "Complete a timed verbal test with 85%+ accuracy"
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "key_vocab": ["verbal reasoning", "deductive reasoning", "inference", "true/false/cannot say", "reading comprehension", "logical conclusion"],
                "feynman_prompt": "Explain the 'cannot say' option in verbal reasoning tests. Why do people get this wrong so often, and what is the strict logical rule for choosing it?",
                "active_recall_questions": [
                    "What is the strict rule for answering 'cannot say' in verbal reasoning?",
                    "What is the fastest strategy for approaching a verbal reasoning passage?",
                    "How do you handle a question where the answer seems obvious but the passage doesn't say it?",
                    "Name 3 common traps in verbal reasoning questions"
                ],
                "resources": [
                    {"name": "Practice Tests", "url": "https://www.practiceaptitudetests.com/verbal-reasoning-tests/"}
                ]
            },
            {
                "id": "R1L4", "title": "Spatial Reasoning", "unit": "Phase 1",
                "subtitle": "3D visualisation, pattern rotation, instrument reading",
                "url": "https://www.practiceaptitudetests.com/spatial-reasoning-tests/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Mentally rotate 2D and 3D shapes accurately",
                    "Identify which shape is different in a series",
                    "Read and interpret aviation-style instrument displays",
                    "Improve spatial processing speed through daily practice"
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "key_vocab": ["spatial reasoning", "mental rotation", "3D visualisation", "instrument reading", "attitude indicator", "altimeter", "pattern recognition"],
                "feynman_prompt": "Describe your mental process when you rotate a 3D shape in your head. What techniques help you avoid getting confused by distractors?",
                "active_recall_questions": [
                    "What is the most reliable mental strategy for rotating 3D objects?",
                    "What does an attitude indicator (artificial horizon) show a pilot?",
                    "How do you systematically eliminate wrong answers in a spatial reasoning question?",
                    "What types of spatial questions are specific to pilot aptitude tests?"
                ],
                "resources": [
                    {"name": "Spatial Tests", "url": "https://www.practiceaptitudetests.com/spatial-reasoning-tests/"},
                    {"name": "Pilot Aptitude", "url": "https://www.pilotaptitudetest.com"}
                ]
            },
            {
                "id": "R1L5", "title": "Working Memory & Multi-Tasking", "unit": "Phase 1",
                "subtitle": "Dual-task performance, information retention, cognitive load",
                "url": "https://www.pilotaptitudetest.com",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Understand what working memory tests in a pilot context",
                    "Practice holding and manipulating multiple pieces of information simultaneously",
                    "Develop strategies for managing cognitive load under pressure",
                    "Understand why multi-tasking ability is critical for pilots"
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "key_vocab": ["working memory", "cognitive load", "dual task", "multi-tasking", "situational awareness", "information processing"],
                "feynman_prompt": "Explain why a pilot needs strong working memory even with modern autopilot systems. What kinds of information must they hold and process simultaneously in the cockpit?",
                "active_recall_questions": [
                    "What is working memory and how is it different from long-term memory?",
                    "Name 3 things a pilot must track simultaneously during an approach to land",
                    "What strategies help improve working memory capacity?",
                    "Why does stress reduce working memory performance and how can you mitigate this?"
                ],
                "resources": [
                    {"name": "Pilot Aptitude Test", "url": "https://www.pilotaptitudetest.com"}
                ]
            },
        ]
    },
    "Phase 2": {
        "title": "RAF Knowledge & Officer Qualities",
        "color": "#2e4d9e",
        "level": "Core Preparation",
        "description": "RAF structure, values, history, current operations, and what it means to be an officer.",
        "lessons": [
            {
                "id": "R2L1", "title": "RAF Structure & Organisation", "unit": "Phase 2",
                "subtitle": "Commands, stations, squadrons, ranks, and how the RAF is organised",
                "url": "https://www.raf.mod.uk/our-organisation/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Describe the RAF's command structure from top to bottom",
                    "Name the major RAF commands and what each is responsible for",
                    "Identify key RAF stations and what aircraft/roles they operate",
                    "Explain the rank structure from Aircraftman to Air Chief Marshal"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["RAF", "Air Command", "Strike Command", "squadron", "station", "wing", "group", "rank structure", "commissioned officer", "non-commissioned officer"],
                "feynman_prompt": "Explain the RAF's organisational structure to someone with no military background. How is it divided, who is in charge of what, and how does a pilot fit into it?",
                "active_recall_questions": [
                    "Name the main commands within the RAF and their primary roles",
                    "What is the difference between a commissioned and non-commissioned officer?",
                    "Name 5 RAF stations and what aircraft/roles they are known for",
                    "What rank does a newly commissioned officer enter at?"
                ],
                "resources": [
                    {"name": "RAF Organisation", "url": "https://www.raf.mod.uk/our-organisation/"},
                    {"name": "RAF Wikipedia", "url": "https://en.wikipedia.org/wiki/Royal_Air_Force"}
                ]
            },
            {
                "id": "R2L2", "title": "RAF Aircraft & Current Operations", "unit": "Phase 2",
                "subtitle": "Current fleet, NATO commitments, recent and ongoing operations",
                "url": "https://www.raf.mod.uk/aircraft/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Name all current front-line RAF aircraft and their primary roles",
                    "Describe the RAF's current operational commitments",
                    "Explain the RAF's role within NATO",
                    "Know recent significant RAF operations and exercises"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["Typhoon", "F-35B", "Voyager", "Atlas", "Poseidon", "Reaper", "Quick Reaction Alert", "NATO", "Air Policing", "Operation Shader"],
                "feynman_prompt": "You're being interviewed and asked 'What do you know about current RAF operations?' Deliver a confident, informed 2-minute answer covering aircraft and commitments.",
                "active_recall_questions": [
                    "Name the RAF's current fast jet aircraft and their roles",
                    "What is Quick Reaction Alert (QRA) and which aircraft perform it?",
                    "What is Operation Shader and what is the RAF's involvement?",
                    "What is the F-35B and how does it differ from the Typhoon?"
                ],
                "resources": [
                    {"name": "RAF Aircraft", "url": "https://www.raf.mod.uk/aircraft/"},
                    {"name": "RAF News", "url": "https://www.raf.mod.uk/news/"}
                ]
            },
            {
                "id": "R2L3", "title": "RAF Core Values & Standards", "unit": "Phase 2",
                "subtitle": "Respect, Integrity, Service, Excellence (RISE)",
                "url": "https://www.raf.mod.uk/our-organisation/raf-ethos-core-values-and-standards/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "State and explain each of the RAF's core values (RISE)",
                    "Give personal examples demonstrating each value",
                    "Explain what the values mean in practice as an officer",
                    "Understand why these values matter operationally and ethically"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["Respect", "Integrity", "Service", "Excellence", "RISE", "ethos", "values", "standards", "Service Test"],
                "feynman_prompt": "Pick one of the RAF core values and explain a real situation from your own life where you demonstrated it. Be specific, honest, and reflective.",
                "active_recall_questions": [
                    "State the 4 RAF core values from memory",
                    "Give a personal example that demonstrates Integrity",
                    "What does 'Service before self' mean in practice for an RAF officer?",
                    "How would you demonstrate Excellence in a non-military context?"
                ],
                "resources": [
                    {"name": "RAF Values", "url": "https://www.raf.mod.uk/our-organisation/raf-ethos-core-values-and-standards/"}
                ]
            },
            {
                "id": "R2L4", "title": "RAF History & Heritage", "unit": "Phase 2",
                "subtitle": "Key moments, Battle of Britain, Cold War, modern era",
                "url": "https://www.raf.mod.uk/our-organisation/history/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Describe key milestones in RAF history from 1918 to present",
                    "Explain the significance of the Battle of Britain",
                    "Know famous RAF figures and their contributions",
                    "Understand how the RAF's role has evolved over 100 years"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["Battle of Britain", "Spitfire", "Hurricane", "Dambusters", "Cold War", "Falklands", "Gulf War", "RAF Centenary", "Hugh Dowding", "Douglas Bader"],
                "feynman_prompt": "Explain why the Battle of Britain is considered the RAF's defining moment. What were the stakes, what tactics were used, and why did the RAF prevail?",
                "active_recall_questions": [
                    "When was the RAF founded and from what predecessor service?",
                    "Describe the tactical situation during the Battle of Britain in summer 1940",
                    "What was Operation Chastise (the Dambusters raid) and what aircraft was used?",
                    "Name two significant RAF operations since 2000"
                ],
                "resources": [
                    {"name": "RAF History", "url": "https://www.raf.mod.uk/our-organisation/history/"}
                ]
            },
        ]
    },
    "Phase 3": {
        "title": "OASC Preparation",
        "color": "#1a5276",
        "level": "High Priority",
        "description": "Officer and Aircrew Selection Centre — interviews, leadership tasks, group exercises, and pilot-specific tests.",
        "lessons": [
            {
                "id": "R3L1", "title": "Understanding OASC", "unit": "Phase 3",
                "subtitle": "What happens at OASC, what they assess, and what to expect",
                "url": "https://www.raf.mod.uk/recruitment/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Know the full OASC schedule and what each element assesses",
                    "Understand the officer qualities the selectors are looking for",
                    "Know what preparation is most valuable for each OASC element",
                    "Understand what makes candidates stand out vs fail"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["OASC", "officer qualities", "leadership", "teamwork", "initiative", "resilience", "communication", "situational judgement", "leaderless exercise"],
                "feynman_prompt": "Explain what OASC is assessing at its core. It's not just about being smart — what human qualities are they really looking for, and why?",
                "active_recall_questions": [
                    "Name the main elements of the OASC selection process",
                    "What are the key officer qualities the RAF looks for at OASC?",
                    "What is a leaderless group exercise and what does it test?",
                    "What are the most common reasons candidates fail OASC?"
                ],
                "resources": [
                    {"name": "RAF Recruitment", "url": "https://www.raf.mod.uk/recruitment/"},
                    {"name": "OASC Guide", "url": "https://www.how2become.com/free-resources/raf-oasc/"}
                ]
            },
            {
                "id": "R3L2", "title": "The Interview — Motivations & Personal Statement", "unit": "Phase 3",
                "subtitle": "Why the RAF, why pilot, your personal journey",
                "url": "https://www.raf.mod.uk/recruitment/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Articulate clearly and convincingly why you want to be an RAF pilot",
                    "Connect your personal background to the RAF's values and requirements",
                    "Prepare honest, specific answers to 'tell me about yourself' style questions",
                    "Know your own CV and application inside out"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["motivation", "personal statement", "STAR technique", "situational", "task", "action", "result", "self-awareness", "career goals"],
                "feynman_prompt": "Give your 2-minute answer to 'Why do you want to be an RAF pilot?' out loud. Be specific, genuine, and link it to your actual experiences.",
                "active_recall_questions": [
                    "Why do you want to be an RAF pilot specifically, not a commercial pilot?",
                    "What experiences in your life have prepared you for a military career?",
                    "What do you know about RAF pilot training and what comes after it?",
                    "What would you say is your biggest weakness and how are you working on it?"
                ],
                "resources": [
                    {"name": "STAR Technique", "url": "https://www.prospects.ac.uk/careers-advice/interview-tips/competency-based-interview-questions"}
                ]
            },
            {
                "id": "R3L3", "title": "Leadership & Group Exercises", "unit": "Phase 3",
                "subtitle": "Leading, contributing, and performing under observation",
                "url": "https://www.how2become.com/free-resources/raf-oasc/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Understand what assessors look for in group and leaderless exercises",
                    "Know how to lead effectively without dominating",
                    "Know how to contribute as a team member when not the designated leader",
                    "Develop a clear decision-making framework for under-pressure scenarios"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["leadership", "delegation", "situational awareness", "decision making", "communication", "assertiveness", "active listening", "team dynamics"],
                "feynman_prompt": "Describe how you would approach a leaderless exercise where you feel the group is going in the wrong direction. How do you assert your view without alienating others?",
                "active_recall_questions": [
                    "What is the difference between being assertive and being aggressive in a group setting?",
                    "How do you demonstrate leadership even when you're not the designated leader?",
                    "Name 3 things that immediately impress assessors in group exercises",
                    "Name 3 things that immediately count against candidates in group exercises"
                ],
                "resources": [
                    {"name": "OASC Guide", "url": "https://www.how2become.com/free-resources/raf-oasc/"}
                ]
            },
            {
                "id": "R3L4", "title": "Fitness Standards & Physical Preparation", "unit": "Phase 3",
                "subtitle": "RAF fitness requirements, bleep test, and ongoing preparation",
                "url": "https://www.raf.mod.uk/recruitment/life-in-the-raf/fitness/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Know the exact fitness standards required for RAF officer entry",
                    "Know the bleep test level required and where you currently are",
                    "Understand the fitness requirements for pilot training specifically",
                    "Have a concrete plan to meet and exceed minimum standards"
                ],
                "techniques": ["Active Recall"],
                "key_vocab": ["bleep test", "multi-stage fitness test", "VO2 max", "press-ups", "sit-ups", "RAF fitness test", "MSFT", "officer fitness standards"],
                "feynman_prompt": "State the exact RAF fitness test requirements for your role. Be specific about numbers. Then honestly assess where you are vs where you need to be.",
                "active_recall_questions": [
                    "What is the minimum bleep test level required for RAF officer entry?",
                    "What are the press-up and sit-up requirements for your age group?",
                    "What level are you currently at and what is your gap to the standard?",
                    "What training approach will get you from your current level to the required standard?"
                ],
                "resources": [
                    {"name": "RAF Fitness", "url": "https://www.raf.mod.uk/recruitment/life-in-the-raf/fitness/"}
                ]
            },
        ]
    },
    "Phase 4": {
        "title": "Pilot Training Pipeline Knowledge",
        "color": "#154360",
        "level": "Background Knowledge",
        "description": "Understanding what happens after selection — Initial Officer Training, EFTS, BFJT, and beyond.",
        "lessons": [
            {
                "id": "R4L1", "title": "RAF Pilot Training Pipeline", "unit": "Phase 4",
                "subtitle": "IOT, EFTS, BFJT, AFJT — the full route to wings",
                "url": "https://www.raf.mod.uk/recruitment/roles/pilot/",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Describe every stage of RAF pilot training from IOT to wings",
                    "Know the aircraft used at each stage of training",
                    "Understand the selection points within training where people wash out",
                    "Know the timeline from OASC pass to first front-line posting"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["IOT", "EFTS", "BFJT", "AFJT", "Grob Prefect", "Tucano", "Hawk T2", "wings ceremony", "fast jet", "multi-engine", "rotary", "Cranwell"],
                "feynman_prompt": "Walk through the complete RAF pilot training pipeline from day one at Cranwell to receiving your wings. What aircraft do you fly at each stage and what are you learning?",
                "active_recall_questions": [
                    "What does IOT stand for and how long does it last?",
                    "What aircraft is used for Elementary Flying Training?",
                    "At what stage do pilots split into fast jet, multi-engine, and rotary streams?",
                    "Approximately how long does it take from starting IOT to reaching a front-line squadron?"
                ],
                "resources": [
                    {"name": "RAF Pilot Role", "url": "https://www.raf.mod.uk/recruitment/roles/pilot/"}
                ]
            },
            {
                "id": "R4L2", "title": "Basic Aviation & Aerodynamics", "unit": "Phase 4",
                "subtitle": "Lift, drag, thrust, weight — the four forces of flight",
                "url": "https://www.skybrary.aero/articles/four-forces-flight",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Explain the four forces of flight and how they interact",
                    "Describe how a wing generates lift using Bernoulli and angle of attack",
                    "Explain what a stall is and why it happens",
                    "Describe the three axes of aircraft movement (roll, pitch, yaw)"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["lift", "drag", "thrust", "weight", "Bernoulli", "angle of attack", "stall", "aerofoil", "roll", "pitch", "yaw", "aileron", "elevator", "rudder"],
                "feynman_prompt": "Explain to a complete non-pilot how an aircraft wing generates lift. Use Bernoulli's principle and angle of attack. Then explain what happens when the aircraft stalls.",
                "active_recall_questions": [
                    "Name the four forces acting on an aircraft in straight and level flight",
                    "What is angle of attack and how does it relate to lift?",
                    "What is a stall and what conditions cause it?",
                    "Name the three axes of aircraft movement and which control surface controls each"
                ],
                "resources": [
                    {"name": "SKYbrary Aerodynamics", "url": "https://www.skybrary.aero/articles/four-forces-flight"},
                    {"name": "NASA Aerodynamics", "url": "https://www.grc.nasa.gov/www/k-12/airplane/bga.html"}
                ]
            },
        ]
    },
}

SR_INTERVALS = {0: 1, 1: 3, 2: 7, 3: 14, 4: 30, 5: 90}


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
        summary[unit_name] = {
            "title": unit_data["title"],
            "completed": completed,
            "total": len(lessons),
            "percent": round(completed / len(lessons) * 100) if lessons else 0,
            "color": unit_data["color"],
            "level": unit_data["level"],
        }
    return summary
