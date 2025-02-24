🚨 **Please don't write in this file**

Don't touch this file ----- please create a copy and name it after your project

# PumpForge

## Link to your project's GitHub repository 
- [https://github.com/lanacreates/PumpForge](https://github.com/lanacreates/PumpForge)

## Team Members GitHub username
- @lanacreates

## Former Participation in Celo Hackathons
*(None yet)*

## Monthly Goal for this Proof of Ship

**Monthly Goal (Feb 16th - Feb 28th):**  
I plan to build the core smart contract suite that enables users to launch their own tokens with a fixed supply of 1 billion coins, set custom metadata (name, symbol, and image via IPFS), and integrate initial swap functionality for trading CELO or cUSD for these tokens. The system will deploy Celo-specific token contracts along with a factory contract to enable one-click token deployment.

**Weekly Milestones:**
- **Week 1:**  
  - Set up the development environment (Hardhat, Node.js, Celo CLI) and initialize the GitHub repository.
  - Draft and test the PumpForgeToken contract which mints exactly 1 billion tokens upon deployment.
  - Develop the PumpForgeFactory contract to allow one-click deployment of new tokens.
- **Week 2:**  
  - Extend the token contract to include functions for customizable metadata (name, symbol, image URL).
  - Deploy the contracts on the Celo Alfajores testnet and record the deployed contract addresses.
  - Begin work on integrating the front-end interface using React/Next.js with the MiniPay template.
- **Upcoming:**  
  - Implement liquidity management via DEX integration.
  - Build an analytics dashboard and explore social features.

### Detailed description of the work you did this month during the contest
- Deployed the production-ready smart contracts on Alfajores:
  - **PumpForgeToken deployed to:** `0xC46dD1Aa2fBD3C606C43d0009c1177D062db4b29`
  - **PumpForgeFactory deployed to:** `0xDDaDc9C6d1893a002e9a0c263EdE11B3f2Be857d`
- Initial commit: [273cf23aad4da97e600290a9f44c72cd95d570c3](https://github.com/lanacreates/PumpForge/commit/273cf23aad4da97e600290a9f44c72cd95d570c3)

## Problem

- There is currently no accessible, user-friendly platform on Celo for launching custom tokens—whether for playful memecoins or practical utility tokens. This gap prevents creative builders from experimenting with token dynamics in a live ecosystem.

## Solution

- **Pump Forge** provides a one-stop, open-source platform for token creation on Celo. Users can launch a token with a fixed supply of 1 billion coins, customize its name, symbol, and upload an image (stored on IPFS), and later enable liquidity swaps with CELO or cUSD. The platform integrates best-in-class features such as custom tax logic, liquidity locking, anti-bot protection, and more, making it both fun and robust.

## Architecture

- **Tech Stack:**
  - **Smart Contracts:** Solidity deployed on Celo (Alfajores Testnet initially).
  - **Development Tools:** Hardhat, Node.js, Celo CLI.
  - **Frontend:** React/Next.js using the Celo Composer MiniPay template.
  - **Storage:** IPFS for hosting token images.
  - **DEX Integration:** Automated Market Maker (AMM) protocols (e.g., Ubeswap/Mobius) for token swaps on Celo.

- **High-Level Overview:**
  - Users interact with the Pump Forge DApp via a mobile-responsive web interface.
  - The DApp interacts with the PumpForgeFactory contract to deploy new PumpForgeToken instances.
  - Each token is deployed with a fixed supply of 1 billion coins and includes customizable metadata.
  - Once launched, tokens can be paired with CELO/cUSD via integrated liquidity pools, enabling market-driven pricing.

## Deployed Contract Addresses on Celo

- **PumpForgeToken:** `0xC46dD1Aa2fBD3C606C43d0009c1177D062db4b29`
- **PumpForgeFactory:** `0xDDaDc9C6d1893a002e9a0c263EdE11B3f2Be857d`

**NOTE:** Our AI Agent Judge tracks transactions on deployed contracts. Deployments are required to receive monthly rewards.

---

This updated PRD now reflects the current status and roadmap of PumpForge based on the deployed contracts and recommendations. Happy building!
