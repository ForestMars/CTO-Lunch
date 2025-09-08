- Dyson bubble → token pricing
    - Pattern of honesty issues dating back to the 2023 release delays ("too dangerous" claims)
    - snatching defeat
        
        Yet buried beneath this spectacle was a quiet triumph that revealed the true dysfunction at play. To understand the magnitude of what OpenAI's product lead Kevin Weil has accomplished, we need to consider the historical context of OpenAI's pricing cliff. When GPT-4 launched, output tokens cost a staggering $60 per million. GPT-4 Turbo cut this to $30, and GPT-4o slashed it further to $15 per million, a 75% reduction that already seemed impossible to sustain profitably.
        
        Then Weil pulled off what may be the greatest "have your cake and eat it too" maneuver in API economics history. GPT-5 launched at $10 per million output tokens, another 33% price cut, while simultaneously introducing semantic caching with a 90% discount that brings cached tokens down to just $0.125 per million (that’s *output* tokens, not input.) But here's where the magic happens: this isn't just customer savings, it's supply-side genius.
        
        Every cached token that saves customers 90% also saves OpenAI 90% of the compute cost, but the semantic matching infrastructure was already built into their system. Meanwhile, the base model efficiency improvements mean GPT-5 uses 22% fewer output tokens while delivering superior performance. The result? OpenAI can offer customers savings that compound—lower base prices plus massive caching discounts—while their own costs plummet even faster.
        
        For high-volume enterprise applications, this pricing model is devastating to competitors. A developer making repeated API calls can see costs drop from the original GPT-4's $60 per million to as low as $0.125 per million with caching—a 99.8% reduction over 18 months—while getting dramatically better performance. OpenAI simultaneously captures market share, improves margins, and makes competition economically impossible.
        
        In any rational universe, engineering a pricing strategy that cuts customer costs by orders of magnitude while reducing your own supply costs would be hailed as a career-defining achievement for any CPO.
        
    - OpenAI released **GPT-4o**, a more efficient and powerful successor to GPT-4.
    - With it came a landmark price drop: output tokens were slashed from **$60 to $15** per million, and input tokens dropped from $30 to $5 (so, $5/$15)
    - $1.25 per million input tokens and $10 per million output tokens. ($1.25/$10)
    - This was a direct, aggressive move to win the code-assistant market, as it made high-volume, long-context workloads significantly cheaper than GPT-4o and its competitors. For example, it was a 50% price cut on input tokens compared to GPT-4o.
    - It also included a **90% discount** for cached input tokens, a feature that provides massive savings for applications with repeated prompts, such as developer tools.
    - Because OpenAI has an out of control CEO who doesn’t know how to share the glory. Honestly, when was the last time you heard him genuinely praise a team member? OpenAI likes to say it’s because it’s a team effort, but that seems like just whitewashing Sama’s need to hog the spotlight.
