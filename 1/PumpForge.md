# PumpForge

## Short Description
PumpForge is a one-stop platform on Celo for launching custom tokens with a fixed supply of 1 billion coins. It offers built-in features like tax logic, liquidity locking, and anti-bot measures, plus a user-friendly UI for token creation and management.

---

## Assets and Links

- **Logo & Screenshots**: (here)[https://drive.google.com/drive/folders/1Q2B0rAOgmttPZhA_1uYY1I-rIlVkxu53?usp=sharing]
- **Demo Video (4 min max)**: 
- **Presentation (max 10 slides)**: (here)[https://www.canva.com/design/DAGgICQlHqU/kI2JVwJr_xOiQ_FGaRHZKw/view?utm_content=DAGgICQlHqU&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h2e069f1d35]

---

## Detailed Description of Work This Month

- **Smart Contracts**  
  - PumpForgeToken: Fixed 1 billion supply, customizable metadata, tax logic, liquidity locking, anti-bot features.  
  - PumpForgeFactory: One-click deployment of new tokens with immediate ownership transfer.

- **Front-End Integration**  
  - Developed a React/Next.js DApp using the MiniPay template for mobile-first Celo support.
  - Implemented a Launch page to connect wallets, display account info, and allow token creation.
  - Introduced IPFS placeholders for future image uploads.

- **Liquidity & Future Enhancements**  
  - Laid groundwork for DEX integration (Ubeswap or Mobius).
  - Planning advanced analytics dashboard for token metrics, holder distribution, and real-time price tracking.

## Problem

**Celo** currently lacks a simple, accessible platform for creating and launching new tokens—be they memecoins or serious utility tokens. Builders need a robust, user-friendly solution to experiment with tokenomics and go live on the Celo ecosystem quickly.

### Competitor Analysis

- **Other ERC-20 Launch Platforms**: Often ETH-based, with high gas fees.  
- **Generic token creation services**: Typically do not include advanced features like anti-bot logic, liquidity locking, or custom tax logic out-of-the-box.  
- **PumpForge’s Advantage**: Focused on Celo’s low fees and mobile accessibility, plus built-in advanced tokenomics, security, and user-friendly design.

---

## Solution

PumpForge is an all-in-one token creation DApp on Celo that:

1. **Mints a Fixed 1 Billion Supply**: Encourages stable token supply across projects.  
2. **Advanced Features**: Built-in tax logic, liquidity locking, and anti-bot measures for a production-ready token from day one.  
3. **Mobile-First & Low Fees**: Harnesses Celo’s mobile accessibility and low transaction costs.  
4. **Open-Source & Extensible**: Encourages community contributions, with easy paths to integrate advanced functionalities like IPFS image uploads, DEX liquidity, and real-time analytics.

---

## Architecture

### Tech Stack

- **Smart Contracts**:  
  - Written in Solidity, deployed on Celo (Alfajores testnet).  
  - Hardhat for compilation, testing, and deployment scripts.

- **Front-End**:  
  - React/Next.js with the MiniPay template for wallet integrations.  
  - Tailwind CSS for styling (or your chosen framework).

- **Storage & Future Integrations**:  
  - IPFS for image uploads (planned).  
  - DEX (Ubeswap/Mobius) for liquidity creation (in progress).

### High-Level Overview

1. **PumpForgeFactory**: Deploys new PumpForgeToken contracts.  
2. **PumpForgeToken**: Enforces a fixed supply of 1B coins, includes advanced tokenomics (tax, liquidity lock, anti-bot).  
3. **Front-End**: Allows users to connect their Celo wallet, customize token parameters, and deploy instantly.  
4. **Optional Modules**: Liquidity management, IPFS image handling, analytics dashboards.


## Issues & Feedback

- **Gas & Contract Complexity**: Balancing advanced features (tax, anti-bot) while keeping deployment costs low on Celo.  
- **Wallet Integration**: Ensuring smooth user experience on mobile devices (MiniPay template simplified this).  
- **Planned Enhancements**: IPFS integration for direct image uploads, deeper liquidity management UI, and an analytics dashboard.

---

## Deployed Contract Addresses on Celo

- **PumpForgeToken (Test Example)**: `0xC46dD1Aa2fBD3C606C43d0009c1177D062db4b29`  
- **PumpForgeFactory**: `0xDDaDc9C6d1893a002e9a0c263EdE11B3f2Be857d`

**NOTE:** Our AI Agent Judge tracks transactions on deployed contracts. Make sure you have deployed your final versions to Alfajores or Mainnet before the deadline.
