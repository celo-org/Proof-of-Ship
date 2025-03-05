 	
# Project Name - Giveth donation handler smart contract 

## Short Description

The goal is to develop and integrate a Donation Handler Smart Contract into Giveth’s donation flow on Celo. This contract acts as an intermediary between donors and project wallets, enabling on-chain tracking, automation, and better reporting.

## Link to GitHub repository

https://github.com/Giveth/donation-handler-foundry

## Link to Video

https://youtu.be/mfVHmcFv7gU

## Link to Deck

https://docs.google.com/presentation/d/19UPaHqhzNHCqX2K4O0SoKvnlVQw3htw3ROkapFdJ_wg/edit?usp=sharing

## Link to assets

https://github.com/Giveth/donation-handler-foundry


## Team Members GitHub username

**Mitch**-  dApp Development & Project Lead  
GitHub: https://github.com/divine-comedian
Twitter: [https://x.com/divine_comedian](https://x.com/divine_comedian) 
Farcaster: https://warpcast.com/divine-comedian

Past experience: DAO Ops Lead & Product Manager at Giveth. Junior Solidity Developer. Formerly Rewards System Lead at TEC, Project Manager at General Magic and Client Relations for Praise

**Carlos**- SR Backend Engineer
GitHub: https://github.com/CarlosQ96
Twitter: [https://x.com/CarlosQ096](https://x.com/CarlosQ096)
Farcaster: N/A
Past experience: 7 Years working as a backend developer, divided into 4 years in the web2 industry for Koombea in e-commerce and mobile applications, and 3 years building robust web3 backend integrations with the blockchain and smart contracts for Giveth and General Magic.

## Former Participation in Celo Hackathons

*Mitch’s Hackathon Team ETHGlobal Bangkok* 
[https://ethglobal.com/showcase/union-registry-oxjax](https://ethglobal.com/showcase/union-registry-oxjax)

## Monthly Goal for this Proof of Ship

- Research on similar smart contracts and necessary imports/libraries 
- Wrote smart contract documentation and project milestones 
- Peer review of contract stack and security considerations 
- Submitted project to Proof of Ship repo
- Finalized architecture 
- Wrote first draft of solidity smart contract 
- Deployed first draft contract to Celo Alfajores
- Started work on foundry tests


### Detailed description of the work you did this month during the contest

- [Wrote smart contract documentation and project specifications](https://www.notion.so/giveth/Donation-Handler-Smart-Contract-MVP-dd0bb21940654f5d9f524870ed04c98a) 
- [Wrote first draft of solidity smart contract](https://github.com/Giveth/donation-handler-foundry/commit/18770eea025fd1cbbcff3d86841cfa38904f6fae)
- [Wrote deployment script](https://github.com/Giveth/donation-handler-foundry/commit/865c9f73677c9f9d6c298e5d026d8da91a150a45)
- [Deployed first draft contract to Celo Alfajores](https://alfajores.celoscan.io/address/0xd363df3de223a73bd78fa27251ad213528bc2761#code)

## Problem

Giveth’s backend is 5 years old, making it outdated and inefficient.

* Relies on centralized back-end service to track donation data and maintain state
* Donations appear as regular token transfers, making them hard to track
* Not designed for external teams to make donations or query donation data. 
* RPC or other infra outages cause massive headaches and lost donations

A Donation Handler Smart Contract modernizes this flow, making it flexible, low overhead, transparent, and scalable.

## Solution

The Donation Handler Smart Contract solves these issues by:
* Allowing donations to be clearly tracked and indexed on-chain
* Reducing reliance on centralized back-end service
* Enabling AI-based donations, opening up design space for new funding mechanism experimentation
* Supporting external transactions, enabling donations outside Giveth’s UI.
* Increasing reliability of donation verification, lowering risks of missing donation data
* Increasing transparency of donation activity by making it distinguishable on-chain

## Architecture

*Components:**
1. DonationHandler.sol
    * Accepts donations.
    * Routes funds to project wallets.
    * Supports donation bundling & batch donations.
    * Stores transaction metadata for verification.
2. Backend Services
    * Subsquid indexer for tracking smart contract interactions
    * mapping indexer queries for getting on-chain information
    * Integrating with existing postgres, nodejs & redis services for verifying donations and filling assets prices
    * GraphQL endpoints for FE
3. Front-End Integration
    * User based smart contract interactions on donation flow
    * Bundling operations for multiple transactions

**Smart Contract Stack**
Foundry/Solidity 
defi-wonderland boilerplate -> https://github.com/defi-wonderland/solidity-foundry-boilerplate
Celoscan
DRPC - RPC infra

**Back-End Stack**
Nodejs, postgresql, express js, graphql apolo, adminjs, redis
Node 20.13.X

Comprehensive documentation and note on architecture will be periodically updated here: 
https://www.notion.so/giveth/Donation-Handler-Smart-Contract-MVP-dd0bb21940654f5d9f524870ed04c98a

## Contracts on Celo

Implementation -> https://alfajores.celoscan.io/address/0xc842a518f6c0fb58a9eb794d2dfd43db4b9551f3
Proxy -> https://alfajores.celoscan.io/address/0xd363df3de223a73bd78fa27251ad213528bc2761#code

