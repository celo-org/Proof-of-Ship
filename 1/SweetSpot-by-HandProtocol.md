# SweetSpot by HandProtocol

## Short Description

A decentralized app that lets you earn and use tokens to support impactful projects. Stake, donate, and grow your impact as you complete quests and help others. 

## Link to assets

- [SweetSpot DApp](https://sweetspot.wtf/) - A decentralized application currently live on the **Celo Alfajores Testnet**, with plans to launch on the **Celo Mainnet** soon.

- [HAND Protocol](https://handprotocol.org/) - A platform for the **HAND Protocol** organization and the projects we are currently working with.

## Link to Video

- [Demo Submission](https://www.youtube.com/watch?v=UDlFJG7GrK8)

## Link to your project's GitHub repository 	

- All Repos at : https://github.com/orgs/HandProtocol/repositories
- TheGraph Indexer : https://github.com/HandProtocol/subgraph-indexer
- Smart Contracts (Sweetspot & Scorer) : https://github.com/HandProtocol/contracts
- SweetSpot (Celo Dapp) : https://github.com/HandProtocol/SweetSpot
- Handprotocol Landing Page : https://github.com/HandProtocol/LandingPage

## Team Members GitHub username	

- RathodDeven (Development) : https://github.com/RathodDeven
- Cryptokoh (Designer, Communitcations, Marketing) : https://github.com/cryptokoh

## Former Participation in Celo Hackathons	

- None

## Monthly Goal for this Proof of Ship	

This month, the focus will be on improving onboarding tools, expanding impact project discovery, and deploying key infrastructure.

---

## **Week 1: Planning & Setup**
- [ ] Define detailed specifications for **allocation tooling** for onboarding.
- [ ] Research and outline key features for the **random project finder**.
- [ ] Set up a deployment pipeline for **Celo mainnet**.
- [ ] Review and finalize **Sweetspot frontend** redesign requirements.

---

## **Week 2: Development & Testing**
- [ ] Begin development of **allocation tooling** MVP.
- [ ] Prototype the **random project finder** logic and user flow.
- [ ] Write and test smart contract changes for **Celo deployment**.
- [ ] Implement initial UI/UX improvements for **Sweetspot frontend**.

---

## **Week 3: Integration & Deployment**
- [ ] Finalize and integrate the **allocation tooling** into onboarding.
- [ ] Deploy and test the **random project finder**.
- [ ] Deploy **smart contracts & subgraph** on **Celo mainnet**.
- [ ] Conduct UI/UX tests on **Sweetspot frontend** and refine based on feedback.

---

## **Week 4: Optimization & Launch Prep**
- [ ] Optimize **allocation tooling** based on testing and feedback.
- [ ] Improve algorithm and user experience for **random project finder**.
- [ ] Debug and refine the **Celo mainnet deployment**.
- [ ] Finalize and polish **Sweetspot frontend redesign** for launch.

---

## **Stretch Goals (if time permits)**
- [ ] Improve documentation for onboarding & integration.
- [ ] Explore additional blockchain integrations for future expansion.
- [ ] Conduct community feedback sessions for usability improvements.

### Detailed description of the work you did this month during the contest	

# Monthly Work Summary - Contest Month

## **Overview**
This month, significant improvements were made to both smart contracts and frontend components of the HAND Protocol. The updates focused on optimizing contract logic, enhancing error handling, improving documentation, and refining the user experience on SweetSpot.

---

## **Smart Contract Enhancements**
### **SweetSpot Contract & Scorer Contract**
- Added proper error handling and optimizations.
- Improved the documentation for better developer accessibility.
- Refactored code for efficiency and maintainability.

**Related Commits:**
- [SweetSpot Contract Update](https://github.com/HandProtocol/contracts/commit/4606ebc5e92e7253dd165c2a9f0bb27b8dd69e89)
- [Scorer Contract Update](https://github.com/HandProtocol/contracts/commit/0c5c220c9e8214c5c69945f18915dfcb071451a3)
- [Pull Request - Smart Contract Improvements](https://github.com/HandProtocol/contracts/pull/5)

---

## **Frontend Improvements**
### **SweetSpot Application Updates**
- Enhanced `UserAvatar` component with a loading state and improved styling.
- Removed unnecessary debug logging from the `getPassportScore` function.
- Updated the app name to `SweetSpot` and integrated **Gitcoin Passport** score fetching.
- Improved documentation, including API documentation for environment variables.
- Updated the README with a detailed project description and setup instructions.

**Related Commit:**
- [SweetSpot Frontend Enhancements](https://github.com/HandProtocol/SweetSpot/commit/d18be092abb211acba07e078a0875bb25aa2f0ed)

## Problem	

Many decentralized funding platforms struggle with **sybil resistance**, where fraudulent identities exploit the system to gain an unfair share of rewards. Without proper verification, resources meant for impactful projects can be misallocated, reducing the effectiveness of decentralized funding.

Additionally, users lack a seamless way to **earn, stake, and donate tokens** while ensuring their contributions go toward legitimate, high-impact initiatives. The absence of transparent scoring mechanisms makes it difficult to assess the credibility of participants, leading to inefficiencies and trust issues in the ecosystem.

	

## Solution	

SweetSpot addresses these challenges by integrating a **decentralized scoring system** that ensures fair participation and **trust-based funding mechanisms**. It utilizes **Gitcoin Passport scores** and the **Scorer Contract** to evaluate users' credibility, preventing sybil attacks and ensuring that funding reaches genuine participants.

### Key Solutions:
- **Scorer Contract**: Assigns and verifies trust scores, ensuring only credible users can access rewards and funding.
- **On-Chain Verification**: Uses decentralized identity solutions to prevent multiple accounts from gaming the system.
- **Token-Based Participation**: Enables users to **stake, donate, and earn tokens** transparently, promoting sustainable engagement with impact-driven projects.
- **Smart Contract Automation**: Ensures fair distribution of funds and rewards based on verified user scores, eliminating manual oversight and potential biases.

By integrating these mechanisms, SweetSpot creates a **secure, transparent, and fair ecosystem** where users can support impactful projects with confidence.

## Competitors and How SweetSpot can be Better 

### Competitors
Some existing platforms that tackle decentralized funding and identity verification include:
- **Gitcoin Grants** - A leading quadratic funding platform that supports open-source projects through community contributions.
- **Giveth** - A donation-based funding platform for public goods projects.
- **Clr.fund** - A funding mechanism using quadratic voting to allocate resources fairly.
- **Snapshot** - A governance platform enabling token holders to vote on funding decisions.

### Why SweetSpot is Better
- **Direct Token Utility**: Unlike traditional donation platforms, SweetSpot enables users to **earn, stake, and donate** in an integrated system that promotes active participation.
- **Automated Trust Scoring**: Using **Gitcoin Passport scores** and **Scorer Contracts**, SweetSpot ensures that only verified, credible users receive funding, solving the **sybil resistance problem** more effectively.
- **Flexible Funding Models**: Supports **quest-based rewards**, **staking mechanisms**, and **donation pools**, offering more engagement opportunities beyond standard grants or donations.
- **Transparent and On-Chain**: All funding decisions, score verifications, and token distributions happen **on-chain**, ensuring transparency and eliminating centralized control.

### Could We Build on Top of Competitors?
Yes. SweetSpot could integrate with:
- **Gitcoin Passport** for enhanced identity verification.
- **Gitcoin Grants & Clr.fund** for expanding funding options.
- **Snapshot** for governance and community decision-making.
- **Giveth** to enhance impact tracking and donation management.

Rather than replacing these platforms, SweetSpot aims to **complement and enhance** their existing solutions by creating a more **integrated and engagement-driven funding ecosystem**.

## Architecture

### **Tech Stack**
SweetSpot leverages a combination of Web3 and traditional technologies to provide a seamless decentralized funding experience. Below are the key technologies used:

#### **Web3 Libraries & Protocols:**
- **TheGraph** - Used to index smart contracts (**Scorer.sol** and **SweetSpot.sol**) for efficient data retrieval.
- **Remix** - For creating, deploying, and managing smart contracts.
- **Ethers.js** - For interacting with Ethereum-based smart contracts in the frontend.
- **GraphQL** - For querying indexed blockchain data from **TheGraph**.
- **IPFS** - For decentralized storage of metadata.
- **Gitcoin Passport** - For verifying user identity and credibility.
- **Gnosis Safe** - For secure contract interactions and fund management.
- **OpenZeppelin TransparentUpgradeableProxy** - Used to deploy **upgradeable** smart contracts, ensuring flexibility and future improvements.

#### **Frontend & Backend Technologies:**
- **Next.js** - Used for building both the **landing page** (for onboarding projects and showcasing them) and the **SweetSpot frontend** (for interacting with smart contracts).
- **MongoDB** - Used for storing off-chain data that doesn’t need to be recorded on the blockchain.
- **Node.js & Express** - Backend services managing API requests and interactions with MongoDB.

### **High-Level Architecture Overview**
1. **Smart Contracts**: 
   - **Scorer.sol**: Assigns and verifies trust scores for users.
   - **SweetSpot.sol**: Manages staking, donations, and reward distribution.
   - **TransparentUpgradeableProxy**: Ensures contracts can be upgraded without disrupting the system.
2. **Subgraph Indexing**:
   - TheGraph indexes contract events and transactions for easy querying.
3. **Frontend Applications**:
   - **Landing Page**: Displays all onboarded projects and fundraising opportunities.
   - **SweetSpot Frontend**: Enables users to interact with the smart contracts, make donations, and claim rewards.
4. **Database & API Layer**:
   - MongoDB stores non-essential off-chain data.
   - API services handle interactions between the frontend, blockchain, and database.
5. **User Authentication & Verification**:
   - Gitcoin Passport ensures only **verified, unique users** can access funding and rewards.
   
This architecture ensures that **on-chain interactions remain efficient, off-chain data is managed securely, and users have a seamless experience** while engaging with the platform.

---

## Deployed Contract Addresses on Celo

SweetSpot contracts have been deployed on the **Celo Alfajores Testnet** and soon will be moved to Mainnet

### **Smart Contract Addresses**
- **Scorer Proxy Contract**: [0x9E2851e9Cb3425BeAC4A18071505BaaE77e3BdEb](https://alfajores.celoscan.io/address/0x9E2851e9Cb3425BeAC4A18071505BaaE77e3BdEb#code)
- **SweetSpot Proxy Contract**: [0xa6e35CCf2950c637AF0F06e162A3991f50CE210f](https://alfajores.celoscan.io/address/0xa6e35CCf2950c637AF0F06e162A3991f50CE210f#writeProxyContract)
- **Subgraph** : https://thegraph.com/studio/subgraph/hand/playground

These contracts are deployed using **OpenZeppelin's TransparentUpgradeableProxy**, ensuring that they can be upgraded in the future to improve functionality and security without disrupting the platform.

