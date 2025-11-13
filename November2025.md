CTO Lunch NYC November 2025
Tech Roundup for CTOs: October → November by Forest Mars
Forest Mars and CTO Lunch NYC
Nov 05, 2025

October brought us the Internet’s greatest achievement and its most catastrophic infrastructure incident in the same breath. Archive.org just crossed the one trillion page mark, a feat of digital preservation so vast it’s like cataloging every grain of sand on a beach nobody asked you to count. Or most likely, will ever be looked at by another human being again. Days later, an AWS control-plane outage took out over 3,500 companies, from fintechs to federal contractors, to well known brands, proving once again that our world now runs on a single distributed dependency graph. We’ve built systems capable of cataloging humanity’s digital history but incapable of failing gracefully when a single control plane hiccups.

It’s a perfect juxtaposition: at the very moment we celebrate our ability
to save everything, we also prove we can’t keep it all running.

A trillion pages doesn’t even include Archive’s book collection (smaller now after this year’s copyright ruling), but the irony holds either way. We’ve reached peak data abundance and yet find ourselves scraping the bottom of the internet’s barrel for more. Foundation models have eaten nearly all public text, and the world is starting to look like a starving AI engineer stumbling home at 3am to find DoorDash done, the fridge empty, and the training run still demanding more data. (Why can’t Mel’s be open until 3:00 every night? But even NYC isn’t 24/7 anymore.) Early architecture promised it just needed more data, more GPUs, more data centers, never mind the water; we’re manufacturing each of them fast as humanly possible, but the big question remains: what happens when models ‘finish’ training and start taking action?

IN THIS ISSUE
Escape Velocity
Atlas Shrugged
Secret Agent Man
Python Sheds its Skin
RIP Modern Data Stack
RSC-y Business

The AI Rloveution
What comes after prediction: when models begin to decide and take action?

If Microsoft’s big ‘reveal’ this month seemed obvious, that every Windows 11 machine is becoming an AI PC (with voice-chatting Copilot, screen-sharing, and permissioned task execution) and users will no doubt welcome the convenience, what this really is, is infrastructure for delegation: the extended substrate our apps will run on. Windows isn’t just adding AI features; it’s becoming an agentic operating system where the UI is increasingly a suggestion layer between the user and autonomous execution. How are you building your apps for this coming age of intent delegation infrastructure?
(Hint: make sure they are machine-discoverable, well-permissioned, & context-aware.)

Apple, not surprisingly, is taking an ‘opposite’ approach. While Microsoft bets on cloud-connected AI everywhere, Apple’s M5 Neural Engine (ANE) represents a different thesis: on-device, post-foundational, AI as UX, reframing the question from how big can you go to how close can you get? And M5’s ANE improvements are genuinely impressive: more cores, better power efficiency, dramatic throughput gains that should enable on-device AI capabilities, making cloud inference look quaint. We live in hope.

Except there’s a problem: Apple’s hardware teams are lapping their software teams, and it’s unclear if this is by design or dysfunction. The ANE still doesn’t have a native programming model. If you want to use it directly, you’re routing through CoreML, wrapping models in Apple’s proprietary format and hoping the compiler makes sensible optimization decisions. MLX, the closest thing to a modern deep learning framework for Apple Silicon, doesn’t even use the neural engine. ANE Transformers exist as a library, Apple’s Foundation models leverage ANE, but if you’re doing custom model work you’re navigating undocumented APIs and hoping you don’t fall off performance cliffs. (Or real ones. Speedy recovery, Kevin!)

While Apple treats ANE programming like a state secret, NVIDIA is publishing CUDA docs like they’re running a university press. The result is bizarre: Apple’s own apps get blazing-fast on-device inference while third-party developers either hit the cloud or accept 10× slower performance using CPU/GPU instead of ANE. (IOW, their usual tricks.) M5 has all the nuts and bolts but isn’t exactly prêt-à-porter for developers who want to ship production AI features. (M6 is supposed to fix this.)

Gruber once said: “All things considered I’d much prefer a PC running Mac OS X to a Mac running Windows.” Fifteen years later, we’re in the mirror world: the hardware is spectacular, the software story is a mess, and developers are left wondering if Apple can actually succor a third-party AI ecosystem or just wants it all to themselves.

OpenAI Season
Restructuring into a $500B public benefit corporation was just the opening act. Microsoft walked away with a 27% stake ($135B), $250B in guaranteed Azure revenue, and rights to OpenAI’s IP until AGI or 2030; the kind of circular round‑tripping that makes accountants twitch. Within a week of Microsoft’s right-of-first-refusal expiring, OpenAI had announced a $38B, seven-year cloud deal with AWS, asserting leverage before anyone could react. Meanwhile $2.5B in stock comp flowed to ~3,000 employees (a jaw-dropping~$830K per person in six months), prompting one CTO to note that OpenAI is effectively “a hedge fund that trains neural networks.”

Lawrence Lessig’s amicus brief on behalf of 12 ex-employees raises uncomfortable questions about sustainability, but this act isn’t going to be about the corporate drama. It’s about what OpenAI is launching while everyone watches that soap opera.

Project Mercury: Launch != Escape Velocity
Project Mercury is OpenAI’s play for Wall Street, and it’s smarter than you think. They’re hiring contractors at $150/hr to train AI on investment banking workflows: IPO modeling, M&A comps, deck reformatting, the grunt work that defines junior analyst life. The insight is simple: whoever wins financial services AI wins enterprise AI. Banks spend hundreds of millions annually on work that’s structurally formulaic. 50% automation = easily $100M annual savings for a large bank, but the real prize is talent arbitrage: senior bankers freed from deck hell can do higher-value work.

The competitive landscape is dotted with the usual suspects. Bloomberg’s AI Terminal leverages decades of proprietary financial data and existing trader workflows; their moat is data access and terminal lock-in. Palantir Foundry already owns complex data integration at major banks; they can add AI features to existing deployments without ripping and replacing infrastructure. Google and Microsoft are pushing Vertex AI and Azure OpenAI respectively, bundling AI capabilities with cloud contracts banks already have.

Here’s where it gets messy for OpenAI: Microsoft’s Azure OpenAI is OpenAI’s models, which means Microsoft is simultaneously OpenAI’s distribution partner and their direct competitor. Banks already paying for Azure can add OpenAI capabilities without a new vendor relationship, they just route through Microsoft. But this is precisely why Project Mercury matters strategically. The $250B Azure revenue guarantee gives OpenAI distribution, but it also creates existential risk: what happens when Microsoft launches “Copilot for Investment Banking” using the same underlying models? Project Mercury is OpenAI’s answer: build such deep domain expertise in financial workflows, through intensive contractor training, proprietary deal data, and operational refinements, that Microsoft can’t simply replicate it by fine-tuning base models.

Every month Project Mercury trains on real investment banking workflows is another month of domain knowledge that doesn’t exist in the base GPT-5 model Microsoft has access to. The goal is to achieve escape velocity: make OpenAI’s banking AI so specialized, (and so operationally refined) that Microsoft would need 18+ months and hundreds of millions to catch up, by which time OpenAI has already captured the enterprise accounts and reached a stable orbit beyond Redmond’s gravitational pull. It’s a brilliant hedge: use Microsoft’s distribution to win customers, but build proprietary domain expertise they can’t easily replicate. The $250B Azure guarantee keeps Microsoft happy in the short term. Project Mercury success ensures OpenAI doesn’t need Microsoft in the long term.

Then there’s Farsight AI, a recent Series A company operating in a different but intersecting orbit. They’re already shipping, automating investment banking deliverables (decks, CIMs, DCF modeling) targeting the same massive cost savings OpenAI is chasing. But while OpenAI is building domain expertise (training models on real banking workflows to understand deal structure, comps logic, output quality), Farsight is building production systems (solving how to reliably generate complex financial documents at scale under deadline pressure.) While OpenAI is still hiring contractors to build training data, Farsight is already live with customers. The challenges aren’t about model capabilities; they’re about operational reliability; not considered as sexy a problem, but the very real difference between a demo and a product. With a catch more like a law of conservation than Jevons Paradox: If the system requires even a small amount of high-cost senior banker time to QA, it can easily erase the savings gained by automating many hours of low-cost junior banker time, and the ROI collapses. The unsexy truth: production AI for financial services is 20% model quality and 80% operational reliability. And 0% trust.

For Farsight, the strategic window is clear; they’re already solving operational challenges, already have customer relationships, already iterating on real feedback. While OpenAI navigates the complexity of contractor training and Microsoft partnership dynamics, they can capture market share by simply reaching operational altitude first. But this is hare vs. hare, not tortoise vs. hare. OpenAI would seem to have better resources, better models, better brand. If they execute reasonably well, they can win. Farsight’s advantage is execution speed and customer proximity:
if they can lock in relationships while OpenAI is still navigating contractor training, Microsoft politics, and figuring out what banks actually need, that’s a real window.

The winner in financial services AI won’t necessarily be the company with the best foundational model; it’ll be whoever achieves sustainable orbit first: trust, integration, and operational reliability that works at scale.

CTOs should watch this closely, not just to see who wins, but to understand the playbook. This is your preview of how 2026 enterprise AI budgets get allocated: not to the best technology, but to whoever achieves escape velocity on execution and trust fast enough to matter. The question isn’t about benchmarks or launch announcements let alone who has the biggest or most recent model; it’s about sustained flight in the operational trenches where production AI actually happens.

Atlas Shrugged
ChatGPT Atlas went GA for macOS (on 10/21) with Android pending. On the surface, it looks like yet another Chromium fork joining Comet and Dia in the AI browser waiting room. Except OpenAI isn’t building a better browser. They’re building distribution control before the model layer commoditizes entirely. (The Interzone, so to speak between tier 4 and tier 5.)

The browser question isn’t “why does OpenAI need one?” It’s “what happens when the browser disappears entirely?” Elon recently prognosticated that future devices will become pure delivery mechanisms for custom AI-generated (video) content. Instant, personalized, generated on-demand. If he’s right, the browser as we know it, tabs, bookmarks, URLs, becomes vestigial. What replaces it is something closer to a *viewport*: a window where AI assembles information, media, and interaction surfaces dynamically, on the fly, tailored to your personal context.

Whoever controls that viewport controls distribution.

OpenAI isn’t competing with Chrome on features. They’re positioning for a world where the browser is the last middleware layer between users and AI-generated reality. Whoever controls that viewport controls distribution. Whoever controls distribution decides which models get used, which data gets accessed, which experiences get prioritized.

Think about what’s already changing: you don’t browse Reddit anymore, you ask ChatGPT to summarize it. You don’t search for restaurants, you ask Claude to plan dinner. The browser as a *place you go* is being replaced by the browser as a *thing that assembles answers.* Atlas is OpenAI’s bet that when the web becomes something AI reads *for* you instead of *to* you, you want to own the viewport doing the reading.

Arc tried to reimagine browsing and failed (though they had a successful exit) because they built a product for a market that didn’t exist yet. Dia hasn’t even launched. Atlas might succeed not because it’s “better” per se, but because it’s infrastructure for the agentic web, not a feature-packed browser for humans who still think in tabs.

Secret Agent Man
40% of agentic AI projects will fail by the end of 2027. [Gartner] That doesn’t mean agentic is over; quite the opposite really: Karpathy went so far as to say the coming 10 years will be the agentic decade and explicitly *not* the decade of AGI’s imminent arrival. Whelp, I guess that gives me a lot longer to finish my book.

For the past two years, enterprises treated agent pilots as sandboxes: promising but unproven. Now, it’s time these pilot graduate to production, and CFOs are asking the tough questions: “What is the measurable ROI?” and “Why does this cost more than three FT developers?” The projects that fail aren’t the ones that don’t work, but the ones that can’t articulate their value in a way that survives budget review.

It’s a familiar pattern. Remember when every company needed a blockchain strategy? The tech worked fine(ish). The projects got canceled because no one could explain why a database with extra steps was worth the architectural complexity. Agentic AI is about to hit the same filter, and the survivors will be the ones that can draw a straight line from “AI agent deployed” to “measurable business outcome achieved.”

Organizations that understand the difference between dataflow and runtime are the ones shipping more successful agents.

While everyone argues about AGI timelines, the real, foundational battle is happening at the infrastructure layer. The emerging pattern is clear: organizations that understand the difference between dataflow and runtime are the ones shipping more successful agents. Those that don’t are six months into “building our agentic platform,” only to discover their architecture cannot actually support the production use cases they promised their leadership.

The infrastructure choices reveal a market split: established enterprises with existing orchestration platforms tend to embed lightweight frameworks like LangChain into their current workflows, while agent-first startups building products where the agent is the core increasingly reach for full-stack platforms (Mastra) providing a dedicated runtime environment, offering the stability and control a complex agent system requires: reproducible decision paths, traceable reasoning, and policy enforcement baked into the execution layer; not just seeing what the agent did, but reconstructing why it did that, and proving it to auditors, stakeholders, or your most suspicious CFO.
The choice tells you almost everything about whether a company is shipping an experimental feature or a scalable, production-ready product. And the tension (framework vs runtime) feels like a classic library-vs-framework tug-of-war, scaled out to autonomous systems.

Industry Impact
Here’s where Observability 2.0 comes in. Traditional observability (logs, dashboards, simple monitoring) was built for predictable pipelines (not to mention the ETL era.) It tells you what happened, sometimes when, rarely why. Agentic AI, however, is autonomous, stochastic, and constantly adapting. Execution debt isn’t about broken code; it’s about trust. Can you explain why the agent acted as it did? Can you reproduce success across contexts? Can you prevent yesterday’s failure from recurring tomorrow?

Execution debt isn’t about broken code; it’s about trust.

The agentic era introduces a new kind of technical debt: execution debt. Traditional debt is about messy code; execution debt is about trust. When your agent acts, can you explain why? When it fails, can you prevent it next time? When it works, can you reproduce the reasoning that led there? Companies treating agents as “better APIs” are accruing execution debt fast. The refactor bill comes due when:

Your agent hallucinates in production and deletes customer data

Compliance asks for an audit trail, and you don’t have one

The agent’s reasoning shifts and no one knows why

You upgrade models but can’t prove behavior stays consistent

The survivors will build observability into the stack from day one. Not logging. Not monitoring. (Modern) Observability. aka O11y 2.0. The ability to reconstruct an agent’s reasoning, trace decisions to data & prove it stayed within policy. Because when your secret agent man says he sees everything, he’d better have the dashboard to prove it.

CTO Playbook: 30/60/90
Implement Agent Observability* Stack: (HIGH PRIORITY - 30 days)
Deploy structured logging for all agent actions with: (1) decision trace (inputs, reasoning chain, outputs), (2) action audit trail (what was executed, when, by which agent, under what permissions), (3) rollback metadata (pre-action state snapshots). Minimum: OpenTelemetry tracing with agent-specific spans, persistent storage for 90 days, dashboard showing agent decision paths. Deliverable: Working observability dashboard showing last 1000 agent actions with full trace reconstruction.
*(Observability here meaning Modern Observability aka O11y 2.0)

Document Agent ROI by Use Case: (HIGH PRIORITY - 30 days)
Create spreadsheet mapping each agentic project to measurable outcomes: hours saved per week, cost per hour, annual savings, implementation cost, payback period. Require project leads to fill this out for every agent pilot. Deliverable: One-page ROI summary per agent showing break-even timeline and monthly cost/benefit. Template: “Agent X saves Y hours/week at $Z/hour = $ABC annual savings vs $DEF implementation cost = F-month payback.”

Architecture Decision Record: Pipeline vs Runtime: (HIGH PRIORITY - 30 days)
For every agentic use case in development, document the architectural decision: stateless pipeline (orchestrated by external scheduler, no persistent state) or stateful runtime (long-lived process, maintains context). Reject any proposal that tries to do both. Deliverable: ADR template with decision criteria, one completed ADR per active agent project, sign-off from technical lead.

Implement Agent Circuit Breakers: (HIGH PRIORITY - 30 days)
Add safety controls to all production agents: (1) action approval thresholds (auto-execute <X,requirehumanapproval>X, require human approval > X,requirehumanapproval>X), (2) rate limits per agent per time window, (3) automatic rollback for failed actions, (4) manual kill switch accessible to ops team. Deliverable: Code PR implementing circuit breaker middleware, runbook for ops team on how to kill rogue agents, test results showing rollback works.

Create Agent Discovery Manifest: (MEDIUM PRIORITY - 60 days)
For each application feature you want agents to invoke, publish a machine-readable manifest: endpoint URL, required parameters with types, permission scopes needed, expected response format, example requests. Format: API spec + permission matrix. Deliverable: /agent-manifest.json endpoint serving your app’s capabilities, test showing Windows Copilot or Claude can parse and invoke your API.

Audit Agent Runtime Compatibility: (MEDIUM PRIORITY - 60 days)
Test your agents across target runtimes (Windows Copilot, Apple Intelligence, Atlas, web browsers). Document: which features work, which degrade, which fail completely. Create compatibility matrix. Deliverable: Test suite running agents in each target environment, spreadsheet showing feature parity across runtimes, prioritized backlog of compatibility fixes.

Run Build-vs-Buy Analysis for Vertical AI: (MEDIUM PRIORITY - 60 days)
If you’re in finance, legal, accounting, or consulting, research vendor offerings targeting your vertical (OpenAI Mercury for banking, Harvey for legal, etc.). Document: vendor capabilities, pricing, data residency requirements, differentiation risk if competitors use same tool. Deliverable: Decision memo with recommendation (build in-house vs adopt vendor solution) backed by total cost of ownership analysis.

Establish Agent Testing Pipeline: (MEDIUM PRIORITY - 60 days)
Create automated test suite for agents covering: permission boundary violations (can agent access data it shouldn’t?), failure mode handling (what happens when API is down?), degraded functionality (does agent fallback gracefully?). Run in CI before any agent deployment. Deliverable: Test suite with minimum 80% coverage of agent code paths, CI integration blocking deploys on test failures, weekly test report showing agent behavior stability.

ROI Calculator - Knowledge Work Automation Risk:
Junior IB analyst comp: $200K base + benefits = $250K per FTE

Typical analyst output: 15-20 models/decks monthly (high vol)

Project Mercury automation: 40-60% workflow reduction

Displaced headcount: 2-3 junior FTEs per senior banker

Cost impact: $500-750K annual savings per senior banker team

Your organization: How many high-value repetitive workflows exist? Multiply by potential 40-60% automation to estimate exposure

Bottom Line
The central tension between peak data abundance (exemplified by Archive’s trillion pages) and system fragility (worst AWS outage ever) forces a bifurcated architectural choice: either Microsoft’s Agentic Substrate where AI acts as an OS service of delegation to manage fragility, or Apple’s On-Device Integrity to achieve a local, non-brittle solution aimed at avoiding the dark cloud. The true commercial battleground, however, is being staked out by OpenAI, which aims to control both the user’s primary assembly point for reality (the Atlas viewport) and become the most precise automation engine for high-value workflows (Project Mercury). The winners in this revolution will be those who control these execution chokepoints, reliably orchestrating human intent regardless of which underlying thesis prevails.

🐍 Python Sheds Its Skin
Python 3.14 landed with features that sound like big wins: built-in Zstandard compression, significant improvements to the typing module, and official support for PEP 703 (no GIL), experimentally introduced in 3.13. The inclusion of Zstandard is an immediate, practical win for cost savings and latency. For CTOs with data pipelines that move terabytes daily, an instant 10x speedup and 3.3x smaller files compared to gzip is long overdue. But let’s be honest: Python is arriving fashionably late to a party Go and Rust attended years ago, and it’s acting like it invented the hors d’oeuvres.

Free-threaded Python is a tectonic shift. While this feature was an optional build in Python 3.13, the RIP GIL moment is no longer experimental as of 3.14. And while we’d love free-threaded execution to be a celebration of real, multi-core concurrency, truth be told, it’s more of a warning about ecosystem fragmentation. Of the top 360 most-downloaded PyPI packages with C extensions (the ones that matter for performance), only 128 (35%) support free-threaded wheels. You can compile and run python3.14t today, but if your critical dependencies don’t support it, you’re back in GIL-land anyway, without concurrency. At least the experiment is over.

NB. If you import a single C extension module (eg. pinned to older version) not marked as thread-safe, the interpreter re-enables the GIL for the entire process.

This ecosystem gap reveals the core conflict: Python is simultaneously dominant (ML, data pipelines) and stagnant (concurrency, modern typing). The language has modern syntax like async/await and match statements, and continues to make incremental type progress with improvements to the typing module in 3.14. Major projects use strict MyPy enforcement. But as one CTO put it: “Type annotations in Python still feel like mere suggestions.”

This connects directly to our “types as AI infrastructure” thesis. TypeScript treats types as contracts enforced at compile time. Python treats types as documentation enforced at runtime (if you remember to add validation.) For human developers, this is an annoyance. For AI agents generating code, it’s catastrophic. An agent can confidently generate thousands of lines of code that pass static checks, integrate across multiple services, only to explode in production, a level of failure no CTO, enterprise or not, can tolerate. The philosophy of Python (”we trust the developer”) breaks down when the developer is a confidently hallucinating AI. The modern app stack is converging to provide end-to-end type safety as infrastructure for AI development. The fact that Mastra was explicitly created in TypeScript because its founders couldn’t build reliable, type-safe, event-driven agents in Python speaks volumes.

Not “taking sides” here but JTN: Python lets agents confidently hallucinate across your production stack, TypeScript forces them to prove every step before deployment. For a CTO, that’s the difference between a minor bug and a multi-service outage that costs millions. (Spoiler: use them together.)

In a odd coda to all this, the Python Software Foundation declined a $1.5M NSF grant over ideological disagreements regarding its DEI requirements. The grant included language requiring recipients to not operate programs that adhere to specific DEI ideologies, which the foundation was not inclined to comply with. The lesson for CTOs isn’t about the policy; it’s about community governance. Python’s strength is its independence, but that independence can ofc be a liability when it comes to funding long-term development. If a community can’t agree on basic financial decisions, what happens when it needs to make high-stakes, technical architecture decisions to keep up with the competition? Python declined $1.5M because no one could agree on the indentation rules for morality; a billion lines of code later: still arguing about whitespace. 🕶️

Bottom Line
Python has long been the language of AI development, but its community-governed evolution creates a structural contrast with patron-backed languages like TypeScript. This isn’t about technical quality, both languages remain critical to the modern agentic stack, but about the operational imperative to upgrade, and acceleration.

TypeScript’s corporate backing (Microsoft, Google, and others) creates business-critical dependencies on its evolution. Features like compile-time type safety aren’t optional niceties; they’re infrastructure requirements that prevent catastrophic failures at scale. For teams building on AI-native SDLCs, staying current with TypeScript isn’t a choice, it’s a competitive necessity baked into the development process itself.

Python’s community governance model, by contrast, means beneficial features land when the ecosystem supports them, not when business timelines demand it. Data science teams upgrade when convenient because Python’s evolution, while valuable, rarely creates the same structural imperative. The language’s principled independence, including its selective approach to funding, preserves autonomy but shifts the burden of maintaining competitive advantage onto individual organizations rather than embedding it in the language’s evolutionary trajectory.

Upgrading Python to 3.14 is exciting in theory, but for real-world, agentic pipelines, the practical gains are largely symbolic.

Python 3.14’s headline features, GIL removal, Zstandard compression, improved typing, illustrate this perfectly. They’re technically interesting but deliver minimal practical gains. The GIL removal promises true multi-core concurrency, yet is largely unsupported. Zstandard compression might save $1,000 annually for a workflow transferring 1GB daily on AWS but that’s hardly enough to break out a ROI calculator, let alone drive urgent migration. Though that does scale linearly, so figure $100K savings for 100GB/day (while updating Docker images, validating CI/CD pipelines, and running compatibility checks for somewhat marginal infrastructure gains.)

While Python 3.14 may or may not give you any appreciable savings on your AWS bill (depending on your data usage), it can definitely be helpful in places where you’re running into rate limits set by Enforced Network Bandwidth Quotas. In which case cutting your guest traffic down to 1/3 of what it was looks pretty good.

But apart from catching up to features found in other languages for some time, there’s little to no business imperative to upgrade, which may echo why organizations lingered on deprecated Python 2.7 for over a decade. This stands in stark contrast to the modern agentic app stack, where corporate patronage and structural incentives create existential pressure: stay current or fall catastrophically behind. Python, for all its capabilities, just doesn’t operate on that clock.

RIP The Modern Data Stack
The Modern Data Stack either died or collapsed into itself this month, depending on whether you’re counting bodies or market caps. Fivetran and dbt are merging in an all-stock deal estimated at potentially over $10 billion, combining Fivetran’s 500-600M ARR against $5.6B valuation with dbt’s 100M ARR against $4.2B valuation. Supabase acquired Triplit, an offline-first database, continuing their quiet march toward becoming the full-stack infrastructure platform for developers who hate AWS. But the Fivetran-dbt merger is the story that matters, because it’s either the final consolidation of the Modern Data Stack or its death certificate.

The Inevitable Vertical Integration
Ingestion and transformation were always going to consolidate. The only question was which would absorb which. Turns out when one company has 5x the revenue of the other, the answer is generally straightforward. Previously, Fivetran acquired Census (reverse-ETL) and Tobiko (SQLMesh, a dbt alternative). Now they’re combining with dbt itself, creating a vertically integrated data pipeline platform that controls everything from source extraction to warehouse transformation. Is this 🦋 synergy, or a monopoly formation with better PR?

For CTOs evolving your company’s DataOps, this means SQLMesh is almost certainly dead. They won’t kill it outright, that would alienate the existing user base and trigger antitrust scrutiny, but expect them to stop adding features, making a switch to dbt not just necessary to keep up with data stack evolution but potentially an easier migration using Fivetran’s tooling. Classic acqui-kill playbook: inherit the users, sunset the product, convert them to the winner. Here we are again.

The other question is what happens to dbt-core (the open-source version) versus dbt Fusion (the commercial product). Fivetran has every incentive to push users toward the commercial version, which means dbt-core will either stay frozen at its current feature set or get “community-driven development” (read: slow death by benign neglect, another playbook classic.) If you’re building on dbt-core, start planning your migration strategy now before the decision gets made for you.

Snowflake’s pg_lake Counterplay
The same month as the Fivetran-dbt announcement, Snowflake released pg_lake: Postgres-compatible lakehouse formats. Not a coincidence. Fivetran-dbt consolidates the transformation layer. Snowflake’s pg_lake attacks the storage layer by making Postgres compatible with lakehouse formats (Iceberg, Delta, Hudi). The battle being fought: who owns the SQL interface? Fivetran-dbt wants to own the transformation SQL that runs in your warehouse. Snowflake wants to own the storage SQL that defines what a warehouse is.

If Postgres becomes the universal interface for lakehouse formats, Snowflake’s proprietary warehouse becomes one option among many rather than the default. Making Postgres compatibility a first-class feature is their hedge against commoditization. The subtext is clear: Snowflake sees the writing on the wall and is trying to stay relevant in a world where open formats (Iceberg, Parquet) eat proprietary warehouses.

DuckDB: The Quiet Assassin
While everyone’s watching the Fivetran-dbt merger, DuckDB is quietly tryna make the entire Modern Data Stack obsolete. Not through acquisition or market consolidation, but by solving the problem so elegantly that the stack becomes unnecessary.

DuckDB is an embedded analytical database that runs in-process. No server. No network calls. No connection pools. Just a library you import that can query Parquet files on S3, CSV files on disk, or Pandas DataFrames in memory, all using standard SQL. It’s SQLite for analytics, and it’s faster than most data warehouses for queries under 100GB.

The implications are staggering. The Modern Data Stack assumes you need:

Fivetran to ingest data into a warehouse

dbt to transform data inside that warehouse

Snowflake/Databricks to store and query that data

A BI tool to visualize it

DuckDB says: what if you just query the files directly? Parquet on S3 is already columnar and compressed. Why copy it into a proprietary warehouse format? Just point DuckDB at the bucket and write SQL. Transformations? Run them in DuckDB and write the results back to S3 as Parquet. Visualization? Connect your BI tool directly to DuckDB or use Jupyter notebooks.

The cost differential is obscene. A Snowflake query that costs $10 in compute might cost $0.02 in S3 data transfer with DuckDB. You’re paying 500x for the privilege of having your data in someone else’s proprietary format.

The Three-Way Battle for SQL’s Soul
Fivetran-dbt wants to own the transformation layer. They control how data moves and how it gets transformed, but they’re agnostic about where it lives. Their bet: the transformation logic is the moat, and they can charge rent on every pipeline regardless of the underlying warehouse.

Snowflake’s pg_lake attacks the storage layer by making Postgres compatible with lakehouse formats (Iceberg, Delta, Hudi). Their bet: if Postgres becomes the universal interface for lakehouse formats, Snowflake’s proprietary warehouse becomes one option among many. Making Postgres compatibility a first-class feature is their hedge against commoditization.

DuckDB is the anarchist in the room saying: why do you need any of them? Just use open formats (Parquet, Iceberg), store them cheaply (S3, GCS), and query them directly. No vendor lock-in. No data movement. No rent-seeking middlemen.

The battle being fought: who owns the SQL interface? Fivetran-dbt wants to own the transformation SQL. Snowflake wants to own the storage SQL. DuckDB wants to make the question irrelevant by making SQL so cheap and portable that vendor choice stops mattering.

Is the Modern Data Stack Actually Dead?
The Modern Data Stack narrative always had a problem: it assumed that data engineering was a separate discipline from software engineering. Fivetran for ingestion, dbt for transformation, Snowflake/Databricks for warehousing, Looker/Tableau for BI. Each layer had its own vendors, its own tooling, its own pricing model. The result was a Rube Goldberg machine where moving data from A to B required six vendors, four different teams and at least three coffee runs.

The consolidation is inevitable. Supabase acquired Triplit because they realized offline-first databases are the future of edge computing. Fivetran merged with dbt because charging separately for ingestion and transformation was leaving money on the table. Airbyte (which raised $150M at $1.5B in 2023) is watching nervously and trying to figure out if they’re next or if they can survive as the “open-source alternative.”

The real winner here is SQL. Not Spark SQL, not Presto SQL, not proprietary query languages, just SQL. The Modern Data Stack was always a bet that SQL is the universal interface for data operations, and the consolidation is proving it right. Every tool in the stack compiles down to SQL in the warehouse. The vendors are just fighting over who gets to generate that SQL and collect the rent.

Is the Modern Data Stack being displaced by observability?
But there’s a darker reading, and it’s the one that should concern you more: is the Modern Data Stack being displaced by observability? The 360° view of data used to require a data warehouse, a transformation layer, and a BI tool. Now it requires an observability platform that captures data at ingestion, indexes it in real time, and surfaces insights without transformation. Datadog, New Relic, and Splunk are eating the MDS from below by making data warehouses feel slow and expensive. (While DuckDB is also gaining traction as a backend for log and observability data analysis.)

The shift is subtle but real: companies are moving from “store everything and query later” to “stream everything and filter in real time.” The Modern Data Stack was built for batch processing. Observability 2.0 is built for real-time. The batch world is shrinking, and the vendors who can’t move to streaming are about to get consolidated into irrelevance. And we all know how that story ends.

The Modern Data Stack assumed data engineering was a separate discipline requiring specialized tools distinct from software engineering workflows. But as data volumes increased and latency requirements tightened, the batch-processing paradigm showed its limits. Why store data in a warehouse, transform it overnight, and query it in the morning when you could stream it, transform it in-flight, and query it in real time?

The consolidation reveals two competing futures: fully integrated platforms (Supabase for transactional, Databricks for analytical) or composable open-source tooling (Airbyte, dbt-core, DuckDB) with no middle ground. The vendors charging rent for the middle are running out of road.

Industry Impact
Snowflake’s pg_lake is a defensive move. If Postgres becomes the universal interface for lakehouse formats, Snowflake’s proprietary warehouse becomes one option among many rather than the default. Making Postgres compatibility a first-class feature is their hedge against commoditization; an admission that even Snowflake sees the open-format future coming.

This consolidation is a signal that the MDS was always a transitional architecture. The future is either fully integrated platforms (Supabase for transactional, Databricks for analytical) or composable open-source tooling (Airbyte, dbt-core, DuckDB), with no middle ground. Vendors charging rent for the glue between systems are being squeezed from both sides.

What This Means for CTOs
For CTOs running Modern Data Stack implementations, this creates immediate planning pressure. If you’re running SQLMesh, start planning your migration to dbt now. The announcement will come eventually, but waiting for it just compresses your timeline. If you’re evaluating data pipeline solutions, assume Fivetran-dbt is the default and ask why you should fragment your tooling. But the bigger question is whether you need a Modern Data Stack at all. If observability platforms plus a lakehouse (Databricks, Iceberg, DuckDB) gets you 80% of the value at 30% of the cost, why maintain the additional complexity?

CTO Playbook: 30/60/90 (Modern Data Stack)
DuckDB Proof-of-Concept (HIGH PRIORITY - 30 days): Identify one analytical workload currently running in Snowflake/Databricks with <100GB working set. Reimplement using DuckDB querying Parquet on S3/GCS. Measure: query latency, cost per query, data transfer costs, developer time to implement. Deliverable: Side-by-side cost comparison showing actual spend (warehouse credits vs S3 access), performance benchmarks on representative queries, decision memo on whether to expand DuckDB usage.

Lakehouse Format Migration Assessment (HIGH PRIORITY - 30 days): Audit current data storage: percentage in proprietary warehouse formats vs open formats (Parquet, Iceberg, Delta). For data still in proprietary formats, document: migration cost, downstream breaking changes, vendor lock-in risk if pricing increases 2x. Deliverable: Migration plan with ROI calculation (cost to migrate vs cost savings from open formats), prioritized backlog of tables to convert, break-even timeline.

Real-Time vs Batch Architecture Decision (MEDIUM PRIORITY - EOY): Map all analytical workloads to latency requirements: can decisions wait for overnight batch (MDS), need hour-level freshness (streaming + lakehouse), or require sub-minute visibility (observability platforms). Document which workloads are mis-architected (using expensive real-time infrastructure for batch-suitable queries or vice versa). Deliverable: Architecture decision matrix, cost optimization opportunities, timeline for right-sizing infrastructure per workload.

SQLMesh Deprecation Plan (MEDIUM PRIORITY - EOY): If running SQLMesh, create migration roadmap to dbt with: (1) automated conversion tooling for existing transforms, (2) parallel run period (both systems operating, validating output parity), (3) cutover criteria and rollback plan. If not on SQLMesh, document strategy if Fivetran sunsets other acquired tools (Census, Tobiko). Deliverable: Migration project plan with resource requirements, compatibility test results, stakeholder sign-off on timeline.

Vendor Concentration Risk Analysis (LOW PRIORITY - 90 days): Calculate percentage of data infrastructure spend going to single vendor (Snowflake, Databricks, Fivetran-dbt post-merger). If >40% with one vendor, document: alternatives with equivalent capabilities, cost to migrate, negotiation leverage. For Fivetran-dbt specifically, assess whether vertical integration creates pricing power that eliminates competitive pressure. Deliverable: Vendor risk scorecard, negotiation strategy for next renewal, multi-vendor architecture options if current concentration is unsustainable.

Risk, Security & Compliance
Following up on August’s SharePoint hack for anyone who doubted its criticality: foreign hackers breached a US nuclear weapons plant via SharePoint flaws.

The CVE-2025-49596 remote code execution vulnerability that Microsoft initially described as “moderate severity” just compromised classified national security infrastructure.

This isn’t a “patch your systems” reminder. This is a “your entire threat model is wrong” alarm. The attack chain went: SharePoint vulnerability → network pivot → exfiltration of sensitive data from a facility that processes nuclear materials. The vulnerability was exploited in the wild for months before the breach was detected. Microsoft’s response was to issue a patch and move on. No acknowledgment of the offshore engineering team that maintains SharePoint on-prem. No explanation of how a “moderate severity” bug became a nation-state attack vector.

For CTOs, the lesson is blunt: SaaS vendor security ratings are theater. Microsoft has SOC 2, FedRAMP, every compliance cert you can name. They still shipped a vulnerability that compromised a nuclear weapons facility. The next time a vendor shows you their security questionnaire, remember that compliance certifications are about covering liability, not preventing breaches. The modern threat model assumes your vendors are compromised, your supply chain is hostile, and your perimeter doesn’t exist. When we say zero trust architecture, we mean it.

At The Agentic Threshold
This month revealed the infrastructure gaps we’re carrying into the agentic era. We’re building systems capable of infinite accumulation but incapable of graceful failure. That mostly worked when systems retrieved information. It’s catastrophic when systems take action. The agentic projects that get canceled won’t fail because the technology doesn’t work. They’ll fail because organizations didn’t architect for the reality that autonomous agents require fundamentally different infrastructure patterns than conversational AI. Stateless pipelines versus stateful runtimes. Compile-time safety versus runtime suggestions. Platform-integrated agents versus browser-based distribution.

The companies pulling ahead are the ones that recognized this early and made hard architectural choices: one pattern per use case, observable agent behavior as infrastructure, graceful degradation by default. The companies falling behind are still treating agents as “ChatGPT with API access” and wondering why their pilots can’t graduate to production.

We’re not growing too fast, we’re growing without the architectural foundation to support what we’re building. The next year will separate organizations that understand this from those that don’t. Your infrastructure decisions today determine whether you’re automating the future or writing postmortems about why an agent took down production.
