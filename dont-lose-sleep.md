CTO Lunch NYC
CTO Lunch NYC

Don't Lose Sleep Over It
CTOs literally lost sleep over the us-east-1 outage. Here's how to make sure you're not one of them next time.
Forest Mars and CTO Lunch NYC
Oct 28, 2025

“It’s always DNS.”

“It’s always us-east-1.”

Corporate needs you to tell the difference between these two pictures. And when AWS has an outage, we don’t need Pam from the office to tell us, it’s the same picture every time. Because of course it was DNS in us-east-1.

For most companies, the sense of being protected was typically something like: we’re fine, we’re multi-region, we’re not in us-east-1. That confidence lasted right up until orchestration pipelines started freezing. As they did for a list of top companies longer than your DevOps team’s overnight Slack thread. Sure, it’s a good start (no business should have us-east-1 as an SPF), but it goes deeper than that. As we saw yesterday, for applications with baked-in control-plane dependencies at runtime, it doesn’t matter which region they’re running in. Runtime data-plane dependencies (including auth) were fine and stayed up. But the global control plane anchored in us-east-1 is still the single point of orchestration (and it’s not going to be fixed anytime soon.)

Monday’s outage was an architectural reckoning of which companies’ cloud engineers actually understand this key distinction, and which CTOs have gone beyond eliminating single-region dependency, to suss out the deeper runtime control-plane coupling baked into supposedly distributed architectures.

This AWS incident wasn’t just another service disruption; it was a systemic architectural reckoning that exposed fundamental flaws in how even highly sophisticated engineering organizations misunderstand and build upon cloud primitives. When the core components of a single region seize up, the resulting chaos shouldn’t be a surprise, it should be a planned-for state. The failure mode cascaded across hundreds of seemingly independent services, freezing everything from customer transactions to internal CI/CD pipelines, revealing a pervasive reliance on assumptions about the cloud control plane that many CTOs have tacitly allowed to propagate unchecked.

Most companies paying for “high availability” were actually only paying for a single region’s worth of availability. When that regional brain short-circuited, they were left with no operational nervous system.

Including, somehow, people’s beds.

Customers of Eight Sleep who’d paid $3,000+ for mattresses that promise to optimize sleep via AI-powered temperature regulation were rudely awoken to find themselves stuck. Some in awkward positions, unable to adjust their beds. Others overheating, their mattresses locked at temperatures designed to keep them awake, with no way to fix. The smart bed, designed to solve sleep, had become the thing preventing it.

Here’s why: A good GPS tracker sends about 30MB of data per month for real-time location tracking. Eight Sleep’s bed was sending 16GB per month. Though not all of that was the current location of your bed (as important as that is to know) but a constant stream of biometrics, temperature readings, and movement (and breathing!) data flowing to AWS. That data plane traffic was fine during the outage. The beds kept collecting data, kept monitoring sleep patterns, kept streaming telemetry to the cloud.

What failed was the ability to send a command back. When a customer tried to adjust their bed’s temperature or change its position, that command required authentication, a call to AWS STS to validate fresh credentials before execution. And because Eight Sleep’s architecture tied their high-volume data stream to their security heartbeat, those credential refreshes happened frequently. Likely every 15 minutes, following standard JWT security practices that made perfect sense for user-facing tokens and security best practices but created a hidden control plane dependency for infrastructure operations. If it sounds like an optimization problem in there, it’s not so much hard, as hardly acknowledged. (Solution below.)

When us-east-1’s control plane seized up, the data kept flowing (data plane), but commands stopped working (control plane). The bed couldn’t verify that you were authorized to adjust your own mattress. The hardware was fine. The logic was in Virginia.

Here’s why you’re reading this: by the time you finish this article, you will never lose sleep over an AWS outage again. Not the metaphorical kind (war rooms, pager duty) and not the literal kind (your infrastructure seizing up while you watch error rates spike). The smart beds froze. Your systems won’t. Because you’re about to understand the one architectural distinction that separated the 85+ companies that went dark from the ones that didn’t even notice.

Context & Background
The October 20th outage in us-east-1 began with a DNS resolution failure hitting a regional DynamoDB endpoint. What happened next was a textbook distributed system disaster: a race condition in DynamoDB’s replication logic. One replica lagged critically, while a second, faster replica accelerated its write cycle. When the faster replica completed its cycle, it mistakenly purged records that were still valid data being processed by the lagging replica. Whoopsie. Every valid IP address for the primary us-east-1 DynamoDB endpoint was wiped out.

Now, you might think: “DNS issue in DynamoDB? In us-east-1? My app doesn’t even use either of those.” That’s an Admiral Ackbar moment. It’s a trap.

DynamoDB isn’t just a database for customers. It’s a foundational internal primitive for countless core AWS services: the EC2 control plane that launches instances, the Network Load Balancer (NLB) health check subsystem, Lambda event source mappings, and dozens of other dependencies. When the DynamoDB endpoint became unreachable, it triggered a cascading control plane amnesia across AWS’s internal systems that quickly lost their ability to confirm state, acquire new resources, or validate dependencies.

The NLB health checks failed, which broke the network routing layer. This, in turn, made recovery efforts (notably, launching new EC2 capacity) nearly impossible. The region was trapped in a death spiral: every system needed the control plane to recover, but the control plane was blocked because it relied on systems that were now down.

And here’s the part that caught everyone off guard: moving out of us-east-1 didn’t save you. Companies running 100% of their production workloads in us-west-2 went down. Much vaunted multi-region architectures failed. Why? Because the dependency wasn’t geographic, it was architectural. If your application made control plane calls at runtime (IAM credential refresh, STS token validation, service discovery, parameter fetching), those calls routed through us-east-1’s global control plane anchor regardless of where your workloads were physically running. Insert your own colorful metaphor of choice here.

The concrete engineering failure came from DynamoDB’s DNS Enactor, the subsystem responsible for authoritatively publishing and reconciling service endpoint DNS records [dynamodb.us-east-1.amazonaws.com] into AWS’s control-plane propagation system. A race condition (known to AWS but improperly mitigated) in the Enactor’s update path caused a transient state where records were cleared before replacements were visible, producing an empty authoritative DNS response.

AWS treats certain DNS names for control-plane activity as authoritative from a specific regional origin. These authoritative names are what the EC2 provisioning APIs, Lambda orchestration, NLB health checks, STS/IAM validation, and CloudFormation use. When the Enactor published empties in us-east-1, those lookups failed globally, even in regions where your data plane was perfectly healthy. The servers kept serving, but the automation brain lost its map.

This is the reality of architectural coupling: your supposedly multi-region stack depending on a single-region control-plane anchor at runtime.

Jassy’s recent claims about AI-generated code are a distraction here. This wasn’t AI gone rogue; it was a basic race condition in replication logic. What made it catastrophic was the architectural coupling: one DNS failure in one service cascaded across the entire control plane because fundamental service dependencies were not resilient to a single point of failure. But here’s the thing: a properly architected application should not be subject to an outage here. Rather than bemoan AWS’ very real “brain drain,” let’s examine what that looks like and how to prevent future occurrences.

Industry Impact
Multi-region Doesn’t Save You
Let’s be absolutely clear about the scale of this failure. This wasn’t a handful of scrappy startups. This was a who’s who of companies that supposedly “get it”:

Adobe Creative Cloud, Airtable, Amazon (yes, Amazon’s own services including Alexa and Prime Video), Apple Music, AT&T, ChatGPT, Coinbase, Delta Air Lines, Duolingo, Fortnite, GoDaddy, HBO Max, Hulu, IMDb, Instacart, League of Legends, Microsoft (including 365, Outlook, and Teams), Navy Federal Credit Union, Peloton, PlayStation Network, Reddit, Ring, Robinhood, Roblox, Roku, Signal, Slack, Snapchat, Starbucks, Steam, T-Mobile, Trello, United Airlines, Venmo, Verizon, Wall Street Journal, Wordle, Xbox, Zoom...

The list goes on. 85+ major companies, many with hundreds of engineers and supposedly sophisticated infrastructure teams. Each one assuming they were fully multi-zoned and protected. Apparently, none had verified their assumptions under fire, though. Extra delicious humble pie was served to companies that had completely migrated out of us-east-1 and still went down. They proudly ran 100% of their PROD workloads in us-west-2 or eu-west-1, thinking they’d escaped the blast radius.

And the multi-region crowd? The ones who’d invested millions in active-active architectures spanning us-west-2 and eu-central-1? (Love active-active.) They went down too. Because even if your data plane is beautifully distributed across regions, if your application makes control plane calls at runtime (IAM credential refresh, CloudFormation stack queries, DynamoDB Global Table metadata, STS token generation), those calls still route through us-east-1’s global control plane anchor.

Multi-AZ doesn’t save you. Multi-region doesn’t save you. Only eliminating runtime control plane dependencies saves you.

The Architectural Wake-Up Call here is that this outage kills two massive, unspoken assumptions in cloud adoption. First: Multi-AZ ≠ Highly Available. For many companies, Multi-AZ only means their workload is spread across different physical buildings that share a single, monolithic control plane state, ie. a single point of systemic failure. Second: Companies that architected their data plane (customer-facing traffic) for multi-region failover often failed to account for their management plane dependencies (CI/CD, monitoring, state verification) remaining fixed, albeit invisibly, to a single region. Failover was configured, but the ability to execute failover died with us-east-1.

AWS didn’t just have a DNS outage; it had a von Neumann moment.

While Von Neumann’s sequential assumptions (control preceding data) work well for single, non-distributed systems, at cloud scale this architecture crumbles under the sheer weight of the data. (Postman and Eight Sleep are obviously not helping here.) Single-threaded control paths in provisioning, replication, and DNS orchestration create global bottlenecks. Data may be abundant and compute distributed, but when the control plane serializes and stalls, you don’t need Turing to predict the outcome: the entire system halts.

AWS didn’t just have a DNS outage; it had a von Neumann moment. This is arguably the real RCA behind this global reckoning. Control became the bottleneck, proving again what researchers outlined at least a decade ago with The Dataflow Model (2016): serializing the control plane is a failure mode when data concurrency overwhelms sequential governance.

True resilience requires shifting to dataflow terms: asynchronous coordination, regional autonomy, and eventual consistency of state and governance. This catastrophic fail mode must transition from an unexpected surprise to a literally planned-for state.

This is why chaos engineering matters. The theory sounds great in conference talks, though it’s unclear if teams are actually putting it into practice. In the absence of such planned fire drills, every affected company essentially had one forced upon them, but with real customer impact. And most failed the test because they hadn’t actually conducted any actual fire drills, simulating the failure of an AWS service that is known to fail. You do have a blue team / red team process for running this playbook, don’t you?

The Control Plane vs. Data Plane Distinction That Will Save Your Job
Moving workloads out of US-EAST-1 is a good start, but it won’t save you. As the 16GB/month smart bed learned, applications with baked-in control plane dependencies at runtime failed regardless of which region they were running in. Runtime data plane operations (like reading, writing, and serving customer requests) were fine. The problem is that the global control plane in US-EAST-1 is not likely to be architecturally decoupled (on their side) anytime soon. Yesterday’s outage was an architectural reckoning. The systems that survived didn’t use a different cloud but rather they understood the distinction between control and data.

Control Plane: Provisioning resources, updating configurations, creating IAM users, modifying policies, and crucially, calling STS AssumeRole to get new temporary credentials.

Data Plane: Validating existing IAM signatures on API requests, reading/writing to DynamoDB tables, S3 objects, SQS queues, ie the actual runtime operations that serve customer requests.

One critical distinction most engineers miss is in the authentication flow. IAM authentication is Data Plane (validating a signature), but IAM credential management (calling STS to refresh tokens) is Control Plane. When your application calls AssumeRole to get fresh credentials, that’s hitting sts.amazonaws.com, which routes through US-EAST-1 for global coordination. But when API Gateway validates a request signature using already-issued credentials, that’s pure Data Plane, with no control plane dependency.

The solution demands not a compromise, but a surgical separation achieving both maximum security and maximum resilience

The Token Expiration Reality: Security vs. Survival
The high-stakes problem of freezing 16GB-per-month smart beds and stalling global resources stems from numerous baked-in control plane dependencies. This token expiration vulnerability, while not trivial to fix, presents the highest-value architectural flaw demanding immediate guidance to resolve. (For additional areas to add to your resilience audit, see part two of this post.) The modern security consensus requires short TTLs; 15-minute TTL for client-side JWTs ensures correct security hygiene. Yet, applying that logic to the application layer forces your infrastructure to ask the paralyzed Control Plane for fresh STS keys every 15 minutes. That security practice creates a resilience killer. The solution demands not a compromise, but a surgical separation achieving both maximum security and maximum resilience.

Security Mandate (JWT TTL): Enforce short 15-minute expiration on user-facing session tokens. (Minimize security risk.)

Resilience Mandate (STS TTL): Configure your IAM roles for the maximum session duration of 12 hours (43,200 seconds, the longest AWS allows) for all application-facing AssumeRole calls. (Maximize operational autonomy.)

This surgical separation works perfectly, if your user authentication doesn’t depend on AWS control plane. If you’re using Auth0, Okta, or your own auth service, you can maintain 15-minute user tokens and refresh them indefinitely during an outage because token issuance happens independently of AWS. But if you’re using Cognito, you have a problem. Cognito requires control plane calls to issue and refresh user tokens. When us-east-1 goes down, users can’t get new tokens. After 15 minutes, everyone’s sessions expire and nobody can log back in. Revenue stops. If you’re on Cognito, you have three options:

Option 1: Extend User Token TTLs (Quick Fix, Security Trade-off)
Set user JWTs to 8-12 hours instead of 15 minutes. Users stay logged in through outages. Your security team will hate this (stolen tokens remain valid for hours instead of minutes.) But it buys survival time without infrastructure changes.

Security mitigations to pair with longer TTLs: Implement aggressive session monitoring (flag unusual IP/device changes), enforce re-authentication for sensitive operations (password changes, payment methods), and enable automatic token revocation on suspicious activity. You’re trading broader exposure windows for operational resilience so make sure your detection and response capabilities match the increased risk.

Cost: $0 (config change) + ~$20K for enhanced monitoring

Time: 1 day (TTL change) + 1-2 sprints (monitoring)

Best for: Band-aid while planning migration

Option 2: Migrate Off Cognito (Correct Solution, Expensive)
Use Auth0, Okta, or run your own auth. These don’t depend on AWS control plane for token operations. Users can log in and refresh tokens during us-east-1 outages. \o/

Cost: $50-200K/year (managed) or $200-500K migration

Time: 3-6 months

Best for: Companies where 15 minutes of downtime costs >$100K

Option 3: Build Cognito Failover (Don’t Do This)
Maintain dual auth systems with automatic failover. If you’re building your own auth anyway, just use it as primary and skip Cognito. This is the kind of over-engineering that looks impressive in architecture reviews and terrible on P&Ls.

Cost: $500K+

Time: 6-12 months

Best for: Nobody

The companies that survived Monday weren’t using Cognito. If you’re looking for the TD;DR TL;DR, that’s it. They’d already migrated to independent auth providers. The companies scrambling in war rooms were the ones who’d optimized for AWS integration convenience and discovered that convenience has a cost measured in revenue per hour.

TL;DR Action Items
Know What Will Kill You - HIGH PRIORITY (30 Days)
Budget: $25-75K | Resources: 1 Sr Eng (80%) | Outcome: Prioritized Risk Assessment

Inventory Global Control Plane Dependencies: Audit your runtime control plane dependencies to identify which services will fail within 15 minutes of a us-east-1 outage. Output: You need a spreadsheet that tells you: “If AWS control plane goes down at 3 AM, which of our services die first, how much revenue do we lose per hour, and what does it cost to fix each one?”

Assign your most senior cloud engineer to audit all AWS API calls in your hot path (or hire a consultant for $15-60K if your team is underwater). Deliver a spreadsheet with every runtime control plane dependency showing: Service name, API called, blast radius (revenue impact/hour), fix cost (engineer-weeks). Sort by blast radius and allocate budget to fix the top 10.

Stop It From Killing You - MEDIUM PRIORITY (EOY)
Budget: $150-400K | Resources: 2-3 FT Eng | Outcome: 95% Vulnerability Eliminated

Top 10 Mitigation: Take the prioritized list from your 30-day audit and fix the top 10 runtime control plane dependencies the ones that will hemorrhage when they fail. Payment processing, authentication, core application APIs. Not the “nice to haves.” Not the internal admin tools. The services that generate revenue. These ten dependencies probably account for 95% of your revenue risk. Fix those 10 and you survive the next outage. Leave them broken and you’re explaining to your board why you were down for 12 hours.

Sample Action Plan: Implementation sprint tackling top 10 items: Extend IAM role sessions from 1 hour to 12 hours ($0 cost, 2 engineer-days). Move Secrets Manager calls out of request path (1 engineer-week per service). Replace ECS DescribeTasks with DNS-based service discovery (1 engineer-week). Remove CloudFormation queries, use environment variables (2 engineer-days per Lambda). Deploy async logging with Fluent Bit sidecars (3 engineer-days). Then run controlled chaos experiments: Block us-east-1 endpoints at network level, verify top 10 services continue operating, document what still breaks (for your 90-day roadmap).

Build vs Buy: Build if it’s core to your business, vendor solutions don’t support your scale, or you have spare engineering capacity (lol). Buy if it’s infrastructure plumbing, vendor solutions are mature, or your engineers are underwater (which they are). Credential management: HashiCorp Vault (~$50K/year) or AWS Systems Manager (included). Service discovery: Consul (~$30K/year) or AWS Cloud Map (<$500/month). Chaos engineering: Gremlin ($36K/year) or AWS Fault Injection Simulator ($300/month).

Build True Resilience (Or Accept Your Fate) - STRATEGIC PRIORITY (90 Days)
Budget: $300K-2M | Resources: 5-10 Eng | Outcome: True Multi-Region Independence

Mandate Control Plane Independence: This is the difference between “we survived with degraded performance” (60-day goal) and “we didn’t even notice the outage” (90-day goal). This is non-negotiable if you’re a public company or processing >$100M ARR. Your 90-day work buys you competitive advantage.

Choose Your Architecture & Implement: Select a strategy (Active-Active, Active-Standby, or Regional Independence). Implement the necessary architectural components: Cross-region database replication (DynamoDB Global Tables, Aurora Global), CloudFront origin failover, and Regional Credential Brokers.

Chaos Drill Validation & KPIs: Block all *.us-east-1.amazonaws.com at the firewall. Measure time to detection (<5 minutes), time to failover (<30 minutes), customer impact (0 failed requests), data loss (0 transactions), and revenue impact ($0). These KPIs determine if the project is done.

Technical Handoff: The full technical plan and detailed implementation guide for Control Plane Independence is contained in Part 2, for handover to your Lead Cloud Engineer.

ROI Calculator:
The question is no longer if a centralized control plane will fail, but when. The financial choice is simple: pay a small, predictable insurance premium for resiliency, or pay the catastrophic, exponential cost of a 15-hour outage.

Investment required is for the mandated quarterly Chaos Engineering fire drills simulating a complete us-east control-plane failure. (At least annual if you’re strapped.)

Investment: Total Annual Cost of the Drill Program

Personnel Cost: 8 FTEs (Architects, SREs) at $150/hr blended rate.

Time Commitment: 40 hours per drill x 4 drills per year. (for >$100M ARR)

Total Annual Investment (A): $192,000

Compare that to a single, avoided loss event, that 15-hour paralysis on October 20th:

Avoided Loss: Cost of a Single 15-Hour Outage

Direct Revenue Loss Rate: $500,000 per hour (Conservative Tier 0/1 estimate).

Direct Loss Calculation: $500,000 x 15$ hours $7,500,000.

Brand/Reputation Damage Multiplier: +25% of Direct Loss for customer churn and stock impact.

Recovery/Post-Mortem Labor: $150,000 in immediate engineering costs.

Total Avoided Loss (B): $9,525,000.

The math is not complex:

Net Gain (Savings): $9,333,000

Return on Investment (ROI): 4860%

The ROI is not 150%; it is 4860%. This number is not an accounting exercise; it is an architectural mandate. For every dollar spent ensuring your systems can operate autonomously when the US-EAST-1 control plane freezes, you save forty-eight dollars by avoiding a single, predictable failure. This confirms that the value of true resilience; decoupling runtime dependencies from the global control plane is a negligible insurance premium against the catastrophe of a Von Neumann Moment.

Credit Where Credit’s Due
Finally, if you were affected by the AWS outage, here’s how to apply for credit, along with some pointers for doing so. AWS will issue Service Credits for the October 20th outage under their SLA, but they don’t make it easy. You need to file within 30 days of the incident, provide specific documentation, and follow their process exactly or your claim gets rejected.

How to file:

Go to AWS Support Center → Create Case → Account and Billing Support

Subject: “SLA Credit Request - October 20, 2025 us-east-1 Outage”

Provide: Affected services, impacted resources (ARNs), duration of impact, business impact statement

Pointers for maximizing your credit:

Document everything now: CloudWatch logs showing error rates, support tickets filed during the outage, customer complaints, revenue impact calculations

Be specific: “DynamoDB in us-east-1 unavailable 14:23-02:15 UTC affecting 47 production tables” beats “stuff was down”

Quantify business impact: “Processing pipeline down 12 hours, 15,000 failed transactions, estimated $250K revenue impact”

Reference the SLA: AWS promises 99.99% uptime for most services—12+ hours down blows past that threshold

File early: Don’t wait until day 29. File within the first week while details are fresh

Reality check: You’ll get maybe 10-30% of your monthly AWS bill back as a credit (not cash). For a $50K/month bill, expect $5-15K in credits. Better than nothing, but nowhere near covering actual business impact. This is why the architectural fixes above matter; you can’t SLA your way out of revenue loss.

The credit application deadline is November 19, 2025. Don’t leave money on the table.

“The companies that survived Monday’s outage weren’t lucky.
They’d just already done the math.”

The Hard Truth: Yes, multi-region is expensive. Not that it helped those 85+ aforementioned companies. Your infrastructure costs increase 20-100%. Your team spends 3-6 months not building features. But your competitors are doing this. Stripe is doing this. Datadog is doing this. Snowflake is doing this. When the next outage hits and you’re down for 12 hours while they stay online, how do you explain that to your customers? The real question isn’t “Can we afford to do this?” The real question is “Can we afford not to?”

Eight Sleep’s customers eventually got their beds back. The engineering teams who spent Monday night in war rooms eventually got their systems back. But only one of those groups learned the architectural lesson that will let them sleep soundly through the next us-east-1 outage. The companies that survived weren’t using multi-cloud voodoo; they understood the distinction between control plane and data plane. They’d already implemented credential caching, DNS-based service discovery, and eliminated runtime dependencies on us-east-1’s global control plane anchor. They weren’t necessarily smarter. They weren’t luckier. They just didn’t lose sleep over it.

Part 2 of this series will provide the complete Technical Remediation Playbook: the grep commands, bash scripts, and specific anti-patterns your Cloud Team needs to execute the 30/60/90 plan above.
