
# SuperFlow – One-Click Token Creation and Liquidity Management

## Link to your project's GitHub repository 
[Link](https://github.com/distroinfinity/superflow)

## Superflow Social

[Link](https://x.com/superflow0)

## Former Participation in Celo Hackathons
EthGlobal Bangok Celo Track Winners.

## Team Members GitHub username

[yeah-ssh](https://github.com/yeah-ssh)
[distroinfinty](https://github.com/distroinfinity)

## Goal for this Proof of Ship

Develop a one-click platform for token creation, bridging, and liquidity management on Celo.Making it *error free*, *robust* and *user friendly*.

### Detailed description of the work you did this month during the contest

- [Link 1](https://github.com/distroinfinity/superflow/pull/17)
- [Link 2](https://github.com/distroinfinity/superflow/pull/14)

## Problem

Launching tokens and managing liquidity across multiple chains is highly complex, time-intensive, and risky. Projects struggle with security vulnerabilities, fragmented tooling, and inefficient workflows that slow adoption.

## Solution

SuperFlow removes these barriers by providing an all-in-one, automated solution for:

- Token Generation – One-click ERC20 deployment with secure, audited contracts.  
- Cross-Chain Liquidity – Instant bridging of Celo tokens to major EVM chains.  
- DEX Liquidity Management – Automated pool creation for seamless trading.  

## Architecture
Token Deployment (newToken.js)
- Deploys new ERC-20 tokens using Hardhat & Ethers.js.
Liquidity Pool Setup (createUniswapPools.js)
- Pairs the deployed token with a collateral token.
Creates Uniswap V3 pools using FactoryV3 & Non-Fungible Position Manager.

## Deployed Contract Addresses on Celo

Tokens deployed on celo alfajores:
- 0x05f61aEA81839B6f4E21A308b1fc70a064bca843  
- 0xDD42Fc42c4D5294dC14bcc06eaC50EaE0387f18F  

## Real World Impact

- Simplifies Token Launches – Empowers projects, communities, and creators to launch, bridge, and scale with ease.
- Prevents Rug Pulls – Secure, pre-audited contracts mitigate investor risks and ensure integrity.
- Expands Celo’s Multi-Chain Reach – Establishes Celo as a key player in the multi-chain DeFi space.
- Democratizes DeFi Access – Allows anyone, regardless of technical expertise, to enter the ecosystem.
- Automates Complex Workflows – Saves time, cost, and effort by eliminating manual tokenomics setup. 
