# I saw the best devs of my generation destroyed by agents, prompting hysterical replaced

Some few dozen CTOs from NYC’s biggest and most technology focused companies recently gathered for a city-wide luncheon. They weren’t debating LLM architectures or which agentic framework was hottest this week. They definitely weren’t discussing model benchmarks or token economics. They were talking about headcount, hiring, and more quietly, AI-related existential questions asked out loud, such as, What does an engineer even do in 18 months, and how do you hire for that?

The room was full of people who’ve already made their AI bets. Teams running with Copilot, engineering orgs experimenting with agents, departments deep into pilots that were supposed to be in production longer ago than anyone cared to admit. The question has long since moved past how much AI to adopt. What was being asked is what adoption means for the shape of engineering itself, and how you staff for a future you can’t predict, on planning cycles that require you do so. 

Do you hire senior engineers with deep architectural intuition but slower adaptation curves to AI-augmented workflows? Do you hire junior engineers native to AI tooling but lacking the experience to evaluate what the model hands them? Do you upskill your existing team, and if so, in what? Context engineering? Agent orchestration? The subtle art of reading AI-generated code as if you’re deciphering a half-forgotten dialect? A very, very verbose dialect.

The market is undergoing a structural contradiction. The overall 240,000 tech worker reduction in 2024 contrasted sharply with the 119,000 jobs added by the broader U.S. economy. The purge included Alphabet (12,000+), Meta (10,000+), Amazon (15,000-30,000), Microsoft (5,000+), and Deloitte (1,200+) with 65,000 roles cut in the last documented month alone. Simultaneously, job listings for forward-deployed engineers surged 800% between January and September. This is the new reality: massive asset reduction alongside desperate, high-velocity hiring for AI integrators.

The Pitch: Companies like Cursor raise billions promising 40%+ productivity gains.

The Reality: Carnegie Mellon found that engineers (r=807) weren’t just writing less code; they were spending more time reviewing AI-generated code that arrived faster and worse.1

The Failure Rate: MIT Media Lab reported a 95% failure rate on enterprise generative AI pilots; and Atlassian showed 96% of enterprises seeing no real efficiency improvement.

The Workslop: Harvard Business Review showed that 40% of workers received AI-generated workslop last month, with each sample taking nearly two hours to fix.

The decks promised efficiency. Ground truth looks a lot more like cost relocation disguised as innovation. It’s a movie we’ve seen before, but such recognition is, tbf, somewhat unevenly distributed. This is an historical structural failure repeating itself. During the Desktop Publishing era (falling between object-oriented programming and cloud computing) PageMaker gave non-designers power without guardrails, resulting in the visually chaotic OG workslop of the 1992 church newsletter scourge (not to mention the curse of comic sans) Today, agents give non-architects power without guardrails, resulting in structural chaos as workslop goes multi-modal.

The decks promised efficiency. Ground truth looks a lot more like cost relocation disguised as innovation. It’s a movie we’ve seen before, but such recognition is somewhat unevenly distributed. This is an historical structural failure repeating itself. During the Desktop Publishing era (falling between object-oriented programming and cloud computing) PageMaker gave non-designers power without guardrails, resulting in the visually chaotic OG workslop of the 1992 church newsletter scourge (not to mention the curse of comic sans) Today, agents give non-architects power without guardrails, resulting in structural chaos as workslop goes multi-modal.

The big layoffs weren’t the result of AI replacing workers. They were the result of leadership not being able to justify headcount while uncertainty is compounding faster than quarterly reviews can track. The topic has moved past AI adoption to how the engineering substrate can support AI safely, and what’s needed to update current infrastructure to support this new complexity.  The question isn’t whether AI replaces developers. It’s how the infrastructure we’re building can support what happens when it tries, and whether we’re measuring what actually matters when we do.

Context & Background: What’s Actually Being Replaced

The Great AI Replacement isn’t happening the way the hype promised. AI isn’t replacing developers; it is replacing bad architecture.  

    The myth is alluring: AI will replace developers, maybe even engineers more broadly. Or in its most pernicious form, AI is a senior engineer you can delegate to. The reality is that AI is like a highly competent junior that’s bizarrely gifted with near-perfect recall and no basis for judgment. Successful teams understand this robo-junior who can move mountains if given the right guardrails; less able teams delegate to it like a senior and are rewarded with chaos.

Underneath all the hype, the  developer extinction extinction event is really an architectural revelation.🕊️ AI isn’t replacing developers; it’s revealing the architectural maturity of your codebase. Which organizations built their engineering substrate with intention, and which ones duct-taped microservices together and called it architecture. This is the part of the conversation that tends to be publicly demurred; high-performing teams care about code style not because they’re pedantic, but because style is the artifact of architecture.

We gave four different models the same bug. We didn’t get four implementations; we got four philosophies. One model overengineered the patch. Another duplicated state even though the canonical data source was right there. A third solved the right problem in a subtly incompatible way. The fourth nailed it, and then wiped the conversation context, nuking reproducibility.

Does the AI know your tombstone pattern? Your last-write-wins semantics? Your state transitions? Your service boundaries? The answer is: not unless you teach it. And teaching it requires the kind of architectural clarity most codebases simply don’t have.

AI isn’t replacing developers; it’s revealing the architectural maturity of your codebase.

The Magic Productivity Theater

The more the industry repeats “40% productivity gains,” the more it feels like a mantra meant to soothe investors rather than inform operators. (And operators mainly talk to investors through markets.) But the ground truth tells a different story, built on structural contradictions that lead to a single thesis: AI generates code quickly, but not code you can actually trust.

Carnegie Mellon’s findings (that AI shifts work from creation to tedious cleanup) are supported by every major survey. (MIT reporting 95% failure rate on enterprise AI pilots. Atlassian showing 96% of companies see no real efficiency gains.) Worse, METR found the cost of AI to experienced developers at 39%. This is why the workslop statistic is so damning: HBR’s “workslop” statistic seals the point: 40% of workers receive AI output that takes two hours to fix per sample which isn’t just productivity robbing Peter to pay Paul, it’s emotional labor disguised as automation.

Broken trust is felt through every layer of the stack; the rage developers feel debugging hallucinated refactors isn’t irrationality, it’s a reasonable response to being handed tedious, unnecessary cleanup work and being told it’s the future. Wasn’t this what Rossum’s robots were supposed to do for us? Wasn’t that literally the name coinage? 

Trust in theory isn’t about believing AI works any more than its about doing  drudgery. Rather, it was about having that done for you. Which in practice means trust is about having infrastructure that catches AI when it doesn’t. Think of it as the other side of Maybe Don’t: what if you have to? 

If you’re a regular reader, you know one answer to that: the AI-native SDLC flywheel built on zero-trust infrastructure. But most organizations haven’t built that. Instead, they delegated architectural trust, often to the model itself. (Holding out hope its API would enforce the constraints their codebases lacked.) But the magic isn’t in the model; it’s in the architectural guardrails and infrastructure constraints that high-leverage teams built before AI arrived:

Architectural Legibility: They enforce yype systems as guardrails rather than aesthetics  (Looking at you, Python) making the codebase legible to machines.

Agent Orchestration: They implement per-repo context engineering (Monorepos hate this one weird trick); encode style guides as system prompts; turn models into specialized, constrained agents.

Zero-Trust SDLC: They treat AI output like a junior’s PR, subjecting it to rigorous review and observable behavior (AI O11y 2.0).

This flips the equation. Once the substrate supports safe code generation, a single engineer with well-instrumented agents can handle work that previously required cross-team coordination.  Stack boundaries collapse. (Latencies drop!) Backend ops are pushed the edge. 10x teams are no longer the aspiration; 100x teams become possible. The ROI split is stark and revealing: While most companies see low or negative ROI; the top 5% see enormous gains. So what’s the magic? 

The teams in the top 5% aren’t smarter or luckier. They built their architecture to support AI before AI arrived. They enforced types. They documented patterns. They made their codebases legible to machines, which made them legible to humans, which made them maintainable at scale. Ok, so maybe they were smarter. The other 95% are learning a lesson in entropy, (that teacher of teachers) namely, you can’t retrofit clarity onto chaos. You can’t bolt AI onto a microservices architecture held together by institutional knowledge and hope it navigates service boundaries correctly. Call it Conway’s revenge. 

Meanwhile the industry is playing out the finale of Steppenwolf, the same desperate drama that consumed Harry Haller in his search for transcendence, finding only a theatre of smoke and mirrors. The applied magic isn’t in the model; it’s in the constraints. Successful teams built architectural guardrails before AI arrived. The industry keeps funding this performance, but when the curtain is pulled back it’s seen to be sustained by the smoke of those promised 40% gains and billion-dollar valuations, while the  mirrors are just reflecting the organization’s own undisciplined substrate, schema-less data paths, ad-hoc service boundaries, type-free interfaces, missing invariants, half-documented patterns, (/etc /etc) and a CI pipeline that treats validation as a suggestion. What looks like “AI productivity” is really your own architectural entropy being poured back into your lap at machine speed and the magic theatre of productivity only feels real until you realize the output isn’t creation at all it’s a funhouse reflection of the system you’ve decided to tolerate.

What CTOs Are Actually Measuring

The questions at the lunch table weren’t just about hiring (though headcount and vendor selection dominated the discussion.) The more salient question is measurement. How do you know if AI is working? Velocity, deployment frequency, and Lines of Code (LOC) were designed for humans writing code; not humans reviewing code that arrives pre-written and quite possibly wrong. 

The gap between perceived productivity and actual productivity is 39 percentage points. Teams feel 20% more productive with AI tools. Measurement shows they’re 19% slower. This is where the measurement question becomes architectural. If you cannot measure PR cycle time, deployment frequency, and change failure rate before and after AI adoption, every decision is guesswork wrapped in vibes. The intelligence flywheel only spins when measurement informs action. You need to know:

How much time is spent generating code vs reviewing code

How often AI-generated code passes review without changes

What types of bugs AI introduces that humans catch

Which architectural patterns AI handles safely vs which it mangles

Whether your experienced engineers are mentoring AI or just cleaning up after it

Only with this data can you actually optimize the system. The 5% who succeed are measuring what matters. The 95% who fail are measuring what’s easy. Andy Grove and Rich Hickey should probably have a fireside chat about this. 

Trust Gap: How often AI-generated code passes review without changes.

Workload Shift: How much time is spent generating code vs. reviewing code.

Pattern Safety: Which architectural patterns AI handles safely versus which it mangles.

The real replacement isn’t of engineers; it’s of the outdated measurement systems that reinforce chaos.

CTO Playbook: 30/60/90

Quarterly OKR:  Shift the engineering culture from mechanically using AI tools to structurally managing the risks associated with agent-generated complexity.

□ 30 day: Foundation Guardrails and Trust Controls

Codebase Legibility Score (CRITICAL):

Action: Audit critical repositories for “machine legibility”: scoring them based on type coverage and formalized state transition patterns.

Goal: Identify the most brittle areas where AI agents will introduce the highest “workslop.”

Encode Style as System Prompts (HIGH):

Action: Formalize style guides and architectural best practices (e.g., “no implicit state sharing”) and encode them directly into the system prompts for all developer-facing AI tools.

Goal: Instantly turn AI from a general code generator into a constrained, domain-aware junior developer.

Adopt “Junior PR” Review Policy (HIGH):

Action: Institute a formal policy that treats all AI-generated code blocks as if they came from a junior developer, requiring 100% human review.

Goal: Close the “broken trust” gap and shift the human workflow to critically auditing and maintaining the system’s structural integrity.

□ 60 day: Agent Orchestration and Measurement

Implement AI Observability (MEDIUM HIGH):

Action: Deploy decision-tracing instrumentation for all autonomous agents: capturing not just what code was written, but why the agent chose that architectural solution.

Goal: Provide the data needed for true root-cause analysis, fulfilling the AI O11y 2.0 mandate.

Establish Trust-Based Metrics (MEDIUM):

Action: Deprecate Lines of Code (LOC). Begin tracking AI-specific metrics: Review Pass Rate (how often AI output passes review without changes) and Change Failure Rate attributable to AI-introduced bugs.

Goal: Close the 39-point gap between perceived and actual productivity.

Upskill in Context Engineering (MEDIUM):

Action: Begin mandatory training for senior engineers on Context Engineering and Agent Orchestration.

Goal: Preserve senior architectural expertise by retraining them to enforce constraints and mentor the AI, rather than cleaning up its “workslop.”

□ 90 day: Structural Investment

Platform Engineering for Agentic SDLC (HIGH STRATEGY):

Action: Task the Platform Engineering team with building internal tools that provide safe, constrained deployment pathways exclusively for agent-generated code.

Goal: Ensure agentic code can move fast within established guardrails, without ever touching brittle manual paths.

Architectural Pattern Enforcement (MEDIUM STRATEGY):

Action: Invest in tools (static analysis, pre-commit hooks) that automatically enforce your architectural patterns and service boundaries, even if the code is AI-generated.

Goal: Make the codebase physically resistant to architectural drift, preventing the AI from introducing misconfigurations.

Hiring Profile Redefinition (MEDIUM STRATEGY):

Action: Redefine the engineering hiring profile: shifting emphasis from coding speed to architectural intuition, critical reasoning, and maintenance skills.

Goal: Hire for the skill that the AI cannot replicate: judgment.

Bottom Line

The Great AI Replacement isn’t happening the way the hype promised. Developers aren’t being replaced; they’re being asked to fix two hours of slop for every two hours of work. The real leverage isn’t automation. It’s augmentation with guardrails.

The best CTOs aren’t talking about “AI strategy”; they’re talking about people, processes, and the underlying architectural substrate that lets AI work safely instead of chaotically. They’re measuring what actually matters: trust, reproducibility, and the delta between what AI generates and what ships to production.

If your strategy is to delegate trust without first enforcing architectural constraints, you’re not building the future. You’re discovering that the infrastructure you built for humans doesn’t support agents; and retrofitting clarity onto chaos is expensive enough that you might as well rebuild from scratch. You are now experiencing the PageMaker Effect in code: structural chaos mirroring the visual chaos of the 1990s.

This illegible, unreadable codebase is, in fact, the ultimate Beached Asset: a massive capital expenditure (your engineering labor and tooling) that can never be fully operationalized by the agentic future, where the winners aren’t the earliest adopters but the ones who adopt with intention, rationalised architecture, and a sober understanding of what AI actually does. Ninety-five percent fail; five percent don’t. The best CTOs are in the five percent, by definition. 

To attend CTO Lunches, please register at ctolunches.com and choose NYC as your city.

Subscribe for free to receive monthly updates and support CTO Lunch NYC.




