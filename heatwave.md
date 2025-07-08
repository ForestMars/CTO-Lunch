- wtf
    
    Tech's heatwave didn’t let up in June—just ask anyone sweating out the GPU backlog or threading AI stack rewrites into their quarterly planning. While OpenAI put its cash cannon to work, Meta went all in on open weights, and Apple snuck new model specs into a WWDC that mostly tried to keep its head down. The AI arms race is now fully agentic, and the money’s flowing accordingly. Meanwhile, the developer stack got a jolt with more evidence that workflows—not just models—are the new frontier.
    
    If you’re a CTO, this is the moment to ask whether your infra is keeping up with the velocity, not just of models, but of the way people are using them. Real capabilities are coming online fast—but so are all the ways they can break, drift, leak, or cost you 7 figures in wasted GPU time. If you’re here, you’re not just paying attention—you’re adjusting:
    
    Meta: The Open Weights Gambit
    Context and Background
    Meta finally dropped LLaMA 3 405B (they skipped 180B), a dense model trained on 15T tokens with a 128K context window and top-tier SWE-Bench results (73.7%). Alongside it: the LLaMA Code family, with 8B/70B variants specifically for software engineering, all open weights and Apache 2.0. They also released a new Agent framework (Meta AgentKit) and are trying to capture the OSS developer community in a pincer move between infra and tooling. All this while whispering about 2025’s 1.8T parameter LLaMA 4, which is already training.
    
    But the real flex wasn’t just weights—it was LLaMA’s ability to outperform Anthropic and OpenAI on core code tasks while staying fully open, even if inference costs make production adoption tricky.
    
    Technical Specs
    Meta LLaMA 3 405B: 15T tokens, 128K context window, 73.7% SWE-Bench Verified.
    Meta LLaMA Code: 8B/70B variants, optimized for code; open weights, Apache 2.0.
    Meta AgentKit: New agentic inference and workflow orchestration framework, designed for integration into Meta AI Studio.
    
    Industry Impact
    Meta’s open strategy is a shot across the bow of Anthropic’s enterprise safety and OpenAI’s commercial moat. For CTOs, it unlocks serious agent experimentation without black-box costs or vendor lock-in—but requires infra tuning and cost scrutiny to match closed-model UX. AgentKit’s success depends on real-world adoption; keep an eye on early dev feedback.
    
    OpenAI’s Cash Mode
    Context and Background
    Altman’s checkbook is open. OpenAI launched a GPU cluster financing program, investing billions in custom datacenter build-outs to lock in future compute. They’re also backing third-party agent startups with prebuilt GPT-4-o integrations (e.g. Corgi, Vanna). Meanwhile, their own model took a backseat to the growing network play around it. No new models were released in June, but the infrastructure moves are telling.
    
    Also notable: the quiet sunset of ChatGPT search, reportedly due to low usage. Indirect confirmation that browser-style use cases may not be the stickiest—or that plugin-era frictions never fully resolved.
    
    Technical Specs
    GPU Financing: \$8B program targeting custom NVIDIA H100 clusters for enterprise resale; first partner expected Q3.
    Corgi: LLM-native code agent, trained on GitHub diff logs and PR metadata. 3x throughput of GitHub Copilot on benchmarked task set.
    Vanna: SQL-autocomplete agent using GPT-4-o backend; now bundled into Snowflake trials.
    ChatGPT Search: Sunset without official postmortem. Usage reportedly under 1%.
    
    Industry Impact
    OpenAI’s evolving from lab to platform operator—and funding its ecosystem accordingly. For CTOs, the key takeaway isn’t the product—it’s the architecture. If you’re betting on GPT-4-o, watch the emerging toolchain (like Corgi) to see where productivity shifts. But don’t expect everything to stick; search didn’t.
    
    Apple's Quiet Power Play
    Context and Background
    WWDC mostly flew under the radar, but buried in the releases was a major move: Apple will run server-side foundation models for Siri upgrades, starting with Apple Intelligence later this year. These are Apple’s own models, not OpenAI’s. Despite headlines, GPT integration is limited to fallback scenarios, with strict user opt-ins.
    
    Behind the scenes: Apple trained a 200B+ parameter model for on-device summarization and intent detection. Benchmarks suggest it's not SOTA, but the OS-level integration is where the leverage lies. Also: Apple is working on a fine-tuning API for developers building on-device agents.
    
    Technical Specs
    Apple Intelligence: Hybrid server/on-device agent architecture, launching with iOS 18.
    On-device model: 3B param class; \~200B server model running in Apple datacenters.
    Privacy Layer: Local execution by default; server-side opt-in via Private Relay.
    
    Industry Impact
    Apple’s play isn’t to win benchmarks—it’s to own distribution. With 2B devices and OS-native hooks, their agents will ship by default. For CTOs building consumer apps, this is a wake-up call: agents are going mainstream at the OS level. Plan integrations or risk obsolescence.
    
    The Stack Gets Agentic
    Context and Background
    From code to workflows, June saw an acceleration of agent-focused infrastructure. Replit released their Code Agent Framework with integrated state management and memory. Sourcegraph’s Cody shipped v1.0 with live context indexing. LangChain announced LangGraph 0.1, their new execution engine built for hierarchical plans and memory-backed sub-agents.
    
    And Microsoft? They announced AgentFlow, which brings Power Automate-style logic to agents, and started seeding it across Azure accounts. Also: whisperings of Github Copilot Enterprise agents launching in Q3.
    
    Technical Specs
    Replit CodeAgent: Multi-hop state machine for dev workflows, integrated into Replit Ghostwriter.
    LangGraph 0.1: DAG-based planning, sub-agent execution, memory-backed context.
    Sourcegraph Cody 1.0: Real-time code index integration, full local context window.
    Microsoft AgentFlow: Logic builder for orchestrating GPT-based tools; preview for enterprise Azure users.
    
    Industry Impact
    The agent wars have moved down-stack. Every tool is becoming agent-aware. For CTOs, this means rethinking workflows, not just prompts. It’s less about chatbot UX and more about letting agents own entire lifecycle tasks—from triage to PR. That’s real leverage, if you can operationalize it.
    
    One More Thing…
    Claude now has an API for memory. For CTOs building SaaS, that means you can sync user state into Claude across sessions. Think onboarding, config recall, customer context. It’s early, and there are limits—but it’s the start of persistent agents as a real app pattern.
    
    See everyone at lunch.