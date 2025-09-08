## Web3

- L1’s, Stablecoins and Real World Adoption
    - US treasury will no longer request user data from decentralizaed crypto apps
    - Google has announced their L1 blockchain.
    - [Stripe launches L1](https://news.ycombinator.com/item?id=45129085)
    - [**MetaMask**](https://www.linkedin.com/company/metamask/)🦊announced mUSD, the wallet's native stablecoin.
    - (both announcements met in Web3 with a collective shrug, as if to say, Token or GTFO.)
    - stablecoins - https://slashdot.org/story/25/08/26/2338207/citi-executive-warns-stablecoin-yields-could-drain-bank-deposits
    - a lot of real-world businesses finding utility in stablecoins. For example, Bridge (a stablecoin orchestration platform that Stripe acquired) is used by SpaceX for managing money in long-tail markets. Another big customer, DolarApp, is providing banking services to customers in Latin America. We're currently adding stablecoin functionality to the Stripe dashboard, and the first user is an Argentinian bike importer that finds transacting with their suppliers to be challenging.
    - Who knew stablecoins would be the killer app?
    - Today, if you want to transact between businesses or retail (folks like you and I), you need to find a route between the two entities' banks. This route might take several hops, passing through some central banks, and some of these hops might be instant or might take days to actually settle. On top of that, you need to pay the service that helped you find a route (SWIFT) and potentially the nodes your transaction goes through. Bottomline, it can be slow and a lot of middle men are taxing you.
    - [Ripple's dedicated bank](https://www.theportugalnews.com/news/2025-08-17/ripples-dedicated-bank-is-about-to-go-live-and-xrp-holders-can-earn-up-to-5700-a-day/601623)
- [ETHGlobal](https://www.youtube.com/live/Q18pnAODgqQ) NYC
    - Every fall since —-, but no longer a full conference just a weekend hackathon
    - Still, drew 690 hackers, 275 teams, from —- countryies, with 10 winning teams (including one of our very own CTO Lunchers.)
- The 10 winning EthGlobal NYC projects included:
    1. reduce latency in coinbase micropayments standard (x402) 
        - include actual measured reduction in x402 latency
        - (2226ms → 166ms? 20x!)
    2. hardhat x ledger → hardhart 3 added solidity testing, multichain support
        - but ledger support not migrated to hardhat3 (bc new ledger library DMK device management kit)
        - was using ethers.js now using vm instead
    3. Noah - beneficiary access to your assets using non npc-wallets
        - rails to take funds, off-ramp them, provide traditional inheritance rails
        - dead mans switch + liquidation
        - no ping = assume they are dead
        - feature not a bug, if you lose your wallet funds get forwarded
        - transfer to bank account from stablecoins
    4. Pumpkin-spice-latte 1:58
        - Staking prize pools
        - prize linked savings accounts as a defi primitive
            - “turn boring yields into jackpots”
            - any ERC-4626 compatible yield source
        - this team featured NYC CTO Luncher Gilad Penn! Congratulations!
    5. kima-pay → very slick 
        - Genius Act
        - US regulatory clarity on Stablecoins
        - still fragmented liquidy and problems
            - Uniswap no different, maybe token pairs
        - Built on ORBITAL AMM - AI https://www.paradigm.xyz/2025/06/orbital
        - stripe alt that supports stablecoins with 10% savings
            - cross chain swap under hood finding best liquidty to undercut stripe
    6. Primer → checkout feature for amazon 
        - (huge TAM, let’s estimate it)
    7. Transaction Delay Insurance 
        - **gas futures for tx! holy toledo**
        - Zircuit can quarantine tx
        - alt to EPIP-1559 (pay xtra to have tx execute faster)
        - send to rx to simple, fully trans RPC proxy except
            - when broadcast (signed)
            - when confirmed (signed)
            - how
                - times tx delays
                - signs delay confirmation
        - factory policy (soft prices mean huge arbitrage)
    8. Swapay: pay w any token, mix different tokens seamlessly in a single payment transaction
        - SDK for checkout in web3
        - make a single payment with funds spread out across multiple token-chains, in a single transaction
        - 5 swaps in example EIP-5792 to batch tx
        - nice UI
    9. **Rivals**: Augmented-reality real-time FPS shooter.
