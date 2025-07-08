- CTO Lunch 7 draft2
    
    Tech continues to propagate at a relentless clip, and this month brought a fresh batch of shifts that cut to the core of what we do as CTOs. AI labs inked new leases, talent wars hit a fever pitch, and security incidents shuffled the deck overnight. If last month felt wild, June was bonkers—and New York’s center stage glow only got brighter.
    
    This month made one thing clear: the AI arms race is moving from the lab to your boardroom—and your budget. Here’s what just changed, and why you’ll feel it sooner than you think.
    
    ---
    
    **NYC: New Leases, Robotaxis, and Legal Pressure**
    
    *Context and Background*
    
    TECH WEEK by a16z (”DIY at scale”) wrapped with private salons and public keynotes but eclipsed by the OpenAI in the news juggernaut claiming 90,000 sq ft at the Puck Building (295 Lafayette St) in SoHo. AsT ech Week’s  rooftop panels wound down, Waymo test cars quietly hit Manhattan streets. Meanwhile, the NYT’s lawyers asked a court to compel OpenAI to preserve every bit of ChatGPT and API data. And yes, don’t click TheTechclusive unless you have emotional armor.
    
    Technical Specs
    
    - Tech Week by a16z (attendance figures, key numbers)
    - OpenAI’s first NYC office: 90K sq ft, Puck Building (lease was signed October 2024; how much are they paying? How many employees will work there?)
    - Waymo NYC trials expanded; randomized rider reports ~~via Fox 5 NY.~~
    - Legal motion: NYT demands preservation of consumer ChatGPT and API logs.
    - TheTechclusive launches (need key metrics here)
    
    Industry Impact
    
    NYC CTOs must brace for stricter data‑retention policies and public autonomy debates. Between soaring real estate and legal discovery risk, factor both into your next office expansion or compliance sprint. And if your UX team wants to demo self‑driving UIs, book Waymo now—before a fresh outage claim hits headlines.
    
    ---
    
    **AI Talent Wars & Shopping Sprees**
    
    *Highlights to be included:*
    
    - CTO Salaries average = $2.5 million
    - Meta “accused” of offering $100M signing bonuses
    - Meta acquires Scale AI for $14 billion
    - Apple in talks to buy Perplexity for similar amount
    - Meta poaches OpenAI scientists (triggering one week shutdown in operations)
    
    *Context and Background*
    
    Meta’s 49% stake purchase in Scale AI set off tremors: literally hours later, Google paused multiple Scale projects (it had spent $150M last year), while some investors jumped ship. Meta’s also courting AI‑VCs Friedman & Gross and quietly compiling top‑engineer hit lists. Even OpenAI and xAI hit pause on Scale engagements, and rumors swirl about projects paused for bio‑prompt tuning.
    
    Technical Specs
    
    - Meta acquires 49% of Scale AI; founder Wang retains control.
    - Google: ~$150M annual spend (20% Scale revenue) paused.
    - Investor exits: some selling stake, citing Big Tech client losses.
    - Meta recruiting blitz: 100M‑bonus rumors, top‑engineer lists from The Guardian leak.
    - Mira Murati’s Thinking Machines Lab Secures $2 Billion Funding, Signals High-Cost Push for Agentic AI
    - Grammarly acquires Superhuman ($825M valuation in 2021; $35M ARR).
    
    Industry Impact
    
    The big platforms are stockpiling talent and tooling. If you’re negotiating retention packages or vendor agreements, expect counter‑offers to land in your inbox—alongside a stack of NDAs. And remember: a vendor pause can be a survival tactic, not a sign of failure.
    
    ---
    
    **OpenAI Woes: Outage, Exodus, Funding**
    
    *Highlights to be included:*
    
    - Day long outage on June 10
    - Microsoft threatens to cool relationship
    - New York law makes demands on OpenAI
    - New York Times request OpenAI violate their users privacy
    - OpenAI accuses Meta of offering $100M signing bonuses. (No one bats an eye.)
    - Meta actually does steal 4 of their top scientists
    - OpenAI literally shuts down for a week (apparently in response)
    
    *Context and Background*
    
    OpenAI’s June 10 outage—nearly a day offline—came as senior researchers bailed for Meta. References to the Jony Ive hardware tie‑up vanished after Iyo’s trademark suit. Meanwhile, Microsoft hinted it might walk from deep integration talks pending OpenAI’s shift from nonprofit roots to a public‑company structure.
    
    Technical Specs
    
    - June 10 ChatGPT outage: ~22 hours downtime.
    - Jony Ive partnership removed amid Iyo lawsuit.
    - MSFT talks on hold until corporate restructure; IPO roadmap uncertain.
    - o3 Pro: marketed stronger than o3 but underperforms on agentic tasks; high cost, low trust.
    - Bindu Reddy: o3 Pro fails agentic‑coding benchmarks vs o3 (X.com status).
    - o3 price drop sparked via Twitter chart (pbs.twimg.com).
    
    Industry Impact
    
    If your roadmap leans on OpenAI SLAs, build contingencies. Outages and licensing pulls can leave teams scrambling. And when your CFO asks about future fees, remember that “enterprise” pricing can shift on a single tweet.
    
    ---
    
    **Model Pricing Models**
    
    *Highlights to be included:*
    
    - Gemini 2.5 Pro’s Dual-Tier Pricing at $1.25–$2.50 per Million Tokens Boosts Enterprise Adoption (Gemini pricing doubled)
    - Claude 4 Sonnet’s $3 per Million Token Pricing Targets Premium Enterprise AI Applications; Claude 3 weights will not be released as OSS but fully deprecated.
    - DeepSeek-V3’s Ultra-Low Pricing of $0.20 per Million Tokens Disrupts AI Market with Open-Source Power
    - OpenAI Slashes GPT-4o Pricing by 26%, Competing with DeepSeek and Gemini at $1.85 per Million Input Tokens
        - o3-pro pricing?
    - Baidu’s Ernie Model Goes Open-Source by June 30, Offering Free AI Chatbot to Expand Market Reach
    
    *Context and Background*
    
    Google’s June preview rolled out Gemini 2.5 Flash, then quietly doubled input/output rates. No more “thinking” vs “non‑thinking”—just one blended, higher price that’ll sting on large‑scale inference.
    
    Technical Specs
    
    - Input (text/image/video): $0.15 → $0.30/million tokens
    - Audio: $1.00/million tokens (unchanged)
    - Output: $0.60 (non-thinking) → $2.50/million tokens; $3.50 thinking tier unchanged
    - Gemini 2.5 Pro GA: 1M token context, 64K max output
    
    Industry Impact
    
    API costs are rising faster than SLAs. Re‑benchmark your projected inference spend—especially for multimodal or chat use cases. And if Anthropic’s $200 plan looks cheaper, plug your real‑world volumes into both calculators before doubling down.
    
    ---
    
    **She Ain’t Heavy, She’s My SDLC** 
    
    *Context and Background*
    
    This June, updates across Node.js, Bun, Deno, and Deno Deploy showcased a strong industry push to simplify and speed up the software development lifecycle (SDLC) through native TypeScript support, zero-config environments, and unified runtimes. Node.js 24.3.0 enhanced direct `.ts` execution and `import.meta.main` detection, moving closer to first-class TypeScript integration. Bun 1.2.16 strengthened its all-in-one runtime with improved file-based routing and Node compatibility. Meanwhile, Deno 2.4.0, released on June 26, continued its standards-first approach with native bundling, OpenTelemetry integration, and WASM improvements, while Deno Deploy’s Early Access updates focused on frictionless cloud deployment by adding storage, secret management, and automatic framework detection. Together, these advances reflect a broader shift toward toolchain consolidation, faster iteration cycles, and prioritizing developer experience over configuration complexity.
    
    In contrast, the Go ecosystem’s approach to observability remains more layered and complex despite notable progress. OpenTelemetry’s metrics SDK, while improving, continues to lag behind Prometheus in usability. Prometheus offers a stable, minimal API with native pull-based scraping and straightforward setup, whereas OpenTelemetry demands layered abstractions, collector infrastructure, and verbose configuration to deliver comparable metrics.
    
    Noteworthy June announcements illustrate this divide: a June 5 guide for securely exposing the OpenTelemetry Collector in Kubernetes with mTLS, the June 12 release of OpenTelemetry spec v1.46 introducing enhanced Prometheus schema compatibility, Grafana’s June 16 update splitting and refining Prometheus integrations into dedicated AWS and Azure plugins, and Splunk’s June 25 donation of the “OTel Injector” to simplify automatic instrumentation for Go applications. These milestones improve security, interoperability, and automation, yet OpenTelemetry’s Go metrics SDK remains heavier and more intricate than Prometheus’s lean, pull-based model—affirming that for many Go teams, Prometheus still provides the cleaner, more reliable path to production metrics.
    
    This theme was echoed at SRE Day in Amsterdam on June 27, 2025, where the community spotlighted the evolving observability landscape. While OpenTelemetry’s recent strides, including the June 26 Deno 2.4 release with OpenTelemetry support and the spec and tooling updates earlier that month, signal steady progress, many attendees reaffirmed that Prometheus remains the more straightforward and dependable choice for production metrics in Go environments. This preference underscores a broader industry reality: simplicity and reliability often outweigh the appeal of all-encompassing but complex solutions.
    
    Technical Specs
    
    - Node 24.3.0: direct `.ts` execution; `import.meta.main`.
    - Bun 1.2.16: enhanced file‑based routing; Node compatibility.
    - Deno 2.4.0: native bundler; WASM & OTel client.
    - Deno Deploy EA: storage + secret management; passive framework detection.
    - OpenTelemetry Spec v1.46: adds Prometheus schema support.
    - Grafana & Splunk: new Prometheus adapters & OTel Injector donation.
    
    Industry Impact
    
    Choose your DX battle: JS runtimes now blur build vs. runtime; Go shops still wrestle with layered OTel configs. At SRE Day Amsterdam, consensus was clear: if your team cares about minimal setup, Prometheus remains the safer path.
    
    ---
    
    **Supply Chains Under Attack**
    
    - Claude 3 weights will not be released as OSS but fully deprecated.
    - ransomware analysts at Halcyon warned that there were “indications that Scattered Spider is also now targeting the Food, Manufacturing, and Transportation (particularly Aviation) sectors in the US.”
    - confirmed by the FBI
    - mainly using social engineering attacks (to target supply chains)
    
    *Context and Background*
    
    Scattered Spider’s social engineering storms hit Hawaiian Airlines and WestJet, bypassing MFA. Simultaneously, Qantas’s third‑party support platform leak exposed 6M customer records. These incidents underscore vendor risk in motion.
    
    Technical Specs
    
    - Scattered Spider: targeted airlines via MFA bypass; FBI alert via TechCrunch.
    - Qantas Breach: 6M records exposed; Reuters report confirms.
    - Third‑party focus: common platform exploited.
    
    Industry Impact
    
    CTOs must vet and monitor every vendor route into production. Social engineering bypasses MFA. Train for breach and enforce granular access revocation. Supply chain security is critical! 
    
    ---
    
    **A Critical MCP Vulnerability**
    
    *Context and Background*
    
    A critical RCE (CVE‑2025‑49596) in Anthropic’s MCP Inspector was patched in June. This flaw let remote attackers execute code via crafted model contexts.
    
    Technical Specs
    
    - CVE‑2025‑49596: remote code execution in MCP Inspector.
    - Patch: June 2025 release; upgrade pipelines imperative.
    
    Industry Impact
    
    If you automate prompt chains, validate every library. AI pipelines introduce new RCE vectors; ensure your CI/CD enforces up‑to‑date dependencies and runtime sandboxing.
    
    ---
    
    **Legal, Compliance & Security (LC&S)**
    
    *Highlights:* 
    
    - *Genius Act Passed*
    - Raise Act passed
    
    *Context and Background*
    
    The RAISE Act passed June 12 (Assembly 95‑0 D, 24‑22 R; Senate 37‑1 D, 21‑0 R), mandating major AI labs publish safety protocols, risk evaluations, and incident reports under $30M penalties. Germany dumped Teams; Denmark ditched Windows for Linux. Atlassian’s new MCP variant was found vulnerable to exfiltration (“legal trifecta” by Simon Willison).
    
    Technical Specs
    
    - RAISE Act: reporting on severe risks, safety protocols; penalties up to $30M.
    - Atlassian MCP: prompt injection → data exfiltration (CATO Networks POC).
    - Germany/Denmark: enterprise migration to open‑source Office/libre stacks.
    - 2FA Warning: “If you’re not using a password manager + 2FA in 2025, you’re basically asking to get drained.”
    
    Industry Impact
    
    Regulation and open‑source preferences are colliding. CTOs must map policy deadlines, audit prompt pipelines, and prepare for forced transparency—and maybe swap proprietary suites for community‑driven alternatives.
    
    ---
    
    **Web3 & Crypto**
    
    Highlights: 
    
    - Stablecoins taking off.
    - Treasuries catching on
    - Quantum developments loom (decryption)
    
    *Context and Background*
    
    At the State of Crypto Summit, Coinbase & Shopify touted native crypto checkouts. Circle Internet Group’s $50B+ valuation raised eyebrows. Analysts see Solana, XRP, and Doge ETFs all but guaranteed. BlackRock pressed for in‑kind Bitcoin ETF redemptions. And IBM’s 2029 quantum roadmap looms over crypto security.
    
    Technical Specs
    
    - Coinbase x Shopify: in‑browser crypto payments demo.
    - Circle: ~$50B valuation; unclear revenue engine.
    - ETF Approvals: Solana, XRP, Doge near‑lock analysts say.
    - BlackRock IBIT: in‑kind creation/redemption request filed.
    - IBM Starling: 100M gate, 200 logical qubit fault‑tolerant quantum by 2029.
    
    *Industry Impact*
    
    CTOs in payments and custody should dust off quantum‑safe roadmaps. Crypto rails are migrating into mainstream stacks; factor in regulatory hooks for value transit and redemption models.
    
    ---
    
    **One more thing: Is Generative the New Web3?**
    
    *Context and Background*
    
    Blockchain’s dream of Web3 stalls outside niche use cases. Generative AI quietly claims the title: static → dynamic → generative.
    
    Technical Specs
    
    - Web 1.0: static HTML.
    - Web 2.0: dynamic platforms (Facebook).
    - Web 3.0: generative interfaces (ChatGPT).
    
    Industry Impact
    
    CTOs building next‑gen user experiences should ask: does your product need a chain, or just a smart prompt? The generative paradigm may eclipse tokenomics for mainstream apps.
    
    Until next month, see everyone at lunch.