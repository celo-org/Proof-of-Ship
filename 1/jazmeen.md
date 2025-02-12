# Project Name

Jazmeen

## Former Participation in Celo Hackathons- Link to hackathon submission

NIL

## Link to your repository. It needs to be Open Source.

[jazmeen](https://github.com/gabrieltemtsen/jazmeen)

## Goal for this Proof of Ship

*What are you planning to achieve. Be as detailed as possible. Try to break it down into weekly milestones.*

### **Week 1: Initial Setup & Smart Contract Development**
- Set up the development environment with Hardhat for smart contract work.
- Develop the factory smart contract for token creation and deployment.
- Implement the base ERC-20 token smart contract with customizable metadata (name, symbol, image).
- Define the automated fee-sharing mechanism (60% Jazmeen, 40% token creator) for token swaps.
- Test and deploy the initial contracts to the Celo testnet.

### **Week 2: Liquidity Provision Automation**
- Design and implement the smart contract logic to automate liquidity provision during token deployment.
- Research and integrate Celo-compatible decentralized exchanges (DEXs) for automated liquidity pools.
- Test liquidity provision with mock swaps and fee collection scenarios.
- Update contracts based on testing feedback.

### **Week 3: Frontend Development (Token Deployment Interface)**
- Set up a Next.js project for the frontend interface.
- Create a user-friendly form for token deployment with fields for token name, image, and symbol.
- Integrate the frontend with the deployed factory contract to initiate token creation.
- Display a summary of the deployed token with key details after successful deployment.

### **Week 4: Real-Time Token Insights**
- Implement a dashboard to display information about deployed tokens (name, symbol, liquidity, image, etc.).
- Integrate with Celo block explorers or APIs to fetch token transaction and swap data.
- Display swap events and earnings from fee-sharing on the dashboard.
- Add basic search and filter functionality for browsing tokens.

### **Week 5: Integration with Farcaster**
- Develop a Farcaster frame to display token updates and allow users to interact with the Jazmeen project.
- Implement a feature for users to cast updates about newly deployed tokens.
- Enable users to subscribe to token-related alerts via Farcaster.

### **Week 6: Advanced UX Features and Optimizations**
- Improve the UX by streamlining token deployment and liquidity provision in a single step.
- Implement a progress indicator and user-friendly error handling for all key actions.
- Add a feature to allow token metadata updates (e.g., changing token image).
- Optimize smart contract and API calls to reduce latency.

### **Week 7: Final Testing and Deployment**
- Conduct end-to-end testing for both the smart contracts and frontend interface.
- Run stress tests to ensure scalability with multiple token deployments and transactions.
- Fix bugs and finalize security audits for smart contracts.
- Deploy the final version to the Celo mainnet.

### **Week 8: Launch and Community Engagement**
- Announce the Jazmeen AI Agent on Farcaster, Twitter, and other platforms.
- Create documentation and tutorials for using the platform.
- Host a launch event or AMA to promote the project and gather feedback.
- Start monitoring user activity and collecting feedback for future updates.


## Detailed description of the work you did during the contest.
NIL

## Problem

### Lack of Memecoins on Celo**
Celo's blockchain ecosystem has limited activity in the memecoin space, which can reduce excitement, user engagement, and network adoption. Memecoins have historically attracted large communities and increased transaction volume on other chains.

## Solution

### Jazmeen AI Agent to Boost Ecosystem Adoption**
The Jazmeen AI Agent makes it easy to deploy and manage memecoins on Celo. By offering streamlined token creation, automated liquidity provision, and real-time insights, Jazmeen encourages memecoin creators and communities to launch projects on Celo. This will drive new users, increase transaction activity, and help grow the ecosystem with fun and viral projects.


## Architecture
### **1. Smart Contracts**
- **Factory Contract**:  
  Manages the creation and deployment of new memecoins on Celo, linking them to Jazmeen's ecosystem.
  
- **Token Contract**:  
  Custom ERC-20 tokens with metadata (name, image, symbol) and an integrated fee-sharing system (60% Jazmeen, 40% creator).

- **DEX Liquidity Pool**:  
  Automates liquidity provision on Celo-compatible decentralized exchanges during token deployment.

---

### **2. Frontend Interface**
- **User Interface (UI)**:  
  Built with Next.js and Tailwind CSS, providing a form to create and manage tokens.

- **Jazmeen Explorer**:  
  A dashboard displaying real-time insights into deployed tokens, liquidity pools, and transaction data.

- **Provision for Telegram & Web Chats**:  
  Enables integration with Telegram bots and web chat interfaces for notifications and user interactions.

---

### **3. Backend & AI Server**
- Handles requests from the frontend, Farcaster bot, and Telegram integration.
- Uses AI services like **Gaiai**, **Eliza**, and **Orbit** to enhance automation, data analysis, and notifications.
- Maintains secure communication with Celo smart contracts and updates real-time data.

---

### **4. Farcaster Bot Implementation**
- Periodically creates and posts casts about token events (new launches, swaps, liquidity updates).
- Provides updates to users who follow the Jazmeen bot or subscribe to specific tokens.
- Enables social engagement by broadcasting project milestones and updates across the Farcaster network.



## Deployed Contract Addresses on Celo

TBD 

## Team

**Gabe**- Fullstack Engineer 
Twitter: [Gabe on X](https://x.com/gabe_temtsen) 
Past experience: Celo BUilder, Based Builder Always Building, Building Never stops

**Kushi**- Frontend Engineer
Twitter: [Kushi on X](https://x.com/KushiNumdin)
Past experience: 6 Years working as a frontend developer