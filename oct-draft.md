
File Settings
Done
Title
Add a title...
Description
Add a description...
Thumbnail
Will be cropped to a 3:2 aspect ratio
Upload

Draft
Near email length limit
Learn more
CTO Lunch October 2025
Tech Roundup for CTOs: September-October by Forest Mars
They say the days grow shorter when you reach September, not that anyone is leaving the office any earlier. In fact, teams are staying later than ever, driven by a combination of personal passion, downward pressures, and the unrelenting pace of technological acceleration. 

IN THIS ISSUE
It's Conference Szn
New Model Army
She Said Sloppy
AI-Native SDLC Flywheel 
Web3 Watercooler

It’s Conference Szn
The final quarter of the year kicked off not just the Fall Conference Season, but a definitively leveraged resurgence in the U.S. tech sector, inaugurated by the White House Tech Dinner on September 4; planned as the first official event in the newly renovated Rose Garden and which served as a high-stakes, a trillion-dollar spectacle focused on capital allocation for Tech and AI investment, withtotal domestic investment pledges in AI infrastructure and manufacturing announced surpassing a somewhat staggering $1.4 Trillion by 2028. (That’s literally over 2 billion a month from now til then.)

Elon and Jensen both had other things to attend to, which was fine; there’s only so much energy you can fit in the room, leaving Zuckerberg to grab the choice seat on the President’s right. (Poor Gates had to pass notes through Melania on his left.) Which was fine by me since I didn’t even get an invitation. Which was also fine by me since there was also only one CTO in attendance at this “tech” dinner. (I’ll let you guess if it was Palantir or Anduril.)

The White House dinner set the stage; the investment, the optics, the political theate, all signaling the scale of what’s coming. But the real work is happening elsewhere. Engineering leaders are already grappling with the operational and organizational challenges of the AI-first era, to turn these abstract mandates into executable plans. The season’s two gatherings where this work was most visible and consequential were ELC Annual in San Francisco at Fort Mason, so all the cool kids met up later at The Interval) and CTO Craft Con in Berlin. The core questions being debugged were remarkably consistent across continents: How do we actually scale our AI initiatives? What does non-performative governance look like? And why does integrating AI into our workflows so often make our most experienced engineers slower? (And also often, grumpier.)

ELC Annual: Refactor Your Playbook
ELC Annual conference in San Francisco is the single highest-value summit for engineering leadership because it has zero interest in the low-signal clutter of traditional trade shows for more of an executive work session intended to address the mission-critical issues keeping CTOs awake at night. It’s highly collaborative with Roundtable Discussions and meticulous curated 1:1 meetings to ensure every connection is a strategic consultation. This highly focused model has cemented the event’s reputation for delivering actionable wisdom directly from leaders in the trenches, making it a mandatory professional investment for the top eng leaders cohort. Somewhat surprisingly there didn’t seem to be many CTO Lunch list members in attendance, though it’s also a newish event, having only gotten off the ground a few years ago as an “unconference.”

This year’s theme, “AI Rewrote Leadership. Refactor Your Playbook,” acknowledged what’s happening across our industry: the AI experimental phase is over, but most organizations still have no idea how to execute at scale. The shift is as profound as the move to cloud computing, except it’s happening faster and the architectural implications go even deeper. For the past 18 months, CTOs have been running pilots, experimenting with agents, and watching our teams use ChatGPT and Claude in ways that violate approximately every security policy ever written. Executive teams have been patient, remarkably patient by C-suite standards, waiting for productivity gains to materialize beyond anecdotal, and not always true, “my team loves it” reports. Now the bill is coming due. Past due, if you ask your CFO, who wants ROI numbers. Boards want strategic frameworks. And everyone is learning together that bolting AI onto existing architectures is like trying to run Kubernetes on a LAMP stack: technically possible (no, it really is) but catastrophically wrong. (Obvi.)

The (un)conference crystallized around three pillars of “AI Native Leadership” that you can think of more or less as diagnostic criteria for whether your engineering org is about to get lapped. First, architectural simplicity in the age of agentic complexity (code for: your microservices architecture is about to look adorably quaint.); Second, scaling innovation through internal competition, matryoshka-style, where governance is the actual bottleneck (not because anyone cares about ethics theater, but because it’s the real constraint preventing deployment); and Third, resource-conscious leadership, which sounds like the same old “do more with less” mantra until you realize that AI-driven teams require organizational and cultural reconfiguration, sophisticated measurement frameworks, and is effectively blurring the lines between engineering, product, and business. Maybe we’re finally understanding that scaling isn’t about increasing headcount?

It sounds obvious out of context but what’s truly fundamental is the shift in developer experience. The cloud-native era was about CI/CD automation and platform adoption, getting developers to use the tools we built. Similarly, the agentic AI era is about AI-integrated DevEx except we haven’t yet built the tools we want them to be using. This is where platform engineering teams need to “own the loop” by integrating seamless AI assistance that minimizes cognitive load while ensuring high-quality outputs. Data architecture has transformed from relational databases and data lakes into vector databases, hybrid search, and RAG loops where contextual knowledge becomes a critical, performance-gated infrastructure layer. That’s a lot to unpack before we even start pushing it out to not just our teams, but cross-functionally across the whole org.

AI can easily exacerbates the already tight bottlenecks in such collaboration, particularly in the design-to-code handoff where design & engineering collide in Storybook or whatever reconciliation loop you’re using to curtail the chaos. Instead of accelerating workflow, AI assistance often slows down experienced team while helping junior developers catch up, two steps forward, three steps back. This pattern keeps showing up in studies, leading to odd conversations about team composition and the need for senior engineering expertise in an AI-assisted world. Meanwhile, the infrastructure requirements aren’t subtle: vector databases have moved from experimental to mandatory, RAG architectures are table stakes (esp. for avoiding hallucinated compliance violations) and the orchestration layer for managing autonomous agents requires rethinking the entire SDLC. The cloud-native era’s primary risks were supply chain integrity and dreaded configuration drift; the agentic era’s risks remind us that we palliated those concerns more than we actually solved them, requiring Agentic DevSecOps (a popular buzzword at ELC) methodologies rebuilt almost from scratch.

ELC 2025 marked the point where AI strategy finally got operational. Every conversation was about execution: which architectures hold up under load, which governance models survive contact with reality, what teams that are actually shipping know that you don’t. The signal was clear: this isn’t theory anymore. The next phase belongs to leaders who can translate architectural clarity into organizational momentum, because the experimentation window is closing fast.

CTO Craft is where European tech leadership cohort goes to admit what’s actually broken. 

CTO Craft Con: Why Your AI Strategy is Culturally Invalid
If ELC Annual was about the tactical and architectural translation of AI strategy, CTO Craft Con in Berlin was the essential counterpoint, focusing squarely on the organizational and cultural re-engineering required to survive the transition. Held (September 23–24) at the Spielfeld Digital Hub in Kreuzberg, which has become a hub for tech startups and creatives. Unlike the Valley’s performance optimism, Berlin’s engineering culture has always trafficked in a certain, dare I say, German pessimism and this year’s iteration distilled this sensibility into a two-day diagnostic of what happens when you try to run an AI-first org in what’s being called the “permacrisis” of economic volatility, geopolitical chaos, and the persistent sense that whatever stability you thought you has now became a liability smh. 

The central thesis wasn’t subtle: technology is cultural, and CTOs who don’t understand this are managing the wrong variables. I had a COO who used to joke that I was also the Chief Cultural Officer, and there’s a deeper reason for that than my perceived erudition. As Don Ihde pointed out in his writings on technological mediation, technology doesn’t just solve problems, it reshapes the organizational context in which those problems exist. GenAI acceleration make this explicit. You can’t bolt AI onto a low-trust culture and expect anything but expensive theater. You can’t mandate platform engineering adoption without first cultivating what the conference called “Challenger Safety,” the organizational capacity to question architectural decisions without triggering defensive bureaucracy or political retaliation. Which just leads to attrition of your best people. 

The burnout data finally got concrete: 41% of engineering leaders are actively considering leaving their roles, and the reasons track directly to the structural contradictions the conference spent both days unpacking. Leadership wants transformative AI deployment but won’t fund the technical debt remediation required to make it viable. Boards want platform-driven operational efficiency but still measure success through headcount growth. Everyone wants innovation, but the organizational maturity required to sustain it, verifiable processes, genuine psychological safety and architectural clarity, remains aspirational at best. Startups have an odd advantage here: they lack legacy inertia to unwind, so they can mature faster, sort of like how people used to look older at the same age. But that only works if they’re intentional about building the right cultural scaffolding from the start, which most aren’t. (ca. OpenAI’s DevDay announcement they are basically Roundup for startups.)

Technical re-engagement as a mandate emerged as the conference’s sharpest diagnostic. The archetype of the CTO as pure people manager, the one who “graduated” from hands-on work years ago, is failing catastrophically in the agentic era. You cannot architect for AI scale-up from 30,000 feet. You cannot evaluate RAG pipelines, vector database performance, or agent orchestration frameworks through executive summaries. The complexity is too high, the pace too fast, and the gap between what vendors promise and what actually ships is too wide. Permacrisis has become a driver of what some are calling the builder-founder revolution: technical leaders who can still ship are suddenly worth exponentially more than those who can only delegate, and the market is repricing accordingly.

Platform engineering became the conference’s organizing principle for making this concrete. Not platform engineering as aspirational excellence, which is an organizational smell that you’re optimizing the wrong layer, but platform engineering as operational reality. Can your platform team actually reduce cognitive load for developers integrating AI tooling? Have you built the feedback loops that let you measure whether your abstractions help or hurt? (cf. DX, following) Are you owning the loop, or just adding more process overhead to an already fragmented developer experience? The questions were sharper than the answers, which was the point. Like the inflection from experimentation to execution highlighted at ELC, this isn’t solved yet, but at least the European cohort is asking the right questions rather than presuming the answers are obvious.

The permacrisis framing cuts deeper than economic uncertainty. It’s fundamentally about the erosion of trust.  High-trust organizational culture isn’t a nice-to-have anymore; it’s the only environment where technical leaders can make the kind of rapid, high-stakes decisions that AI deployment requires. High trust culture meets zero-trust architecture. 

TL;DR Action Items
The mandate from ELC is stark: refactor architecture for agentic systems immediately, allocate protected time for cultural reskilling (the Duolingo approach got namechecked repeatedly for ensuring actual competency rather than superficial AI fluency), and move governance away from shallow activity metrics toward outcome-focused frameworks like the AI Impact Framework or QuADS that link AI-amplified throughput to strategic business objectives and justify the capital investment to the board. Incremental integration is insufficient. Success requires architectural foundations, talent reskilling, team restructuring, and outcome-based governance. The organizations treating AI as incremental tooling are falling behind those treating it as architectural transformation. The question isn’t whether to adopt AI. It’s whether your current foundations can support what’s coming. ELC made clear: most can’t.

Agentic IAM & Token Governance: URGENT – 30 days: Define and implement Agentic Identity and Access Management (IAM). Enforce token Time-to-Live (TTL) ≤15 minutes for all write-capable agents and mandate immutable logging of agent event chains. Agent failure modes are now system failure modes; govern them as such.

Mandate Challenger Safety: URGENT – 30 days: Immediately implement a culture-first program focusing on psychological safety and dissent (Challenger Safety). Without the high-trust culture that enables humans to challenge an agent’s output, technical governance is insufficient. This is the Who and Why of scaling AI.

Agentic Security/Threat Model: URGENT – 30 days: Update all threat models to account for autonomous AI attack vectors. Pilot AI-assisted red-teaming (XBOW-style) and integrate LLM-specific adversarial tests (reasoning fuzzing, chained-prompt stress tests) into the SRE test matrix.

Formalize Agentic Operating Model (AOM): MEDIUM PRIORITY – 45 days: Stop calling it “GenAI initiatives.” The new architecture is the AOM. Define the core agentic DevEx loops, the data flow (vector/RAG strategy), and the orchestration layer now. This definition must precede all major Q4 infrastructure spend.

Leadership Metrics Refactoring: MEDIUM PRIORITY – 45 days: Deprioritize traditional vanity metrics (Velocity, Deployment Frequency). Reorient dashboards to focus on Time to Value (TTV), Adoption Rate, and Customer Retention Cost (CRC) to align engineering effort with measurable business impact (The shift from output to outcome).

ELC only + Bottom Line (verbose

Based on the ELC Annual content and matching your style from the September newsletter, here’s the TL;DR Action Items section:

Bottom Line
The era of merely experimenting with large language models is over. The immediate and non-negotiable shift is from a service-oriented architecture (SOA) to an Agentic Operating Model. The central engineering challenge is no longer about API composition, but about creating robust, observable, and governable environments for autonomous agents to execute on behalf of the business.

This architectural shift carries a dual, urgent mandate for the CTO. ELC provided the How: the refactoring playbook for enabling vector infrastructure and agentic DevEx loops. CTO Craft Con, however, delivered the true strategic bottleneck: this technical scale is impossible without a culture built on high trust and Challenger Safety. Execution is the new spectacle, and the only path to it runs directly through a re-engineered engineering culture.

The AI Rloveution
New Model Army
September’s models arrived as a torrent of leaves carried on the winds of Fall. They covered every sidewalk, piled up across lawns, and spilled into the streets so high demanding someone get out there and rake them all up. Claude 4.5 (9/12) solved a million-dollar problem you didn’t know you had. GPT-5 Codex (9/18) can run for seven hours straight without supervision (longer than many of your devs, tbh.) Gemini 3.0 Pro (preview, 9/20) was released to VIP users. And Qwen3-VL (9/25) matched the performance of GPT-5 Mini and Claude 4 with just 3B active parameters, proving that the “bigger is better” narrative was always more marketing than math.

The real story isn’t in the model releases themselves but in what’s happening around them. Mira Murati left OpenAI and founded Thinking Machines Lab, wisely choosing not to build another foundation model but instead launching Tinker, a cloud API that lets you write training loops locally while handling its distributed infrastructure. Picks and shovels, to be sure, but for an arms race, not a gold rush.

Context and Background
The foundation model oligopoly is cracking. What’s next is the Great Unbundling, where value is shifting from who trains the best model to who invents the tooling that makes them seriously useful. For two years, CTOs have been held hostage to API pricing, rate limits, and the whims of a handful of labs. That era is ending, not because the big labs are failing but because the economics of AI are fundamentally restructuring around three parallel trends: model commoditization, infrastructure democratization, and tooling maturation.

Claude 4.5 arrived this month, emphasizing operational capability: its server-side container access is the kind of infrastructure change that sounds boring until you realize it eliminates an entire class of security objections. Claude can now execute code in isolated containers on Anthropic’s infrastructure, meaning you can give it database access, API credentials, and system-level capabilities without the security nightmare of exposing those to a conversational interface. This is why we say Agentic AI is speedrunning the cloud computing migration. It’s also how you go from “AI assistant” to “AI operator” without getting fired when the audit comes.

GPT-5-Codex is OpenAI’s best shot at agentic coding, and its 7 hours may be enough for bounded workflows but it’s nowhere close to infrastructure-grade stamina or Claude 4.5’s 30-hour operational window. And unlike Claude 4.5, it lacks any built-in ability to plan or reorganize codebases across modules. This makes it a capable executor for discrete tasks but not yet the backbone of an AI-native development pipeline.

Qwen3-VL-30B-A3B-Instruct is where the commoditization thesis becomes undeniable. With just 3B active parameters (in a sparse mixture-of-experts architecture), it’s matching GPT-5-Mini and Claude 4 on reasoning tasks while being small enough to run on a single H100. The full 30B parameter model has thinking capabilities that rival frontier models, but the real story is the 3B active version: enterprise-grade performance at gaming-GPU scale. Chinese labs are shipping models that match your $200K/year API spend on hardware you can buy on Newegg. The unit economics of AI just changed forever.

And then there’s Gemini 3.0 Pro, which Google is somehow positioning as both a reasoning breakthrough and a cost-effective alternative. Early tests show genuine improvements in multi-step logical reasoning, but the real question is whether Google can overcome the organizational dysfunction that’s plagued every Gemini launch. (Narrator voice: they probably can’t.) Still, the fact that Google is even in the conversation signals something important: the model quality floor is rising so fast that even Google’s execution challenges can’t keep them out of enterprise consideration.

As model quality converges and diverges simultaneously, with Qwen proving cost efficiency, Gemini showing even laggards can compete, Claude and GPT-5-Codex splitting on operational patterns. Microsoft added Claude Sonnet and Opus 4.1 (still topping the ASCII benchmark board) to Copilot Studio for building custom enterprise agents and to its Researcher agent for deep, multi-step analysis. OpenAI still powers standard Office productivity tasks; Claude can now handle the complex reasoning workflows that enterprises build through Copilot Studio’s developer platform. So the company with the largest financial stake in OpenAI just said “we need Anthropic too,” giving every CTO’s multi-model strategy board-level cover. You can now route tasks across OpenAI, Anthropic, and Azure Model Catalog options within the same multi-agent system, treating model selection as an operational choice rather than a procurement commitment.

Multi-model orchestration creates the conditions for something more radical at the infrastructure level. llm-intercept is a fully functional PyPI package that turns expensive LLM API calls into free, self-hosted models. It’s not a hack or a wrapper; it’s a systematic interception layer that routes your existing API calls to local models with minimal code changes. In addition to the substantial cost savings, the technical achievement here is a death knell for API lock-in as a sustainable moat. You can transparently swap Claude API calls for local Llama models without rewriting application code. Vendor switching costs approach zero. Tinker completes the other side of the equation: once you’ve collected training data through llm-intercept, Tinker makes fine-tuning accessible at $2/GPU-hour with orchestration handled, turning what used to require an ML platform team into a hackday project.

Technical Specs
Claude 4.5: 200K context, server-side container execution (gVisor isolation); $3/M input/$15/M output tokens; 22% latency reduction vs Claude 4

Qwen3-VL-30B-A3B-Instruct: 30B total params (3B active per inference via MoE), 32K context, matches GPT-5-Mini on MMLU-Pro (81.3%), Apache 2.0 license, runs on single H100 (24GB VRAM), separate Thinking mode for chain-of-thought

Gemini 3.0 Pro: 2M context window maintained, 35% improvement on MATH benchmark vs Gemini 2.5, $3.75/M input/$15/M output tokens (25% cost reduction), early access shows GPT-5 parity on MMLU-Pro

GPT-5-Codex: 7+ hour autonomous operation with no intervention, 128K context, no planning mode (reactive execution only), 89.2% HumanEval pass@1, $2.50/M input/$10/M output tokens

Microsoft Copilot Multi-Model: Claude Sonnet 4 and Opus 4.1 available in Copilot Studio for custom agent development and Researcher agent for deep research tasks; dynamic model selection across OpenAI, Anthropic, and Azure Model Catalog; opt-in access through Microsoft 365 admin center

Thinking Machines Lab Tinker: Cloud API for distributed training, $2/GPU-hour (50% reduction vs raw compute), handles automatic checkpointing and distributed coordination, supports 7B-70B model fine-tuning

llm-intercept: PyPI package enabling transparent model switching; routes API calls to local models with minimal code changes; collects training data from production traffic; compatibility layer for Claude/OpenAI/local model interchange

Industry Impact
The foundation model oligopoly is fracturing, not because the big labs are failing but because the entire value chain is restructuring. Model selection needs to be task-dependent, not vendor-dependent. The idea that you’d standardize on a single model provider made sense two years ago with two viable options and massive quality gaps. With no less than six credible frontier models (GPT-5, Claude 4.5, Gemini 3.0, Llama 4, Mistral Large 3, Qwen3-VL) and a growing bench of others, multi-model architecture is the only rational strategy. 

The commoditization of reasoning capabilities through models like Qwen3-VL creates a new cost structure dilemma for OpenAI and Anthropic. A 3B model matching your current $75/M token API on reasoning tasks means model quality is no longer a moat. The focus shifts to integration depth and trust relationships. Everyone talks about productization, but it’s not the model that’s being productized, it’s the operational envelope around it. Mira Murati had direct visibility into OpenAI’s model development roadmap and chose to build training infrastructure instead of another model. 

llm-intercept is the opening salvo in what will become a much broader pattern: transparent model arbitrage. Today it’s a PyPI package for Python developers. Tomorrow it’s middleware in your API gateway routing requests to the cheapest adequate model. Next quarter it’s baked into LangChain (ugh, I know) and every agent framework. Model switching transparent to application code means pricing power evaporates. The labs can see this coming, which explains the sudden rush to add features that create stickiness beyond pure model quality. 

The tandem of llm-intercept and Tinker is dismantling the pricing power of the large model labs by tackling both sides of the LLM cost equation: llm-intercept pioneers transparent model arbitrage, evolving from a simple logging tool that collects high-value training data into dynamic API middleware that automatically routes requests to the cheapest adequate model; concurrently, Tinker champions infrastructure democratization by reducing fine-tuning (the core mechanism for creating cheaper, task-specific models from that intercepted data) from an expensive ML platform project to a trivial $2/GPU-hour orchestration task. This perfect storm of transparent model switching and accessible customization is why model labs are now scrambling to build proprietary, “sticky” feature ecosystems, knowing that relying on model quality alone will soon be insufficient to maintain market dominance. The market is already being flooded by cost-effective competitors like DeepSeek’s GLM-4.5, which is crushing it for coding, displaying superior, more reliable performance than recent output from models like Claude, at a fraction of the cost. Model switching transparent to application code plus operationally trivial customization equals the fundamental pricing power of the labs evaporating.

Sloppy, She Said Sloppy
Remember when OpenAI needed $7 trillion and 10GW of power to cure cancer? Yeah, so does Pepperidge Farm. Now they’re launching AI slop videos marketed as personalized ads. The trajectory from “we’re building superintelligence to solve humanity’s grand challenges” to “we’re Canva with worse margins” happened so fast it gave the entire industry whiplash. This month’s calvalcade of product releases from OpenAI included Pulse (morning news, except it’s ads), GPT-Stripe integration (monetization infrastructure finally), and Sora 2 (the infinite video slop machine) mark the definitive point they stopped pretending they’re solving hard problems and started admitting it’s just another attention merchant with a better pitch deck and an insane burn rate. (And a killer engineering team, it must be said.)

Context and Background
OpenAI pulled in $3.5 billion in revenue against $5.3 billion in losses in 2024. First half of 2025? $4.3 billion in income, $13.5 billion in loss. They’re paying AI cloud service providers nearly three times what they collect from AI users. With unit economics that broken, they’ve noticeably stopped talking about AGI curing cancer and built an ad platform, hoping no one calls them out on the $7 Trillion Slop Machine Pivot.

Enter Fidji Simo, OpenAI’s freshly minted “CEO of Applications,” whose LinkedIn trajectory (Meta → Instacart → OpenAI) has little to do with AGI, more like “how do we monetize engagement at scale?” No shade. Her first major product launch was Pulse, ChatGPT’s morning news feature that OpenAI is carefully not calling an ad product, despite it very obviously being, an ad product. It’s the kind of semantic game that works until it doesn’t, which is most likely just how long it takes for users to realize their AI assistant is now serving them sponsored content alongside their morning coffee. We probably need a better word than enshittification, though it got thrown around a lot in the wake of the Sora 2 launch, where the promotional reel conspicuously omitted anything resembling gymnastics. Instead, we got brand-safe b-roll optimized for buy-side advertising and waaay too much of Sama. Sora isn’t the filmmaking revolution we were promised. At best, it’s a content mill for marketing teams who need 44 variations of the same product shot and don’t want to pay a production company. At worst, it’s a TikTok competitor. As more than a few people noted, we were promised superintelligence and got an infinite AI video slop machine. One that OpenAI now charges $200 a month for the privilege of using.

GPT-Stripe integration is where the mask fully slips. It’s brilliant infrastructure work, again they have an incredible engineering team (led by Sulman Choudhry, who spoke at ELC) with truly elegant API design that makes payment processing native to conversational AI. But it’s also the clearest signal yet that OpenAI has fully committed to the “turn models into apps” playbook: Chat (conversational interface), Codex (developer tools), Sora (video generation), and now Stripe integration to monetize all of it. This isn’t the roadmap of a company building AGI. This is the roadmap of a company desperately trying to close a $9 billion annual loss gap by becoming a payments processor that happens to use AI.

OpenAI also spent a cool $15 million acquiring chat.com (last November) because when you’re losing $13.5 billion in six months, what you really need is a premium domain name. The symbolism is almost too perfect: a company that started with a mission to ensure AGI benefits all of humanity is now optimizing for SEO and brand recall like it’s 2011 and they’re pivoting to mobile-first social commerce. Mo So LoCo. But yeah, grandparents everywhere will likely be “asking chat” for answers to all their questions. Finally, there’s the Databricks partnership, making OpenAI models natively available within the Databricks Data Intelligence Platform and Agent Bricks; it’s the one move that makes strategic sense, and you’d be forgiven for thinking that OpenAI is increasingly positioning more of a vendor than an actual platform, if not for DevDay. 

The shoe didn’t just drop at DevDay, they dropped an entire shoe store this year, making the shift explicit: OpenAI has doubled down on products, not long-context models. The event was a blueprint for making ChatGPT the default interface for everything; “you can now chat with apps in ChatGPT” collapsing user workflows into a walled garden rather than teaching models to use external apps through a browser. They shipped Apps SDK to build native apps inside ChatGPT, ChatKit for embeddable/customizable chat UIs, and AgentKit, a full agentic workflow suite that functions like a baked-in n8n: a drag-and-drop Agent Builder, WYSIWYG workflow canvas, guardrails for inputs/outputs, and evals for dataset/trace grading and auto-prompt optimization. They also pushed more powerful Codex tooling and announced Sora 2 and GPT-5-Pro in the API. Much to the disappointment of many devs there for better models, the message was not “we’re giving you longer context,”  it was “we’re giving you richer product hooks inside ChatGPT.” In short, ChatGPT-as-OS is the strategic bet: your Spotify, Zillow, Coursera, all native in ChatGPT, so people spend their time there and all transactions, content slots, and experiences flow through OpenAI’s surface.

For developers at DevDay who showed up for models, not productization, who came expecting large-context engineering, and model capabilities, what they got instead was a C-suite playbook of apps, SDKs, and monetization primitives, the sort of productization that makes CFOs and marketing teams clap. Whether or not OpenAI’s product strategy is solid (and it kinda is, if you ignore the burn rate) and whether or not their engineering team continues to deliver (yeah they do), the event landed as a love letter to executives, not builders. There’s also a sour note about leadership: the company’s culture and management have been criticized internally which further soured the vibes for engineers expecting a model-first technical summit. If you were at DevDay hoping for deep model-level breakthroughs, you left annoyed. If you were a C-suite exec, you left with a checklist.

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

When Anthropic announced the Model Context Protocol last November, the pitch was compelling: an open standard that would let AI assistants connect to any data source, any tool, any API. No vendor lock-in. No proprietary integration layers. Just clean, interoperable infrastructure that would let developers build once and deploy everywhere. The engineering dream: never write glue code again. MCP servers would become the universal AI adapter layer. “HTTP for the LLM era” as someone called it. 

What we got instead was a year of everyone building the same thing: wrappers around vector databases that expose search endpoints. RAG servers with MCP labels and some functions sprinkled on top. The protocol supported arbitrary tool definitions and rich interaction patterns, but nobody wanted to do the work. Easier to slap an MCP interface on your existing retrieval pipeline and call it a day. The “open standard” became a lowest-common-denominator race to ship the minimum viable implementation.

Then came September 10th, when OpenAI finally announced MCP support in ChatGPT. Developer mode only, naturally. Or actually on September 9th, when they originally announced it, then deleted everything, (!) then re-announced the next day. Because profesh. But the real kicker was that their “MCP support” only works if your server implements search and fetch tools to OpenAI’s exact specifications. In other words, if your MCP server is basically a RAG server. They mumbled something about this only being the first step. Where have we heard that before?

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
Multi-Model Strategy (Next 30 Days): Deploy a multi-model orchestration layer immediately. Route tasks by cost-performance and trust tier (Anthropic for secure reasoning, OpenAI for broad API coverage, Qwen for local efficiency). Begin real-time benchmarking for each model per use case. Include planning for dynamic switching between new API models like Sora 2 and GPT-5-Pro as they come online.

Agentic Infrastructure (This Quarter): Adopt isolated container execution templates akin to Claude 4.5. Enable AI agents to run securely with system-level access while maintaining audit-ready pipelines. Integrate DevDay AgentKit workflows to automate common enterprise tasks and test edge-case interactions with ChatKit-embedded UIs.

Model Arbitrage & Data Strategy (Q4 Roadmap): Evaluate the potential of transparent model routing and interception tools (like llm-intercept) but do not assume mandatory adoption. Focus instead on establishing an architecture that supports model switching, logging, and fine-tuning pipelines where it aligns with operational needs. Consider cost-effective model selection across OpenAI, Anthropic, and other providers, factoring in upcoming GPT-5-Pro and Sora 2 operational characteristics.

Developer Retention (Strategic Risk): Protect engineering-first culture. Ensure new productization efforts (Chat as OS, App SDK, AgentKit) do not alienate developers. Provide direct access to APIs, sandbox environments, and extensible workflow tools; avoid limiting early adopters to pre-built product integrations only.

Financial Governance (Q1 Planning): Reassess cost exposure given high-context, long-running model operations and agentic workflows. Plan for 50–70% API cost compression. Structure contracts and infrastructure for fluid provider switching, accounting for DevDay products’ monetization layers and potential SaaS integration fees.

App Integration & Chat as OS (Next 60 Days): Begin exploring embedding third-party app connectivity directly within AI interfaces. Treat AI as default interaction layer for business apps, using ChatGPT-like multi-app integration to streamline workflows, improve UX, and measure productivity gains across Spotify, Coursera, and internal tools.

Agent Builder & Workflow Optimization (Next 90 Days): Invest in WYSIWYG agent workflow creation tools, Guardrails for safety, and automated evaluation datasets to streamline AI workflow deployment. Include monitoring for agent-led automation in complex enterprise processes and incorporate DevDay AgentKit pipelines for continuous improvement and risk mitigation.

Ecosystem Monitoring (Ongoing): Track adoption, feature releases, and competitive multi-model deployments. Adjust internal AI strategy and tooling investments in response to OpenAI, Anthropic, Google Gemini, and Tinker updates. Ensure visibility into new model capabilities, API changes, and developer feedback loops to maintain strategic advantage.

Interface Governance – URGENT (30 days): Audit every planned or existing ChatGPT integration for data egress, telemetry exposure, and UX control. Require internal API façades to insulate business logic and customer data from external platforms. Treat ChatGPT as a distribution surface, not an infrastructure dependency.

Platform Portability – URGENT (30 days): Abstract AgentKit, Apps SDK, and MCP integrations behind a vendor-neutral orchestration layer. Build explicit migration paths and telemetry parity tests to detect silent lock-in.

Data Residency & Compliance – 45 days: Require full auditability for where user, agent, and eval data reside. Define deletion, retraining, and export policies in procurement contracts. Treat model retraining exposure as a compliance risk.

Evals Integration – 45 days: Deploy Evals 2.0 locally for controlled prompt testing and regression tracking. Integrate eval telemetry with CI/CD to benchmark reasoning stability against business-critical workflows.

Content Authenticity – 60 days: Implement video and image fingerprinting to track provenance of Sora-generated assets. Start canonicalization pilots for marketing and knowledge management teams.

Interface Security – 60 days: Treat chat surfaces as threat vectors. Add prompt-injection fuzzing, context poisoning, and chained-prompt penetration tests to your SRE playbooks.

Governance Resilience – 90 days: Define and simulate exit scenarios from ChatGPT’s ecosystem. Establish an internal “AI abstraction committee” responsible for contract versioning, policy enforcement, and long-term portability strategy.

Bottom Line: CTOs, treat the convergence of model releases, agentic tooling, and productized AI platforms as an immediate operational imperative. Prioritize rapid experimentation with multi-model orchestration, secure agentic infrastructure, and integrated app interfaces, while maintaining developer culture and financial discipline. The key is building adaptable systems that extract real business value from the accelerating pace of AI productization.

Web3 Watercooler
The GENIUS Act rewrote the rules for stablecoins in one paragraph and the macro in one law. By forcing 1:1 Treasury backing plus mandatory audits and AML/KYC, Washington just created a private demand engine for U.S. debt—one that pays the issuer a risk‑free spread on Treasuries. That’s why Circle’s USDC yield math ($~2B/year today) matters politically and geopolitically: private stablecoins now act like a covert Treasury buyer and a new lever of dollar influence.

At the same time, legacy finance is experimenting with decentralization. SWIFT’s pilot with ConsenSys signals that interbank settlement is moving from proof‑of‑concept to institutional experiment. This is not fantasy railroading — it’s incumbents writing migration plans for a shared ledger layer.

On the product side, Dev and infra signals show the stack maturing. Supabase shipping Web3 login primitives, projects like Bittensor proving permissionless AI utility, and the SEC signing off on a memecoin ETF (Dogecoin) are not isolated headlines but tell a coherent story: (weird for web3, I know) Crypto is exiting niche subculture and entering commodity plumbing for apps, payments, and identity.

The three moments you must care about: policy (GENIUS Act → Treasury demand), institutionalization (SWIFT → interbank pilots), and developerization (Supabase, Bittensor, memecoin ETF). 

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




Forest Mars
CTO Lunch NYC

*To attend CTO Lunches, please register at ctolunches.com and choose NYC as your city.

Thanks for reading! Subscribe for free to receive new posts and support my work.

Type your email…
Subscribe













































































































































2025/09/26
