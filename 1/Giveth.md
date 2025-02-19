# Project Name

Giveth donation handler smart contract 

## Former Participation in Celo Hackathons- Link to hackathon submission

*Mitch’s Hackathon Team ETHGlobal Bangkok* 
[https://ethglobal.com/showcase/union-registry-oxjax](https://ethglobal.com/showcase/union-registry-oxjax)

## Link to your repository. It needs to be Open Source.

[https://github.com/Giveth/Proof-of-Ship](https://github.com/Giveth/Proof-of-Ship)

## Goal for this Proof of Ship

*What are you planning to achieve. Be as detailed as possible. Try to break it down into weekly milestones.*

The goal is to develop and integrate a Donation Handler Smart Contract into Giveth’s donation flow on Celo. This contract will serve as an intermediary between donors and project wallets, enabling on-chain tracking, automation, and improved reporting. Building the first version of a Donation Handler for Giveth opens up many possibilities for Giveth and its donors including:	



* Allowing donations to be made externally outside of Giveth’s UI
* AI Agent integrated public goods funding 
*  “Cart of donations” bundled into a single transaction

## Weekly Milestones:

### Week 1:
* Define contract architecture and outline required functionalities.
* Draft initial smart contract implementation with core functions:
    * Receiving and forwarding donations made in ERC20 and native ETH
    * Routing funds to project recipient addresses
    * Bundling optional % based donations to Giveth into a single tx
    * Contract Upgradeability
    * Owner/Admin functions 

### Week 2:
* Peer review and soft audit of proposed Donation Handler contract code

### Week 3:
* Implement peer review changes and soft audit observations into final code draft

### Week 4:
* Write successful  tests in Foundry framework for:
    * handling ETH donations
    * handling ERC20 donations 
    * sending % based donations to Giveth
    * contract upgradeability

### Week 5:
* Deploy Donation Handler to Celo Alfajores.
* Integrate smart contract into existing Giveth BE infrastructure

### Week 6 & 7
* Continue Integrating Donation Handler into BE 
    * Indexing donation transactions 
    * Parsing relevant donation data from transactions 
    * Filling price information for assets 
    * Creating/updating endpoints for serving data to FE
    * QA

### Week 8 & 9 
* Update Giveth Front-End
* Fetching data from BE endpoints 
* Showing correct data for user & project information 
* Ensuring timeliness of indexing and data delivery to FE

### Week 10
* QA
* Ensure features work as expected, end to end

### Week 11 
* Deploy Donation Handler to Celo Mainnet 
* Prepare necessary configurations for production release 

## Detailed description of the work you did during the contest.


#### **Pull Requests:**

* PR for Donation Handler Contract
* PR for BE release to production
* PR for FE release to production

## Problem

Giveth’s backend is 5 years old, making it outdated and inefficient.

* Relies on centralized back-end service to track donation data and maintain state
* Donations appear as regular token transfers, making them hard to track
* Not suited for external teams to make donations or query donation data 
* RPC or other infra outages cause massive headaches and lost donations

A Donation Handler Smart Contract modernizes this flow, making it flexible, low overhead, transparent, and scalable.

## Solution

The Donation Handler Smart Contract solves these issues by:



* Allowing donations to be clearly tracked and indexed on-chain
* Reducing reliance on centralized back-end service
* Enabling AI-based donations, opening up design space for new funding mechanism experimentation
* Allowing external transactions, so donations can be made outside Giveth’s UI.
* Increasing reliability of donation verification, lowering risks of missing donation data
* Increasing transparency of donation activity by making it distinguishable on-chain

## Architecture

**Components:**
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

## Deployed Contract Addresses on Celo

TBD 

## Team

**Mitch**-  dApp Development & Project Lead  
GitHub: https://github.com/divine-comedian
Twitter: [https://x.com/divine_comedian](https://x.com/divine_comedian) 
Past experience: DAO Ops Lead & Product Manager at Giveth. Junior Solidity Developer. Formerly Rewards System Lead at TEC, Project Manager at General Magic and Client Relations for Praise

**Carlos**- SR Backend Engineer
GitHub: https://github.com/CarlosQ96
Twitter: [https://x.com/CarlosQ096](https://x.com/CarlosQ096)
Past experience: 7 Years working as a backend developer, divided into 4 years in the web2 industry for Koombea in e-commerce and mobile applications, and 3 years building robust web3 backend integrations with the blockchain and smart contracts for Giveth and General Magic.
