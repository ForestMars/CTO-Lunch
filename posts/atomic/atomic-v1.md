It’s 2AM and you’re staring at the sixth-largest bank’s data lake, except “lake” is generous. And it’s actually well after 3AM, but we just set the clocks back. A seemingly appropriate hour for staring into the abyss that’s not so much a lake as it’s more like an ocean-sized swamp, one containing every single document that’s flowed through the system for 20+ years. Compliance dumped it all there. No one and I mean no one even knows what’s in there. And now someone upstairs wants answers.

Your first instinct is probably “let’s classify it” or “throw Spark at it” or maybe “fine-tune an LLM on the whole thing.” All reasonable. All doomed to fail in ways that are both predictable and instructive. Because what you’re actually confronting isn’t a technology problem, it’s an architectural primitive problem. And the solution involves understanding something most engineers learn once, forget immediately, and spend the rest of their careers rediscovering: the impedance mismatch between atomic and relational data.

The Primitives No One Talks AboutWhy ETL Failed and ELT WonSpider And I Sit Watching the SkyWhy Warehouse → Lake Is ImpossibleHadoop, Spark, and the Dematerialization of ComputeBloom Filter Paradox: Atomic Efficiency vs. Relational SynergyWhat This Means for Your SwampWhy This Matters Beyond Your SwampThe Real Trade-Off

The Primitives No One Talks About

Let’s start with definitions, because we’re going to need them.

Atomic data: Immutable blobs. Documents, files, objects. No inherent relationships. Schema-less. Append-only. Preserves raw reality exactly as it arrived. Your data lake is atomic. S3 is atomic. Every PDF, email, and scanned fax from 1998 sitting in that swamp is atomic. 

Relational data: Structured rows and columns. Explicit relationships via foreign keys. Schema-enforced. Update-in-place. Models an interpretation of reality, not reality itself. Your data warehouse is relational. SQL is relational. Every cleaned, transformed, aggregated view you’ve ever built is relational.

The fundamental truth that everyone misses or forgets: You can go atomic → relational, but you cannot go relational → atomic. One direction preserves optionality. The other destroys information irreversibly. This is the load-bearing architectural principle underlying a thousand different technology decisions you make every quarter, whether you realize it or not.

Why ETL Failed and ELT Won

Good ole Extract-Transform-Load. The warehouse-first era. Clean your data before storing it. Transform it into the shape you need. Load it into the structured database. Such innocent times. 

To put it bluntly: ETL died because it destroys the atomic layer too early. You transform data before you know all the questions you’ll need to ask. You aggregate before you understand which aggregations matter. You filter before you realize what you filtered out was actually the signal. Call it premature optionalization. 

Once you’ve transformed the data, the raw atomic reality is gone. You can’t go back and ask new questions. You can’t reprocess with better logic. You can’t recover from the mistakes you made when you thought you understood the business requirements.

Optionality is priceless. But of course it comes at a cost.

ELT, Extract-Load-Transform, won because it preserves the atomic substrate. Dump everything into the lake first. Keep the raw data forever. Transform it as many times as you want, as many different ways as you need. Storage is cheap. Optionality is priceless. But of course it comes at a cost. The cost is the complexity of managing and governing a massive, unstructured, immutable swamp. Losing the atomic layer is like burning the original film negative once you’ve made a print. The print is nice, but you can never go back and re-edit, or print in a new format. The lake is the negative .

This is also why S3 ate Redshift’s lunch as a foundation. (Despite the ambitious brilliance of the OG Redshift paper in flipping off the CAP theorem.) Not because Redshift is bad (hardly). But because a data warehouse is a materialized view, and you can’t rebuild the source of truth from a materialized view. The lake is the source of truth. The warehouse is just a cache. (Of course even lakes are just holding pools for flowing tributaries, but don’t get me started.) 

The Spider Problem

Back to your 20-year document swamp. You want to “spider” it: index it, classify it, make it queryable. Let’s walk through why the obvious approaches don’t work.

Approach 1: Throw it all at an LLMYou could fine-tune a model on the entire corpus. The model would “learn” what’s in there. Except now you have a knowledge representation, not a data inventory. Ask it “how many contracts are in there?” and it will hallucinate a plausible number based on statistical patterns, not count actual documents. Ask it “who lives at 123 Main Street?” and it might confidently name one of ten thousand people, or invent someone who doesn’t exist. Ask it how many documents refer to the property at 123 Main and again, it will hallucinate something plausible. The atomic reality is gone, replaced by a probabilistic approximation.

LLMs are brilliant at extracting meaning. Terrible at preserving facts. You need both.

Approach 2: Build a classifier and index everything in SparkThis works, technically. You’ll spend six months building a supervised classifier, labeling training data, handling edge cases from 75 different document formats across three deprecated HR systems. Then you’ll run it across petabytes of data in Spark, watching job failures and OOM errors like it’s your full-time job (because it is.) 

The problem isn’t that this approach fails as well. For one thing, it’s horrifically expensive in human time. You’re trying to impose a relational schema (your classification taxonomy) onto atomic chaos (20 years of unstructured documents) using pure brute force. And every time the business changes—new document types, new departments, new compliance requirements—you rebuild the classifier and reprocess everything.

Approach 3: Unsupervised clustering + LLM interpretationNow we’re getting somewhere. This is the hybrid approach that actually works:

Use unsupervised learning (embeddings + clustering) to let the data tell you what natural groupings exist

Let the data’s inherent structure reveal itself, rather than imposing your assumptions

Use an LLM to interpret what each cluster represents—not to generate the taxonomy, but to understand it

Write the metadata (cluster assignments, category names, confidence scores) to a structured layer (Delta/Iceberg tables)

You’re preserving the atomic layer (documents never move) while building a relational interpretation layer (queryable metadata) on top. The documents stay in S3. The structure lives in Delta tables. You can query “how many contracts from 2015-2020 are settleable in USD?” because you have real counts in structured tables. But you can also go back to the raw documents whenever you need to reprocess with better models or new business logic.

This architecture understands the atomic-relational divide.

Why Warehouse → Lake Is Impossible

Here’s the trap that catches everyone: once you’ve built the warehouse, you can’t reverse-engineer the lake.

Say you’ve been running ETL for five years. You have beautiful Redshift tables. Clean schemas. Aggregated metrics. Executive dashboards that make the CFO happy. Then someone asks: “Can we reprocess last year’s data with the new fraud detection algorithm?”

No. You can’t. Because the raw atomic data, the actual transactions, the original documents, the unmodified logs, is gone. You threw it away when you transformed it. Or you kept it for 90 days and then deleted it because storage was “expensive.” (Narrator voice: it wasn’t.)

You built a relational interpretation. You can’t reverse-engineer the atomic reality from that interpretation. Information loss is permanent. (Reminds me of something.)

This is why the “modern data stack” converged on lakes-first architecture. Keep the atomic layer forever. Build as many relational interpretations as you need. Throw them away and rebuild them when requirements change. The atomic substrate is the source of truth. Everything else is a disposable view.

Hadoop, Spark, and the Dematerialization of Compute

Let’s trace the evolution, because it’s the same atomic-relational pattern playing out at the infrastructure level.

Pre-Hadoop: Data to computeYou have a database server. You query it. Data moves over the network to your application. Doesn’t scale. Network becomes the bottleneck. The data is too big to move.

Hadoop: Compute to dataHDFS chunks data across machines. MapReduce ships code to the storage nodes. Processing happens where data already lives (data locality). The breakthrough: move the computation, not the data. This was the right architecture for 2006.

Spark: Dematerialized computeKeeps the “compute to data” philosophy but abstracts away the physical location. You don’t care which nodes hold which blocks. You say “process this dataset” and Spark figures out optimal execution. Can run on HDFS (data locality maintained) or S3 (no locality, but elastic compute). The compute layer is logically separated from the storage layer, even if they’re co-located physically.

Why HDFS diedHDFS was operationally brutal. NameNode failures. DataNode rebalancing. Rack awareness. Capacity planning. You needed a whole team just to keep it running. And for what? So you could have data locality? That was the dream, anyway. 

Then networks got way faster (10Gb, 100Gb in datacenters), cloud object storage got really good (S3’s 11 9’s durability), and the penalty for “data over the wire” became acceptable. The economics flipped: pay for network transfer became cheaper than pay for a team of HDFS engineers. (Spoiler: everything that flips, flips back.) 

Hadoop’s insight, compute to data, was correct for its era. But the operational cost of maintaining that architecture became unacceptable. And so we went back to moving data over the network, except now it’s fast enough and cheap enough that we don’t care. Even at the peta-approaching-exa scale of this GSIB’s spent fuel dump of every document they’ve ever produced. 

The lesson: Brilliant architecture + operational hell = eventually loses to “good enough” architecture + zero ops.

What This Means for Your Swamp

You have petabytes of atomic data (the swamp). You need relational structure (queryable metadata). The solution isn’t to convert one into the other. It’s to build the relational layer on top of the atomic layer without destroying the atomic layer.

The architecture:

Documents stay in S3 (the atomic substrate, immutable, forever)

Distributed compute (Ray, because you’re smart) reads from S3, extracts text, generates embeddings, classifies documents

Metadata gets written to Delta tables (the relational layer): document_id, file_path, embeddings, cluster_id, category_name, confidence_scores

You query the Delta tables for counts, filters, aggregations

You retrieve documents from S3 when you need the raw atomic data

The documents never move. The compute goes to the data (logically; physically it’s over the wire, but that’s fine for reasons just noted.) The metadata is structured and queryable. The atomic reality is preserved forever.

And when the business decides they need to reclassify everything because compliance changed the rules? You don’t move documents. You don’t rebuild the lake. You just regenerate the metadata and write new Delta tables. The atomic layer is unchanged. The relational interpretation is disposable. And not safe for swimming. 

Why This Matters Beyond Your Swamp

The atomic-relational divide isn’t just about data lakes. It’s the architectural pattern underlying basically everything:

Microservices vs monoliths: Atomic services with relational contracts (APIs)

Event sourcing: Atomic event log, relational projections

Git: Atomic commits, relational branch pointers

Blockchain: Atomic transactions, relational state

Your codebase: Atomic files, relational module dependencies

Every time you face an architectural decision, you’re choosing between preserving atomic independence versus imposing relational structure. And the right answer is almost always: preserve the atomic layer, build relational interpretations on top.

Because you can always add structure. You can’t recover lost atomicity.

Entropy, Bloom Filters, and the Asymmetry of Knowledge

Here’s where it gets weird. The atomic-relational divide isn’t just an architectural pattern, it’s a manifestation of thermodynamic directionality. Entropy, our old friend from physics, has been hiding in the data architecture all along.

Entropy only increases. Information, once lost, cannot be recovered. You can scramble an egg, but you can’t unscramble it. You can transform atomic data into relational structure, but you can’t reverse-engineer the atomic reality from the structure. The directionality is baked into the universe.

And if you squint, you’ll notice something else lurking in this pattern: Bloom filters.

Bloom filters are beautifully counterintuitive. They can tell you with certainty that something is not in a set, but can only give you a probabilistic answer about whether something is in a set. False positives are possible. False negatives are impossible. This is the exact opposite of how human knowledge normally works.

In everyday experience: if you see something, you know it exists. If you don’t see it, you can never be certain it doesn’t exist. (”Absence of evidence is not evidence of absence.”) You can’t prove a negative. This is logic 101, common sense, the foundation of empirical reasoning.

Bloom filters invert this completely. They can prove a negative with certainty (”this item is definitely not in the set”) but cannot prove a positive with certainty (”this item might be in the set, better check the source”). The asymmetry runs in the opposite direction from human intuition.

And this maps perfectly onto atomic vs relational data.

The atomic layer is the Bloom filter’s backing store—the source of truth you check when you get a “maybe.” The relational layer is the probabilistic filter—fast, queryable, but potentially incomplete. You can prove something is in the relational layer (check the index, get a result). But if it’s not in the relational layer, you can’t be certain it doesn’t exist in the atomic layer. Maybe your classifier missed it. Maybe it’s in a format you didn’t account for. Maybe it was added after the last indexing run.

The only way to prove something doesn’t exist is to check the atomic source. The lake is the ground truth. The warehouse is the optimistic approximation.

This is why you can’t go backward from relational to atomic. The relational layer is a lossy compression, like a Bloom filter with an impossibly high false-negative rate. Once you’ve thrown away the atomic data, you can query the structure all you want, but you’ll never know what you’re missing. The entropy has increased. The information is gone. You can’t unscramble the egg.

The Real Trade-Off

I’m not saying relational is bad. Relational databases are incredible for what they do. SQL is beautiful. Schemas are useful. Structure enables queries.

The mistake is imposing structure too early, in a way that destroys the atomic substrate.

ETL does this. Redshift-first architecture does this. Any pipeline that transforms data before storing it does this. You’re making irreversible decisions about what matters before you fully understand what you need.

The winning architecture preserves optionality by keeping the atomic layer intact and making the relational layer disposable and regenerable.

Lakes → warehouses works. Warehouses → lakes doesn’t. Not because of technology limitations. Because of information theory. You can’t uncompress a lossy compression. You can’t reverse an irreversible transformation. Entropy only goes one direction.

How to Think About Your Next Architecture Decision

When you’re designing your next data pipeline, ask:

Am I preserving the atomic layer? Can I go back to raw data and reprocess?

Is my relational layer disposable? Can I throw it away and rebuild it from atomic data?

What information am I losing? If I can’t answer “none,” I’m making irreversible decisions too early.

If your architecture passes these tests, you’re probably fine. If it doesn’t, you’re building technical debt that will explode the moment requirements change (and they will change).

The Bottom Line

Your data lake is a swamp because it’s supposed to be a swamp. It’s atomic chaos. That’s not a bug, it’s the entire point. The swamp preserves reality exactly as it happened, with no assumptions about what matters.

The warehouse is where you impose structure. Where you decide what’s important. Where you build the relational interpretation that makes the chaos queryable.

But the warehouse is downstream of the swamp. Always. The moment you try to make the warehouse the source of truth, you’ve lost. Because you’ve destroyed the atomic layer, and you can’t get it back.

This is the impedance mismatch that drives a thousand architectural decisions. ETL vs ELT. Data lakes vs data warehouses. S3 vs Redshift. HDFS vs object storage. Atomic vs relational.

It’s not about which is better. It’s about which comes first, and what you lose if you get the order wrong.

Keep the atomic layer. Build disposable relational interpretations on top. And when someone asks you to spider a 20-year-old document swamp at the sixth-largest bank in the world, you’ll know exactly what to do: preserve the swamp, build the structure on top, and whatever you do, don’t try to turn the swamp into a swimming pool.

Because you can always add chlorine later. You can’t un-drain the ocean.
