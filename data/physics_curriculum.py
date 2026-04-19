"""
AQA GCSE Physics Curriculum (8463) — full overhaul
All 8 topics, spec-accurate content only.
Each lesson has knowledge_bank + expected_answers for AI marking.
active_recall_questions and feynman_prompt removed — AI generates these dynamically.
"""

PHYSICS_CURRICULUM = {

    # ══════════════════════════════════════════════════════════════════
    # TOPIC 1 — ENERGY  (Paper 1)
    # ══════════════════════════════════════════════════════════════════
    "Topic 1": {
        "title": "Energy",
        "color": "#e74c3c",
        "level": "Foundation",
        "description": "Energy stores, transfers, conservation, efficiency, and global energy resources.",
        "lessons": [
            {
                "id": "P1L1",
                "title": "Energy Stores & Systems",
                "unit": "Topic 1",
                "subtitle": "Eight stores, what a system is, and how energy changes between stores",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/1",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Name all 8 energy stores from memory",
                    "Explain what a 'system' means in physics",
                    "Describe energy store changes for common everyday situations",
                    "Distinguish between an energy store and an energy transfer pathway",
                ],
                "key_vocab": [
                    "energy store", "kinetic", "gravitational potential", "elastic potential",
                    "thermal", "chemical", "nuclear", "electrostatic", "magnetic", "system",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/1"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/energy"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "A system is an object or group of objects. When a system changes, energy "
                        "is transferred between stores. The eight energy stores are: kinetic, "
                        "gravitational potential, elastic potential, thermal, chemical, nuclear, "
                        "electrostatic, and magnetic. Energy is transferred via four pathways: "
                        "mechanical work, electrical work, heating, and radiation. Energy cannot "
                        "be created or destroyed — only transferred between stores."
                    ),
                    "facts": [
                        "The 8 energy stores are: kinetic, gravitational potential, elastic potential, thermal, chemical, nuclear, electrostatic, magnetic.",
                        "A system is an object or group of objects.",
                        "Energy transfer pathways: mechanical work, electrical work, heating, radiation.",
                        "An object projected upwards: kinetic store → gravitational potential store.",
                        "A moving object hitting an obstacle: kinetic store → thermal store (and sound).",
                        "A vehicle slowing down: kinetic store → thermal store (brakes/road).",
                        "Boiling water in a kettle: chemical/electrical store → thermal store.",
                        "Energy cannot be created or destroyed.",
                    ],
                    "spec_points": ["4.1.1.1"],
                },
                "expected_answers": {
                    "Name all 8 energy stores.": (
                        "Kinetic, gravitational potential, elastic potential, thermal, chemical, "
                        "nuclear, electrostatic, magnetic."
                    ),
                    "What is a system in physics?": (
                        "A system is an object or a group of objects."
                    ),
                    "Describe the energy store changes when a ball is thrown upwards.": (
                        "Chemical store (muscles) → kinetic store (moving ball) → gravitational "
                        "potential store (at highest point). On the way down: GPE → KE."
                    ),
                    "What is the difference between an energy store and an energy transfer pathway?": (
                        "A store holds energy at a given moment. A transfer pathway is the process "
                        "by which energy moves between stores — e.g. heating, mechanical work."
                    ),
                },
            },
            {
                "id": "P1L2",
                "title": "Kinetic, GPE & Elastic PE Calculations",
                "unit": "Topic 1",
                "subtitle": "Ek = ½mv², Ep = mgh, Ee = ½ke²",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/2",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Recall and apply Ek = ½mv²",
                    "Apply Ep = mgh (g is given in the exam)",
                    "Recall and apply Ee = ½ke²",
                    "Substitute and rearrange all three equations correctly",
                ],
                "key_vocab": [
                    "kinetic energy", "gravitational potential energy", "elastic potential energy",
                    "spring constant", "extension", "limit of proportionality",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/2"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/energy"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Three equations give the energy in common stores. Kinetic energy "
                        "Ek = ½mv² (recall and apply). Gravitational PE Ep = mgh (given on "
                        "equation sheet; g given in questions). Elastic PE Ee = ½ke² "
                        "(recall and apply; only valid up to the limit of proportionality)."
                    ),
                    "equations": [
                        "Ek = ½mv²  (kinetic energy, J; mass m in kg; speed v in m/s)",
                        "Ep = mgh   (GPE, J; mass m in kg; g in N/kg; height h in m) — given on sheet",
                        "Ee = ½ke²  (elastic PE, J; spring constant k in N/m; extension e in m)",
                    ],
                    "worked_example": {
                        "problem": "A 2 kg ball moves at 3 m/s. Calculate its kinetic energy.",
                        "steps": [
                            "Write equation: Ek = ½mv²",
                            "Substitute: Ek = ½ × 2 × 3²",
                            "Calculate: Ek = ½ × 2 × 9 = 9 J",
                        ],
                    },
                    "common_mistakes": [
                        "Forgetting to square the speed in Ek = ½mv².",
                        "Using cm instead of m for extension in Ee = ½ke².",
                        "Using g = 9.8 when the question has already given g — use the given value.",
                    ],
                    "spec_points": ["4.1.1.2"],
                },
                "expected_answers": {
                    "Calculate the KE of a 2 kg object moving at 3 m/s.": (
                        "Ek = ½mv² = ½ × 2 × 3² = ½ × 2 × 9 = 9 J"
                    ),
                    "A spring with k = 200 N/m is stretched 0.05 m. Find the elastic PE.": (
                        "Ee = ½ke² = ½ × 200 × 0.05² = ½ × 200 × 0.0025 = 0.25 J"
                    ),
                    "An object of mass 5 kg is raised 4 m (g = 10 N/kg). Find the GPE gained.": (
                        "Ep = mgh = 5 × 10 × 4 = 200 J"
                    ),
                },
            },
            {
                "id": "P1L3",
                "title": "Specific Heat Capacity",
                "unit": "Topic 1",
                "subtitle": "ΔE = mcΔθ — Required Practical 1",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/3",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Define specific heat capacity in plain language",
                    "Apply ΔE = mcΔθ to calculate energy changes",
                    "Describe the RP1 method and identify key variables",
                    "Explain why water is used in central heating systems",
                ],
                "key_vocab": [
                    "specific heat capacity", "thermal energy", "temperature change",
                    "joules per kilogram per degree Celsius", "J/kg°C",
                ],
                "techniques": ["Active Recall", "Show Working", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/3"},
                    {"name": "GCSE Physics Online — Required Practicals", "url": "https://www.gcsephysicsonline.com/required-practicals"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "The amount of thermal energy stored or released as temperature changes is "
                        "given by ΔE = mcΔθ. Specific heat capacity c is the energy required to raise "
                        "1 kg of a substance by 1°C. Unit: J/kg°C. RP1: heat a block electrically, "
                        "measure V, I, t → ΔE = VIt; measure mass and temperature rise → c = ΔE/(mΔθ). "
                        "Wrap block in insulation to reduce heat loss to surroundings."
                    ),
                    "equations": [
                        "ΔE = mcΔθ  (ΔE in J; mass m in kg; c in J/kg°C; temperature change Δθ in °C) — given on sheet",
                        "ΔE = VIt  (used to find energy input in RP1)",
                    ],
                    "facts": [
                        "Specific heat capacity: energy needed to raise 1 kg of substance by 1°C.",
                        "Water has a high SHC (4200 J/kg°C) — stores a lot of energy per kg.",
                        "RP1 independent variable: material. Control: mass, insulation.",
                        "Insulating the block in RP1 reduces heat loss to surroundings.",
                    ],
                    "common_mistakes": [
                        "Confusing specific heat capacity (temperature change) with specific latent heat (state change).",
                        "Not converting mass to kg before substituting.",
                    ],
                    "spec_points": ["4.1.1.3"],
                },
                "expected_answers": {
                    "What does specific heat capacity mean?": (
                        "The amount of energy (in joules) required to raise the temperature of "
                        "1 kg of the substance by 1°C."
                    ),
                    "Calculate the energy needed to heat 2 kg of water (c = 4200 J/kg°C) by 50°C.": (
                        "ΔE = mcΔθ = 2 × 4200 × 50 = 420,000 J"
                    ),
                    "Why is water used in central heating systems?": (
                        "Water has a high specific heat capacity, so it stores a large amount of "
                        "thermal energy per kilogram, making heat transfer to rooms efficient."
                    ),
                    "In RP1, why is the metal block wrapped in insulation?": (
                        "To reduce heat loss to the surroundings, making the measurement of energy "
                        "transferred to the block more accurate."
                    ),
                },
            },
            {
                "id": "P1L4",
                "title": "Power",
                "unit": "Topic 1",
                "subtitle": "P = E/t and P = W/t — rate of energy transfer",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/4",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Define power as the rate of energy transfer or work done",
                    "Recall and apply P = E/t and P = W/t",
                    "State that 1 watt = 1 joule per second",
                    "Compare power in everyday scenarios",
                ],
                "key_vocab": ["power", "watt", "joule per second", "rate of energy transfer", "work done"],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/4"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Power is the rate at which energy is transferred or work is done. "
                        "P = E/t = W/t. Unit: watts (W). 1 W = 1 J/s. A higher power device "
                        "transfers more energy per second. Two motors doing the same job: the "
                        "faster one is more powerful."
                    ),
                    "equations": [
                        "P = E/t  (power P in W; energy E in J; time t in s) — recall and apply",
                        "P = W/t  (work done W in J)",
                    ],
                    "facts": [
                        "1 watt = 1 joule per second.",
                        "Power tells you how quickly energy is transferred, not how much total.",
                    ],
                    "spec_points": ["4.1.1.4"],
                },
                "expected_answers": {
                    "A motor transfers 600 J in 30 s. What is its power?": (
                        "P = E/t = 600 / 30 = 20 W"
                    ),
                    "Two motors both lift the same weight the same height. Motor A takes 5 s, B takes 10 s. Which is more powerful?": (
                        "Motor A — it does the same work in half the time, so it has twice the power."
                    ),
                    "What does it mean for a device to have a power of 1 watt?": (
                        "It transfers 1 joule of energy every second."
                    ),
                },
            },
            {
                "id": "P1L5",
                "title": "Conservation & Dissipation of Energy",
                "unit": "Topic 1",
                "subtitle": "Energy is always conserved; dissipation and thermal conductivity",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/5",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "State the law of conservation of energy",
                    "Explain what 'dissipated' energy means",
                    "Explain how lubrication and insulation reduce unwanted transfers",
                    "Describe how wall thickness and thermal conductivity affect cooling rate",
                ],
                "key_vocab": [
                    "conservation of energy", "dissipation", "wasted energy",
                    "thermal conductivity", "lubrication", "thermal insulation", "closed system",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/5"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Energy cannot be created or destroyed — only transferred between stores "
                        "or dissipated. Dissipated energy spreads out to the surroundings as "
                        "thermal energy in less useful ways. Lubrication reduces friction → less "
                        "energy transferred to thermal store. Thermal insulation slows conduction. "
                        "Higher thermal conductivity of a material → faster rate of energy transfer "
                        "by conduction. Thicker walls with lower k → slower cooling of buildings. "
                        "Students do NOT need to know the definition of thermal conductivity."
                    ),
                    "facts": [
                        "Energy cannot be created or destroyed.",
                        "In a closed system there is no net change to total energy.",
                        "Dissipated energy is stored in less useful ways, often as heat in the surroundings.",
                        "Lubrication reduces friction between surfaces, reducing thermal dissipation.",
                        "Thermal insulation reduces the rate of energy transfer by conduction.",
                        "Higher thermal conductivity → faster conduction through a material.",
                        "Thicker walls and lower thermal conductivity → slower rate of building heat loss.",
                    ],
                    "spec_points": ["4.1.2.1"],
                },
                "expected_answers": {
                    "What does it mean for energy to be dissipated?": (
                        "Energy is spread out to the surroundings as thermal energy in a less "
                        "useful form — it cannot easily be recovered."
                    ),
                    "How does lubrication reduce energy wastage?": (
                        "Lubrication reduces friction between moving surfaces, so less energy "
                        "is transferred to the thermal store by heating."
                    ),
                    "A building has thick walls with low thermal conductivity. How does this affect heat loss?": (
                        "It reduces the rate of energy transfer by conduction through the walls, "
                        "so the building loses heat more slowly and stays warmer."
                    ),
                },
            },
            {
                "id": "P1L6",
                "title": "Efficiency",
                "unit": "Topic 1",
                "subtitle": "efficiency = useful output / total input",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/6",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Recall and apply both efficiency equations",
                    "Express efficiency as a decimal and as a percentage",
                    "Explain why efficiency can never exceed 1 (100%)",
                    "(HT) Describe ways to increase efficiency of an energy transfer",
                ],
                "key_vocab": [
                    "efficiency", "useful output energy", "total input energy",
                    "useful power output", "total power input",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/6"},
                    {"name": "Physics & Maths Tutor", "url": "https://www.physicsandmathstutor.com/physics-revision/gcse-aqa/"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Efficiency = useful output energy transfer / total input energy transfer. "
                        "Also: efficiency = useful power output / total power input. "
                        "Can be a decimal (0 to 1) or percentage (multiply by 100). "
                        "Efficiency can never exceed 1 because that would require more useful "
                        "energy out than total energy in — violating conservation. "
                        "HT: ways to increase efficiency include reducing friction (lubrication), "
                        "better thermal insulation, streamlining to reduce air resistance."
                    ),
                    "equations": [
                        "efficiency = useful output energy transfer / total input energy transfer",
                        "efficiency = useful power output / total power input",
                    ],
                    "facts": [
                        "Efficiency is dimensionless — expressed as decimal or percentage.",
                        "Efficiency cannot exceed 1 (100%) — conservation of energy.",
                        "HT: Increase efficiency by reducing friction, insulating, streamlining.",
                    ],
                    "spec_points": ["4.1.2.2"],
                },
                "expected_answers": {
                    "A machine uses 500 J and produces 350 J of useful output. Calculate efficiency.": (
                        "efficiency = 350 / 500 = 0.7 (or 70%)"
                    ),
                    "Can efficiency ever be greater than 1? Explain.": (
                        "No — that would mean more useful energy out than total energy in, "
                        "which violates the law of conservation of energy."
                    ),
                    "(HT) Give two ways to increase the efficiency of a car engine.": (
                        "Reduce friction between moving parts via lubrication; "
                        "use thermal insulation to reduce heat loss from the engine."
                    ),
                },
            },
            {
                "id": "P1L7",
                "title": "National & Global Energy Resources",
                "unit": "Topic 1",
                "subtitle": "Renewable vs non-renewable, uses, environmental impacts",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/7",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Name all main energy resources and classify as renewable or non-renewable",
                    "Compare reliability and environmental impact of different resources",
                    "Identify the three main uses: transport, electricity generation, heating",
                    "Explain why science alone cannot always solve energy policy problems",
                ],
                "key_vocab": [
                    "renewable", "non-renewable", "fossil fuels", "nuclear", "bio-fuel",
                    "wind", "hydroelectricity", "geothermal", "tidal", "solar", "water waves",
                    "carbon footprint", "reliability",
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/7"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/energy"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Main energy resources: fossil fuels (coal, oil, gas), nuclear fuel, "
                        "bio-fuel, wind, hydroelectricity, geothermal, tides, solar (the Sun), "
                        "water waves. Renewable = replenished as fast as it is used. "
                        "Non-renewable = finite. Uses: transport, electricity generation, heating. "
                        "Environmental impacts vary (CO2, land use, radioactive waste). "
                        "Science identifies problems but political, social, ethical, and economic "
                        "factors determine which solutions are implemented. "
                        "Note: descriptions of HOW electricity is generated are NOT required."
                    ),
                    "facts": [
                        "Fossil fuels: coal, oil, gas — non-renewable.",
                        "Renewable resources: bio-fuel, wind, hydroelectricity, geothermal, tidal, solar, water waves.",
                        "Nuclear fuel is non-renewable but produces very low CO2 during operation.",
                        "Three uses of energy resources: transport, electricity generation, heating.",
                        "Wind and solar are intermittent — reliability is a disadvantage.",
                        "Fossil fuels produce CO2 → global warming. Nuclear produces radioactive waste.",
                        "Science can identify environmental issues but political/economic factors control implementation.",
                    ],
                    "spec_points": ["4.1.3"],
                },
                "expected_answers": {
                    "List four renewable energy resources.": (
                        "Any four from: wind, solar, hydroelectricity, tidal, geothermal, bio-fuel, water waves."
                    ),
                    "Give one advantage and one disadvantage of nuclear power.": (
                        "Advantage: low CO2 emissions during operation. "
                        "Disadvantage: produces radioactive waste requiring safe long-term storage."
                    ),
                    "Why can't science alone solve the problem of climate change from fossil fuels?": (
                        "Political, social, ethical and economic factors also determine energy policy. "
                        "Science identifies the problem and potential solutions, but it cannot force "
                        "governments or industries to act."
                    ),
                    "What is meant by a renewable energy resource?": (
                        "One that is being (or can be) replenished as it is used — it will not run out."
                    ),
                },
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # TOPIC 2 — ELECTRICITY  (Paper 1)
    # ══════════════════════════════════════════════════════════════════
    "Topic 2": {
        "title": "Electricity",
        "color": "#f39c12",
        "level": "Foundation",
        "description": "Circuits, current, resistance, power, mains electricity, and static charge.",
        "lessons": [
            {
                "id": "P2L1",
                "title": "Charge, Current & Circuit Symbols",
                "unit": "Topic 2",
                "subtitle": "Q = It, standard symbols, current in series loops",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/1",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Draw and interpret standard circuit diagram symbols",
                    "Define electric current as rate of flow of charge",
                    "Recall and apply Q = It",
                    "State that current is the same at all points in a series loop",
                ],
                "key_vocab": [
                    "electric current", "charge", "coulomb", "ampere", "potential difference",
                    "circuit symbol", "ammeter", "voltmeter", "diode", "LDR", "thermistor",
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/1"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/electricity"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Electric current is a flow of electrical charge. The size of the current "
                        "is the rate of flow of charge: Q = It. Charge in coulombs (C), current "
                        "in amperes (A), time in seconds (s). For electrical charge to flow, the "
                        "circuit must include a source of potential difference and be closed. "
                        "Current has the same value at any point in a single closed (series) loop. "
                        "Standard symbols must be drawn and recognised: cell, battery, switch, "
                        "resistor, variable resistor, lamp, ammeter, voltmeter, diode, LDR, "
                        "thermistor, LED, fuse."
                    ),
                    "equations": [
                        "Q = It  (charge Q in C; current I in A; time t in s) — recall and apply",
                    ],
                    "facts": [
                        "Electric current = rate of flow of charge.",
                        "1 coulomb = charge flowing when 1 A flows for 1 s.",
                        "Current is the same everywhere in a single series loop.",
                        "A closed circuit with a source of pd is needed for current to flow.",
                        "Ammeter connected in series; voltmeter connected in parallel.",
                    ],
                    "spec_points": ["4.2.1.1", "4.2.1.2"],
                },
                "expected_answers": {
                    "What is electric current?": (
                        "Electric current is the rate of flow of electrical charge."
                    ),
                    "A current of 3 A flows for 20 s. What charge has flowed?": (
                        "Q = It = 3 × 20 = 60 C"
                    ),
                    "What conditions are needed for current to flow in a circuit?": (
                        "The circuit must be closed (complete loop) and include a source of "
                        "potential difference."
                    ),
                },
            },
            {
                "id": "P2L2",
                "title": "Resistance & Ohm's Law",
                "unit": "Topic 2",
                "subtitle": "V = IR, ohmic conductors, RP3",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/3",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Recall and apply V = IR",
                    "Explain what an ohmic conductor is",
                    "Describe how resistance of a filament lamp changes with temperature",
                    "Describe RP3 — investigating resistance of a wire",
                ],
                "key_vocab": [
                    "potential difference", "resistance", "ohm", "ohmic conductor",
                    "Ohm's law", "filament lamp", "thermistor", "LDR",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/3"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/electricity"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "The current through a component depends on resistance and potential "
                        "difference across it: V = IR. An ohmic conductor (at constant temperature) "
                        "has constant resistance — current is directly proportional to pd. "
                        "Filament lamp: resistance increases as temperature increases (ions vibrate "
                        "more, impede electrons). Diode: current in one direction only; very high "
                        "resistance in reverse. Thermistor: resistance decreases as temperature "
                        "increases. LDR: resistance decreases as light intensity increases. "
                        "RP3: measure resistance of a wire at different lengths; also series/parallel combinations."
                    ),
                    "equations": [
                        "V = IR  (pd V in volts; current I in A; resistance R in Ω) — recall and apply",
                    ],
                    "facts": [
                        "Ohmic conductor: R is constant at constant temperature (I ∝ V).",
                        "Filament lamp: R increases with temperature — non-ohmic.",
                        "Diode: current flows in forward direction only; very high R in reverse.",
                        "Thermistor: R decreases as temperature increases — used in thermostats.",
                        "LDR: R decreases as light intensity increases — used in light-sensitive switches.",
                        "RP3: independent variable = length of wire (or component type).",
                    ],
                    "spec_points": ["4.2.1.3", "4.2.1.4"],
                },
                "expected_answers": {
                    "A pd of 12 V drives a current of 0.5 A through a resistor. What is its resistance?": (
                        "R = V/I = 12 / 0.5 = 24 Ω"
                    ),
                    "Why does the resistance of a filament lamp increase as it gets hotter?": (
                        "As temperature rises, the metal ions vibrate more vigorously, impeding the "
                        "flow of electrons more — so resistance increases."
                    ),
                    "What is an ohmic conductor?": (
                        "A conductor where current is directly proportional to potential difference "
                        "at constant temperature — resistance stays constant."
                    ),
                    "Describe the resistance behaviour of a thermistor.": (
                        "Its resistance decreases as temperature increases."
                    ),
                },
            },
            {
                "id": "P2L3",
                "title": "I–V Characteristics",
                "unit": "Topic 2",
                "subtitle": "Graph shapes for resistor, filament lamp, and diode — RP4",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/4",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Describe and explain the I–V graph for an ohmic resistor",
                    "Describe and explain the I–V graph for a filament lamp",
                    "Describe and explain the I–V graph for a diode",
                    "State the purpose of a variable resistor in RP4",
                ],
                "key_vocab": [
                    "I–V characteristic", "linear", "non-linear", "gradient", "forward threshold",
                    "reverse bias", "variable resistor",
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/4"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "I–V graph for ohmic resistor: straight line through the origin — gradient = 1/R. "
                        "Filament lamp: S-shaped curve — gradient decreases at higher currents because "
                        "resistance increases with temperature. "
                        "Diode: flat/near-zero current for reverse/small forward pd; steep rise above "
                        "forward threshold (~0.6 V); virtually zero current in reverse. "
                        "RP4: use a variable resistor to vary pd; record I and V; plot I–V for "
                        "filament lamp, diode, and ohmic resistor."
                    ),
                    "facts": [
                        "Ohmic resistor I–V: straight line through origin. Gradient = 1/R.",
                        "Filament lamp I–V: curve that flattens — R increases as current heats filament.",
                        "Diode I–V: near-zero current in reverse; sharp rise in forward direction above threshold.",
                        "Gradient of I–V graph = 1/R (steeper = lower resistance).",
                        "RP4: variable resistor varies current/pd; ammeter in series; voltmeter in parallel.",
                    ],
                    "spec_points": ["4.2.1.4"],
                },
                "expected_answers": {
                    "Describe the I–V graph shape for a filament lamp and explain why.": (
                        "An S-shaped curve that flattens at higher currents. As current increases, "
                        "the filament heats up, resistance increases, so the current rises less "
                        "steeply for the same increase in voltage."
                    ),
                    "What does the gradient of an I–V graph represent?": (
                        "1/R — a steeper gradient means lower resistance."
                    ),
                    "Why is a variable resistor included in the RP4 circuit?": (
                        "To vary the current and potential difference across the component so the "
                        "full I–V characteristic can be plotted."
                    ),
                },
            },
            {
                "id": "P2L4",
                "title": "Series & Parallel Circuits",
                "unit": "Topic 2",
                "subtitle": "Rules for current, pd, and resistance in each circuit type",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/5",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "State the rules for current and pd in series circuits",
                    "State the rules for current and pd in parallel circuits",
                    "Calculate total resistance for series combinations",
                    "(HT) Calculate total resistance for parallel combinations using 1/R formula",
                ],
                "key_vocab": [
                    "series", "parallel", "total resistance", "branch current",
                    "potential difference shared", "potential difference same",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/5"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Series: same current through each component; pd shared across components; "
                        "Rtotal = R1 + R2. "
                        "Parallel: same pd across each branch; total current = sum of branch currents; "
                        "total R is less than the smallest individual R. "
                        "HT: 1/Rtotal = 1/R1 + 1/R2."
                    ),
                    "equations": [
                        "Series: Rtotal = R1 + R2  (recall and apply)",
                        "HT Parallel: 1/Rtotal = 1/R1 + 1/R2",
                    ],
                    "facts": [
                        "Series: current same everywhere; pd splits across components.",
                        "Parallel: pd same across each branch; current splits at junctions.",
                        "Adding resistors in series increases total resistance.",
                        "Adding resistors in parallel decreases total resistance — more paths for current.",
                        "Total parallel R is always less than the smallest individual resistor.",
                    ],
                    "spec_points": ["4.2.2"],
                },
                "expected_answers": {
                    "Two resistors, 4 Ω and 6 Ω, are in series. What is the total resistance?": (
                        "Rtotal = 4 + 6 = 10 Ω"
                    ),
                    "(HT) The same resistors are in parallel. What is the total resistance?": (
                        "1/R = 1/4 + 1/6 = 3/12 + 2/12 = 5/12. R = 12/5 = 2.4 Ω"
                    ),
                    "Why does adding resistors in parallel reduce total resistance?": (
                        "Each new parallel branch provides an additional path for current to flow, "
                        "so overall opposition to current flow decreases."
                    ),
                    "In a series circuit, what happens to current across each component?": (
                        "Current is the same through every component in a series circuit."
                    ),
                },
            },
            {
                "id": "P2L5",
                "title": "Domestic Electricity — AC, Mains & Safety",
                "unit": "Topic 2",
                "subtitle": "AC vs DC, UK mains supply, plugs, live/neutral/earth, fuses",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/6",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Distinguish between direct current (dc) and alternating current (ac)",
                    "State UK mains supply: ~230 V, 50 Hz",
                    "Explain the role of live, neutral, and earth wires",
                    "Explain how a fuse protects an appliance",
                ],
                "key_vocab": [
                    "alternating current", "direct current", "mains supply", "live wire",
                    "neutral wire", "earth wire", "fuse", "frequency", "hertz",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/6"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Direct current (dc): flows in one constant direction (batteries). "
                        "Alternating current (ac): direction reverses periodically. UK mains: ~230 V, 50 Hz. "
                        "UK plug wiring: live (brown) carries 230 V; neutral (blue) ~0 V completes circuit; "
                        "earth (green/yellow) safety wire. Fuse in live wire — if current too high, fuse "
                        "melts and breaks the circuit, cutting off supply. Earth wire: if a fault connects "
                        "live to metal casing, large current flows to earth → blows fuse → safe."
                    ),
                    "facts": [
                        "DC: flows in one direction only. AC: reverses periodically.",
                        "UK mains: approximately 230 V, 50 Hz.",
                        "Live wire: brown, 230 V — dangerous to touch.",
                        "Neutral wire: blue, ~0 V.",
                        "Earth wire: green/yellow — safety only.",
                        "Fuse is always placed in the live wire.",
                        "If fault occurs: large current → fuse blows → circuit broken → safe.",
                    ],
                    "spec_points": ["4.2.3", "4.2.4"],
                },
                "expected_answers": {
                    "What is the difference between ac and dc?": (
                        "DC flows in one constant direction. AC reverses direction "
                        "periodically (50 times per second in the UK)."
                    ),
                    "What colour is the live, neutral, and earth wire in a UK plug?": (
                        "Live: brown. Neutral: blue. Earth: green and yellow."
                    ),
                    "How does a fuse protect an appliance?": (
                        "If the current exceeds the fuse rating, the fuse wire melts, "
                        "breaking the circuit and cutting off the supply to the appliance."
                    ),
                    "Why is the fuse placed in the live wire, not the neutral?": (
                        "If the fuse blows, it breaks the high-voltage side of the circuit, "
                        "making the appliance and its casing safe to touch."
                    ),
                },
            },
            {
                "id": "P2L6",
                "title": "Electrical Power & Energy",
                "unit": "Topic 2",
                "subtitle": "P = IV, P = I²R, P = V²/R, E = QV",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/7",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Recall and apply P = IV and P = I²R",
                    "Apply E = Pt and E = QV",
                    "Select the correct power equation given available quantities",
                    "Explain why transmission lines use high voltage and low current",
                ],
                "key_vocab": [
                    "electrical power", "watt", "P = IV", "P = I²R", "E = Pt", "E = QV",
                    "energy transferred",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/7"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Electrical power: P = IV = I²R = V²/R. Energy transferred: E = Pt. "
                        "Also E = QV. P = I²R shows why transmission lines use high voltage and "
                        "low current — lower current means much less power lost as heat in cables."
                    ),
                    "equations": [
                        "P = IV  (power P in W; current I in A; pd V in volts) — recall and apply",
                        "P = I²R  (recall and apply)",
                        "P = V²/R  (given on sheet)",
                        "E = Pt  (energy E in J; power P in W; time t in s) — recall and apply",
                        "E = QV  (given on sheet)",
                    ],
                    "facts": [
                        "P = I²R: power lost in a resistor depends on current squared — halving current reduces power loss by 4.",
                        "National Grid uses high voltage to keep current low, minimising I²R losses in cables.",
                    ],
                    "spec_points": ["4.2.5", "4.2.6"],
                },
                "expected_answers": {
                    "A kettle draws 10 A from a 230 V supply. Calculate its power.": (
                        "P = IV = 10 × 230 = 2300 W"
                    ),
                    "A 60 W bulb runs for 2 hours. How much energy is used (in joules)?": (
                        "E = Pt = 60 × (2 × 3600) = 60 × 7200 = 432,000 J"
                    ),
                    "(HT) Why do transmission lines carry electricity at high voltage?": (
                        "Using high voltage means low current for the same power. Lower current "
                        "means much less power lost as heat in the cables (P = I²R)."
                    ),
                },
            },
            {
                "id": "P2L7",
                "title": "The National Grid",
                "unit": "Topic 2",
                "subtitle": "Step-up and step-down transformers, why high voltage is efficient",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/8",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Explain the purpose of the National Grid",
                    "Explain why step-up transformers are used for transmission",
                    "Explain why step-down transformers are used at the consumer end",
                    "State why transformers require ac and not dc",
                ],
                "key_vocab": [
                    "National Grid", "step-up transformer", "step-down transformer",
                    "transmission", "high voltage", "low current", "alternating current",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/8"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "The National Grid transmits electrical power across the UK. "
                        "Step-up transformers increase voltage (and reduce current) for transmission — "
                        "less power lost as P = I²R in cables. Step-down transformers reduce voltage "
                        "to safe levels for domestic use. Transformers only work with ac because they "
                        "require a changing current to produce a changing magnetic flux, which induces "
                        "a voltage in the secondary coil."
                    ),
                    "facts": [
                        "National Grid: network of cables and transformers transmitting electricity nationally.",
                        "Step-up transformer: increases voltage, decreases current.",
                        "Step-down transformer: decreases voltage, increases current.",
                        "High voltage in cables → low current → low P = I²R losses.",
                        "Transformers only work with ac — dc produces no changing flux, so no induction.",
                    ],
                    "spec_points": ["4.2.7"],
                },
                "expected_answers": {
                    "Why does the National Grid use high voltage for transmission?": (
                        "High voltage means lower current for the same power (P = IV). "
                        "Lower current means less power wasted as heat in the cables (P = I²R)."
                    ),
                    "Why do transformers require ac, not dc?": (
                        "AC is needed because transformers work by electromagnetic induction. "
                        "A changing (ac) current produces a changing magnetic flux, which induces "
                        "a voltage in the secondary coil. DC produces no changing flux."
                    ),
                },
            },
            {
                "id": "P2L8",
                "title": "Static Electricity",
                "unit": "Topic 2",
                "subtitle": "Charging by friction, electric fields, sparks — Physics only",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/9",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Explain how objects become charged by friction (electron transfer)",
                    "State that like charges repel and unlike charges attract",
                    "Describe an electric field and what field lines represent",
                    "Give a real-world risk from static electricity and how it is managed",
                ],
                "key_vocab": [
                    "static electricity", "electron transfer", "insulator", "electric field",
                    "field lines", "ionisation", "earthing",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgy9q6f/revision/9"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Rubbing two insulating materials transfers electrons from one to the other. "
                        "The object gaining electrons becomes negatively charged; the other positive. "
                        "Like charges repel; unlike charges attract. "
                        "An electric field is a region where a charged object experiences a force. "
                        "Field lines point from positive to negative; closer lines = stronger field. "
                        "When field is strong enough, it can ionise air causing sparks. "
                        "Risk: static spark igniting fuel vapour. Managed by earthing."
                    ),
                    "facts": [
                        "Friction transfers electrons — object gains electrons → negative; loses → positive.",
                        "Like charges repel; unlike attract.",
                        "Electric field: region where charged object experiences a force.",
                        "Field lines: direction of force on a positive test charge; positive → negative.",
                        "Sparks caused when strong field ionises air.",
                        "Earthing: provides a path for charge to flow away, preventing build-up.",
                        "Risk: static spark near fuel vapour during refuelling — controlled by earthing tanker.",
                    ],
                    "spec_points": ["4.2.8"],
                },
                "expected_answers": {
                    "A plastic rod is rubbed with a cloth and becomes negatively charged. Explain.": (
                        "Electrons are transferred from the cloth to the rod during rubbing. "
                        "The rod gains electrons, giving it a net negative charge."
                    ),
                    "What does an electric field line represent?": (
                        "The direction of the force that would act on a small positive test charge "
                        "placed at that point in the field."
                    ),
                    "Give a practical risk from static electricity and how it is controlled.": (
                        "Static spark igniting fuel vapour during aircraft or vehicle refuelling. "
                        "Controlled by earthing the tanker/aircraft to allow charge to flow away safely."
                    ),
                },
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # TOPIC 3 — PARTICLE MODEL OF MATTER  (Paper 1)
    # ══════════════════════════════════════════════════════════════════
    "Topic 3": {
        "title": "Particle Model of Matter",
        "color": "#27ae60",
        "level": "Foundation",
        "description": "Density, states of matter, changes of state, specific latent heat, and gas pressure.",
        "lessons": [
            {
                "id": "P3L1",
                "title": "Density & States of Matter",
                "unit": "Topic 3",
                "subtitle": "ρ = m/V, particle arrangements, RP5",
                "url": "https://www.bbc.co.uk/bitesize/guides/zssmn39/revision/1",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Recall and apply ρ = m/V",
                    "Describe particle arrangement in solids, liquids, and gases",
                    "Explain why gases have much lower density than solids",
                    "Describe the RP5 method for regular and irregular solids",
                ],
                "key_vocab": [
                    "density", "mass", "volume", "solid", "liquid", "gas",
                    "particle arrangement", "displacement", "Eureka can",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zssmn39/revision/1"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/particle-model"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Density ρ = m/V (kg/m³ or g/cm³). Solid: particles in fixed lattice, "
                        "closely packed — high density. Liquid: similar density to solid but "
                        "particles can flow. Gas: particles far apart with large empty spaces — "
                        "much lower density. RP5 (physics only): regular solid — measure dimensions "
                        "and calculate V; irregular solid — submerge in water and measure displaced "
                        "volume (Eureka can or measuring cylinder)."
                    ),
                    "equations": [
                        "ρ = m/V  (density in kg/m³; mass m in kg; volume V in m³) — recall and apply",
                    ],
                    "facts": [
                        "Solid: particles in fixed positions, vibrate, closely packed.",
                        "Liquid: particles close but can move past each other.",
                        "Gas: particles far apart, move quickly, large spaces between them.",
                        "Gas much less dense than solid: much more empty space between particles.",
                        "RP5 irregular: volume = volume of water displaced when object submerged.",
                    ],
                    "spec_points": ["4.3.1"],
                },
                "expected_answers": {
                    "Calculate the density of a 500 g object with volume 250 cm³.": (
                        "ρ = m/V = 500/250 = 2 g/cm³ (or 0.5 kg / 0.00025 m³ = 2000 kg/m³)"
                    ),
                    "Why is a gas much less dense than a solid of the same substance?": (
                        "In a gas, particles are much further apart with large empty spaces between "
                        "them, so there is far less mass in any given volume."
                    ),
                    "How do you find the volume of an irregularly shaped solid in RP5?": (
                        "Submerge the solid in water and measure the volume of water displaced — "
                        "this equals the volume of the solid."
                    ),
                },
            },
            {
                "id": "P3L2",
                "title": "Changes of State & Internal Energy",
                "unit": "Topic 3",
                "subtitle": "Latent heat, E = mL, why temperature is constant during state changes",
                "url": "https://www.bbc.co.uk/bitesize/guides/zssmn39/revision/2",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Define internal energy as the sum of KE and PE of particles",
                    "Explain why temperature stays constant during a change of state",
                    "Define specific latent heat and apply E = mL",
                    "Distinguish between specific heat capacity and specific latent heat",
                ],
                "key_vocab": [
                    "internal energy", "specific latent heat", "latent heat of fusion",
                    "latent heat of vaporisation", "melting", "boiling", "condensing", "freezing",
                ],
                "techniques": ["Active Recall", "Show Working", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zssmn39/revision/2"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Internal energy = total kinetic energy + total potential energy of all "
                        "particles. Heating increases internal energy. If temperature rises, KE "
                        "increases. If state changes at constant temperature, potential energy "
                        "increases (bonds being broken) — NOT kinetic energy. "
                        "Specific latent heat L: energy to change state of 1 kg without temperature "
                        "change. E = mL. Lf = fusion (melting/freezing); Lv = vaporisation."
                    ),
                    "equations": [
                        "E = mL  (energy E in J; mass m in kg; specific latent heat L in J/kg) — given on sheet",
                        "ΔE = mcΔθ  (also applies here for temperature-changing sections)",
                    ],
                    "facts": [
                        "Internal energy = sum of KE + PE of all particles.",
                        "Temperature constant during state change: energy goes to PE (breaking bonds).",
                        "SHC: energy per kg per °C for temperature change (no state change).",
                        "SLH: energy per kg for state change at constant temperature.",
                        "Lf (fusion): melting or freezing. Lv (vaporisation): boiling or condensing.",
                    ],
                    "spec_points": ["4.3.2"],
                },
                "expected_answers": {
                    "Why does temperature stay constant during melting even though energy is being added?": (
                        "Energy is used to break the bonds between particles (increasing potential "
                        "energy), not to increase their kinetic energy — so temperature does not rise."
                    ),
                    "Calculate the energy needed to melt 2 kg of ice (Lf = 334,000 J/kg).": (
                        "E = mL = 2 × 334,000 = 668,000 J"
                    ),
                    "What is the difference between specific heat capacity and specific latent heat?": (
                        "SHC: energy per kg per °C for a temperature change (no state change). "
                        "SLH: energy per kg for a change of state at constant temperature."
                    ),
                },
            },
            {
                "id": "P3L3",
                "title": "Pressure in Gases",
                "unit": "Topic 3",
                "subtitle": "Particle collisions, p ∝ T, pV = constant (HT) — Physics only",
                "url": "https://www.bbc.co.uk/bitesize/guides/zssmn39/revision/3",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Explain gas pressure in terms of particle collisions with container walls",
                    "Explain how increasing temperature at constant volume increases pressure",
                    "Convert between Celsius and Kelvin (K = °C + 273)",
                    "(HT) Apply the pressure–volume relationship p₁V₁ = p₂V₂",
                ],
                "key_vocab": [
                    "gas pressure", "particle collisions", "kelvin", "absolute zero",
                    "temperature-pressure relationship", "Boyle's Law",
                ],
                "techniques": ["Active Recall", "Show Working", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zssmn39/revision/3"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/particle-model"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Gas pressure arises from particles colliding with container walls, "
                        "exerting a force per unit area. More frequent or harder collisions → "
                        "greater pressure. Increasing temperature at constant volume: particles "
                        "move faster → more frequent and more forceful collisions → higher pressure. "
                        "At constant volume: p ∝ T (kelvin). Absolute zero: 0 K = −273°C — "
                        "particles have minimum internal energy. "
                        "HT: at constant temperature, p₁V₁ = p₂V₂ (Boyle's Law). "
                        "K = °C + 273."
                    ),
                    "equations": [
                        "p ∝ T (at constant volume; T in kelvin)",
                        "HT: p₁V₁ = p₂V₂ (at constant temperature — given on sheet for HT)",
                        "K = °C + 273",
                    ],
                    "facts": [
                        "Gas pressure = force per unit area from particle collisions with walls.",
                        "Faster particles (higher T) → harder, more frequent collisions → higher p.",
                        "At constant volume: pressure proportional to absolute temperature.",
                        "Absolute zero = 0 K = −273°C (minimum possible temperature).",
                        "HT: halving volume at constant temperature doubles pressure.",
                    ],
                    "spec_points": ["4.3.3"],
                },
                "expected_answers": {
                    "Explain why increasing temperature of a gas in a sealed container increases pressure.": (
                        "Higher temperature gives particles more kinetic energy so they move faster. "
                        "They collide with the container walls more frequently and with greater force, "
                        "increasing the pressure."
                    ),
                    "Convert 27°C to kelvin.": (
                        "K = 27 + 273 = 300 K"
                    ),
                    "(HT) A gas at 100 kPa occupies 2 m³. Volume is halved at constant temperature. Find new pressure.": (
                        "p₁V₁ = p₂V₂ → 100 × 2 = p₂ × 1 → p₂ = 200 kPa"
                    ),
                    "What is absolute zero?": (
                        "The lowest possible temperature: 0 K (−273°C), where particles have minimum internal energy."
                    ),
                },
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # TOPIC 4 — ATOMIC STRUCTURE  (Paper 1)
    # ══════════════════════════════════════════════════════════════════
    "Topic 4": {
        "title": "Atomic Structure",
        "color": "#8e44ad",
        "level": "Foundation",
        "description": "Atomic models, isotopes, radioactive decay, half-life, nuclear fission and fusion.",
        "lessons": [
            {
                "id": "P4L1",
                "title": "Structure of the Atom & Atomic Models",
                "unit": "Topic 4",
                "subtitle": "Protons, neutrons, electrons — Rutherford scattering and Bohr model",
                "url": "https://www.bbc.co.uk/bitesize/guides/zg4jtv4/revision/1",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "State the relative mass and charge of protons, neutrons, electrons",
                    "Define atomic number and mass number; calculate neutrons",
                    "Define isotopes",
                    "Describe how the nuclear model developed from plum pudding to Rutherford to Bohr",
                ],
                "key_vocab": [
                    "proton", "neutron", "electron", "nucleus", "atomic number", "mass number",
                    "isotope", "ion", "plum pudding model", "nuclear model", "Bohr model",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zg4jtv4/revision/1"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/atomic-structure"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Atom: nucleus (protons + neutrons) with electrons orbiting. Size ~10⁻¹⁰ m; "
                        "nucleus ~10⁻¹⁵ m. Proton: relative charge +1, mass 1. "
                        "Neutron: charge 0, mass 1. Electron: charge −1, mass ~1/2000. "
                        "Atomic number = number of protons. Mass number = protons + neutrons. "
                        "Neutrons = mass number − atomic number. "
                        "Isotopes: same element (same protons), different neutron numbers. "
                        "Thomson: plum pudding (electrons embedded in positive sphere). "
                        "Rutherford: gold foil — most α passed through, few deflected, tiny % bounced "
                        "back → dense positive nucleus. Old model disproved: plum pudding predicted "
                        "only small deflections. Bohr: electrons in fixed energy levels (shells)."
                    ),
                    "facts": [
                        "Proton: charge +1, relative mass 1.",
                        "Neutron: charge 0, relative mass 1.",
                        "Electron: charge −1, relative mass ~1/2000.",
                        "Atomic number = protons. Mass number = protons + neutrons.",
                        "Neutrons = mass number − atomic number.",
                        "Isotopes: same proton number, different neutron number.",
                        "Rutherford gold foil: most α through, few deflected at large angles, very few back.",
                        "Result proved: nucleus is tiny, dense, and positively charged.",
                        "Bohr added: electrons in fixed energy levels/orbits.",
                    ],
                    "spec_points": ["4.4.1.1", "4.4.1.2"],
                },
                "expected_answers": {
                    "State the relative mass and charge of a proton, neutron and electron.": (
                        "Proton: mass 1, charge +1. Neutron: mass 1, charge 0. "
                        "Electron: mass ~1/2000, charge −1."
                    ),
                    "Carbon-14 has atomic number 6 and mass number 14. How many neutrons?": (
                        "Neutrons = 14 − 6 = 8"
                    ),
                    "What are isotopes?": (
                        "Atoms of the same element with the same number of protons but different "
                        "numbers of neutrons."
                    ),
                    "Why did the gold foil experiment disprove the plum pudding model?": (
                        "The plum pudding model predicted only small deflections. The large-angle "
                        "deflections and back-scattering of some alpha particles showed that positive "
                        "charge and mass are concentrated in a tiny nucleus — which the plum pudding "
                        "model cannot explain."
                    ),
                },
            },
            {
                "id": "P4L2",
                "title": "Radioactive Decay — Alpha, Beta, Gamma",
                "unit": "Topic 4",
                "subtitle": "Properties, penetration, ionisation, nuclear equations",
                "url": "https://www.bbc.co.uk/bitesize/guides/zg4jtv4/revision/3",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Describe alpha, beta, and gamma radiation — composition and charge",
                    "Compare penetration and ionising ability of each type",
                    "Write and interpret nuclear equations for alpha and beta decay",
                    "Name sources of background radiation",
                ],
                "key_vocab": [
                    "alpha particle", "beta particle", "gamma ray", "ionisation", "penetration",
                    "nuclear equation", "background radiation", "decay",
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zg4jtv4/revision/3"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/atomic-structure"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Alpha (α): helium nucleus (2 protons, 2 neutrons), charge +2. "
                        "Stopped by paper or a few cm of air. Highly ionising. Most dangerous inside body. "
                        "Beta (β): fast electron, charge −1. Stopped by ~3 mm aluminium. Moderately ionising. "
                        "Beta decay: neutron → proton + electron; atomic number increases by 1, mass unchanged. "
                        "Gamma (γ): EM wave, no charge, no mass. Reduced by thick lead/concrete. Weakly ionising. "
                        "Nuclear equations conserve mass number and atomic number on both sides. "
                        "Alpha decay: mass number −4, atomic number −2. "
                        "Background radiation sources: radon gas, cosmic rays, food/drink, medical, nuclear industry."
                    ),
                    "facts": [
                        "Alpha: helium-4 nucleus, charge +2, stopped by paper, most ionising.",
                        "Beta: electron, charge −1, stopped by 3mm aluminium, moderately ionising.",
                        "Gamma: EM wave, no charge, reduced by thick lead/concrete, least ionising.",
                        "Alpha most dangerous inside body (high ionisation); least dangerous outside (can't penetrate skin).",
                        "Beta decay: atomic number +1, mass number unchanged.",
                        "Alpha decay: atomic number −2, mass number −4.",
                        "Background sources: radon, cosmic rays, medical X-rays, food, nuclear industry, building materials.",
                    ],
                    "spec_points": ["4.4.2.1", "4.4.2.2"],
                },
                "expected_answers": {
                    "Which type of nuclear radiation has the greatest ionising power?": (
                        "Alpha radiation."
                    ),
                    "A nucleus emits a beta particle. How does the atomic number change?": (
                        "Atomic number increases by 1 (a neutron decays into a proton and an electron)."
                    ),
                    "Why is alpha radiation most dangerous when the source is inside the body?": (
                        "Inside the body there is no skin to stop it — alpha's high ionising power "
                        "causes intense local damage to cells and DNA."
                    ),
                    "Name three sources of background radiation.": (
                        "Any three: radon gas (from rocks), cosmic rays, medical X-rays, food and drink, "
                        "nuclear industry, building materials."
                    ),
                },
            },
            {
                "id": "P4L3",
                "title": "Half-Life & Activity",
                "unit": "Topic 4",
                "subtitle": "Random and spontaneous decay, half-life calculations",
                "url": "https://www.bbc.co.uk/bitesize/guides/zg4jtv4/revision/4",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Define half-life clearly",
                    "Calculate remaining activity or count rate after multiple half-lives",
                    "Explain why decay is described as random and spontaneous",
                    "Use or interpret a decay graph to find half-life",
                ],
                "key_vocab": [
                    "half-life", "activity", "becquerel", "count rate",
                    "random", "spontaneous", "undecayed nuclei",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zg4jtv4/revision/4"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Activity: number of nuclear decays per second, measured in becquerels (Bq). "
                        "Half-life: time for the activity (or count rate, or number of undecayed nuclei) "
                        "to halve. Radioactive decay is random: cannot predict when any single nucleus "
                        "will decay. Spontaneous: not triggered by external conditions. "
                        "After n half-lives, activity = initial activity × (½)ⁿ."
                    ),
                    "equations": [
                        "After n half-lives: N = N₀ × (½)ⁿ",
                    ],
                    "facts": [
                        "Activity measured in becquerels (Bq) = decays per second.",
                        "Half-life: time for activity/count rate/number of nuclei to halve.",
                        "Random: cannot predict when individual nucleus decays.",
                        "Spontaneous: decay occurs without any external trigger.",
                        "External factors (temperature, pressure, chemical state) do NOT affect decay rate.",
                        "After 3 half-lives: 1/8 of original activity remains.",
                    ],
                    "spec_points": ["4.4.3"],
                },
                "expected_answers": {
                    "Define half-life.": (
                        "The time taken for the activity (or the number of undecayed nuclei) of a "
                        "radioactive source to fall to half its initial value."
                    ),
                    "A source has an initial activity of 800 Bq. After 3 half-lives, what is the activity?": (
                        "800 → 400 → 200 → 100 Bq"
                    ),
                    "Why is radioactive decay described as random and spontaneous?": (
                        "Random: you cannot predict when any individual nucleus will decay. "
                        "Spontaneous: it happens without any external trigger or influence."
                    ),
                },
            },
            {
                "id": "P4L4",
                "title": "Nuclear Fission, Fusion & Uses of Radiation",
                "unit": "Topic 4",
                "subtitle": "Fission chain reactions, fusion in stars, medical and industrial uses",
                "url": "https://www.bbc.co.uk/bitesize/guides/zg4jtv4/revision/5",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Describe nuclear fission and explain what a chain reaction is",
                    "Explain nuclear fusion and why it requires very high temperature",
                    "Give uses of radiation in medicine and industry",
                    "Explain how a smoke detector uses alpha radiation",
                ],
                "key_vocab": [
                    "nuclear fission", "chain reaction", "nuclear fusion", "neutron",
                    "radioactive tracer", "radiotherapy", "smoke detector",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zg4jtv4/revision/5"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Fission: a heavy nucleus (e.g. U-235) absorbs a neutron, becomes unstable, "
                        "splits into two smaller nuclei + 2–3 neutrons + energy released. "
                        "Chain reaction: released neutrons trigger further fissions. Nuclear reactor "
                        "uses a controlled chain reaction. "
                        "Fusion: two light nuclei combine to form a larger nucleus + energy. "
                        "Requires extremely high temperature (~10⁷ K) to overcome electrostatic repulsion. "
                        "Powers stars. "
                        "Uses: medical imaging (gamma tracers), radiotherapy (gamma to kill cancer cells), "
                        "industrial thickness gauging (beta), smoke detectors (Am-241, alpha ionises air "
                        "between plates; smoke interrupts current → alarm)."
                    ),
                    "facts": [
                        "Fission: heavy nucleus + neutron → 2 smaller nuclei + 2–3 neutrons + energy.",
                        "Chain reaction: each fission releases neutrons that trigger more fissions.",
                        "Fusion: two light nuclei → one heavier nucleus + energy.",
                        "Fusion requires ~10⁷ K — electrostatic repulsion between positive nuclei is enormous.",
                        "Fusion powers stars (hydrogen → helium on main sequence).",
                        "Smoke detector: Am-241 (alpha source) ionises air; current flows; smoke absorbs alpha → current drops → alarm.",
                        "Medical tracer: gamma-emitting isotope injected; detected externally.",
                    ],
                    "spec_points": ["4.4.4.1", "4.4.4.2"],
                },
                "expected_answers": {
                    "What is the difference between fission and fusion?": (
                        "Fission: a heavy nucleus is split into smaller nuclei. "
                        "Fusion: two light nuclei join to form a heavier one. Both release energy."
                    ),
                    "Why is nuclear fusion so difficult to achieve on Earth?": (
                        "It requires temperatures of around 10 million kelvin to give nuclei enough "
                        "kinetic energy to overcome the electrostatic repulsion between their positive charges."
                    ),
                    "How does a smoke detector use alpha radiation?": (
                        "Americium-241 emits alpha particles that ionise air between two electrodes, "
                        "creating a small current. Smoke particles absorb the alpha radiation, "
                        "reducing ionisation and the current — this triggers the alarm."
                    ),
                },
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # TOPIC 5 — FORCES  (Paper 2)
    # ══════════════════════════════════════════════════════════════════
    "Topic 5": {
        "title": "Forces",
        "color": "#3498db",
        "level": "Intermediate",
        "description": "Scalars, vectors, Newton's laws, motion, momentum, and pressure.",
        "lessons": [
            {
                "id": "P5L1",
                "title": "Scalars, Vectors & Free Body Diagrams",
                "unit": "Topic 5",
                "subtitle": "Contact vs non-contact forces, resultant force, FBDs",
                "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/1",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Distinguish scalars from vectors with examples",
                    "Classify forces as contact or non-contact",
                    "Draw accurate free body diagrams",
                    "Calculate or estimate a resultant force",
                ],
                "key_vocab": [
                    "scalar", "vector", "resultant force", "free body diagram",
                    "contact force", "non-contact force", "tension", "normal force",
                    "friction", "weight", "upthrust",
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/1"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Scalar: magnitude only (distance, speed, mass, time, temperature). "
                        "Vector: magnitude and direction (displacement, velocity, acceleration, force, momentum). "
                        "Contact forces: friction, normal/reaction, tension, upthrust, air resistance. "
                        "Non-contact forces: gravity, electrostatic, magnetic. "
                        "Free body diagram: shows all forces on ONE object as arrows (size ∝ magnitude). "
                        "Resultant force: single force that has the same effect as all forces combined. "
                        "HT: add perpendicular vectors using Pythagoras."
                    ),
                    "facts": [
                        "Scalars: distance, speed, mass, time, temperature, energy.",
                        "Vectors: displacement, velocity, acceleration, force, momentum.",
                        "Contact: friction, air resistance, tension, normal force, upthrust.",
                        "Non-contact: gravity, electrostatic, magnetic.",
                        "FBD: one object, all forces shown as arrows from centre, size to scale.",
                        "Resultant force = vector sum of all forces acting.",
                        "HT: resultant of two perpendicular forces = √(F₁² + F₂²).",
                    ],
                    "spec_points": ["4.5.1.1", "4.5.1.2"],
                },
                "expected_answers": {
                    "Give two examples of scalars and two of vectors.": (
                        "Scalars: speed, mass (any valid). Vectors: velocity, force (any valid)."
                    ),
                    "Is gravity a contact or non-contact force?": (
                        "Non-contact — it acts between masses without them needing to touch."
                    ),
                    "(HT) Two forces act on an object: 5 N east and 12 N north. Find the resultant.": (
                        "Resultant = √(5² + 12²) = √(25 + 144) = √169 = 13 N"
                    ),
                },
            },
            {
                "id": "P5L2",
                "title": "Weight, Gravity & Hooke's Law",
                "unit": "Topic 5",
                "subtitle": "W = mg, F = ke, limit of proportionality, RP6",
                "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/2",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Distinguish mass from weight; apply W = mg",
                    "Recall and apply F = ke (Hooke's Law)",
                    "Explain the limit of proportionality",
                    "Describe RP6 and how to find spring constant from a graph",
                ],
                "key_vocab": [
                    "weight", "mass", "gravitational field strength", "spring constant",
                    "extension", "Hooke's Law", "limit of proportionality", "elastic",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/2"},
                    {"name": "GCSE Physics Online — Required Practicals", "url": "https://www.gcsephysicsonline.com/required-practicals"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Weight W = mg (W in N; mass m in kg; g in N/kg). On Earth g = 9.8 N/kg (given). "
                        "Weight acts at the centre of mass. "
                        "Hooke's Law: F = ke — force proportional to extension up to the limit of "
                        "proportionality. Spring constant k in N/m; extension e in m. "
                        "RP6: add weights to spring, measure extension. Plot F vs extension — "
                        "gradient = spring constant k. Identify limit of proportionality as point "
                        "where graph deviates from straight line."
                    ),
                    "equations": [
                        "W = mg  (weight W in N; mass m in kg; g in N/kg) — recall and apply",
                        "F = ke  (force F in N; spring constant k in N/m; extension e in m) — recall and apply",
                    ],
                    "facts": [
                        "Mass: amount of matter in kg; constant everywhere.",
                        "Weight: gravitational force in N; varies with g.",
                        "g on Earth ≈ 9.8 N/kg; on Moon ≈ 1.6 N/kg.",
                        "Hooke's Law only valid up to the limit of proportionality.",
                        "RP6: gradient of F–extension graph = spring constant k.",
                    ],
                    "spec_points": ["4.5.1.3", "4.5.1.6"],
                },
                "expected_answers": {
                    "A 70 kg person stands on the Moon (g = 1.6 N/kg). Find their weight.": (
                        "W = mg = 70 × 1.6 = 112 N"
                    ),
                    "A spring with k = 40 N/m is stretched 0.1 m. What is the restoring force?": (
                        "F = ke = 40 × 0.1 = 4 N"
                    ),
                    "What is the limit of proportionality?": (
                        "The point beyond which the extension is no longer proportional to the force "
                        "— Hooke's Law no longer applies and the spring is permanently deformed."
                    ),
                },
            },
            {
                "id": "P5L3",
                "title": "Moments, Levers & Pressure in Fluids",
                "unit": "Topic 5",
                "subtitle": "M = Fd, principle of moments, p = F/A, p = hρg — Physics only",
                "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/3",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Define and calculate the moment of a force",
                    "State and apply the principle of moments",
                    "Apply p = F/A and p = hρg",
                    "Explain why atmospheric pressure decreases with altitude",
                ],
                "key_vocab": [
                    "moment", "pivot", "principle of moments", "equilibrium", "lever",
                    "pressure", "pascal", "upthrust", "Archimedes", "atmospheric pressure",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/3"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Moment M = Fd (M in Nm; F in N; d = perpendicular distance from pivot in m). "
                        "Principle of moments: for equilibrium, sum of clockwise moments = "
                        "sum of anticlockwise moments about any point. "
                        "Pressure p = F/A (Pa; N; m²). "
                        "Fluid pressure at depth h: p = hρg (Pa; depth m; density ρ in kg/m³; g in N/kg). "
                        "Upthrust = weight of fluid displaced. "
                        "Atmospheric pressure decreases with altitude — less air above means less weight "
                        "of air column pressing down."
                    ),
                    "equations": [
                        "M = Fd  (moment M in Nm; force F in N; distance d in m) — recall and apply",
                        "p = F/A  (pressure in Pa; force in N; area in m²) — recall and apply",
                        "p = hρg  (given on sheet; depth h in m; density ρ in kg/m³)",
                    ],
                    "facts": [
                        "Moment = force × perpendicular distance from pivot.",
                        "Equilibrium: clockwise moments = anticlockwise moments.",
                        "Pressure in a fluid increases with depth.",
                        "p = hρg: deeper → higher pressure.",
                        "Upthrust = weight of displaced fluid (Archimedes' principle).",
                        "Atmospheric pressure decreases with altitude — fewer air molecules above.",
                    ],
                    "spec_points": ["4.5.3", "4.5.5.4"],
                },
                "expected_answers": {
                    "A 40 N force acts 2 m from a pivot. What is the moment?": (
                        "M = Fd = 40 × 2 = 80 Nm"
                    ),
                    "State the principle of moments.": (
                        "For a system in equilibrium, the sum of the clockwise moments about any "
                        "point equals the sum of the anticlockwise moments about that same point."
                    ),
                    "Calculate the pressure at depth 5 m in water (ρ = 1000 kg/m³, g = 10 N/kg).": (
                        "p = hρg = 5 × 1000 × 10 = 50,000 Pa"
                    ),
                    "Why does atmospheric pressure decrease with altitude?": (
                        "At higher altitude there is less air above, so the weight of the air "
                        "column pressing down is smaller, giving lower pressure."
                    ),
                },
            },
            {
                "id": "P5L4",
                "title": "Distance, Speed, Velocity & Acceleration",
                "unit": "Topic 5",
                "subtitle": "Motion equations, distance–time and velocity–time graphs",
                "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/4",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Distinguish distance/speed (scalar) from displacement/velocity (vector)",
                    "Apply v = s/t and a = Δv/Δt",
                    "Interpret gradients and areas on distance–time and velocity–time graphs",
                    "Apply v² = u² + 2as and s = ut + ½at² (HT)",
                ],
                "key_vocab": [
                    "distance", "displacement", "speed", "velocity", "acceleration",
                    "gradient", "area under graph", "uniform acceleration",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/4"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/forces"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Distance: scalar (total path length). Displacement: vector (straight-line start to end). "
                        "Speed v = s/t. Velocity: displacement/time (vector). "
                        "Acceleration a = Δv/Δt. "
                        "d–t graph: gradient = speed. Curved line = changing speed. "
                        "v–t graph: gradient = acceleration; area under graph = displacement. "
                        "Equations (all HT except v = u + at): "
                        "v = u + at; s = ut + ½at²; v² = u² + 2as. "
                        "Typical speeds: walking ~1.5 m/s, cycling ~6, car ~30, sound ~340 m/s."
                    ),
                    "equations": [
                        "v = s/t  (recall and apply)",
                        "a = Δv/Δt  (recall and apply)",
                        "v = u + at  (given on sheet)",
                        "HT: s = ut + ½at²  (given on sheet)",
                        "HT: v² = u² + 2as  (given on sheet)",
                    ],
                    "facts": [
                        "d–t graph gradient = speed.",
                        "v–t graph gradient = acceleration.",
                        "Area under v–t graph = displacement.",
                        "Horizontal line on d–t graph = stationary.",
                        "Horizontal line on v–t graph = constant velocity (no acceleration).",
                    ],
                    "spec_points": ["4.5.6.1", "4.5.6.2"],
                },
                "expected_answers": {
                    "A car travels 150 m in 10 s. What is its average speed?": (
                        "v = s/t = 150 / 10 = 15 m/s"
                    ),
                    "What does the gradient of a velocity–time graph represent?": (
                        "Acceleration."
                    ),
                    "What does the area under a velocity–time graph represent?": (
                        "Displacement (distance if only in one direction)."
                    ),
                    "(HT) Using v² = u² + 2as, find v for an object starting from rest, a = 3 m/s², s = 8 m.": (
                        "v² = 0 + 2 × 3 × 8 = 48 → v = √48 ≈ 6.9 m/s"
                    ),
                },
            },
            {
                "id": "P5L5",
                "title": "Newton's Laws of Motion",
                "unit": "Topic 5",
                "subtitle": "N1, N2 (F = ma), N3, inertia",
                "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/5",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "State Newton's three laws clearly",
                    "Apply F = ma to calculate force, mass, or acceleration",
                    "Identify Newton's Third Law pairs in real situations",
                    "Explain inertia and its link to mass",
                ],
                "key_vocab": [
                    "Newton's First Law", "Newton's Second Law", "Newton's Third Law",
                    "inertia", "resultant force", "F = ma", "action-reaction pair",
                ],
                "techniques": ["Active Recall", "Show Working", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/5"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "N1: An object remains at rest or constant velocity unless acted on by a "
                        "resultant force. Tendency to remain in current state = inertia (related to mass). "
                        "N2: F = ma (resultant force F in N; mass m in kg; acceleration a in m/s²). "
                        "HT: F = Δ(mv)/Δt (rate of change of momentum). "
                        "N3: Every action force has an equal and opposite reaction force acting on a "
                        "different object (force pairs are always on different objects, same type of force)."
                    ),
                    "equations": [
                        "F = ma  (resultant force F in N; mass m in kg; a in m/s²) — recall and apply",
                        "HT: F = Δ(mv)/Δt  (given on sheet)",
                    ],
                    "facts": [
                        "N1: zero resultant force → constant velocity (or rest).",
                        "N2: resultant force = mass × acceleration.",
                        "N3: action and reaction are equal and opposite; act on different objects.",
                        "Inertia: tendency to resist change in motion; greater mass = greater inertia.",
                    ],
                    "spec_points": ["4.5.6.3", "4.5.6.4"],
                },
                "expected_answers": {
                    "State Newton's First Law.": (
                        "An object will remain at rest or continue at constant velocity unless "
                        "acted upon by a resultant (unbalanced) force."
                    ),
                    "A 1000 kg car has a resultant force of 3000 N. Find its acceleration.": (
                        "a = F/m = 3000 / 1000 = 3 m/s²"
                    ),
                    "A rocket expels gas downwards. Using N3, explain how it accelerates upwards.": (
                        "The rocket exerts a downward force on the gas (action). By N3, the gas "
                        "exerts an equal and opposite upward force on the rocket (reaction), "
                        "accelerating it upwards."
                    ),
                },
            },
            {
                "id": "P5L6",
                "title": "Stopping Distances & Momentum",
                "unit": "Topic 5",
                "subtitle": "Thinking/braking distance, p = mv, conservation of momentum",
                "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/6",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Explain factors affecting thinking distance and braking distance",
                    "Recall and apply p = mv",
                    "Apply conservation of momentum to collisions",
                    "(HT) Explain how crumple zones reduce force using F = Δ(mv)/Δt",
                ],
                "key_vocab": [
                    "stopping distance", "thinking distance", "braking distance",
                    "momentum", "conservation of momentum", "impulse",
                    "crumple zone", "airbag",
                ],
                "techniques": ["Active Recall", "Show Working", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z3g7hyc/revision/6"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Stopping distance = thinking distance + braking distance. "
                        "Thinking distance affected by: speed, reaction time (tiredness, drugs, alcohol, distractions). "
                        "Braking distance affected by: speed, road condition (wet/icy), tyre condition, brake condition. "
                        "Large braking force → dangerous (skid/tyre damage/loss of control). "
                        "Momentum p = mv (kg m/s). "
                        "Conservation: total momentum before = total momentum after in a closed system. "
                        "HT: force = rate of change of momentum = Δ(mv)/Δt. "
                        "Crumple zones/airbags extend collision time → same Δ(mv) → smaller F."
                    ),
                    "equations": [
                        "p = mv  (momentum p in kg m/s; mass m in kg; velocity v in m/s) — recall and apply",
                        "HT: F = Δ(mv)/Δt  (given on sheet)",
                    ],
                    "facts": [
                        "Stopping distance = thinking distance + braking distance.",
                        "Thinking distance increases with speed and impaired reaction time.",
                        "Braking distance increases with speed, wet roads, worn tyres/brakes.",
                        "Momentum is conserved in all collisions in a closed system.",
                        "HT: crumple zones increase collision time → smaller force for same change in momentum.",
                    ],
                    "spec_points": ["4.5.6.5", "4.5.7"],
                },
                "expected_answers": {
                    "Give two factors that increase braking distance.": (
                        "Any two: higher speed, wet or icy road surface, worn tyres, faulty brakes."
                    ),
                    "Calculate the momentum of a 1200 kg car travelling at 15 m/s.": (
                        "p = mv = 1200 × 15 = 18,000 kg m/s"
                    ),
                    "(HT) How do crumple zones reduce injury force in a crash?": (
                        "Crumple zones extend the time over which the change in momentum occurs. "
                        "By F = Δ(mv)/Δt, a longer time for the same change in momentum means "
                        "a smaller force on the occupants."
                    ),
                },
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # TOPIC 6 — WAVES  (Paper 2)
    # ══════════════════════════════════════════════════════════════════
    "Topic 6": {
        "title": "Waves",
        "color": "#16a085",
        "level": "Intermediate",
        "description": "Wave properties, EM spectrum, sound, light, lenses, and black body radiation.",
        "lessons": [
            {
                "id": "P6L1",
                "title": "Wave Properties & Types",
                "unit": "Topic 6",
                "subtitle": "v = fλ, transverse vs longitudinal, amplitude, frequency, period",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/1",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Define amplitude, frequency, wavelength, wave speed, period",
                    "Distinguish transverse from longitudinal waves with examples",
                    "Recall and apply v = fλ and T = 1/f",
                    "Describe how waves transfer energy without net transfer of matter",
                ],
                "key_vocab": [
                    "amplitude", "frequency", "wavelength", "wave speed", "period",
                    "transverse", "longitudinal", "compression", "rarefaction",
                ],
                "techniques": ["Active Recall", "Show Working"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/1"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/waves"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Waves transfer energy without net transfer of matter. "
                        "Transverse: oscillation perpendicular to direction of travel (all EM waves, water waves). "
                        "Longitudinal: oscillation parallel to direction of travel (sound, P-seismic). "
                        "Amplitude: maximum displacement from equilibrium. "
                        "Frequency f: number of complete waves per second (Hz). "
                        "Wavelength λ: distance between two identical points. "
                        "Period T = 1/f (s). Wave speed v = fλ."
                    ),
                    "equations": [
                        "v = fλ  (speed v in m/s; frequency f in Hz; wavelength λ in m) — recall and apply",
                        "T = 1/f  (period T in s; frequency f in Hz) — recall and apply",
                    ],
                    "facts": [
                        "Transverse: oscillation ⊥ to direction of travel. Examples: all EM, water.",
                        "Longitudinal: oscillation ∥ to direction of travel. Examples: sound.",
                        "Waves transfer energy not matter.",
                        "Longitudinal waves have compressions (high pressure) and rarefactions (low pressure).",
                    ],
                    "spec_points": ["4.6.1.1"],
                },
                "expected_answers": {
                    "What is the difference between transverse and longitudinal waves?": (
                        "Transverse: oscillations are perpendicular to the direction of wave travel (e.g. light). "
                        "Longitudinal: oscillations are parallel to the direction of wave travel (e.g. sound)."
                    ),
                    "A wave has frequency 200 Hz and wavelength 1.5 m. Find the wave speed.": (
                        "v = fλ = 200 × 1.5 = 300 m/s"
                    ),
                    "What is the period of a wave with frequency 50 Hz?": (
                        "T = 1/f = 1/50 = 0.02 s"
                    ),
                },
            },
            {
                "id": "P6L2",
                "title": "Reflection, Refraction & EM Spectrum",
                "unit": "Topic 6",
                "subtitle": "Angle of incidence/reflection, bending at boundaries, all 7 EM types",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/2",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Apply the law of reflection",
                    "Explain refraction in terms of wave speed change at a boundary",
                    "List all 7 EM waves in order of frequency and wavelength",
                    "State that all EM waves travel at 3 × 10⁸ m/s in a vacuum",
                ],
                "key_vocab": [
                    "reflection", "refraction", "normal", "angle of incidence",
                    "angle of refraction", "electromagnetic spectrum", "speed of light",
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/2"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Reflection: angle of incidence = angle of reflection (both measured from normal). "
                        "Refraction: wave changes speed at a boundary → changes direction (unless normal incidence). "
                        "Slows down when entering denser medium → bends towards normal. "
                        "EM spectrum (lowest to highest frequency): radio, microwave, infrared, visible, "
                        "UV, X-ray, gamma. All EM waves travel at c = 3 × 10⁸ m/s in vacuum. "
                        "Higher frequency → shorter wavelength → more energy per photon."
                    ),
                    "facts": [
                        "Law of reflection: angle of incidence = angle of reflection.",
                        "Refraction: change in speed at boundary → change in direction.",
                        "Wave slows entering denser medium → bends TOWARDS normal.",
                        "EM spectrum (low f → high f): radio, microwave, IR, visible, UV, X-ray, gamma.",
                        "All EM waves: c = 3 × 10⁸ m/s in vacuum.",
                        "Higher frequency = more energy per photon.",
                    ],
                    "spec_points": ["4.6.1.2", "4.6.2.1"],
                },
                "expected_answers": {
                    "Order the EM spectrum from lowest to highest frequency.": (
                        "Radio, microwave, infrared, visible light, ultraviolet, X-rays, gamma rays."
                    ),
                    "A ray of light passes from air into glass. Does it bend towards or away from the normal?": (
                        "Towards the normal — it slows down on entering the denser glass."
                    ),
                    "What is the speed of all EM waves in a vacuum?": (
                        "3 × 10⁸ m/s"
                    ),
                },
            },
            {
                "id": "P6L3",
                "title": "Uses & Hazards of EM Radiation",
                "unit": "Topic 6",
                "subtitle": "Applications of all 7 EM types, health risks",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/3",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "State uses for each of the 7 EM wave types",
                    "State hazards for the more energetic types (UV, X-ray, gamma)",
                    "Explain why UV causes sunburn but visible light does not",
                    "Explain why X-rays can image bone but not soft tissue",
                ],
                "key_vocab": [
                    "radio", "microwave", "infrared", "ultraviolet", "X-ray", "gamma ray",
                    "ionising radiation", "cancer", "sterilisation",
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/3"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Radio: broadcasting, communications. "
                        "Microwave: satellite TV, mobile phones, cooking. "
                        "Infrared: thermal imaging, remote controls, optical fibres, grills. "
                        "Visible: photography, human vision. "
                        "UV: security marking, sterilisation, fluorescent lamps. Hazard: skin cancer, eye damage. "
                        "X-rays: medical imaging (absorbed by bone/dense tissue), airport security. Hazard: cell/DNA damage. "
                        "Gamma: cancer treatment, medical tracers, sterilising equipment. Hazard: cell/DNA damage, cancer. "
                        "Higher frequency → more energy → more hazardous (ionising)."
                    ),
                    "facts": [
                        "UV causes sunburn — higher energy than visible; damages DNA in skin cells.",
                        "X-rays: not absorbed by soft tissue but absorbed by bone → medical imaging.",
                        "Gamma and X-rays: ionising — damage DNA, cause cancer.",
                        "Gamma: sterilises equipment; cancer radiotherapy kills cancer cells.",
                        "Infrared: all warm objects emit; detected by thermal cameras.",
                    ],
                    "spec_points": ["4.6.2.2"],
                },
                "expected_answers": {
                    "Give one use and one hazard of ultraviolet radiation.": (
                        "Use: sterilising water/surfaces. Hazard: causes skin cancer and eye damage."
                    ),
                    "Why are X-rays used for medical imaging rather than visible light?": (
                        "X-rays pass through soft tissue but are absorbed by denser material like bone, "
                        "creating an image of internal bone structure. Visible light cannot penetrate the body."
                    ),
                    "Why does UV cause sunburn but visible light does not?": (
                        "UV has higher frequency and therefore more energy per photon than visible light. "
                        "It can damage DNA in skin cells, causing sunburn and potentially cancer."
                    ),
                },
            },
            {
                "id": "P6L4",
                "title": "Sound & Ultrasound",
                "unit": "Topic 6",
                "subtitle": "Longitudinal mechanical waves, ultrasound applications, RP8",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/4",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Explain why sound cannot travel through a vacuum",
                    "State the human hearing frequency range (~20 Hz to 20 kHz)",
                    "Explain how ultrasound is used in medicine and industry",
                    "Describe RP8 method to measure speed of sound",
                ],
                "key_vocab": [
                    "sound wave", "longitudinal", "mechanical wave", "medium",
                    "ultrasound", "sonar", "echo", "frequency range",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/4"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Sound is a longitudinal, mechanical wave — it requires a medium (particles to vibrate). "
                        "Cannot travel through a vacuum. Human hearing: ~20 Hz to 20 kHz. "
                        "Ultrasound: frequency > 20 kHz. Uses: foetal scanning (safe, no ionising radiation), "
                        "industrial flaw detection (ultrasound reflects at cracks). "
                        "RP8: two microphones a known distance apart connected to a data logger; "
                        "create a sharp sound; measure time between signals; v = distance / time."
                    ),
                    "facts": [
                        "Sound: longitudinal, mechanical — needs particles to travel.",
                        "Cannot travel in a vacuum (space is silent).",
                        "Human hearing range: ~20 Hz to 20,000 Hz.",
                        "Ultrasound: > 20 kHz.",
                        "Medical ultrasound: non-ionising, safe for foetal imaging.",
                        "Industrial: ultrasound reflects at flaws/cracks, locating them by echo timing.",
                        "RP8: v = distance between mics / time difference of signal arrival.",
                    ],
                    "spec_points": ["4.6.1.3"],
                },
                "expected_answers": {
                    "Why can't sound travel through space?": (
                        "Sound is a mechanical wave — it requires particles to vibrate. Space is "
                        "(near) vacuum with no particles, so sound cannot propagate."
                    ),
                    "How is ultrasound used to detect flaws in metal castings?": (
                        "Ultrasound pulses are sent through the metal. Flaws reflect pulses back "
                        "before the far surface does — the time and position of the reflected signal "
                        "reveal the flaw's location and depth."
                    ),
                    "Describe the RP8 method to measure speed of sound.": (
                        "Place two microphones a measured distance apart connected to a data logger. "
                        "Create a sharp sound. Record the time delay between signals at each mic. "
                        "v = distance / time."
                    ),
                },
            },
            {
                "id": "P6L5",
                "title": "Seismic Waves & Lenses",
                "unit": "Topic 6",
                "subtitle": "P-waves/S-waves, Earth's structure, converging/diverging lenses — Physics only",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/5",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Distinguish P-waves and S-waves; state what each can travel through",
                    "Explain what studying seismic waves tells us about Earth's interior",
                    "Describe how converging and diverging lenses form images",
                    "Define magnification and apply it",
                ],
                "key_vocab": [
                    "P-wave", "S-wave", "seismic wave", "outer core", "inner core",
                    "converging lens", "diverging lens", "principal focus", "real image",
                    "virtual image", "magnification",
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/5"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "P-waves (primary): longitudinal, travel through solids AND liquids. "
                        "S-waves (secondary): transverse, travel through solids ONLY (not liquids). "
                        "S-waves do not pass through Earth's outer core → outer core is liquid. "
                        "P-waves refract at boundaries → shadow zones. "
                        "Converging (convex) lens: focuses parallel rays to principal focus. Object beyond F → real, inverted image. "
                        "Diverging (concave) lens: always produces virtual, upright, diminished image. "
                        "Magnification = image height / object height = image distance / object distance."
                    ),
                    "facts": [
                        "P-waves: longitudinal, through solid and liquid.",
                        "S-waves: transverse, through solid only.",
                        "S-waves absent in earthquake shadow zones → outer core is liquid.",
                        "P-waves refract at core boundary → change speed and direction.",
                        "Converging lens: object beyond F → real, inverted image on far side.",
                        "Diverging lens: always virtual, upright, smaller image.",
                        "Magnification = image height / object height (no units).",
                    ],
                    "spec_points": ["4.6.1.5", "4.6.3.1"],
                },
                "expected_answers": {
                    "What does the absence of S-waves in certain parts of the Earth tell us?": (
                        "S-waves cannot travel through liquids. Their absence in the outer core "
                        "shadow zone tells us the outer core is liquid."
                    ),
                    "What type of image does a converging lens form when the object is beyond the focal point?": (
                        "A real, inverted image on the far side of the lens (can be projected on a screen)."
                    ),
                    "An image is 6 cm tall and the object is 2 cm tall. What is the magnification?": (
                        "Magnification = 6/2 = 3"
                    ),
                },
            },
            {
                "id": "P6L6",
                "title": "Black Body Radiation & the Greenhouse Effect",
                "unit": "Topic 6",
                "subtitle": "Emission and absorption, temperature equilibrium, climate — Physics only",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/6",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Define a perfect black body absorber/emitter",
                    "Explain how peak frequency changes with temperature",
                    "Explain the Earth's temperature in terms of absorbed and emitted radiation",
                    "Describe the greenhouse effect",
                ],
                "key_vocab": [
                    "black body", "radiation intensity", "peak frequency", "greenhouse effect",
                    "greenhouse gas", "infrared", "climate change",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgf96g8/revision/6"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "All objects emit and absorb radiation. A perfect black body absorbs all "
                        "incident radiation and is the best possible emitter at any temperature. "
                        "Hotter objects: emit more radiation; peak shifts to higher frequency/shorter wavelength. "
                        "Sun's peak: visible range. Earth's peak: infrared. "
                        "Earth's temperature set by balance between solar radiation absorbed and IR emitted. "
                        "Greenhouse effect: solar radiation (mainly visible) absorbed by Earth; "
                        "Earth re-emits IR; greenhouse gases (CO2, water vapour) absorb and re-emit IR "
                        "back towards Earth → warming. Increasing greenhouse gases → enhanced greenhouse effect."
                    ),
                    "facts": [
                        "Perfect black body: absorbs 100% of incident radiation; best possible emitter.",
                        "Higher temperature → more radiation emitted at higher frequencies.",
                        "Earth's equilibrium temperature: absorbed solar = emitted IR.",
                        "Greenhouse gases absorb IR emitted by Earth and re-emit in all directions including downward.",
                        "More CO2 → enhanced greenhouse effect → global warming.",
                    ],
                    "spec_points": ["4.6.2.3"],
                },
                "expected_answers": {
                    "What is a perfect black body?": (
                        "An ideal object that absorbs all incident radiation and is the best possible "
                        "emitter of radiation at any given temperature."
                    ),
                    "How does the peak frequency of radiation emitted change as temperature increases?": (
                        "The peak frequency increases (shifts to shorter wavelengths/higher frequencies)."
                    ),
                    "Explain the greenhouse effect in terms of radiation.": (
                        "Solar radiation (mainly visible/UV) passes through the atmosphere and is "
                        "absorbed by Earth. Earth re-emits infrared radiation. Greenhouse gases absorb "
                        "this IR and re-emit it in all directions, including back towards Earth, "
                        "warming the surface further."
                    ),
                },
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # TOPIC 7 — MAGNETISM & ELECTROMAGNETISM  (Paper 2)
    # ══════════════════════════════════════════════════════════════════
    "Topic 7": {
        "title": "Magnetism & Electromagnetism",
        "color": "#e67e22",
        "level": "Intermediate",
        "description": "Magnetic fields, motor effect, electromagnetic induction, and transformers.",
        "lessons": [
            {
                "id": "P7L1",
                "title": "Permanent Magnets & Magnetic Fields",
                "unit": "Topic 7",
                "subtitle": "Field lines, poles, induced magnetism",
                "url": "https://www.bbc.co.uk/bitesize/guides/zb4nmfr/revision/1",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Describe the magnetic field pattern for a bar magnet",
                    "Explain what magnetic field lines represent",
                    "Distinguish permanent from induced magnets",
                    "Explain why an induced magnet is always attracted, never repelled",
                ],
                "key_vocab": [
                    "magnetic field", "field lines", "north pole", "south pole",
                    "permanent magnet", "induced magnet", "compass",
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zb4nmfr/revision/1"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/magnetism"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Like poles repel; unlike poles attract. "
                        "Permanent magnet: retains magnetism without an external field. "
                        "Induced magnet: becomes magnetised only in presence of external field; "
                        "always attracted to the inducing pole — never repelled. "
                        "Magnetic field: region where a magnetic material or current experiences a force. "
                        "Field lines: drawn from N to S outside the magnet; closer lines = stronger field; "
                        "arrows show direction of force on a free N pole. "
                        "Earth has a magnetic field (molten iron in outer core) — compass aligns with it."
                    ),
                    "facts": [
                        "Like poles repel; unlike attract.",
                        "Permanent magnet: retains magnetism indefinitely.",
                        "Induced magnet: magnetised by an external field; demagnetises when removed.",
                        "Induced magnet: always attracted, never repelled.",
                        "Field lines: N to S outside magnet; arrows show direction.",
                        "Closer field lines = stronger field.",
                    ],
                    "spec_points": ["4.7.1.1"],
                },
                "expected_answers": {
                    "What is the difference between a permanent magnet and an induced magnet?": (
                        "A permanent magnet retains its magnetism without any external field. "
                        "An induced magnet is only magnetic when placed in an external field, "
                        "and loses its magnetism when the field is removed."
                    ),
                    "Is an induced magnet ever repelled?": (
                        "No — an induced magnet is always attracted to the magnet causing the "
                        "induction; it is never repelled."
                    ),
                },
            },
            {
                "id": "P7L2",
                "title": "Electromagnetism & The Motor Effect",
                "unit": "Topic 7",
                "subtitle": "Solenoids, Fleming's Left Hand Rule, F = BIl (HT), dc motor",
                "url": "https://www.bbc.co.uk/bitesize/guides/zb4nmfr/revision/2",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Describe the magnetic field around a current-carrying conductor and solenoid",
                    "State three ways to increase the strength of an electromagnet",
                    "Apply Fleming's Left Hand Rule to find force direction",
                    "(HT) Recall and apply F = BIl",
                ],
                "key_vocab": [
                    "electromagnet", "solenoid", "motor effect", "magnetic flux density",
                    "Fleming's Left Hand Rule", "commutator", "dc motor",
                ],
                "techniques": ["Active Recall", "Pattern Recognition"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zb4nmfr/revision/2"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "A current-carrying conductor has a circular magnetic field around it. "
                        "Solenoid: coiled wire produces a field similar to a bar magnet. "
                        "Increase electromagnet strength: increase current, increase turns, add iron core. "
                        "Motor effect: a current in a magnetic field experiences a force. "
                        "Fleming's Left Hand Rule: thumb = force/motion, index = field (N→S), "
                        "middle = conventional current. "
                        "HT: F = BIl (force F in N; flux density B in T; current I in A; length l in m). "
                        "DC motor: commutator reverses current direction every half-turn to maintain rotation."
                    ),
                    "equations": [
                        "HT: F = BIl  (force F in N; magnetic flux density B in T; current I in A; length l in m) — recall and apply",
                    ],
                    "facts": [
                        "Increase electromagnet: more current, more turns, iron core.",
                        "Fleming's LHR: thumb = force, index = field, middle = current.",
                        "Motor effect: current in field → force on conductor.",
                        "DC motor: commutator reverses current every half-turn → continuous rotation.",
                        "Loudspeaker uses motor effect: ac current → alternating force → vibrating cone → sound.",
                    ],
                    "spec_points": ["4.7.2", "4.7.3"],
                },
                "expected_answers": {
                    "What three things increase the strength of an electromagnet?": (
                        "Increasing the current, increasing the number of turns of wire, "
                        "adding a soft iron core."
                    ),
                    "(HT) A wire of length 0.2 m carries 5 A in a field of 0.3 T. Find the force.": (
                        "F = BIl = 0.3 × 5 × 0.2 = 0.3 N"
                    ),
                    "What is the role of the commutator in a dc motor?": (
                        "It reverses the direction of current in the coil every half-revolution, "
                        "so the force on the coil always acts in the same rotational direction, "
                        "maintaining continuous rotation."
                    ),
                },
            },
            {
                "id": "P7L3",
                "title": "Electromagnetic Induction & Generators",
                "unit": "Topic 7",
                "subtitle": "Induced pd, alternators, microphones, transformers",
                "url": "https://www.bbc.co.uk/bitesize/guides/zb4nmfr/revision/3",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Explain the conditions needed to induce a potential difference",
                    "State three ways to increase the induced pd",
                    "Explain how an alternator produces ac",
                    "Apply Vp/Vs = np/ns and (HT) VpIp = VsIs for transformers",
                ],
                "key_vocab": [
                    "electromagnetic induction", "induced pd", "alternator", "generator",
                    "transformer", "primary coil", "secondary coil", "step-up", "step-down",
                ],
                "techniques": ["Active Recall", "Show Working", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zb4nmfr/revision/3"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "A potential difference is induced when a conductor moves through a magnetic "
                        "field, or when the field through a conductor changes. "
                        "Increase induced pd: move conductor faster, stronger magnetic field, more turns. "
                        "Alternator: coil rotated in field → ac output. "
                        "Microphone: sound → vibrating diaphragm → coil moves in field → induced current. "
                        "Loudspeaker (physics only): ac in coil → motor effect → cone vibrates → sound. "
                        "Transformer: Vp/Vs = np/ns. Step-up: ns > np → higher voltage. "
                        "HT: VpIp = VsIs (assuming 100% efficiency). Only work with ac."
                    ),
                    "equations": [
                        "Vp/Vs = np/ns  (given on sheet — recall and apply)",
                        "HT: VpIp = VsIs  (given on sheet)",
                    ],
                    "facts": [
                        "Induction requires relative motion between conductor and magnetic field (or changing field).",
                        "Three ways to increase induced pd: faster movement, stronger field, more turns.",
                        "Transformers: only work with ac (changing flux needed).",
                        "Step-up: ns > np → Vs > Vp (and Is < Ip).",
                        "Step-down: ns < np → Vs < Vp.",
                    ],
                    "spec_points": ["4.7.4", "4.7.5"],
                },
                "expected_answers": {
                    "State three ways to increase the induced pd in a wire moving through a field.": (
                        "Move the wire faster; use a stronger magnet; use a longer wire (or more turns in a coil)."
                    ),
                    "A transformer has 500 primary turns and 50 secondary turns, with 230 V input. Find output voltage.": (
                        "Vs = (ns/np) × Vp = (50/500) × 230 = 23 V"
                    ),
                    "(HT) Primary: 230 V, 0.1 A. Secondary: 11.5 V. Find secondary current (100% efficiency).": (
                        "VpIp = VsIs → Is = (230 × 0.1) / 11.5 = 2 A"
                    ),
                    "Why do transformers only work with ac?": (
                        "Transformers need a continuously changing magnetic flux to induce a voltage "
                        "in the secondary coil. AC produces a changing flux; DC does not."
                    ),
                },
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # TOPIC 8 — SPACE PHYSICS  (Paper 2, Physics only)
    # ══════════════════════════════════════════════════════════════════
    "Topic 8": {
        "title": "Space Physics",
        "color": "#2c3e50",
        "level": "Advanced",
        "description": "Solar system, stellar evolution, the Big Bang, red-shift, and dark matter.",
        "lessons": [
            {
                "id": "P8L1",
                "title": "The Solar System & Orbits",
                "unit": "Topic 8",
                "subtitle": "Gravity, orbital speed, satellites — Physics only",
                "url": "https://www.bbc.co.uk/bitesize/guides/zs4thyc/revision/1",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Describe the structure of the Solar System",
                    "Explain that gravity provides centripetal force for orbital motion",
                    "Explain why planets closer to the Sun orbit faster",
                    "Compare geostationary and low Earth orbit satellites",
                ],
                "key_vocab": [
                    "solar system", "orbit", "gravity", "centripetal force",
                    "geostationary", "low Earth orbit", "satellite",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zs4thyc/revision/1"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/space"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Solar System: Sun + 8 planets + moons + asteroids + comets. Planets orbit "
                        "in ellipses (nearly circular). Gravity provides the centripetal force. "
                        "Closer to Sun → stronger gravity → higher orbital speed needed. "
                        "Geostationary orbit: period = 24 h; stays above same point on Earth; used "
                        "for TV/communications. Low Earth orbit: period ~90 min; lower altitude; "
                        "used for weather, GPS, ISS, polar imaging."
                    ),
                    "facts": [
                        "Gravity provides centripetal force for all orbits.",
                        "Closer to Sun → stronger gravity → faster orbital speed (shorter period).",
                        "Geostationary: 24 h period, equatorial, fixed point above Earth, ~36,000 km altitude.",
                        "LEO: ~90 min period, ~200–2000 km altitude, not fixed above one point.",
                        "LEO satellites: weather, GPS, ISS, Earth observation.",
                    ],
                    "spec_points": ["4.8.1"],
                },
                "expected_answers": {
                    "What force keeps planets in orbit around the Sun?": (
                        "Gravity — the gravitational attraction between the planet and the Sun "
                        "provides the centripetal force needed for the orbit."
                    ),
                    "Why do planets closer to the Sun orbit faster?": (
                        "Closer planets experience stronger gravitational force. A higher orbital "
                        "speed is needed to maintain a circular orbit against this stronger pull."
                    ),
                    "Give one advantage of a geostationary orbit for communications.": (
                        "The satellite remains above the same point on Earth at all times, so "
                        "fixed dish antennas on the ground can maintain constant communication."
                    ),
                },
            },
            {
                "id": "P8L2",
                "title": "Life Cycle of Stars",
                "unit": "Topic 8",
                "subtitle": "From nebula to end state — nuclear fusion and element formation",
                "url": "https://www.bbc.co.uk/bitesize/guides/zs4thyc/revision/2",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Describe the full life cycle of a Sun-like star",
                    "Describe the full life cycle of a massive star",
                    "Explain the role of nuclear fusion and radiation pressure vs gravity",
                    "Explain how heavy elements form and are distributed",
                ],
                "key_vocab": [
                    "nebula", "protostar", "main sequence", "red giant", "red supergiant",
                    "white dwarf", "supernova", "neutron star", "black hole", "nuclear fusion",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zs4thyc/revision/2"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "All stars: nebula (dust + gas) → protostar (gravity contracts) → main sequence "
                        "(fusion: H → He; radiation pressure balances gravity). "
                        "Small/medium star: main sequence → red giant → planetary nebula → white dwarf → black dwarf. "
                        "Massive star: main sequence → red supergiant → supernova → neutron star OR black hole. "
                        "Elements up to iron formed by fusion in stars. "
                        "Elements heavier than iron only formed in supernovae. "
                        "Supernovae distribute heavy elements throughout the universe — we are 'star stuff'."
                    ),
                    "facts": [
                        "Main sequence: hydrogen fusion, radiation pressure balances gravity.",
                        "Small star ends: white dwarf → black dwarf (over billions of years).",
                        "Massive star ends: supernova → neutron star or black hole.",
                        "Elements up to iron: formed by stellar fusion.",
                        "Elements heavier than iron: only formed in supernovae.",
                        "Supernovae disperse heavy elements — source of elements in planets and life.",
                    ],
                    "spec_points": ["4.8.2"],
                },
                "expected_answers": {
                    "What process releases energy in a main sequence star?": (
                        "Nuclear fusion — hydrogen nuclei fuse to form helium, releasing large amounts of energy."
                    ),
                    "What is the difference in the final stages of a small star and a massive star?": (
                        "Small star: ends as a white dwarf (via planetary nebula). "
                        "Massive star: ends as a neutron star or black hole (via supernova)."
                    ),
                    "Why are supernovae important for the elements found on Earth?": (
                        "Elements heavier than iron are only created in supernovae. The explosion "
                        "scatters these heavy elements through space, where they can form new "
                        "solar systems, planets, and ultimately life."
                    ),
                },
            },
            {
                "id": "P8L3",
                "title": "The Big Bang, Red-Shift & Dark Matter",
                "unit": "Topic 8",
                "subtitle": "Evidence for expanding universe, CMBR, dark matter and energy",
                "url": "https://www.bbc.co.uk/bitesize/guides/zs4thyc/revision/3",
                "estimated_minutes": 25,
                "split": False,
                "learning_goals": [
                    "Explain what red-shift is and what it tells us about galaxies",
                    "State two pieces of evidence for the Big Bang",
                    "Explain what CMBR is and its significance",
                    "Describe the observational basis for dark matter and dark energy",
                ],
                "key_vocab": [
                    "red-shift", "expanding universe", "Big Bang", "cosmic microwave background",
                    "dark matter", "dark energy", "galaxy recession",
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "resources": [
                    {"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zs4thyc/revision/3"},
                    {"name": "GCSE Physics Online", "url": "https://www.gcsephysicsonline.com/space"},
                ],
                "knowledge_bank": {
                    "summary": (
                        "Red-shift: light from distant galaxies is shifted to longer wavelengths "
                        "(lower frequency), indicating they are moving away. More distant galaxies → "
                        "greater red-shift → receding faster. "
                        "Evidence for Big Bang: (1) red-shift of all galaxies → universe is expanding; "
                        "(2) cosmic microwave background radiation (CMBR) — microwave radiation filling "
                        "all of space, remnant of the very hot early universe. "
                        "Dark matter: galaxies rotate faster at their edges than visible mass predicts — "
                        "unseen mass must exist. Not yet directly detected. "
                        "Dark energy: universe's expansion is accelerating, not slowing — "
                        "dark energy opposes gravity. Not yet understood. "
                        "Both illustrate limits of current scientific knowledge."
                    ),
                    "facts": [
                        "Red-shift: galaxies moving away → light stretched to longer wavelengths.",
                        "More distant galaxy → greater red-shift → faster recession.",
                        "CMBR: microwave radiation from all directions; left over from Big Bang.",
                        "Big Bang: universe started ~13.8 billion years ago from hot dense state.",
                        "Dark matter evidence: galaxies rotate too fast at edges for visible mass.",
                        "Dark energy evidence: universe expansion is accelerating.",
                        "Neither dark matter nor dark energy is directly detected or fully understood.",
                    ],
                    "spec_points": ["4.8.3"],
                },
                "expected_answers": {
                    "What is red-shift and what does it indicate?": (
                        "Red-shift is the increase in wavelength (shift towards red end of spectrum) "
                        "of light from distant galaxies. It indicates those galaxies are moving away from us."
                    ),
                    "Give two pieces of evidence supporting the Big Bang theory.": (
                        "1. Red-shift: all distant galaxies are moving away, so the universe is expanding "
                        "— consistent with originating from a single point. "
                        "2. Cosmic microwave background radiation: uniform microwave radiation filling "
                        "all of space, the cooled remnant of the extremely hot early universe."
                    ),
                    "What observational evidence suggests dark matter exists?": (
                        "Galaxies rotate faster at their outer edges than can be explained by the "
                        "gravitational pull of visible matter alone — extra unseen mass (dark matter) "
                        "must be present."
                    ),
                    "What does the accelerating expansion of the universe suggest?": (
                        "The existence of dark energy — an unknown force that counteracts gravity "
                        "and is causing the expansion to speed up."
                    ),
                },
            },
        ],
    },
}


# ─── Spaced Repetition Intervals ────────────────────────────────────────────
SR_INTERVALS = {0: 1, 1: 3, 2: 7, 3: 14, 4: 30, 5: 90}


# ─── Helper functions (unchanged API — app.py uses these) ────────────────────

def get_all_physics_lessons():
    lessons = []
    for unit_data in PHYSICS_CURRICULUM.values():
        for lesson in unit_data["lessons"]:
            lesson["unit_title"] = unit_data["title"]
        lessons.extend(unit_data["lessons"])
    return lessons


def get_physics_lesson_by_id(lesson_id: str):
    for unit_name, unit_data in PHYSICS_CURRICULUM.items():
        for lesson in unit_data["lessons"]:
            if lesson["id"] == lesson_id:
                lesson["unit"] = unit_name
                lesson["unit_title"] = unit_data["title"]
                return lesson
    return None


def get_physics_unit_progress_summary(progress_data: dict):
    summary = {}
    colors = [
        "#e74c3c", "#f39c12", "#27ae60", "#8e44ad",
        "#3498db", "#16a085", "#e67e22", "#2c3e50",
    ]
    for i, (unit_name, unit_data) in enumerate(PHYSICS_CURRICULUM.items()):
        lessons = unit_data["lessons"]
        completed = sum(
            1 for l in lessons
            if progress_data.get(l["id"], {}).get("status") == "completed"
        )
        summary[unit_name] = {
            "title": unit_data["title"],
            "completed": completed,
            "total": len(lessons),
            "percent": round(completed / len(lessons) * 100) if lessons else 0,
            "color": colors[i % len(colors)],
            "level": unit_data["level"],
        }
    return summary
