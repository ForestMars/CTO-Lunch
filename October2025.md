CTO Lunch NYC
CTO Lunch NYC
CTO Lunch October 2025
Tech Roundup for CTOs: September-October by Forest Mars
CTO Lunch NYC and Forest Mars
Oct 08, 2025

This month’s CTO Lunch is Thursday, October 9th. Sign up (below) for location.

They say the days grow shorter when you reach September, not that anyone is leaving the office any earlier. In fact, teams are staying later than ever, driven by a combination of personal passion, downward pressure, and the unrelenting pace of technological acceleration. Smashing your WLB is one thing when you’re hot on the heels of ASI. It’s quite another to trade your life away building a slop machine for ad revenue. This month we got clarification as to which of them we’re actually skating to, and on thin ice at that (the solution to which everyone knows is to just skate faster.) CTOs want to know exactly what it is we’re tryna outpace, so we can de-risk it.

Turns out it’s not the models. OpenAI’s $13.5B six-month loss and pivot to ad infrastructure made that clear, as did watching Qwen’s 3B parameter one match frontier performance on hardware affordable enough for your average Twitch streamer. (Zero Theorem, LFG!) The underlying pressure is structural: development stacks reconfiguring around what autonomous agents need to operate safely, senior engineers slowing down because the pattern library for this hasn’t been built yet, and the gap between organizations executing and those still workshopping governance frameworks compounding faster than quarterly reviews can track. CTOs passionate about the HOW and the WHY driving all these factors met up in SF and Berlin respectively to understand the current inflection point, where it’s now time to ship the experiment, as AI has its Yoda moment: there is no longer any try, only do.

IN THIS ISSUE
It's Conference Szn
Model Behavior
Sloppy, She Said Sloppy
Is MCP an API for RAG?
AI-Native SDLC Flywheel
Web3 Watercooler

It’s Conference Szn
The final quarter of the year kicked off not just the Fall Conference Season, but a definitively leveraged resurgence in the U.S. tech sector, inaugurated by the White House Tech Dinner on September 4 (planned as the first official event in the newly renovated Rose Garden) and which served as a trillion-dollar spectacle focused on capital allocation for Tech and AI investment, with total pledges in AI infrastructure and manufacturing announced surpassing a somewhat staggering $1.4 Trillion by 2028. (That’s literally over 2 billion a month from now til then.)

Elon and Jensen both had other things to attend to, which was fine; there’s only so much energy you can fit in the room, leaving Zuck to grab the choice seat on the President’s right. (Poor Gates had to pass notes through Melania on his left.) There was also only one CTO in attendance at this “tech” dinner. (I’ll let you guess if he was from Palantir or Anduril.)

The White House dinner set the stage; the investment, the optics, the political theatre, all signaling the scale of what’s coming. But ofc the real work’s happening elsewhere. Engineering leaders are already grappling with the operational and organizational challenges of the AI-first era, to turn these abstract mandates into executable plans. Theis season’s top gatherings where this work is most visible and consequential were ELC Annual in San Francisco (at Fort Mason, so all the cool kids met up later at The Interval) and CTO Craft Con in Berlin. The core questions being debugged were remarkably consistent across continents: How do we actually scale our AI initiatives? What does non-performative governance look like? And why does integrating AI into our workflows so often make our most experienced engineers slower? (And not infrequently, grumpier?)

ELC Annual: Refactor Your AI Strategy Playbook
ELC Annual in San Francisco is the single highest-value summit for engineering leadership because it has zero interest in the low-signal clutter of traditional trade shows, for more of an 2-day executive work session intended to address the mission-critical issues CTOs are really dealing with day-to-day. It’s highly collaborative, with Roundtable Discussions and meticulously curated 1:1 meetings to ensure every connection is a strategic consultation. This highly focused model has cemented the event’s reputation for delivering actionable wisdom directly from those in the trenches, making it a mandatory professional investment for the top engineering leaders cohort. Somewhat surprisingly there didn’t seem to be many CTO Lunch list members in attendance, though it’s also a newish event, having only gotten off the ground a few years ago as an “unconference.”

This year’s theme, “AI Rewrote Leadership. Refactor Your Playbook,” acknowledged what’s happening across our industry: the AI experimental phase is over, but most organizations still have no idea how to execute at scale. The shift is as profound as the move to cloud computing, except it’s happening faster and the architectural implications go even deeper. For the past 18 months, CTOs have been running pilots, experimenting with agents, and watching our teams use ChatGPT and Claude in ways that violate approximately every security policy ever written. Executive stakeholders have been patient, remarkably patient by C-suite standards, waiting for productivity gains to materialize beyond anecdotal, and not always true, “my team loves it” reports. Now the bill is coming due. Past due, if you ask your CFO, who wants ROI numbers from last quarter. Boards want strategic frameworks. And everyone is learning together that bolting AI onto existing architectures is like trying to run Kubernetes on a LAMP stack: technically possible (no, it really is) but catastrophically wrong.

The (un)conference crystallized around three pillars of “AI Native Leadership” that you can think of more or less as diagnostic criteria for whether your engineering org is about to get lapped. First, architectural simplicity in the age of agentic complexity (code for: your microservices spaghetti, I mean architecture, is about to look adorably quaint); Second, scaling innovation through internal competition, matryoshka-style, (“startups within startups”) where governance is the actual bottleneck, not because anyone cares about ethics theater, but because it’s the real constraint preventing deployment; and Third, resource-conscious leadership, which sounds like the same old “do more with less” mantra until you realize that AI-driven teams require organizational and cultural reconfiguration, sophisticated measurement frameworks, and it’s effectively blurring the lines between engineering, product, and business.

It sounds obvious out of context but what’s truly fundamental is the shift in developer experience. The cloud-native era was about CI/CD automation and platform adoption, getting developers to use the tools we built. Similarly, the agentic AI era is about AI-integrated DX except we haven’t yet built the tools we want them to be using. This is where platform engineering teams need to “own the loop” by integrating seamless AI assistance that minimizes cognitive load while ensuring high-quality outputs. Data architecture has transformed from relational databases and data lakes into vector databases, hybrid search, and RAG loops where contextual knowledge becomes a critical, performance-gated infra layer. That’s a lot to unpack before we even start pushing it out not just to our ENG teams, but cross-functionally across the whole org.

AI can easily exacerbate the already tight bottlenecks in such collaboration, particularly in the design-to-code handoff where product & engineering collide in Storybook or whatever reconciliation loop you’re using to curtail the chaos. Instead of accelerating workflow, AI assistance often slows down experienced team members while helping junior developers catch up somewhat, three steps forward, two steps back. Or is that two steps forward, three steps back? This difference comes down to critical decisions CTOs are making under such high pressure. This pattern keeps showing up in studies, leading to odd conversations about team composition and the need for senior engineering expertise in an AI-assisted world. Meanwhile, the infrastructure requirements aren’t subtle: vector databases have moved from experimental to mandatory, RAG architectures are table stakes (esp. for avoiding hallucinated compliance violations) and the orchestration layer for managing autonomous agents requires rethinking the entire SDLC. The cloud-native era’s primary risks were supply chain integrity and dreaded configuration drift; the agentic era’s risks remind us that we palliated those concerns more than we actually solved them, requiring newly Agentic DevSecOps (a popular buzzword at ELC) methodologies to be rebuilt almost from scratch.

ELC 2025 marked the point where our AI strategies finally got operational. Every conversation was about execution: which architectures hold up under load, which governance models survive contact with reality, what teams that are actually shipping know that you don’t. The signal was clear: the next phase belongs to leaders who can translate architectural clarity into organizational momentum, those who know HOW, because the experimentation window is closing fast.

CTO Craft is where European tech leadership cohort goes to admit what’s actually broken.

CTO Craft Con: Why Your AI Strategy is Culturally Invalid
If ELC Annual was about the tactical and architectural translation of AI strategy, CTO Craft Con in Berlin was the essential counterpoint, focusing squarely on the organizational and cultural re-engineering required to survive the transition. Held (September 23–24) at the Spielfeld Digital Hub in Kreuzberg, which has become a hub for tech startups and creatives (as well as the world’s best vegan doner kabab.) Unlike the Valley’s performance optimism, Berlin’s engineering culture has always trafficked in a certain, dare I say German, pessimism and this year’s iteration distilled this sensibility into a two-day diagnostic of what happens when you try to run an AI-first org in what’s being called the permacrisis of economic volatility, geopolitical chaos, and the persistent sense that whatever stability you thought you had, has now became a liability smh.

The central thesis wasn’t subtle: technology is cultural, and CTOs who don’t understand this are managing the wrong variables. I had a COO who used to joke that I was also the Chief Cultural Officer, and there’s a deeper reason for that than my perceived erudition. As Don Ihde pointed out in his writings on technological mediation, technology doesn’t just solve problems, it reshapes the organizational context in which those problems exist. GenAI acceleration make this explicit. You can’t bolt AI onto a low-trust culture and expect anything much more than expensive theater. You can’t mandate platform engineering adoption without first cultivating what the conference called “Challenger Safety,” the organizational capacity to question architectural decisions without triggering defensive bureaucracy or political retaliation. Which just leads to attrition of your best people.

The burnout data is supported with concrete numbers: 41% of engineering leaders are actively considering leaving their roles, and the reasons track directly to the structural contradictions the conference spent both days unpacking. Execs upstairs want transformative AI deployment but won’t fund the technical debt remediation required to make it viable. Boards want platform-driven operational efficiency but still measure success through headcount growth. Everyone wants innovation, but the organizational maturity required to sustain it, verifiable processes, genuine psychological safety and architectural clarity, remains aspirational for most. Startups have an odd advantage here: they lack legacy inertia to unwind, so they can mature faster, sort of like how people used to look older at the same age. But that only works if they’re intentional about building the right cultural scaffolding from the start, which most aren’t. (ca. OpenAI’s DevDay announcement they want to be basically Roundup for startups.)

Technical re-engagement as a mandate emerged as the conference’s sharpest diagnostic. The archetype of the CTO as pure people manager, the one who “graduated” from hands-on work years ago, is failing catastrophically in the agentic era. You cannot architect for AI scale-up from 30,000 feet. You cannot evaluate RAG pipelines, vector database performance, or agent orchestration frameworks through executive summaries. The complexity is too high, the pace too fast, and the gap between what vendors promise and what actually ships is too wide. Permacrisis has become a driver of what some are calling the builder-founder revolution: technical leaders who can still ship are suddenly worth exponentially more than those who can only delegate, and the market is repricing accordingly.

Platform engineering became the conference’s organizing principle for making this concrete. Not platform engineering as aspirational excellence, which is an organizational smell that you’re optimizing the wrong layer, but platform engineering as operational reality. Can your platform team actually reduce cognitive load for developers integrating AI tooling? Have you built the feedback loops that let you measure whether your abstractions help or hurt? (cf. DX, following) Are you owning the loop, or just adding more process overhead to an already fragmented developer experience? The questions were sharper than the answers, which was the point. Like the inflection from experimentation to execution highlighted at ELC, this isn’t solved yet, but at least the European cohort is asking the right questions rather than presuming the answers are obvious.

The permacrisis framing cuts deeper than economic uncertainty. It’s fundamentally about the erosion of trust. High-trust organizational culture isn’t a nice-to-have anymore; it’s the only environment where technical leaders can make the kind of rapid, high-stakes decisions that AI deployment requires. High trust culture meets zero-trust architecture.

TL;DR Action Items (30/60/90)
The convergence of insights from ELC Annual and CTO Craft Con reveals a brutal truth: the experimental phase is over, but most organizations lack both the architectural substrate and cultural capacity to execute at scale. ELC made the technical requirements explicit: refactor architecture for agentic systems immediately, allocate protected time for cultural reskilling; move governance away from shallow activity metrics toward outcome-focused frameworks. (cf. AI Impact Framework or QuADS that link AI-amplified throughput to strategic business objectives and justify the CapEx to the board.) Success requires architectural foundations, talent reskilling, team restructuring, and outcome-based governance. CTO Craft made the organizational requirements unavoidable: you cannot bolt AI onto low-trust cultures and expect anything beyond expensive performance art. It’s WHY nearly half of engineering leaders are ready to walk given an incrementally better offer.

The organizations treating AI as incremental tooling are falling behind those treating it as architectural transformation.

The action items below aren’t recommendations; they’re prerequisites for survival in an environment where AI deployment velocity is becoming the primary competitive differentiator.

The ‘Why’ (Cultural Foundation)
Mandate Challenger Safety: 30 days. Lacking the organizational capacity to question AI outputs and architectural decisions without triggering defensive bureaucracy, technical governance is theater. Implement concrete mechanisms: dedicate sprint planning time to “challenge the assumptions,” create explicit channels for dissent, and publicly reward engineers who catch AI-generated bugs before production. If senior engineers aren’t routinely questioning AI outputs, you either lack Challenger Safety or lack senior engineers.

Protected Reskilling Time: 60 days. AI access is not AI ability. Early success with GenAI masks shallow understanding, and superficial AI fluency creates false confidence that ships broken code to production. Mandate 4 hours per week of structured, protected learning where engineers build genuine proficiency with AI-augmented workflows—no meetings, no interruptions, no exceptions. (You can add this to meeting-free-Wednesdays if you already implement WEM.) Measure competency, not completion. The 41% burnout rate isn’t from lack of training—it’s from being asked to deliver AI transformation without time to develop actual skill.

Technical Re-Engagement Mandate: 90 days. You cannot architect for agentic scale from 30,000 feet. The CTO-as-pure-people-manager archetype is failing catastrophically in the agentic era. You cannot evaluate RAG pipelines, vector database performance, or agent orchestration through executive summaries. If you haven’t personally instrumented a RAG pipeline or debugged a multi-agent workflow in the last 90 days, you’re managing the wrong variables. Allocate 20% of your time to hands-on technical work—code reviews, architecture spikes, infrastructure debugging. The builder-founder revolution is repricing technical leaders who can still ship.

The “How” (Execution Mechanics)
Deploy Measurement Infrastructure: 30 days. The gap between perceived productivity (+20%) and actual productivity (-19%) for AI tools is 39 percentage points. If you cannot measure PR cycle time, deployment frequency, and change failure rate before and after AI adoption, every decision is guesswork. Implement developer intelligence tooling (DX, Jellyfish, Haystack) immediately to capture baseline metrics before expanding AI tool deployment. The intelligence flywheel only spins when measurement informs action and RTO is irrelevant.

Refactor for Agentic Simplicity: 60 days. Your microservices architecture was built for humans orchestrating services. Agentic systems require fundamentally different patterns: fewer boundaries, more composability, orchestration layers that AI agents can reason about. Audit one critical service against this question: “Can an AI agent understand this well enough to modify it safely?” Start with one service, simplify the architecture, and document (with types all the way down.)

Outcome-Based Governance Frameworks: 90 days. Move governance from shallow activity metrics (velocity, deployment frequency) to outcome-focused frameworks that link AI-amplified throughput to strategic business objectives: Time to Value, Adoption Rate, Customer Retention Cost. AI agents excel at producing output; humans still own defining valuable outcomes. Start quarterly outcome reviews where teams justify investment based on customer impact, not feature delivery. Present AI Impact reports to executive leadership that translate engineering metrics into business outcomes the CFO can actually use.

Bottom Line
The era of merely experimenting with large language models is over. The immediate and non-negotiable shift is from a service-oriented architecture (SOA) to an Agentic Operating Model. The central engineering challenge is no longer about API composition, but about creating robust, observable, and governable environments for autonomous agents to execute on behalf of the business.

This architectural shift carries a dual, urgent mandate for the CTO. ELC provided the HOW: the refactoring playbook for enabling vector infrastructure and agentic DevEx loops. CTO Craft Con, however, delivered the true strategic bottleneck: WHY technical scale is impossible without a culture built on high trust and Challenger Safety. The only path to high impact execution runs directly through a re-engineered engineering culture. And we all know WHO is responsible for that.

The AI Rloveution
Model Behavior
September’s models arrived as a torrent of leaves carried on the winds of Fall. They covered every sidewalk, piled up across lawns, and spilled into the streets so high demanding someone get out there and rake them all up. Claude 4.5 (9/12) solved a million-dollar problem you didn’t know you had. GPT-5 Codex (9/23) can run for seven hours straight without supervision (longer than many of your devs, tbh.) Gemini 3.0 Pro (preview, 9/18) was released to select users. And Qwen3-VL (9/25) matched the performance of GPT-5 Mini and Claude 4 with just 3B active parameters, proving that the “bigger is better” narrative was always more marketing than math.

The real story isn’t in the model releases themselves but in what’s happening around them. Mira Murati left OpenAI and founded Thinking Machines Lab, wisely choosing not to build another foundation model but instead launching Tinker, a cloud API that lets you write training loops locally while handling its distributed infrastructure. Picks and shovels, to be sure, but for an arms race, not a gold rush.

Context and Background
The foundation model oligopoly is cracking. What’s next is the Great Unbundling, where value is shifting from who trains the best model to who invents the tooling that makes them seriously useful. For two years, CTOs have been held hostage to API pricing, rate limits, and the whims of a handful of labs. That era is ending, not because the big labs are failing but because the economics of AI are fundamentally restructuring around three parallel trends: model commoditization, infrastructure democratization, and tooling maturation.

Claude 4.5 arrived this month, emphasizing operational capability: its server-side container access is the kind of infrastructure change that sounds boring until you realize it eliminates an entire class of security objections. Claude can now execute code in isolated containers on Anthropic’s infrastructure, meaning you can give it database access, API credentials, and system-level capabilities without the security nightmare of exposing those to a conversational interface. This is why Agentic AI is lowkey speedrunning the cloud computing migration. It’s also how you go from “AI assistant” to “AI operator” without getting fired when the audit comes. Or LYDM.

GPT-5-Codex is OpenAI’s best shot at agentic coding, and its 7 hours may be enough for bounded workflows but it’s nowhere close to infrastructure-grade stamina or Claude 4.5’s 30-hour operational window. And unlike Claude 4.5, it lacks any built-in ability to plan or reorganize codebases across modules. This makes it a capable executor for discrete tasks but not yet the backbone of an AI-native development pipeline.

Qwen3-VL-30B-A3B-Instruct is where the commoditization thesis becomes undeniable. With just 3B active parameters (in a sparse mixture-of-experts architecture), it’s matching GPT-5-Mini and Claude 4 on reasoning tasks while being small enough to run on a single H100. The full 30B parameter model has thinking capabilities that rival frontier models, but the real story is the 3B active version: enterprise-grade performance at gaming-GPU scale. Chinese labs are shipping models that can match your $200K/year API spend on hardware you could buy off Newegg. At this rate we’ll soon be running SLMs on a disposable vape.

And then there’s Gemini 3.0 Pro, which Google is somehow positioning as both a reasoning breakthrough and a cost-effective alternative. Early tests show genuine improvements in multi-step logical reasoning, ok, but the real question is whether Google can overcome the organizational dysfunction that’s plagued every Gemini launch. (Narrator voice: they probably can’t.) Still, the fact that Google is even in the conversation signals something important: the model quality floor is rising so fast that even Google’s execution challenges can’t keep them out of enterprise consideration.

As model quality converges and diverges simultaneously, with Qwen proving cost efficiency, Gemini showing even laggards can compete, and Claude & GPT-5-Codex splitting on operational patterns, Microsoft added Claude Sonnet and Opus 4.1 (still topping the ASCII benchmark board) to Copilot Studio for building custom enterprise agents and to its Researcher agent for deep, multi-step analysis. OpenAI still powers standard Office productivity tasks; Claude can now handle the complex reasoning workflows that enterprises build through Copilot Studio’s developer platform. So the company with the largest financial stake in OpenAI just threw down with Anthropic, giving every CTO’s multi-model strategy board-level cover. You can now route tasks across OpenAI, Anthropic, and Azure Model Catalog options within the same multi-agent system, treating model selection as an operational choice rather than a procurement commitment. (Your board still wants a framework, btw.)

Multi-model orchestration creates the conditions for something more radical at the infrastructure level: llm-intercept is a fully functional PyPI package that turns expensive LLM API calls into free, self-hosted models. It’s not a hack or a wrapper; it’s a systematic interception layer that routes your existing API calls to local models with minimal code changes. In addition to the substantial cost savings, the technical achievement here is a death knell for API lock-in as a sustainable moat. You can transparently swap Claude API calls for local Llama models without rewriting application code. Vendor switching costs approach zero. Tinker completes the other side of the equation: once you’ve collected training data through llm-intercept, Tinker makes fine-tuning accessible at $2/GPU-hour with orchestration handled, turning what used to require an ML platform team into a hackday project.

Technical Specs
Claude 4.5: 200K context, server-side container execution (gVisor isolation); $3/M input/$15/M output tokens; 22% latency reduction vs Claude 4

Qwen3-VL-30B-A3B-Instruct: 30B total params (3B active per inference via MoE), 32K context, matches GPT-5-Mini on MMLU-Pro (81.3%), Apache 2.0 license, runs on single H100 (24GB VRAM), separate Thinking mode for chain-of-thought

Gemini 3.0 Pro: 2M context window maintained, 35% improvement on MATH benchmark vs Gemini 2.5, $3.75/M input/$15/M output tokens (25% cost reduction), early access shows GPT-5 parity on MMLU-Pro

GPT-5-Codex: 7+ hour autonomous operation with no intervention, 128K context, no planning mode (reactive execution only), 89.2% HumanEval pass@1, $2.50/M input/$10/M output tokens

Microsoft Copilot Multi-Model: Claude Sonnet 4 and Opus 4.1 available in Copilot Studio for custom agent development and Researcher agent for deep research tasks; dynamic model selection across OpenAI, Anthropic, and Azure Model Catalog; opt-in access through Microsoft 365 admin center

Thinking Machines Lab Tinker: Cloud API for distributed training, $2/GPU-hour (50% reduction vs raw compute), handles automatic checkpointing and distributed coordination, supports 7B-70B model fine-tuning

llm-intercept: PyPI package enabling transparent model switching; routes API calls to local models with minimal code changes; collects training data from production traffic; compatibility layer for Claude/OpenAI/local model interchange

Industry Impact
The foundation model oligopoly is fracturing, which is having the effect of restructuring the entire value chain. Model selection needs to be task-dependent, not vendor-dependent. The idea that you’d standardize on a single model provider made sense two years ago with two viable options and massive quality gaps. With no less than six credible frontier models (GPT-5, Claude 4.5, Gemini 3.0, Llama 4, Mistral Large 3, Qwen3-VL) and a growing bench of others, multi-model architecture is the only rational strategy.

The commoditization of reasoning capabilities through models like Qwen3-VL creates a new cost structure dilemma for OpenAI and Anthropic. A 3B model matching your current $75/M token API on reasoning tasks means model quality is no longer a moat. The focus shifts to integration depth and trust relationships. Everyone talks about productization, but it’s not the model that’s being productized, it’s the operational envelope around it. Mira Murati had direct visibility into OpenAI’s model development roadmap and chose to build training infrastructure instead of another model. Prescient, but still, “what did Ilya see"?” has not been answered, even if he does now have his own line of swag.

llm-intercept is the opening salvo in transparent model arbitrage. Today it’s a PyPI package. Tomorrow it’s middleware in your API gateway. Next quarter it’s baked into LangChain (ugh, I know) and every agent framework. The tandem of llm-intercept and Tinker dismantles lab pricing power from both sides: intercept routes requests to the cheapest adequate model while Tinker reduces fine-tuning from an expensive ML platform project to a trivial $2/GPU-hour orchestration task. This hits a market already flooded by cost-effective competitors like DeepSeek’s GLM-4.5, crushing it for coding at a fraction of Claude’s cost with superior reliability. Model switching transparent to application code plus operationally trivial customization equals evaporating pricing power. The labs can see this coming, which explains the sudden rush to add stickiness beyond pure model quality

Sloppy, She Said Sloppy
Remember when OpenAI needed $7 trillion and 10GW of power to cure cancer? Yeah, so does Pepperidge Farm. Now they’re launching AI slop videos marketed as personalized ads. The trajectory from “we’re building superintelligence to solve humanity’s grand challenges” to “we’re Canva with worse margins” happened so fast it gave the entire industry whiplash. This month’s calvalcade of product releases from OpenAI, including Pulse (morning news, except it’s ads), GPT-Stripe integration (monetization infrastructure finally), and Sora 2 (the infinite video slop machine) mark the definitive point they stopped pretending they’re solving hard problems and started admitting they’re just another attention merchant with a better pitch deck and an insane burn rate. (And a killer engineering team, it must be said.)

Context and Background
OpenAI pulled in $3.5 billion in revenue against $5.3 billion in losses in 2024. First half of 2025? $4.3 billion in income, $13.5 billion in loss. They’re paying AI cloud service providers nearly three times what they collect from AI users. With unit economics that broken, they’ve noticeably stopped talking about AGI curing cancer and built an ad platform, hoping no one calls them out on the $7 Trillion Slop Machine Pivot.

Enter Fidji Simo, OpenAI’s freshly minted “CEO of Applications,” whose LinkedIn trajectory (Meta → Instacart → OpenAI) has little to do with AGI, more like “how do we monetize engagement at scale?” (For companies with upside-down financials.) No shade. Her first major product launch was Pulse, ChatGPT’s morning news feature that OpenAI is carefully not calling an ad product, despite it very obviously being, an ad product. It’s the kind of semantic game that works until it doesn’t, which is most likely just how long it takes for users to realize their AI assistant is now serving them sponsored content alongside their morning coffee. We probably need a better word than enshittification, though it got thrown around a lot in the wake of the Sora 2 launch, where the promotional reel conspicuously omitted anything resembling gymnastics. Instead, we got brand-safe b-roll optimized for buy-side advertising and waaay too much of Sama. Sora isn’t the filmmaking revolution we were promised. At best, it’s a content mill for marketing teams who need 44 variations of the same product shot and don’t want to pay a production company. At worst, it’s a TikTok competitor. As more than a few people noted, we were promised superintelligence and got an infinite AI video slop machine. One that OpenAI now charges $200 a month for the privilege of using.

GPT-Stripe integration is where the mask fully slips. It’s brilliant infrastructure work, again they have an incredible engineering team (led by Sulman Choudhry, who spoke at ELC) with truly elegant API design that makes payment processing native to conversational AI. But it’s also the clearest signal yet that OpenAI has fully committed to the “turn models into apps” playbook: Chat (conversational interface), Codex (developer tools), Sora (video generation), and now Stripe integration to monetize all of it. This isn’t the roadmap of a company building AGI. This is the roadmap of a company desperately trying to close a $9 billion annual loss gap by becoming a payments processor that happens to use AI.

OpenAI also spent a cool $15 million acquiring chat.com (last November) because when you’re losing $13.5 billion in six months, what you really need is a premium domain name. The symbolism is almost too perfect: a company that started with a mission to ensure AGI benefits all of humanity is now optimizing for SEO and brand recall like it’s 2011 and they’re pivoting to mobile-first social commerce. Mo’ So LoCo. But yeah, grandparents everywhere will likely be “asking chat” for answers to all their questions. Finally, there’s the Databricks partnership, making OpenAI models natively available within the Databricks Data Intelligence Platform and Agent Bricks; it’s the one move that makes non-slop machine sense, though you’d be forgiven for thinking that OpenAI is increasingly positioning themselves as more of a vendor than an actual platform, if not for DevDay.

The shoe didn’t just drop at DevDay, they dropped an entire shoe store this year, making the shift explicit: OpenAI has doubled down on products, not long-context models. Turns out science doesn’t really pay the bills. The event was a blueprint for making ChatGPT the default interface for everything; “you can now chat with apps in ChatGPT” collapsing user workflows into a walled garden rather than teaching models to use external apps through a browser. They shipped Apps SDK to build native apps inside ChatGPT, ChatKit for embeddable/customizable chat UIs, and AgentKit, a full agentic workflow suite that functions like a baked-in n8n: a drag-and-drop Agent Builder, WYSIWYG workflow canvas, guardrails for inputs/outputs, and Evals for dataset/trace grading and auto-prompt optimization. They also pushed more powerful Codex tooling and announced Sora 2 and GPT-5-Pro in the API. Much to the disappointment of many devs there for better models, the message was not “we’re giving you longer context,” it was “we’re giving you richer product hooks inside ChatGPT.” In short, ChatGPT-as-OS is the strategic bet: your Spotify, Zillow, Coursera, all native in ChatGPT, so people spend their time there and all transactions, content slots, and experiences flow through OpenAI’s consumer control surface.

For developers at DevDay who showed up for models, not productization, who came expecting large-context engineering, and model capabilities, what they got instead was a C-suite playbook of apps, SDKs, and monetization primitives, the sort of productization that makes CFOs and marketing teams clap. Whether or not OpenAI’s product strategy is solid (and it kinda is, *if* you ignore the burn rate) and whether or not their engineering team continues to deliver (yeah they do), the event landed as a love letter to executives, not builders. There’s also a sour note about leadership: the company’s culture and management have been criticized internally which further killed the vibe for engineers expecting a model-first technical summit. If you were at DevDay hoping for deep model-level breakthroughs, you left annoyed. If you were a C-suite exec, you left with a checklist.

Technical Specs
H1 Financials: $4.3 B Revenue vs. $13.5 B Net Loss (314% loss-to-revenue ratio); CAPEX driven primarily by $8.2 B in Azure Compute COGS.

GPT-Stripe Integration: Native API-level custom function-calls (Stripe::PaymentIntent.create) supporting one-time and SaaS logic; P2P marketplace enablement via Stripe Connect at standard 2.9%+$0.30 transactional rates.

GPT‑5 Pro: Flagship model offering faster latency, improved reasoning chain consistency, and full compatibility with AgentKit and Apps SDK ecosystem; context window capped at 32k (permanently disappointing developers hoping for long‑context breakthroughs).

AgentKit: OpenAI’s agentic workflow framework for building, deploying, and optimizing LLM agents. Includes Guardrails (input/output safety), Agent Builder (WYSIWYG workflow canvas), and Evals (auto‑prompt grading datasets). Early access to runtime telemetry for trace‑level inspection.

ChatKit: Embeddable, customizable ChatGPT‑style UI component framework for third‑party developers. Supports multi‑session state management, theming, and contextual handoffs to AgentKit workflows.

Apps SDK: Full stack tooling for building native apps inside ChatGPT. Enables direct integration of partner services (Spotify, Zillow, Coursera, etc.) within the ChatGPT interface. Marks the pivot from model access to app ecosystem.

Agent Builder: Drag‑and‑drop visual interface for constructing AI workflows in minutes; integrated deployment to ChatGPT apps with evaluation pipelines via Evals.

Evals 2.0: Expanded dataset support for LLM behavioral testing and auto‑prompt optimization with trace grading and multi‑metric dashboards.

Databricks Integration: LLM access (GPT-5, Codex) via private, low-latency Agent Bricks API; enables secure multi-model orchestration within Unity Catalog/Lakehouse enterprise architecture.

Industry Impact
OpenAI’s DevDay sent a clear signal: the dominant AI vendor is pivoting from selling models to selling interfaces, transactions, and distribution. That matters because infrastructure markets don’t just shape engineering choices; they reprice business models, procurement flows, and competitive moats.

First-order effects for enterprises: OpenAI-as-OS lowers integration friction for services that accept being embedded. If your product maps cleanly into a ChatGPT app model (payment flows, short-form content, conversational commerce), you get a distribution channel with instant reach. Databricks integration accelerates internal adoption by collapsing model + data + orchestration into the enterprise stack. That reduces time-to-value for teams who want turnkey LLM capabilities. But convenience has a cost: embedding into ChatGPT’s ecosystem means surrendering control over UX, data residency, pricing, and upgrade paths. For enterprise procurement, this shifts negotiations from model SLAs to platform terms; data portability, portability of stateful agent workflows, and exit clauses become the new redlines.

Second-order effects for product and engineering teams: the economics of building on top of models changes. Instead of competing on model quality alone, vendors now compete on app hooks, payment rails, and UX frameworks. Developers must decide whether to chase distribution inside a dominant interface or double down on open stacks and long-term portability. The MCP domestication problem is central here: a protocol originally intended to avoid vendor lock-in is now a compatibility shim for one vendor’s app economy. That means the rational short-term play for many engineering teams is to adopt OpenAI’s SDKs for speed; the rational long-term play is to abstract those integrations behind your own platform layer to avoid unilateral lock-in.

Third-order effects for the market and incumbents: expect a renewed consolidation wave around interface owners. Companies that control high-frequency user surfaces (chat, search, inbox) will become distribution monopolists. OpenAI’s play is a textbook platform-bite: make the interface sticky, monetize via content and payments, and become the default runtime for third-party apps. Traditional SaaS vendors should reassess whether they are a feature inside a more powerful app or whether they retain the ability to be the destination. Not to mention the IP quagmire this invites.

Is MCP an API for RAG?
No, but Pepperidge Farm remembers when that wasn’t even the question.

When Anthropic announced the Model Context Protocol last November, the pitch was compelling: an open standard that would let AI assistants connect to any data source, any tool, any API. No vendor lock-in. No proprietary integration layers. Just clean, standards-based interoperable infrastructure that would let developers build once and deploy everywhere. The engineering dream: never write glue code again. MCP servers would become the universal AI adapter layer. “HTTP for the LLM era” it was even called (as well as “USB-C for AI”)

What we got instead was a year of everyone building the same thing: wrappers around vector databases that expose search endpoints. RAG servers with MCP labels and some functions sprinkled on top. The protocol supported arbitrary tool definitions and rich interaction patterns, but nobody wanted to do the work. Easier to slap an MCP interface on your existing retrieval pipeline and call it a day. The “open standard” became a lowest-common-denominator race to ship the minimum viable implementation. Or ship a crippleware version and gate actually useful functionality behind a paywall. (Notion could not be reached for comment.)

Then came September 10th, when OpenAI finally announced MCP support in ChatGPT. Developer mode only, naturally. Or actually on September 9th, when they originally announced it, then deleted everything (!) then re-announced the next day. Because profesh. But the real kicker was that their “MCP support” only works if your server implements search and fetch tools to OpenAI’s exact specifications. In other words, if your MCP server is basically a RAG server. They mumbled something about this only being the first step. Where have we heard that before?

If you built MCP servers expecting OpenAI to honor the standard, congrats, you now maintain two parallel implementations: the MCP version for Claude & the OpenAI-specific version for GPT.

And then came DevDay. On October 6th, OpenAI dropped the other shoe. (As noted, it was more like an entire shoe store.) Their Real-Time API v2 now supports tool integration with sub-100ms latency and streaming function results. Except it’s OpenAI’s own proprietary tool protocol, not OG MCP. They literally had the opportunity to make MCP the standard for real-time agent interactions and instead built yet another vendor-specific integration layer. Can’t blame them for being greedy.

The structured outputs announcement is more devastating: OpenAI now guarantees that tool calls will match your JSON schema exactly, with zero hallucination in the structure. Massive for production reliability, except it only works with OpenAI’s tool definition format. If you built MCP servers expecting OpenAI to honor the standard, congrats, you now maintain two parallel implementations: the MCP version for Claude and the OpenAI-specific version for GPT.

The timing is almost comedic. Anthropic spent a year evangelizing MCP as the universal standard. The community built hundreds of servers. And OpenAI showed up to DevDay essentially saying: “Cool protocol, bro. We’ll support the retrieval parts when we feel like it, but for everything that actually matters (real-time voice interactions, guaranteed structured outputs) you’re using our stack.”

What This Means for CTOs
The calculus is brutal: MCP gives you portability with degraded performance. OpenAI’s Real-Time API v2 and structured outputs are legitimately better (lower latency, guaranteed schema compliance, better error handling) but lock you into their ecosystem. If you bet on MCP as your universal integration layer, you’re now writing the same glue code not two, but three times: once for MCP, once for OpenAI’s Real-Time API, and once for whatever Google announces next quarter.

The tragedy is this was avoidable. MCP is technically capable. But when the largest player in the market ships proprietary alternatives that work better and ship faster, standards lose. OpenAI has zero incentive to make MCP succeed when they can build better tools that keep customers in their ecosystem. It’s yet another cautionary tale about how open protocols fail not through technical flaws, but through lack of incentive alignment.

Technical Specs
OpenAI Real-Time API v2: Sub-100ms tool call latency; streaming function results; WebSocket-based; proprietary tool protocol (not MCP-compatible)

Structured Outputs for Tools: JSON schema enforcement with zero hallucination; works only with OpenAI’s function calling format

MCP “Support” in ChatGPT: Limited to search/fetch operations; requires OpenAI-specific tool naming; Developer Mode only; full protocol support: “eventually, trust us”

Integration Tax: 2-3 parallel implementations per tool (MCP for Claude, OpenAI format for GPT, native for everything else)

TL;DR Action Items
Platform Portability – HIGH PRIORITY (30 days): Abstract MCP, AgentKit, and OpenAI integrations behind vendor-neutral orchestration. Build explicit migration paths. You’re already writing glue code three times so make it count.

Multi-Model Orchestration – MEDIUM PRIORITY (60 days): Route by cost-performance tier. Benchmark per use case. Plan dynamic switching as new models drop.

Interface Governance – LOW PRIORITY (90 days): Audit integrations for data egress. Require internal API façades. Treat AI platforms as distribution surfaces, not infrastructure dependencies.

Bottom Line
CTOs, treat the convergence of model releases, agentic tooling, and productized AI platforms as an immediate operational imperative. Prioritize rapid experimentation with multi-model orchestration, secure agentic infrastructure, and integrated app interfaces, while maintaining developer culture and financial discipline. The key is building adaptable systems that extract real business value from the accelerating pace of AI productization. You can tell your board I said so.

AI-Native SDLC Flywheel
TanStack Start ships with runtime type validation. Node adds SQLite as core functionality. Hugging Face lets you import transformer models like lodash. These look like unrelated product launches, but they’re all responses to the same tectonic shift: our entire development stack is restructuring around what AI agents need to operate safely at scale.

Types aren’t about code quality anymore. They’re the load-bearing infrastructure that makes autonomous code generation safe enough to trust.

Six months ago, autonomous AI refactoring was professional malpractice. Agents hallucinated APIs, broke type contracts, and generated code that compiled but exploded at runtime. Now we’re racing to execute because we’ve reached critical maturity in two areas: collapsing knowledge contexts and feedback loops, and achieving type safety across the entire stack. Types aren’t about code quality anymore. They’re the load-bearing infrastructure that makes autonomous code generation safe enough to trust. Once types provide safety rails, the work that used to require coordinating between teams can be done by a single person with AI doing the heavy lifting. Database management moves into the browser. ML models become npm packages. The handoffs that used to define team structures evaporate because our new architecture makes them unnecessary.

This creates a flywheel effect. Types make AI agents safe. Safe AI agents enable smaller teams. Smaller teams need fewer handoffs. Fewer handoffs allow for more uniform substrate. (This is literally Conway’s law.) Better substrate enables more autonomous agents. More autonomous agents require stronger type enforcement. The loop accelerates, and companies that see it early are restructuring everything: their tooling, their teams, their workflows. Companies that don’t are wondering why their competition ships so much faster with half the headcount. We’re not building 10x teams, we’re building 100x teams. And 1000x teams.

The CRA → Vite → TanStack Start progression shows how the stack is restructuring. Create React App was built for humans writing all code and catching type errors during development. Vite made iteration faster but assumed humans still structured projects. TanStack Start assumes AI agents are generating half your code and will confidently hallucinate nonsense unless the framework catches them. Type-safe file-based routing via TanStack Router. Runtime validation, not just compile-time checks. URL-as-state primitives with full type safety. Your routing layer enforces type contracts at runtime so AI agents can generate routing code safely because the framework catches mistakes before they become runtime errors. This is why Anders Hjelsberg rewrote TypeScript in Go. Type safety used to be about catching human mistakes. Now it’s about constraining AI in production. Each framework generation is structurally better suited to a world where sometimes the developer is Claude and sometimes might be a junior engineer who slept through database systems CS 145.

The DrizzleORM discourse looks like developers nitpicking edge cases, but Drizzle is winning adoption because its type inference is good enough that AI coding assistants can generate correct code without human supervision. Types are becoming the contract between human developers and AI agents. For AI-augmented development, type safety is the only thing preventing chaos at scale. Once the SDLC provides end-to-end type safety, stack compression becomes inevitable. Node’s SQLite integration looks like a convenience feature until you see what it eliminates: the entire “file a ticket with the database team, wait for provisioning, set up connection pooling, write migrations” dance disappears. Agents can now scaffold full-stack apps with persistent storage without managing dependencies.

This continues the lakehouse convergence pattern. The 30-year-old OLTP/OLAP divide is healing. Now the application-infrastructure divide is following. When a single team member can handle database schema, business logic, and UI in the same type-safe environment without context-switching, you don’t need database specialists anymore. You need engineers who can reason about the full stack, but increasingly that reasoning is being done by AI agents that won’t break production because types catch their mistakes. Supabase turning the browser console into a full database management environment enshrines the pattern. Schema inspection, query execution, real-time debugging, all in DevTools. Your developers already spend 40% of their time in browser DevTools. Database management moving there isn’t about ergonomics. It’s about eliminating the handoff. Hugging Face’s TypeScript SDK pushes this further with direct transformer model imports, client-side inference via WASM, under 50ms cold start. You can now import a language model the same way you import lodash. Machine learning expertise, which used to require a separate ML engineering team, just became a one-line import statement. Anti-gravity for Python.

Intelligence is dispersing out of specialized teams into the development substrate itself. The browser console is becoming the last mile of infrastructure. Supabase’s $5B valuation is a bet that infrastructure management happens where developers already are, not in specialized tools that require specialized knowledge. The intelligence isn’t in the model, it’s in the architecture. The framework enforces contracts, the types provide guardrails, the AI fills in implementation. A junior developer with minimal skills can now ship features that used to require senior expertise because the substrate prevents the catastrophic errors that juniors used to make. This is workforce decomposition at scale, aka the democratization of AI, masked by engineer title inflation. Senior eng roles used to mean knowing enough not to break production. That knowledge is now encoded in the type system and enforced by the framework.

Atlassian’s $1 billion DX acquisition reveals the final piece: closed-loop systems where measurement, action, and learning happen in the same stroke. The feedback loop that used to take weeks of retrospective analysis now happens continuously. Systems detect friction and route around it faster than you can schedule a meeting about it. Or get a reply on Slack. The gap between companies riding this wave and companies still coordinating handoffs between teams is compounding quarterly.

Technical Specs
TanStack Start: AI-proof code gen w type-safe file-based routing; runtime validation via TanStack Router; URL-as-state w full type safety; RSC in 1.x;

DrizzleORM: E2E type safety from schema to results; infers return types w/o manual annotations; 96% AI-generated code compatibility (vs Prisma’s 78%)

Node.js SQLite: Built-in node:sqlite module (v23.0+); zero npm dependencies; synchronous and async APIs; eliminates db team dependency

Bun v1.3: 25ms package install vs npm’s 1.2s; native TS transpilation; built-in bundler 2.4× faster than Vite; all-in-one runtime/package manager/bundler

Supabase Browser Tooling: Database schema inspection, query execution, debugging in DevTools; TypeScript Language Server integration; eliminates DBA role for routine operations

Hugging Face TypeScript SDK: Direct transformer model imports; client-side inference via WASM; <50ms cold start; eliminates ML engineering team dependency

Lovable Agent Mode: Autonomous execution; 4.2 iterations avg to prodx``-ready

Atlassian DX: $1B acquisition; integrates DORA metrics, qualitative surveys, CI/CD telemetry; real-time bottleneck detection, automated remediation

TL;DR Action Items (30/60/90)
Type Coverage Audit: HIGH PRIORITY (30 days) - Map type coverage from database to UI. Every gap is where AI generates bugs that reach production. This is the foundation for autonomous agent workflows. Target: 85%+ in critical paths within 90 days.

Agent Mode Pilot: HIGH PRIORITY (30 days) - Select 2-3 greenfield projects for autonomous agent workflows. Require end-to-end types as prerequisite. Measure velocity gains vs traditional suggestion-review workflows. Decision gate: if 2× faster, expand to 50% of projects within 90 days.

Eliminate Team Handoffs: HIGH PRIORITY (30 days) - Audit how many features require coordination between database, DevOps, and application teams. Migrate to substrate that eliminates handoffs (Node SQLite, Supabase browser tooling). Target: 80% of features shippable by single developer within 60 days.

Closed-Loop Telemetry: MEDIUM PRIORITY (60 days) - Instrument DORA metrics plus qualitative friction surveys. Connect telemetry to automated remediation. Stop running retrospectives. Start running self-optimizing systems.

Skill Floor Assessment: MEDIUM PRIORITY (60 days) - Evaluate what skill level is required to ship features on your current stack vs AI-native substrate. If “senior engineer” expertise is required for routine features, your substrate is obsolete. Budget for migration.

Runtime Strategy: LOW PRIORITY (90 days) - Evaluate Bun for greenfield projects. If 10× faster dev loops without stability issues, migration saves weeks of developer time annually. (Honestly this should probably be 60 not 90 days.)

Bottom Line
The development stack is restructuring around a single architectural requirement: AI agents need types to be safe at scale. That requirement is driving workforce decomposition, stack compression, and the collapse of the application/infrastructure boundary. Types make autonomous execution possible. Autonomous execution enables smaller teams. Smaller teams drive stack compression. Stack compression closes the measurement-execution loop. The flywheel is spinning, and it’s accelerating.

Companies that see this early and restructure their tooling, teams, and workflows around types-as-infrastructure will pull away from competitors still treating types as optional code quality tooling. For CTOs: the 20-30% AI productivity gains represent the suggestion-review paradigm where humans write most code. The 2-3× gains represent autonomous agent workflows where types provide the safety rails for AI to operate at scale. The gap will define competitive advantage in 2026. Choose your substrate wisely.

Web3 Watercooler
The GENIUS Act rewrote the rules for stablecoins in one paragraph and macro in
one law. By forcing 1:1 Treasury backing plus mandatory audits and AML/KYC, Washington just created a private demand engine for U.S. debt; one that pays the issuer a risk‑free spread on Treasuries. That’s why Circle’s USDC yield math ($~2B/year today) matters politically and geopolitically: private stablecoins now act like a covert Treasury buyer and a new lever of dollar influence.

At the same time, legacy finance is experimenting with decentralization. SWIFT’s pilot with ConsenSys signals that interbank settlement is moving from proof‑of‑concept to institutional experiment.

On the product side, Dev and infra signals show the stack maturing. Supabase shipping Web3 login primitives, projects like Bittensor proving permissionless AI utility, and the SEC signing off on a memecoin ETF (Dogecoin) are not isolated headlines but tell a coherent story: (weird for web3, I know) Crypto is exiting niche subculture and entering commodity plumbing for apps, payments, and identity.

The three moments you must care about: policy (GENIUS Act → Treasury demand), institutionalization (SWIFT → interbank pilots), and developerization (Supabase, Bittensor, memecoin ETF). Yes, I just made that word up.

Technical Specs
GENIUS Act Stablecoins: 1:1 Treasury backing; public attestations/audits; mandatory AML/KYC; issuers retain Treasury yields (~4% current); operational reserve models require same‑day settlement windows and custodial proofing.

SWIFT + ConsenSys Pilot: ISO‑20022 compatible blockchain ledger for interbank settlement; pilot throughput targets ~10k tx/sec; permissioned consortium governance; native messaging + on‑chain settlement reconciliation.

Dogecoin ETF: SEC‑cleared exchange product; custodial infrastructure with insured custody; tradeable on regulated U.S. venues; creates on‑ramp for retail crypto into regulated ETFs.

Supabase Web3 Logins: Wallet‑based authentication SDKs for Ethereum & Solana; OAuth2 compatibility; session handling for Web2 apps with Web3 identity binding.

USDC Instant Transfers: Phone‑number or code based USDC rails enabling near‑instant UX; settlement via Treasury‑backed reserves; AML/KYC linkage and on‑chain/off‑chain reconciliation.

Bittensor / Permissionless AI Signals: Decentralized model marketplaces and token‑incentivized compute; early proof that incentive‑aligned, permissionless compute can deliver useful ML primitives.

Industry Impact (Trends & What To Watch)
Stablecoins as fiscal infrastructure. Treasury‑backed stablecoins convert private balance sheets into implicit demand for government paper. This lowers sovereign financing costs and creates a new form of monetary intermediation—private issuers capture risk‑free yield and build regulatory moats via compliance. Watch reserve composition, custody counterparties, and audit cadence.

Institutional ledger adoption. SWIFT’s involvement means banks are prepping for ledgered settlement. Expect hybrid architectures: permissioned settlement with off‑chain liquidity overlays. This reduces settlement friction for cross‑border flows and forces incumbents to negotiate new interoperability standards.

Normalization of crypto retail products. A memecoin ETF is symbolic but consequential: it lowers the political stigma of crypto products and expands consumer onramps. Risk profiles change when retail capital flows through regulated wrappers. Monitor flows and know your counterparty custodians.

Developer mainstreaming. Tools like Supabase and middleware packages make Web3 primitives first‑class for app teams. The barrier for experimentation drops; the risk is that many pilots will leak production data into vendor ecosystems unless contracts enforce exportability and data controls.

Permissionless AI & tokenized compute. Projects like Bittensor suggest a future where compute markets are decentralized and monetized via tokens—this could rewire the cost structure for model training and inference if adoption hits critical mass.

One More Thing...
The long goodbye is over. Windows 10 officially ends support on October 14, 2025.
No more security patches, no more updates. Microsoft’s “last version of Windows” is finally getting the retirement it kept threatening. Time to find every Win10 box in your org (I promise you have a few you don’t know about), update before then, and sandbox anything that can’t be upgraded immediately. Oh, and as an added touch, Microsoft literally just patched the last local account bypass in Windows 11 (on Monday.) Every machine now requires a Microsoft Account. So it’s not just an OS update; you’re migrating your fleet into Microsoft’s cloud identity stack.

You said you wanted to SSO all the things. Lucky you.

Forest Mars
CTO Lunch NYC

*To attend CTO Lunches, please register at ctolunches.com and choose NYC as your city.

U.S. Tech Investment Commitment Calculator
$1,4T ÷ 84 months = $16,666B monthly

$16,666B ÷ 30 days = $555,555M invested daily

$555,555M ÷ 24 hours = ~$23M invested hourly

$23K ÷ 60 minutes = $385K invested every minute

$385,802 ÷ 60 seconds ≈ $6,430 invested every second

H100 GPU cost: $30K (SXM, not PCIe)

$6,430 ÷ $30K ≈ 0.214 H100 per second ≈ Buying another GPU every ~5 seconds

0.214 H100/sec × 60 sec ≈ That’s 12.86 H100’s per minute

Total GPUs by 2028: $1.4T ÷ $30,000 ≈ For a total of 46,666,667 H100 GPUs.

Whose total thermal output is 32.67 GW

46,666,667 × 700W (SXM) ≈ 32.67 GW

That’s 127 Scottsdale Kitchen Infernos
