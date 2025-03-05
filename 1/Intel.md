# Project Name

## Intel

## Link to your project's GitHub repository 

- [Intel's github Link](https://github.com/jeffIshmael/Intel)

## Team Members GitHub username

- [Member 1](https://github.com/jeffIshmael)

## Former Participation in Celo Hackathons

- None

## Monthly Goal for this Proof of Ship

### 1st Month Goals

 - Identify and integrate a tool to retrieve all available staking pools on Celo.

 - Develop a mechanism to evaluate and select the most profitable staking pool.
 
 - Set up a user-friendly frontend to facilitate interaction with staking pools.

 - Enable users to manually stake their cUSD in chosen liquidity pools.

 - Design an AI agent that dynamically selects the optimal staking pool and automates the staking process.

**Note:** In this phase, we are utilizing the user's wallet to stake directly in liquidity pools without an intermediary staking smart contract. Once this system is fully functional, we will introduce a dedicated staking smart contract.

### 2nd Month Goals

 - Develop and deploy smart contracts to efficiently manage staking in liquidity pools.

 - Perform comprehensive testing and security audits to ensure system integrity.

 - Launch on the Celo mainnet with an optimized and improved UI/UX experience.


## Problem

- Manually staking stablecoins (cUSD) in liquidity pools can be inefficient, requiring constant monitoring and strategy adjustments.

- Users often lack the expertise or time to optimize yield farming strategies effectively.

## Solution

- Intel automates cUSD staking by leveraging an AI agent that continuously monitors liquidity pools and adjusts staking strategies in real time to maximize returns.

- It removes the need for manual intervention, making yield farming accessible and efficient for all users.

## Architecture

### Tech stack
  - **Blockchain:** Celo
  - **Smart Contract:** Solidity
  - **Frontend:** Next.js, Tailwind CSS
  - **ORM:** Prisma
  - **Database:**  PostgreSQL (To keep data of user's staked pools)

### High level overview of your project architecture

  - Users deposit cUSD into Intel’s AI wallet.
  - The AI agent monitors liquidity pools and automatically moves funds to the most profitable options.
  - A frontend dashboard provides real-time updates on the staking pools.

## Deployed Contract Addresses on Celo

 - Contract Address (Testnet - Alfajores): To be deployed
 - Mainnet Address: To be deployed
