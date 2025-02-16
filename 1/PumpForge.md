🚨 **Please don't write in this file**

Don't touch this file ----- please create a copy and name it after your project

# PumpForge

## Link to your project's GitHub repository 

- [https://github.com/lanacreates/PumpForge](https://github.com/lanacreates/PumpForge)

## Team Members GitHub username

- @lanacreates

## Former Participation in Celo Hackathons


## Monthly Goal for this Proof of Ship

**Monthly Goal (Feb 16th - Feb 28th):**  
I plan to build the core smart contract that enables users to launch their own tokens with a fixed supply of 1 billion coins, set custom metadata (name, symbol, and image via IPFS), and integrate initial swap functionality for trading Celo or cUSD for these tokens.

**Weekly Milestones:**
- **Week 1:**  
  - Set up development environment (Hardhat/Truffle, Node.js, Celo CLI) and initialize our GitHub repository.
  - Draft and test a Solidity smart contract that mints exactly 1 billion tokens on deployment.
- **Week 2:**  
  - Extend the smart contract to include functions for setting token metadata (name, symbol, image URL).
  - Deploy the contract on the Celo Alfajores testnet and record the contract address.
  - Begin work on a simple front-end interface for users to launch tokens.

### Detailed description of the work you did this month during the contest


## Problem

- Currently, there is no accessible platform on Celo for users to quickly launch their own tokens—whether for fun as memecoins or for practical utility. This gap makes it hard for creative builders to experiment with token dynamics in a live ecosystem.

## Solution

- **Pump Forge** provides a one-stop platform where anyone can create a token with a fixed supply of 1 billion coins. Users can customize the token’s name, symbol, and even upload an image (stored on IPFS) to represent their coin. Once launched, tokens can be swapped with Celo or cUSD, allowing market dynamics to determine value, all while being fully open-source and continuously updated.

## Architecture

- **Tech Stack:**
  - **Smart Contracts:** Solidity deployed on Celo (Alfajores Testnet initially)
  - **Development Tools:** Hardhat/Truffle, Node.js, Celo CLI
  - **Frontend:** React/Next.js for the web interface
  - **Storage:** IPFS for hosting token images
  - **DEX Integration:** Automated Market Maker (AMM) for token swaps on Celo

- **High-Level Overview:**
  - Users interact with the Pump Forge DApp through a web interface.
  - The DApp calls our smart contract to deploy a new token instance with a fixed supply of 1 billion coins.
  - Custom token metadata (name, symbol, image URL) is stored either on-chain or referenced via IPFS.
  - Once the token is launched, liquidity is provided so that users can swap Celo/cUSD for the newly minted tokens, with market dynamics determining price.

## Deployed Contract Addresses on Celo

- **Contract Address on Celo Alfajores Testnet:**  

- **NOTE:** Our AI Agent Judge tracks transactions on deployed contracts. Contracts are required in order to receive monthly rewards.
