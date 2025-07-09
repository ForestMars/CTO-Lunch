- final
    
    This month didn’t just accelerate; it splintered in all directions, with investors and founders racing to navigate a dynamic landscape rapidly being reshaped by AI, transforming everything from coding to infrastructure. OpenAI made big bets, Anthropic leveled up, and Google had its best I/O to date. Data systems rapidly evolved to meet AI-driven demands, consolidating legacy platforms and pushing new models for scale and workflow. Amid this upheaval, NYC’s tech scene grew quietly strong, while West Coast giants stumbled through costly deals and PR stunts.
    
    For CTOs, just keeping pace isn’t enough anymore, if it ever was. The real challenge is reading all these shifts as they happen and knowing which ones actually change your game plan. It’s no longer about what’s new; it’s about what’s real. (And what scales. And who’s paying attention.)
    
    ### **NYC Tech Economy Booming**
    
    New York’s tech landscape is no longer just Wall Street meets venture capital; it’s a full-throttle ecosystem, where DoubleClick’s legacy as digital ad pioneer still echoes, but today's story is all about AI startups, fintech disruptors, and big data center plays. NYC is rebooting itself as a gritty innovation hub that’s less Silicon Valley shine and more Brooklyn spine (albeit with a Manhattan portfolio.)
    
    ### **Technical Specs**
    
    - Economic Data: Tech employs 400,000+ in NYC (2025 estimate), with AI firms adding 15% growth year-over-year. Data center capacity expanded 20% since 2024.
    - Key Players: Startups like DoubleClick successors (e.g., AppNexus) and fintechs (e.g., Plaid) lead, backed by $5B in venture funding Q1 2025.
    - Infrastructure: 5G rollout covers 85% of Manhattan, supporting low-latency AI apps. Canvas tools enable seamless remote collaboration.
    
    ### **Industry Impact**
    
    NYC’s tech boom is a goldmine for CTOs; talent here is plentiful (with an increasing number of SF transplants) and the infrastructure to support serious AI workloads mere nanoseconds away from Wall Street. But real estate costs and regulatory hurdles  are real. Lean into our local talent for AI projects, but keep an eye on compliance; this isn’t a free-for-all like the dot-com days. (Unless you're day running meme coins, obviously.)
    
    ## **The AI ‘Rloveution’**
    
    ### **Context and Background**
    
    This was the month AI stopped pretending it knew what it wanted to be. OpenAI lit almost $10B on fire tryna buy a strategy (with Sama/Ive's "io" landing like an overdesigned shrug) then ghost-launched o3-pro with barely a whisper. Anthropic responded with tactical maneuvering and real upgrades, including the top benchmarked coding model, but buried them under “AI Safety Level 3” theatrics. (Literally the same week Eliezer Yudkowsky signed a female fan’s breasts.) Apple shipped an on-device model no one can use yet. All of which served to invite the question: is this really a revolution or just AI playing musical chairs while investors gets restless?
    
    ### Is Open AI Treading Water?
    
    OpenAI used to speak in grand terms about AGI and Superintelligence and nuclear launch codes and national security. Now they’re buying VS Code forks and sparring with Gary Marcus on X. They acquired Windsurf (ARR: $40M) for an astounding $3 billion (that’s a 75x multiple, which is eye-popping even by tech sector standards.) Windsurf is a money factory, sure, (expected revenue of $300M in 2025, which is 10x their 2024 income) but at that multiple, it’s unclear whether it actually moves the needle for OpenAI, or even whether it’s moving in the right direction. And no one should confuse this mini shopping spree with Zuckerberg’s acquisitions of WhatsApp and Instagram, which were clearly about scaling user bases and ecosystem consolidation, generally speaking the kind of thing you want to be spending the big money on. In contrast, it's unclear what exactly OpenAI is buying in Windsurf… (besides time.)
    
    ### Anthropic Goes to Defcon 3
    
    Seemingly in response to Open AI’s purchase of Windsurf, Anthropic pulled Claude from that app (though you can still use it with bring-your-own-key.) The big announcement tho was of course the release of their 4th generation models, Claude Opus 4 (72.5% SWE-bench, 43.2% Terminal-bench) and Sonnet 4 (72.7% SWE-bench) which being the high scorer led to it being heralded as the best coding model. But it’s ok, Gemini, we still love you anyway for your long context window (MRCR: 94.5% at 128k).
    
    Anthropic also introduced their (first) bug bounty program, aimed at testing the safety of their systems and activated “AI Safety Level 3” protections, so apparently SOTA AI is currently at DefCon 3.
    
    ### Apple: We’re Not Cooked Yet
    
    *"The software just didn't converge in the way we thought it would."*
    
    Not to be outdone, Apple introduced a new Foundation Models framework for iOS that gives developers direct access to a ~3B parameter on-device language model, with deep Swift integration for those still pretending they enjoy writing Swift (I kid, I kid.)
    
    They also introduced “vibe coding” in XCode, following the wake of controversy over what vibe coding *really* means, as the rush of books to take advantage of this hot topic changed the definition of vibe coding to suit their own needs (much to Andrej Karpathy’s chagrin.) That’s the thing about vibes, tho.
    
    Meanwhile, Apple execs spent a week defending their AI strategy after quietly axing several major Siri upgrades that were trumpeted at WWDC; features that, as it turns out, “didn’t *converge* in the way we expected.” Which is Cupertino-speak for: we overpromised and underdelivered, sorry, bro. See you on the earnings call.
    
    Almost seeming to justify their misses (based on the timing anyway) Apple published a new paper co-authored by their senior AI director Samy Bengio that generated quite a lot of buzz around the idea that models don’t actually think. Or to be more precise: all models have an upper bound on problem difficulty. Response was swift and brutal with several parody papers noting that since humans also have an upper bound, perhaps the problem is that humans don’t actually reason themselves (which was actually a trenchant critique of what most people took to be the authors’ claim) as well as directly addressing the question Can Language Models Reason? (A: [No, because that would be scary](http://pbs.twimg.com/media/Gs6bchFbYAAw4ai?format=png&name=medium).)
    
    ### **Technical Specs**
    
    - **OpenAI** paid $3B for Windsurf ($300M ARR expected in 2025, reflecting 10x growth over 2024; o3-pro scores 63.8% SWE-bench.
    - **Anthropic**: Claude Opus 4 (72.5% SWE-bench, 43.2% Terminal-bench), Sonnet 4 (72.7% SWE-bench) set new records for any models.
    - **Google**: Gemini 2.5 Pro: 1M token context window (2M planned), 64K max output tokens, 63.8% SWE-Bench Verified, excels in deep reasoning for coding and complex tasks. Gemini 2.5 Flash: 1M token context window, 24K max thinking budget, ~50% SWE-Bench Verified, optimized for low latency with 700+ t/s Vertex throughput, prioritizing speed over reasoning depth.
    - **Apple** Foundation Models: ~3B parameter on-device model, Swift-integrated, for iOS apps. Siri features shelved due to “quality convergence” issues.
    - **DeepSeek**: Their May 28th update (R1-0528) to DeepSeek R1 puts performance on par with OpenAI o1, *but open-sourced and with fully open reasoning tokens.* It's 671B parameters in size, with 37B active in an inference pass, and available from 7 providers [through openrouter](https://openrouter.ai/deepseek/deepseek-r1-0528/providers).
    - **io**: Totally unclear specs bc there’s no actual product announcement, just a treacle video that wrapped itself in nostalgia but gave no technical details.
    
    ### **Industry Impact**
    
    OpenAI’s acquisitions are buying time, not strategy. It’s also unclear if they are really aware of how bad the io video flopped, or in denial about that. Anthropic’s generative coding lead and safety push have big appeal for enterprise, though the Defcon 3 thing  feels a bit theatrical. Meanwhile Google is quietly leveraging Google’s established position to AI all the things with a focus on real-time multimodal capabilities (Astra, AI Mode) and creative tools (Flow, Veo 3) that differentiates it from Anthropic’s enterprise and safety focus and OpenAI’s general-purpose agentic approach. Apple’s framework is a developer win, but Siri’s flop dents their credibility yet again.
    
    CTOs: ignore the bluster and focus on tools with *proven* ROI. Altman’s got none of Jobs’ taste; we could be seeing a $30B train wreck in slow motion. Read [The Illusion of Thinking](https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf) paper, don’t just read *about* it.
    
    ## **AI Code Generation Surge**
    
    ### **Context and Background**
    
    So how is AI code generation going?  GitHub Copilot made a remarkabe $500M ARR in 2024, launched their new agent, while OpenAI (who *lost* $5 BILLION in 2024) added their Codex agent to ChatGPT; meanwhile, Google’s agent Jules went into beta. Tech giants rushed to brag their stats, with Microsoft, Google and Meta all claiming AI is now generating 20-30% of the code they’re shipping. So apparently we’re back to counting loc. Sorry to anyone who thought we laid that ghost to rest.
    
    Klarna, who loudly proclaimed to be replacing their workforce with AI became a political football in all this, with competing PR firms placing stories both that their much heralded use of AI to replace employees was [backfiring spectacularly](https://www.msn.com/en-in/money/topstories/klarna-s-ai-replaced-700-workers-now-the-fintech-ceo-wants-humans-back-after-40b-fall/ar-AA1F08eX) and also that their [revenue per employee had skyrocketed](https://techcrunch.com/2025/05/19/klarnas-revenue-per-employee-soars-to-nearly-1m-thanks-to-ai-efficiency-push/). Sorry to keep you in suspense which is actually true. Klarna also ended their SalesForce partnership, which is ironic (in the *Alanisian* sense) because if there’s another CEO who’s been as vocally bullish as Klarna’s about AI reducing headcount, it’s Marc Benioff. (With Nadella and Krishna getting place and show respectively.) And then there was the Buider.ai code gen scandal (not to be confused with the completely innocent [builder.io](http://builder.io/)!) revealing that the AI you replace your employees with might just be different employees in a far off place, and not actually AI at all.
    
    But mechanical turk startup scams aside , how good is all this code slop? Firecrawl, the model-first, prompt-driven data transformation pipeline to “turn websites into LLM-ready data" have been [looking to hire](https://techcrunch.com/2025/05/17/y-combinator-startup-firecrawl-is-ready-to-pay-1m-to-hire-three-ai-agents-as-employees/) not 1 but 3 AI coding agents to add to their team (up to $1M TC) but haven’t found a single one worth hiring yet, out of 50 ‘applicants’ so far. (But as they say on the other side of the GPU custody battle, “we’re so early.”)
    
    ### **Technical Specs**
    
    - **Copilot**: $500M ARR, powers 40% of GitHub’s coding workflows with Codex-derived models. GitHub Copilot now supports fully autonomous async agents for feature building, bug fixes, and refactoring.
    - **Codex**: agent powered by codex-1, a version of their o3 AI reasoning model optimized for software engineering tasks, with <1s latency.
    - **Jules**: Google’s agent, beta with 65% accuracy on WebDev Arena tasks.
    - **Builder.ai**: Blew through nearly $450M before anyone realized it was humans writing their “AI” code and they were caught round-tripping (circular billing) with partner companies complicit in their scam.
    - **Firecrawl**: Tests 50 AI agents; none meet the threshold for precision.
    - **Sourcegraph Amp**: Seeming to care quite a lot about precision in version numbering, released [version 0.0.1749312731](https://open-vsx.org/extension/sourcegraph/amp) of their VS extension AmpCode coding assistant. They are also producing a software bill of materials of [all the open source software used in Amp](http://x.com/GeoffreyHuntley/status/1929389876518216112) (coincidentally, software bill of goods was one of the Biden tech policies Trump reversed this month, see below.)
    - [**entelligence**](https://www.entelligence.ai/?ref=producthunt) released their Github app for code review and an official GitHub Action (ai-pr-reviewer) which you configure by adding a .github/workflows/ai-pr-reviewer.yml file; which configures their bot (e.g., @Entelligence.AI) to comment on your pull requests using environment variables eg. GITHUB_TOKEN and OPENAI_API_KEY.
    - [**OpenCode**](https://github.com/opencode-ai/opencode) is a Go-based CLI application (TUI) that brings AI assistance to your terminal.
    - **Xcode**: “vibe coding” suggests context-aware code snippets, but raises questions about how context aware Apple is. (and has no actual benchmarks claimed.)
    
    ### **Industry Impact**
    
    Copilot’s revenue proves AI coding’s traction, but 20-30% claims raise more questions than they answer; CTOs know quality’s the real test, obvi. Jules and Codex seem solid for prototyping but vibe coding’s still just a buzzword even if Apple wants to capitalize it (or just capitalize *on* it.) Firecrawl’s experience more than hints at overhyped agents. CTOs, plan for *real productivty gains* and don’t trust the hype. AI applying for jobs? We’re closer than you think, but not there yet.
    
    ## **Data Engineering**
    
    ### **Context and Background**
    
    The Postgres ecosystem is growing and consolidating at the same time. Databricks bought Neon for $1B to fold serverless Postgres into its AI stack, then arch-competitor Snowflake (who are betting big on Python and Iceberg) snapped up the last* remaining Enterprise grade Postgres service Crunchy Data for $250M (just a few weeks later); with Neon off the table, Crunchy was the only serious move left if Snowflake wanted to match Databricks on transaction credibility.
    
    At the same time, companies like Xata and FoundationDB are reimagining Postgres for modern, AI-driven developer workflows. Following the release of their Agent v0.2.0 in April, Xata relaunched as a full *Postgres at scale* platform, a fully pg-compatible service with instant copy‑on‑write branching, built-in PII anonymization, and storage/compute separation using NVMe/TCP; it’s fully vanilla Postgres on top of distributed storage. Meanwhile there’s a new pg extension aimed at FoundationDB ([pgfdb](https://fabianlindfors.se/blog/making-postgres-distributed/)) to use it as storage engine for a fully distributed (master-master!) Postgres.  It’s experimental, not officially supported (yet) but is one to watch.
    
    The broader data stack is fragmenting under the pressure of these AI-native demands. dbt is no longer just “T after EL,” pivoting hard into semantic layers with Mesh. Airbyte is shipping observability agents; DuckDB went server-mode; MotherDuck raised $52M to push it cloud-native. Dagster and Prefect are locked in a tight feature race. (Airflow 3.0, we hardly knew you.) And a new crop of startups (Piper, Decile, others) are building LLM-native ETL from scratch. The old extract-transform-load model is being torn apart and reassembled for a world where compute is cheap, data is messy, and latency matters less than alignment.
    
    ### **Technical Specs**
    
    - **Snowflake + Crunchy**: Snowflake acquires Crunchy Data (~$30M ARR, ~$250M deal), gaining Crunchy Bridge + full pgAdmin ecosystem; phased integration into Snowflake’s native Postgres connectors and Iceberg stack by or begins Q3.
    - **EnterpriseDB**: (EDB) is *technically* the last remaining independent enterprise grade postgres offering. No shade.
    - **FoundationDB**: pgfdb is an xperimental heap access method to use FoundationDB’s MVCC key-value store as a Postgres storage (engine) layer; fully stateless compute, globally consistent, master-master capable. Latency benchmarks show sub-10ms reads at scale; no WAL, no VACUUM. Wow.
    - **Xata**: Postgres on CloudNativePG with dynamic branching via NVMe/TCP and built-in PII masking. Xata Agent v0.2.0 enables persistent AI chat for workload diagnostics. Targets use cases across multi-tenant SaaS and developer self-serve.
    - **Supabase**: Implements end-to-end type inference across client, edge, and database using declarative schemas + TypeScript. Added vector search backed by pgvector 0.6, integrated with RLS and foreign data wrappers.
    - **Prisma MCP**: Modern control plane integrates Windsurf for hot-reload schema updates; enables programmatic GraphQL + SQL-type sync from one source-of-truth model. Optimized for full-stack TypeScript workflows.
    - **dbt Mesh**: Treats semantic layers as versioned, modular assets. Git-based governance, decoupled from warehouse execution. Supports federated modeling across domains, with DAG visualizations and schema diff tooling.
    - **Airbyte**: Adds OpenLineage metadata layer, improving impact analysis and observability; supports 350+ connectors with native CDC for MySQL, Postgres, and Mongo.
    - **DuckDB**: Now supports persistent multiclient sessions via DuckDB Server. Opens path to OLAP-in-place; supports Parquet, Arrow, and Hive metastores with zero-copy reads.
    - **Dagster**: Asset-aware orchestration with hybrid DAG execution across local and cloud runners. Refreshed UI integrates partitioned materialization state and backfill tooling. Python-native, declarative I/O.
    - **Piper**: LLM-native ETL layer combining prompt chaining with auto-synthesized SQL sketches. Experimental now, but shows potential in non-tabular extraction and schema suggestion.
    
    ### **Industry Impact**
    
    The modern data stack is splintering under AI pressure with Postgres poised to come into its fully distributed era. What used to be vertical is now branching. Xata and pgfdb mark the rise of stateless Postgres backends optimized for AI-native workloads. Supabase and Prisma are solidifying a new app-to-db type pipeline (which Typescript’s rewrite in Go extends to LLMs, btw) while DuckDB’s move to server mode sets it on a crash course with warehouse incumbents.
    
    For CTOs, now is the time to reassess Postgres workloads through the lens of distributed, stateless backends (like pgfdb, Aurora, and Xata) especially for AI-driven applications where latency tolerance and scalability matter. Embracing semantic modeling early is critical, as tools like dbt Mesh signal Git-native governance becoming the new baseline. Observability is no longer optional; comprehensive metadata lineage and asset tracking are essential for managing increasingly fragmented pipelines. Meanwhile, LLM-native ETL solutions such as Piper and Decile remain experimental but offer CTOs valuable insight into the future of data workflows. Given ongoing consolidation, it’s vital to rigorously test integrations and design architectures that allow for component swap-ability to avoid lock-in and hidden complexity.
    
    But ETL isn’t dead, it’s just grown a few extra letters. Call it ETLLLMMCP, stitched together with prompt chains, agents, and metadata sync.
    
    ## **SDLC Evolution**
    
    ### **Context and Background**
    
    Java just turned 30 though with a bit of a shrug, while JavaScript got Explicit Resource Management. TypeScript’s rewrite in Go (which Anders Hejlsberg cites LLM speed as one of the main drivers of) now has a TS compiler preview available via npm and front-end development are leaning harder into AI-fueled micro frameworks. It’s more of a quiet revolution (much like Java’s early days, some 30 years ago.)
    
    ### **Technical Specs**
    
    - **TypeScript Native**: Compiler rewitten in Go for 2x parsing throughput, enabling stateless builds and schema lifting; AST and symbol table synchronization with LLM prompt tokens via shared protobuf schema ensures 1-to-1 mapping between TS types and generative context in a bidirectional pipeline where type safety enforces prompt integrity and model completions inherit structural guarantees.
    - **JavaScript ERM**: Adds using declarations for resource cleanup, compatible with Node.js 22.
    - **Enzyme**: React testing library updated, supports hooks and context with 95% coverage.
    - **Prism AI**: Session replay analysis, integrates with Mixpanel; accuracy untested.
    
    ### **Industry Impact**
    
    TypeScript’s Go pivot is such a win: faster builds and type synergy with LLMs. Look out Python. ERM cleans up JS memory leaks, a must if your app needs to scale. Enzyme’s update aids testing rigor; Prism’s replay play needs validation with analytics suites. CTOs, upgrade stacks but verify integrations and remember: efficiency’s the goal, not a gimmick.
    
    ## **Legal, Compliance & Security**
    
    ### **Context and Background**
    
    Over on the LC&S side it’s feeling more and more like what you get when too many AI commiters are given access to a repo with no merge policy. It’s a circus. Meta’s mounting an “enshittification” defense against the FTC (“since when is it illegal to suck?”), while Disney and NBCUniversal just filed the first major Hollywood lawsuit against a generative AI company (Midjourney) in LA federal court. Trump’s tech EOs are piling up: zero trust is out, post-quantum crypto stays, AI gets mandated across K–12 education. That last move helped fuel Miami-Dade’s rollout of Gemini bots to 105K high schoolers, just as New South Wales discovered Microsoft Teams was quietly harvesting students’ voice and face biometric data with no prior consent. Privacy’s not for everyone, it seems (especially if you’re leaking secrets via Postman URLs.)
    
    ### US Cybersecurity Policy Updates
    
    President Trump’s Executive Orders  EO#13694 “Sustaining Select Efforts To Strengthen the Nation’s Cybersecurity and EO#14144 “Amending Executive  and Executive Order” reverses ‘much’ of Biden’s cyber policy. They preserve efforts around [post-quantum cryptography](https://www.axios.com/2024/08/13/nist-post-quantum-cryptography-encryption), advanced encryption standards, and [border gateway protocol security,](https://bidenwhitehouse.archives.gov/oncd/briefing-room/2024/09/03/fact-sheet-biden-harris-administration-releases-roadmap-to-enhance-internet-routing-security/) while hallmark programs tied to [software bills of materials](https://www.axios.com/2023/05/09/biden-software-bill-of-materials-cybersecurity), [zero-trust implementation](https://www.axios.com/2023/01/06/zero-trust-cybersecurity-white-house), and space contractor [cybersecurity requirements](https://www.axios.com/2023/08/22/space-cybersecurity-frontier-espionage) have been either rescinded or left in limbo
    
    ### **Technical Specs**
    
    - FTC v. Facebook: [Meta argues platform decay isn’t illegal](https://cdn.arstechnica.net/wp-content/uploads/2025/05/FTC-v-Meta-Motion-for-Judgment-5-15-25.pdf); case drags into 2026.
    - Disney/NBC v. Midjourney: Lawsuit cites 10,000+ infringing images, seeks $150M.
    - **Microsoft Team**s: [Collects voice/facial data since April 2025 with no opt-in](https://www.theguardian.com/australia-news/2025/may/19/nsw-education-department-caught-unaware-after-microsoft-teams-began-collecting-students-biometric-data).
    - Postman: Logs API secrets since v10.20, patched in v10.21.
    
    ### **Industry Impact**
    
    Postman’s slip-up demands immediate audits; CTOs, check your logs (but also, stop putting secrets in URLs, whether or not you are using Postman.) The Midjourney suit could redefine AI copyright; monitor outcomes. Trump’s policy flip keeps encryption but ditches zero-trust; time to assess your security stack. Miami’s chatbot push is bold, but NSW’s biometric snafu screams consent issues and Microsoft’s commitment. CTOs, tighten privacy controls; regulators *are* watching.
    
    ## **Web3 Whispers**
    
    ### **Context and Background**
    
    Web3’s not sleeping in June 2025; it’s throwing sparks, even if the hype’s less frothy than the old days. EMCD’s Spotlight Grant dropped on June 11, offering a $25,000 marketing package and free listing for Web3 projects in DeFi, GameFi, or Layer 2, targeting builders with live tokens ready to scale globally. It’s not just a cash grab; they’re vetting for community size and market cap, aiming for long-term players, not pump-and-dump scams. But speaking of, Pump.fun’s raise/offering hints at a funding play, but details are murky; more like pre-ICO hype with better branding. Meanwhile, Proof of Talk’s Paris summit on June 10-11 brought 10,000+ Web3 folks to the Louvre, with a Bittensor track and startup pitch comp for VCs. Honestly it felt like less of a conference than a deal-making pit. Nexa will be sponsoring the WAIB Summit in Monaco (June 27-28), showing off new tech at their booth, a sign Middle East money’s (still) flowing into Crypto. More on the tech side, Eclipse’s testnet now lets users pick fee lanes for speed or cost, and Quai Network’s merge-mined Layer 1 is pushing Proof-of-Entropy-Minima for real scalability. Ethereum gas fees are stable at 20-30 gwei. But then the price of ETH is stable at like 5 years ago. What cycle are we in again?
    
    ### **Technical Specs**
    
    - EMCD Spotlight Grant: $25K marketing package, free listing for one winner; two runners-up get 50% off. Open to DeFi, GameFi, Layer 2 projects with live tokens. Deadline TBD.
    - Proof of Talk: June 10-11, Paris, 10,000+ attendees, Bittensor track, Proof of Pitch comp for startups.
    - Eclipse Testnet: Modular gas markets for user-selected fee lanes (speed vs. cost).
    - Quai Network: Merge-mined Layer 1 (100K+ TPS, sub-100ms finality) using proof-of-Entropy-Minima consensus is a bold scalability play, but N1’s horizontal scaling (also claiming 100K+ TPS, sub-1ms latency) and developer-friendly VMs (EVM, TypeScript-native SDK) may have something to say, especially with its 01 Exchange testnet going live in June. (Quai’s mainnet is post-January 2025, while N1’s is still pre-launch, so it’s a real race of execution.)
    - Pump.fun: Raise targets $50M, tied to NFT/decentralized app ecosystem; terms unclear. But then that only seems appropriate for pump.fun. I mean, who actually reads the tokenomics?
    
    ### **Industry Impact**
    
    EMCD’s grant could juice up smaller Web3 projects, but applicant projects should expect to be grilled; too many ICO ghosts linger. Proof of Talk and WAIB Summit are networking gold for Web3 CTOs, but everyone knows the real value’s in side deals, not the keynotes. Eclipse and Quai’s tech pushes are worth a look for scalable dApps, especially if you’re building on Ethereum or eyeing DeFi. Pump.fun’s raise smells like hype, so wait for hard numbers before buying in. Web3’s may seem quiet lately, but  it’s just weeding out the noise. (Which can always be found on CT if you really miss it.)
    
    ## One More Thing…
    
    ### **Starbucks’ Green Dot Assist**
    
    Starbucks is rolling out “Green Dot Assist,” a Microsoft Azure OpenAI assistant for baristas, promising order optimization; it integrates with POS systems and analyzes orders in <2s (which is ofc an *eternity* if you haven’t had your coffee.) It’s definitely AI spotted in the wild but “less barista bot, more coffee whisperer.” Green Dot could streamline peak hours, but CTOs need to test reliability by placing extremely complicated coffee orders. Yes that’s a joke. No AI did not write this.
    
    AI however *is* writing something no one else wants to. Code comments! Which  apparently is the reason no one is commenting their code anymore (as if they ever did.) Comments in your code is now a sign (along with the infamous em-dash) that it was written by AI. Which raises the question though, why you don’t seen more em-dashes in code comments? 🤔
    
    Until next month, see everyone at today’s lunch!