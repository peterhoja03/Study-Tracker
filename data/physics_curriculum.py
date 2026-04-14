"""
AQA GCSE Physics Curriculum
All 8 topics with 25-min sessions, active recall focus, no note-copying.
"""

PHYSICS_CURRICULUM = {
    "Topic 1": {
        "title": "Energy",
        "color": "#e74c3c",
        "level": "Foundation",
        "description": "Energy stores, transfers, conservation, and efficiency. The bedrock of all physics.",
        "lessons": [
            {
                "id": "P1L1", "title": "Energy Stores & Systems", "unit": "Topic 1",
                "subtitle": "Kinetic, gravitational, elastic, thermal, chemical, nuclear, magnetic, electrostatic",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/1",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Name all 8 energy stores from memory",
                    "Give a real-world example for each store",
                    "Explain what a 'system' means in physics",
                    "Identify energy stores in everyday objects (phone, spring, car)"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Pattern Recognition"],
                "key_vocab": ["energy store", "kinetic", "gravitational potential", "elastic potential", "thermal", "chemical", "nuclear", "electrostatic", "magnetic", "system"],
                "feynman_prompt": "Explain the 8 energy stores to someone who has never studied physics. Use everyday objects as examples — what energy store is a stretched elastic band? A hot cup of tea? A moving car?",
                "active_recall_questions": [
                    "Without looking, name all 8 energy stores",
                    "What energy stores does a roller coaster have at the top of a hill vs the bottom?",
                    "A phone battery — what energy store is it, and what does it transfer to?",
                    "What is the difference between an energy store and an energy transfer?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/1"}, {"name": "AQA Spec", "url": "https://www.aqa.org.uk/subjects/science/gcse/physics-8463"}]
            },
            {
                "id": "P1L2", "title": "Energy Transfers & Pathways", "unit": "Topic 1",
                "subtitle": "Mechanical work, electrical work, heating, radiation",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/2",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Describe the 4 energy transfer pathways",
                    "Draw and label a Sankey diagram for a simple device",
                    "Explain the difference between useful and wasted energy",
                    "Trace energy transfers in a kettle, light bulb, and car engine"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Writing Practice"],
                "key_vocab": ["mechanical work", "electrical work", "heating", "radiation", "Sankey diagram", "useful energy", "wasted energy", "energy pathway"],
                "feynman_prompt": "Draw a Sankey diagram for a light bulb from memory and explain what it shows. Where does the energy come from, where does it go, and what's wasted?",
                "active_recall_questions": [
                    "What are the 4 energy transfer pathways?",
                    "In a Sankey diagram, what does the width of each arrow represent?",
                    "A car engine is 25% efficient — what does that mean in plain English?",
                    "Name 3 devices and trace their energy transfers from input to output"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/2"}]
            },
            {
                "id": "P1L3", "title": "Conservation of Energy", "unit": "Topic 1",
                "subtitle": "Energy cannot be created or destroyed, only transferred",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/3",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "State the law of conservation of energy",
                    "Apply conservation to closed and open systems",
                    "Explain why perpetual motion machines are impossible",
                    "Calculate total energy in a system before and after a transfer"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["conservation of energy", "closed system", "open system", "perpetual motion", "dissipation"],
                "feynman_prompt": "A friend says 'if energy can't be destroyed, why do we run out of it?' Explain why they're confused and what actually happens to energy.",
                "active_recall_questions": [
                    "State the law of conservation of energy in one sentence",
                    "What is a closed system? Give an example",
                    "Why can't a perpetual motion machine ever work?",
                    "A ball is dropped from 10m. Where does all the energy go when it hits the floor?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/3"}]
            },
            {
                "id": "P1L4", "title": "Efficiency", "unit": "Topic 1",
                "subtitle": "Efficiency = useful output / total input",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/4",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Write and apply the efficiency equation",
                    "Calculate efficiency as a decimal and percentage",
                    "Explain how to improve efficiency of devices",
                    "Understand why 100% efficiency is impossible in practice"
                ],
                "techniques": ["Active Recall", "Writing Practice", "Pattern Recognition"],
                "key_vocab": ["efficiency", "useful output energy", "total input energy", "percentage efficiency", "lubrication", "insulation"],
                "feynman_prompt": "Explain efficiency to someone who thinks a 'more efficient' car just means it goes faster. What does efficiency actually measure, and how do engineers improve it?",
                "active_recall_questions": [
                    "Write the efficiency equation from memory",
                    "A motor takes in 500J and outputs 350J of useful energy. What is its efficiency?",
                    "Name 3 ways engineers improve the efficiency of a car engine",
                    "Why can no device ever be 100% efficient?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/4"}]
            },
            {
                "id": "P1L5", "title": "Energy Resources", "unit": "Topic 1",
                "subtitle": "Renewable vs non-renewable, uses, advantages and disadvantages",
                "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/5",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Classify all major energy resources as renewable or non-renewable",
                    "Explain how each resource generates electricity",
                    "Compare reliability, environmental impact, and cost for each",
                    "Evaluate the UK's energy mix and future trends"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Pattern Recognition"],
                "key_vocab": ["renewable", "non-renewable", "fossil fuels", "nuclear", "wind", "solar", "hydroelectric", "tidal", "geothermal", "biomass", "carbon footprint"],
                "feynman_prompt": "Imagine you're advising the UK government on energy policy. Which resources would you recommend and why? What are the trade-offs between reliability, cost, and environmental impact?",
                "active_recall_questions": [
                    "Name all renewable energy resources from memory",
                    "What are the 3 fossil fuels and why are they non-renewable?",
                    "What is the main disadvantage of wind and solar power?",
                    "How does a nuclear power station generate electricity?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z6sbtv4/revision/5"}]
            },
        ]
    },
    "Topic 2": {
        "title": "Electricity",
        "color": "#f39c12",
        "level": "Foundation",
        "description": "Circuits, current, voltage, resistance, and electrical power.",
        "lessons": [
            {
                "id": "P2L1", "title": "Current, Potential Difference & Resistance", "unit": "Topic 2",
                "subtitle": "V = IR — the most important equation in electricity",
                "url": "https://www.bbc.co.uk/bitesize/guides/zq7sb82/revision/1",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Define current, potential difference, and resistance in plain English",
                    "State and apply Ohm's Law (V = IR)",
                    "Explain what an ohmic conductor is",
                    "Describe how resistance changes with temperature in a metal wire"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Writing Practice"],
                "key_vocab": ["current", "potential difference", "voltage", "resistance", "Ohm's Law", "ohmic conductor", "ampere", "volt", "ohm"],
                "feynman_prompt": "Explain current, voltage, and resistance using a water pipe analogy. What is the 'water', what is the 'pressure', and what is the 'pipe width'?",
                "active_recall_questions": [
                    "Write Ohm's Law from memory and state the units for each quantity",
                    "What is an ohmic conductor? Give an example",
                    "A 12V battery drives 2A through a resistor. What is the resistance?",
                    "Why does resistance increase when a metal wire gets hotter?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zq7sb82/revision/1"}]
            },
            {
                "id": "P2L2", "title": "Series & Parallel Circuits", "unit": "Topic 2",
                "subtitle": "How components behave differently depending on circuit type",
                "url": "https://www.bbc.co.uk/bitesize/guides/zq7sb82/revision/2",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Draw and label series and parallel circuits",
                    "State the rules for current and voltage in each circuit type",
                    "Calculate total resistance in series and parallel",
                    "Explain why household circuits are wired in parallel"
                ],
                "techniques": ["Active Recall", "Writing Practice", "Pattern Recognition"],
                "key_vocab": ["series circuit", "parallel circuit", "total resistance", "branch", "junction", "potential divider"],
                "feynman_prompt": "Your house lights are wired in parallel, not series. Explain to a non-physicist why this is, and what would happen if they were in series instead.",
                "active_recall_questions": [
                    "In a series circuit, what happens to current and voltage across components?",
                    "In a parallel circuit, what stays the same across all branches?",
                    "Two 6Ω resistors in series — what is the total resistance?",
                    "Two 6Ω resistors in parallel — what is the total resistance?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zq7sb82/revision/2"}]
            },
            {
                "id": "P2L3", "title": "Electrical Power & Energy", "unit": "Topic 2",
                "subtitle": "P = IV, P = I²R, energy transferred equations",
                "url": "https://www.bbc.co.uk/bitesize/guides/zq7sb82/revision/3",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "State and apply P = IV and P = I²R",
                    "Calculate energy transferred using E = Pt",
                    "Explain what a watt and kilowatt-hour mean",
                    "Calculate electricity costs using power and time"
                ],
                "techniques": ["Active Recall", "Writing Practice"],
                "key_vocab": ["power", "watt", "kilowatt", "kilowatt-hour", "energy transferred", "P = IV", "P = I²R", "E = Pt"],
                "feynman_prompt": "Explain why a 100W light bulb left on for 10 hours costs more than a 1000W kettle used for 5 minutes, even though the kettle has higher power.",
                "active_recall_questions": [
                    "Write all three power equations from memory",
                    "A kettle is rated 2kW and runs for 3 minutes. How much energy does it use in joules?",
                    "What is a kilowatt-hour and why do energy companies use it instead of joules?",
                    "An appliance draws 5A at 230V. What is its power rating?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zq7sb82/revision/3"}]
            },
            {
                "id": "P2L4", "title": "Mains Electricity & Safety", "unit": "Topic 2",
                "subtitle": "AC vs DC, UK mains supply, plugs, fuses, earthing",
                "url": "https://www.bbc.co.uk/bitesize/guides/zq7sb82/revision/4",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Distinguish between AC and DC",
                    "State UK mains supply values (230V, 50Hz)",
                    "Explain the role of live, neutral, and earth wires",
                    "Describe how a fuse and RCD protect against electric shock"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["alternating current", "direct current", "mains supply", "live wire", "neutral wire", "earth wire", "fuse", "RCD", "frequency", "hertz"],
                "feynman_prompt": "Explain to someone why touching the live wire is dangerous but touching the neutral wire is much less so. What is the earth wire actually for?",
                "active_recall_questions": [
                    "What is the difference between AC and DC?",
                    "State the UK mains voltage and frequency",
                    "What colour is the live, neutral, and earth wire in a UK plug?",
                    "How does a fuse protect an appliance? What happens when it blows?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zq7sb82/revision/4"}]
            },
        ]
    },
    "Topic 3": {
        "title": "Particle Model of Matter",
        "color": "#27ae60",
        "level": "Foundation",
        "description": "States of matter, density, changes of state, and specific heat capacity.",
        "lessons": [
            {
                "id": "P3L1", "title": "Density & States of Matter", "unit": "Topic 3",
                "subtitle": "ρ = m/V, solid/liquid/gas particle arrangements",
                "url": "https://www.bbc.co.uk/bitesize/guides/zsk8ng8/revision/1",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Describe particle arrangement in solids, liquids, and gases",
                    "State and apply the density equation ρ = m/V",
                    "Explain why gases have much lower density than solids",
                    "Calculate density from mass and volume measurements"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Writing Practice"],
                "key_vocab": ["density", "mass", "volume", "solid", "liquid", "gas", "particle model", "arrangement", "ρ = m/V"],
                "feynman_prompt": "Explain why a block of lead sinks in water but a huge ship made of steel floats. Use particle model and density in your explanation.",
                "active_recall_questions": [
                    "Write the density equation and state units for each quantity",
                    "Describe the particle arrangement in a solid, liquid, and gas",
                    "Why is a gas much less dense than a solid of the same substance?",
                    "A block has mass 500g and volume 250cm³. What is its density?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zsk8ng8/revision/1"}]
            },
            {
                "id": "P3L2", "title": "Changes of State & Specific Heat Capacity", "unit": "Topic 3",
                "subtitle": "Melting, boiling, specific heat capacity equation",
                "url": "https://www.bbc.co.uk/bitesize/guides/zsk8ng8/revision/2",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Name all changes of state and the direction of energy transfer",
                    "Explain what happens at a molecular level during melting and boiling",
                    "State and apply Q = mcΔT",
                    "Explain why temperature stays constant during a change of state"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Writing Practice"],
                "key_vocab": ["melting", "freezing", "evaporation", "condensation", "sublimation", "specific heat capacity", "latent heat", "Q = mcΔT"],
                "feynman_prompt": "You're heating ice from -20°C to steam at 120°C. Draw the temperature-time graph from memory and explain every flat section and every slope.",
                "active_recall_questions": [
                    "Write the specific heat capacity equation and define each term",
                    "Why does the temperature stay flat when ice is melting, even though you're still adding heat?",
                    "Water has a specific heat capacity of 4200 J/kg°C. What does that number mean?",
                    "Name all 6 changes of state and whether they absorb or release energy"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zsk8ng8/revision/2"}]
            },
            {
                "id": "P3L3", "title": "Pressure in Gases", "unit": "Topic 3",
                "subtitle": "Gas pressure, temperature, volume relationships",
                "url": "https://www.bbc.co.uk/bitesize/guides/zsk8ng8/revision/3",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Explain gas pressure in terms of particle collisions",
                    "Describe how pressure changes with temperature at constant volume",
                    "Apply the pressure-volume relationship (Boyle's Law)",
                    "Explain what absolute zero means and why it matters"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["gas pressure", "particle collisions", "Boyle's Law", "absolute zero", "kelvin", "temperature-pressure relationship"],
                "feynman_prompt": "Explain why a car tyre pressure increases on a hot day using particle physics. Then explain what would happen if you cooled the tyre to absolute zero.",
                "active_recall_questions": [
                    "Why does gas exert pressure on the walls of its container?",
                    "What happens to gas pressure when you increase temperature at constant volume?",
                    "What is absolute zero in Celsius and Kelvin?",
                    "A gas at 2 atm occupies 3L. What volume does it occupy at 6 atm?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zsk8ng8/revision/3"}]
            },
        ]
    },
    "Topic 4": {
        "title": "Atomic Structure & Radioactivity",
        "color": "#8e44ad",
        "level": "Foundation",
        "description": "Atomic structure, isotopes, radioactive decay, half-life, and nuclear radiation.",
        "lessons": [
            {
                "id": "P4L1", "title": "Atomic Structure & Isotopes", "unit": "Topic 4",
                "subtitle": "Protons, neutrons, electrons, atomic number, mass number",
                "url": "https://www.bbc.co.uk/bitesize/guides/zb3yb82/revision/1",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Describe the structure of an atom including relative masses and charges",
                    "Define atomic number and mass number",
                    "Explain what isotopes are and give examples",
                    "Describe how the model of the atom changed historically"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["proton", "neutron", "electron", "nucleus", "atomic number", "mass number", "isotope", "ion", "nuclear model", "plum pudding model"],
                "feynman_prompt": "Explain how our model of the atom changed from Thomson to Rutherford. What experiment changed everything, and why was the result so surprising?",
                "active_recall_questions": [
                    "State the relative mass and charge of protons, neutrons, and electrons",
                    "What is an isotope? Give two examples using carbon",
                    "What is the atomic number and mass number of Carbon-14?",
                    "Describe Rutherford's gold foil experiment and what it proved"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zb3yb82/revision/1"}]
            },
            {
                "id": "P4L2", "title": "Radioactive Decay & Types of Radiation", "unit": "Topic 4",
                "subtitle": "Alpha, beta, gamma — properties, penetration, ionisation",
                "url": "https://www.bbc.co.uk/bitesize/guides/zb3yb82/revision/2",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Describe alpha, beta, and gamma radiation and their properties",
                    "Compare penetrating power and ionising ability of each type",
                    "Write nuclear equations for alpha and beta decay",
                    "Explain what background radiation is and its sources"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Writing Practice"],
                "key_vocab": ["alpha particle", "beta particle", "gamma ray", "ionisation", "penetration", "nuclear equation", "background radiation", "radioactive decay"],
                "feynman_prompt": "You're a nuclear safety officer explaining to staff why alpha radiation is the most dangerous inside the body but least dangerous outside. Explain the reasoning clearly.",
                "active_recall_questions": [
                    "What is an alpha particle made of? What about beta?",
                    "Which type of radiation is stopped by paper? By aluminium? By lead?",
                    "Write the nuclear equation for alpha decay of Uranium-238",
                    "Name 4 sources of background radiation in everyday life"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zb3yb82/revision/2"}]
            },
            {
                "id": "P4L3", "title": "Half-Life & Uses of Radiation", "unit": "Topic 4",
                "subtitle": "Half-life calculations, medical, industrial, and dating uses",
                "url": "https://www.bbc.co.uk/bitesize/guides/zb3yb82/revision/3",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Define half-life and calculate remaining activity after multiple half-lives",
                    "Explain carbon dating and why it works",
                    "Describe medical uses of radiation (tracers, radiotherapy)",
                    "Evaluate risks and benefits of using radiation"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["half-life", "activity", "becquerel", "carbon dating", "radioactive tracer", "radiotherapy", "irradiation", "contamination"],
                "feynman_prompt": "Explain to a sceptic how scientists can be confident about the age of a 50,000-year-old fossil using carbon dating. Walk through the logic step by step.",
                "active_recall_questions": [
                    "Define half-life in one sentence",
                    "A sample starts with 800 atoms. After 3 half-lives, how many remain?",
                    "Why is carbon-14 used for dating organic material but not rocks?",
                    "What is the difference between irradiation and contamination?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zb3yb82/revision/3"}]
            },
        ]
    },
    "Topic 5": {
        "title": "Forces",
        "color": "#3498db",
        "level": "Intermediate",
        "description": "Contact and non-contact forces, Newton's Laws, momentum, and pressure.",
        "lessons": [
            {
                "id": "P5L1", "title": "Forces & Free Body Diagrams", "unit": "Topic 5",
                "subtitle": "Contact vs non-contact, resultant force, drawing FBDs",
                "url": "https://www.bbc.co.uk/bitesize/guides/zcrd7ty/revision/1",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Distinguish between contact and non-contact forces with examples",
                    "Draw accurate free body diagrams for objects in various situations",
                    "Calculate resultant force from multiple forces",
                    "Explain what it means for forces to be balanced or unbalanced"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Writing Practice"],
                "key_vocab": ["contact force", "non-contact force", "resultant force", "free body diagram", "balanced forces", "unbalanced forces", "tension", "normal force", "friction", "weight", "gravity"],
                "feynman_prompt": "Draw a free body diagram for a skydiver at terminal velocity. Label every force and explain why they are balanced. Then draw a second diagram just after they jump — what's different?",
                "active_recall_questions": [
                    "Name 3 contact forces and 3 non-contact forces",
                    "Draw a free body diagram for a book resting on a table",
                    "A 500N push right and 200N friction left — what is the resultant force?",
                    "What does it mean when the resultant force on an object is zero?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zcrd7ty/revision/1"}]
            },
            {
                "id": "P5L2", "title": "Newton's Three Laws", "unit": "Topic 5",
                "subtitle": "Inertia, F=ma, action-reaction pairs",
                "url": "https://www.bbc.co.uk/bitesize/guides/zcrd7ty/revision/2",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "State Newton's three laws of motion clearly",
                    "Apply F = ma to calculate force, mass, or acceleration",
                    "Identify Newton's third law pairs in real situations",
                    "Explain inertia and relate it to mass"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Writing Practice"],
                "key_vocab": ["Newton's First Law", "Newton's Second Law", "Newton's Third Law", "inertia", "F = ma", "acceleration", "action-reaction", "force pair"],
                "feynman_prompt": "Explain Newton's Third Law using a rocket launching into space. Why does the rocket go up when the exhaust goes down? Why doesn't the exhaust push the launch pad away equally?",
                "active_recall_questions": [
                    "State Newton's three laws of motion from memory",
                    "A 1000kg car accelerates at 3 m/s². What force is acting on it?",
                    "Identify the Newton's third law pair when you push against a wall",
                    "Why does a heavy truck take longer to stop than a small car at the same speed?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zcrd7ty/revision/2"}]
            },
            {
                "id": "P5L3", "title": "Motion Graphs", "unit": "Topic 5",
                "subtitle": "Distance-time and velocity-time graphs, gradients, areas",
                "url": "https://www.bbc.co.uk/bitesize/guides/zcrd7ty/revision/3",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Interpret distance-time and velocity-time graphs",
                    "Calculate speed/velocity from gradient of d-t graph",
                    "Calculate acceleration from gradient of v-t graph",
                    "Calculate distance travelled from area under v-t graph"
                ],
                "techniques": ["Active Recall", "Writing Practice", "Pattern Recognition"],
                "key_vocab": ["distance-time graph", "velocity-time graph", "gradient", "area under graph", "acceleration", "deceleration", "uniform motion", "speed", "velocity"],
                "feynman_prompt": "Sketch a velocity-time graph for a car journey: speeds up, cruises, brakes hard to a stop. Label every section and explain how to find the total distance from the graph.",
                "active_recall_questions": [
                    "What does the gradient of a distance-time graph tell you?",
                    "What does the gradient of a velocity-time graph tell you?",
                    "What does the area under a velocity-time graph represent?",
                    "Sketch a v-t graph for an object in free fall with air resistance reaching terminal velocity"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zcrd7ty/revision/3"}]
            },
            {
                "id": "P5L4", "title": "Momentum", "unit": "Topic 5",
                "subtitle": "p = mv, conservation of momentum, impulse",
                "url": "https://www.bbc.co.uk/bitesize/guides/zcrd7ty/revision/4",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Define momentum and state the equation p = mv",
                    "Apply conservation of momentum to collisions",
                    "Explain impulse and relate it to safety features",
                    "Solve problems involving collisions and explosions"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Writing Practice"],
                "key_vocab": ["momentum", "p = mv", "conservation of momentum", "impulse", "force-time graph", "crumple zone", "airbag"],
                "feynman_prompt": "Explain why cars have crumple zones and airbags using the concept of impulse and momentum. Why does increasing the time of impact reduce the force on the driver?",
                "active_recall_questions": [
                    "Write the momentum equation and state units",
                    "State the law of conservation of momentum",
                    "A 2kg ball at 5m/s hits a stationary 3kg ball. They stick together. What is their combined velocity?",
                    "Why do airbags reduce injury using physics? (mention impulse)"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zcrd7ty/revision/4"}]
            },
        ]
    },
    "Topic 6": {
        "title": "Waves",
        "color": "#16a085",
        "level": "Intermediate",
        "description": "Wave properties, electromagnetic spectrum, sound, and light.",
        "lessons": [
            {
                "id": "P6L1", "title": "Wave Properties", "unit": "Topic 6",
                "subtitle": "Amplitude, frequency, wavelength, wave speed equation",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgmxsbk/revision/1",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Define amplitude, frequency, wavelength, and wave speed",
                    "Distinguish between transverse and longitudinal waves",
                    "Apply v = fλ to solve wave speed problems",
                    "Draw and label a transverse wave diagram"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Writing Practice"],
                "key_vocab": ["amplitude", "frequency", "wavelength", "wave speed", "transverse", "longitudinal", "compression", "rarefaction", "v = fλ", "hertz"],
                "feynman_prompt": "Explain the difference between transverse and longitudinal waves using a slinky as your prop. Then explain how a sound wave travels through air as a longitudinal wave.",
                "active_recall_questions": [
                    "Draw and label a transverse wave showing amplitude and wavelength",
                    "Write the wave speed equation and state units",
                    "A wave has frequency 200Hz and wavelength 1.5m. What is its speed?",
                    "Is sound a transverse or longitudinal wave? How do you know?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgmxsbk/revision/1"}]
            },
            {
                "id": "P6L2", "title": "Electromagnetic Spectrum", "unit": "Topic 6",
                "subtitle": "All 7 types, properties, uses, and hazards",
                "url": "https://www.bbc.co.uk/bitesize/guides/zgmxsbk/revision/2",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "List all 7 types of EM radiation in order of frequency/wavelength",
                    "State uses and hazards for each type",
                    "Explain why all EM waves travel at the same speed in a vacuum",
                    "Describe how wavelength relates to energy and frequency"
                ],
                "techniques": ["Active Recall", "Pattern Recognition", "Feynman Technique"],
                "key_vocab": ["electromagnetic spectrum", "radio waves", "microwaves", "infrared", "visible light", "ultraviolet", "X-rays", "gamma rays", "frequency", "wavelength", "speed of light"],
                "feynman_prompt": "Explain why UV radiation causes sunburn but visible light doesn't, even though both come from the Sun. Use frequency and energy in your explanation.",
                "active_recall_questions": [
                    "List all 7 EM waves from lowest to highest frequency",
                    "What speed do all EM waves travel at in a vacuum?",
                    "Name a use and a hazard for UV radiation and X-rays",
                    "Which has more energy — red light or violet light? Why?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zgmxsbk/revision/2"}]
            },
        ]
    },
    "Topic 7": {
        "title": "Magnetism & Electromagnetism",
        "color": "#e67e22",
        "level": "Intermediate",
        "description": "Magnetic fields, motors, generators, and transformers.",
        "lessons": [
            {
                "id": "P7L1", "title": "Magnetic Fields & Permanent Magnets", "unit": "Topic 7",
                "subtitle": "Field lines, poles, induced magnetism, compasses",
                "url": "https://www.bbc.co.uk/bitesize/guides/z3fq7ty/revision/1",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Draw magnetic field patterns for bar magnets and between two poles",
                    "Explain what field lines represent (direction and strength)",
                    "Describe induced magnetism and how to make/destroy a magnet",
                    "Explain how a compass works using field lines"
                ],
                "techniques": ["Active Recall", "Feynman Technique", "Writing Practice"],
                "key_vocab": ["magnetic field", "field lines", "north pole", "south pole", "induced magnetism", "permanent magnet", "temporary magnet", "compass"],
                "feynman_prompt": "Explain to a 10-year-old why a compass always points north. Use the concepts of magnetic field lines and the Earth's magnetic field.",
                "active_recall_questions": [
                    "Draw the magnetic field pattern around a bar magnet",
                    "What do the spacing of field lines tell you about field strength?",
                    "How can you make a steel nail into a temporary magnet?",
                    "Why does heating a magnet cause it to lose its magnetism?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z3fq7ty/revision/1"}]
            },
            {
                "id": "P7L2", "title": "Electromagnetism & the Motor Effect", "unit": "Topic 7",
                "subtitle": "Solenoids, Fleming's Left Hand Rule, motors",
                "url": "https://www.bbc.co.uk/bitesize/guides/z3fq7ty/revision/2",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Describe the magnetic field around a current-carrying wire",
                    "Explain how a solenoid works and how to increase its strength",
                    "Apply Fleming's Left Hand Rule to find force direction",
                    "Explain the basic principle of an electric motor"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["electromagnet", "solenoid", "current", "magnetic field", "Fleming's Left Hand Rule", "motor effect", "force", "electric motor", "commutator"],
                "feynman_prompt": "Explain step by step how an electric motor works. Start from current entering the coil and end with the coil spinning. Use Fleming's Left Hand Rule.",
                "active_recall_questions": [
                    "How can you increase the strength of an electromagnet?",
                    "Use Fleming's Left Hand Rule: current flows north, field points up — which way does the force act?",
                    "What is the role of the commutator in a DC motor?",
                    "Why does a current-carrying wire in a magnetic field experience a force?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/z3fq7ty/revision/2"}]
            },
        ]
    },
    "Topic 8": {
        "title": "Space Physics",
        "color": "#2c3e50",
        "level": "Advanced",
        "description": "Solar system, stellar evolution, Big Bang, and space exploration.",
        "lessons": [
            {
                "id": "P8L1", "title": "Our Solar System & Beyond", "unit": "Topic 8",
                "subtitle": "Planets, moons, asteroids, comets, light-years, scale",
                "url": "https://www.bbc.co.uk/bitesize/guides/zc7sb82/revision/1",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Describe the structure of the solar system in order from the Sun",
                    "Explain what keeps planets in orbit (gravity + velocity)",
                    "Understand the scale of space using light-years",
                    "Distinguish between solar system, galaxy, and universe"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["solar system", "orbit", "gravity", "light-year", "galaxy", "universe", "asteroid belt", "comet", "planet", "moon", "nebula"],
                "feynman_prompt": "Explain what keeps the Earth in orbit around the Sun. Why doesn't it fall into the Sun, and why doesn't it fly off into space?",
                "active_recall_questions": [
                    "Name the 8 planets in order from the Sun",
                    "What is a light-year and approximately how many km is it?",
                    "What two factors determine whether an object stays in orbit?",
                    "What is the difference between a galaxy and the universe?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zc7sb82/revision/1"}]
            },
            {
                "id": "P8L2", "title": "Stellar Evolution", "unit": "Topic 8",
                "subtitle": "Life cycle of stars, from nebula to black hole",
                "url": "https://www.bbc.co.uk/bitesize/guides/zc7sb82/revision/2",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Describe the full life cycle of a star like our Sun",
                    "Describe the life cycle of a massive star ending in a black hole",
                    "Explain nuclear fusion and why it powers stars",
                    "Explain what a red giant, white dwarf, neutron star, and black hole are"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["nebula", "protostar", "main sequence", "red giant", "white dwarf", "supernova", "neutron star", "black hole", "nuclear fusion", "gravity"],
                "feynman_prompt": "Trace the entire life of our Sun from its birth to its death. At each stage, explain what is happening inside the star and what forces are in balance.",
                "active_recall_questions": [
                    "List the stages of a Sun-like star's life in order",
                    "What is the difference in the final stages of a small vs massive star?",
                    "What is nuclear fusion and why does it stop eventually?",
                    "What happens when gravity wins over radiation pressure in a star?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zc7sb82/revision/2"}]
            },
            {
                "id": "P8L3", "title": "The Big Bang & Expanding Universe", "unit": "Topic 8",
                "subtitle": "Red-shift, cosmic microwave background, evidence for Big Bang",
                "url": "https://www.bbc.co.uk/bitesize/guides/zc7sb82/revision/3",
                "estimated_minutes": 25, "split": False,
                "learning_goals": [
                    "Explain what red-shift is and what it tells us about the universe",
                    "Describe the evidence for the Big Bang theory",
                    "Explain what the cosmic microwave background radiation is",
                    "Describe the current understanding of the age and fate of the universe"
                ],
                "techniques": ["Active Recall", "Feynman Technique"],
                "key_vocab": ["Big Bang", "red-shift", "blue-shift", "expanding universe", "cosmic microwave background", "Hubble", "dark matter", "dark energy"],
                "feynman_prompt": "Explain how scientists know the universe is expanding, using only the concept of red-shift. Then explain why this leads us to conclude there was a Big Bang.",
                "active_recall_questions": [
                    "What is red-shift and what does it tell us about galaxies?",
                    "Name two pieces of evidence for the Big Bang theory",
                    "What is the cosmic microwave background radiation?",
                    "Approximately how old is the universe according to current evidence?"
                ],
                "resources": [{"name": "BBC Bitesize", "url": "https://www.bbc.co.uk/bitesize/guides/zc7sb82/revision/3"}]
            },
        ]
    },
}

SR_INTERVALS = {0: 1, 1: 3, 2: 7, 3: 14, 4: 30, 5: 90}


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
    colors = ["#e74c3c","#f39c12","#27ae60","#8e44ad","#3498db","#16a085","#e67e22","#2c3e50"]
    for i, (unit_name, unit_data) in enumerate(PHYSICS_CURRICULUM.items()):
        lessons = unit_data["lessons"]
        completed = sum(1 for l in lessons if progress_data.get(l["id"], {}).get("status") == "completed")
        summary[unit_name] = {
            "title": unit_data["title"],
            "completed": completed,
            "total": len(lessons),
            "percent": round(completed / len(lessons) * 100) if lessons else 0,
            "color": colors[i % len(colors)],
            "level": unit_data["level"],
        }
    return summary
