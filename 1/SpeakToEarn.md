# Project Name

SpeakToEarn

## Short Description

Speak To Earn empowers native speakers from low-resource communities to earn for sharing their linguistic expertise, helping create AI that reflects humanity's true linguistic and cultural diversity.

## Link to your project's GitHub repository 

- https://github.com/thealexyao/speaktoearn-agent
- https://github.com/thealexyao/speaktoearn-app
- https://github.com/thealexyao/speaktoearn-data

## Team Members GitHub username

https://github.com/thealexyao

## Former Participation in Celo Hackathons

### Safe Agentathon (February 2024) - 48 Hour Sprint
Built SpeakToEarn, a decentralized marketplace for language data collection using AI agents & Celo Blockchain in just 48 hours:

#### Day 1: Core Infrastructure
- Smart contract development and deployment to Alfajores
- AI agent implementation with GPT-4o evaluation system
- Basic frontend setup with wallet integration

#### Day 2: Feature Completion & Launch
- Complete evaluation pipeline with real-time verification
- Frontend polish and user experience improvements
- Live deployment of dApp and data commons
- Demo video and presentation creation

#### Achievement
Won first place in the Celo x Safe Agentathon for the DeFAI track, demonstrating rapid execution and technical excellence.

### Detailed description of the work completed in 48 hours

Rapid development and deployment of:
- Smart contract integration with Celo Alfajores
- AI agent system for automated task matching and verification
- Frontend dApp with seamless user experience
- Backend services for real-time AI evaluation

Live Results:
- Demo: https://speaktoearn.app/
- Data Commons: https://commons.speaktoearn.org
- Demo Video: https://www.loom.com/share/d1473f89df58401989c134bec49f28ac
- Project Page: https://devfolio.co/projects/yapper-9cfd

#### Assets

- Screenshots of the app:

![Screenshot 1](https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/f8ebb5924ab74123bbd7088731ca9ab8/projects/c69d85acc1574359a097a903ceba8ff1/d57d84ec-d1fe-4c1d-a71c-ca0fb36e0ff6.png)
![Screenshot 2](https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/f8ebb5924ab74123bbd7088731ca9ab8/projects/c69d85acc1574359a097a903ceba8ff1/d57d84ec-d1fe-4c1d-a71c-ca0fb36e0ff6.png)
![Screenshot 3](https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/f8ebb5924ab74123bbd7088731ca9ab8/projects/c69d85acc1574359a097a903ceba8ff1/8ca249db-d51c-4949-a5e3-76772905842c.png)
![Screenshot 4](https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/f8ebb5924ab74123bbd7088731ca9ab8/projects/c69d85acc1574359a097a903ceba8ff1/6a97783d-e251-4723-be5f-d01b426bdaa4.png)
![Screenshot 5](https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/f8ebb5924ab74123bbd7088731ca9ab8/projects/c69d85acc1574359a097a903ceba8ff1/98b6c272-e0f6-4f28-a857-1ed9e58a9d62.png)
![Screenshot 6](https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/f8ebb5924ab74123bbd7088731ca9ab8/projects/c69d85acc1574359a097a903ceba8ff1/053489f7-10d4-42f9-a0f9-fea63098490a.png)

## Monthly Goal for this Proof of Ship

What are you planning to ship this month? Be as detailed as possible. Try to break it down into weekly milestones. 

- Build a new AI agent for language data collection
- Build a new frontend for the dApp
- Build a new backend for the dApp
- Deploy the smart contracts to Celo
- Deploy the dApp to Celo

### Detailed description of the work you did this month during the contest

Completed development and deployment of:
- Smart contract integration
- AI agent system for automated task matching and verification
- Frontend dApp
- Backend services for AI evaluation

Links to work:
- Live demo: https://speaktoearn.app/
- Data commons: https://commons.speaktoearn.org

## Next Steps & Future Development

Post-Hackathon Roadmap:
1. Scale & Optimization
   - Support for 10+ languages
   - Build full AI agent evaluation pipeline
   - Enhance real-time performance

2. User Growth
   - Launch contributor onboarding
   - Build community features
   - Expand task types

## Problem

- AI models lack high-quality, diverse language data
- Traditional data collection methods are slow and expensive
- Native speakers aren't fairly compensated for their knowledge
- Low-resource languages are underrepresented in AI training

## Solution

Speak to Earn creates a decentralized marketplace where:
- Users earn CELO stablecoins for verified language contributions
- AI agents automate task matching and quality verification
- Smart contracts ensure transparent, instant payments
- Contributors build a valuable data commons for AI advancement

## Architecture

Tech Stack:
- Frontend: React, TailwindCSS, ethers.js
- Backend: Node.js, Express, OpenAI
- Blockchain: Solidity, Hardhat, OpenZeppelin
- Storage: Web3.Storage

Architecture Overview:
1. Smart Contracts
   - Reward distribution system
   - Task verification
   - Fund management

2. AI Agents
   - Task matching
   - Quality verification
   - Real-time evaluation

3. User Interface
   - Wallet integration
   - Task submission
   - Payment tracking

## Deployed Contract Addresses on Celo

Alfajores Testnet:
- SpeakToEarn.sol: 0x1c65ad6F6FD141E2cfdee83F524ADA6E70eaea3f

# Updates

## Final Week / Monthly Work Update

### 1. Detailed Description of This Month's Work

**Summary:**  
This month we built the core MVP for our crowdsourced language data platform. Our demo uses a chat-based interface where users complete two tasks—paraphrasing a financial report sentence and correcting a misstated fact—to earn crypto rewards. The system integrates an AI evaluation engine (using GPT‑4o assistant with function calling) with smart contract-based payments on the Celo Alfajores testnet. We completed the following key components:
- **Smart Contracts:** Designed and deployed a Payment Contract on Celo Alfajores that triggers token transfers based on approved submissions.
- **AI Evaluation Module:** Developed a backend function that sends task submissions to GPT‑4o with function calling, returning structured JSON output (pass/fail, score, qualitative feedback).
- **Chat-Based Interface:** Implemented a React+Vite chat UI that guides users through task selection, displays detailed instructions with realistic examples, collects their input, and shows evaluation results.
- **Backend Integration:** Wired together the chat UI, AI evaluation, and smart contract interaction using Node.js and ethers.js.

We also built out a frontend for the hackathon demo and also the data commons dashboard.
- Live demo: https://speaktoearn.app/
- Data commons: https://commons.speaktoearn.org

---

### 2. Problem

**Competitor Landscape:**  
Traditional crowdsourcing platforms (e.g., Mechanical Turk, Figure Eight) rely heavily on human moderators and manual quality checks, leading to inconsistent data quality and slower processing. Other blockchain-based solutions either lack a robust AI evaluation process or require users to interact via complex dashboards.

**Our Differentiation:**  
We offer a unique, automated approach that combines:
- **Automated Quality Evaluation:** Using GPT‑4o assistant with function calling to rigorously check language quality (accuracy, relevance, coherence, and fluency) without human intervention.
- **Seamless Crypto Payments:** A smart contract on Celo Alfajores that instantly rewards contributors based on evaluation outcomes.
- **Intuitive Chat-Based Interface:** A conversational UI that guides users through tasks without the need for a complex dashboard, making it mobile-friendly and user-centric.

---

### 3. Solution

**Task Flow and Functionality:**  
We designed two primary tasks for the MVP:
- **Paraphrase Task:** Users rewrite a sentence from a financial report in their own words.  
  - *Example:*  
    - **Original:** "According to the company's quarterly report, revenue grew by 12% compared to the previous quarter despite a downturn in global markets."  
    - **Expected Paraphrase:** "The quarterly report shows that revenue increased by 12% over the last quarter, even though global markets were declining."
- **Factual Verification Task:** Users review and correct a factual statement.  
  - *Example:*  
    - **Input:** "The capital of Australia is Sydney."  
    - **Expected Correction:** "The capital of Australia is Canberra. Although Sydney is the largest city, Canberra is the political center."

**How It Works:**  
1. **User Interaction:**  
   - The chat interface welcomes the user and asks which task they'd like to perform.
   - Based on selection, the system sends detailed instructions and an example.
2. **Submission & Evaluation:**  
   - The user submits their response as a chat message.
   - The backend calls the GPT‑4o assistant with a task-specific prompt using function calling.  
   - GPT‑4o returns a structured JSON (pass/fail, score, feedback).
3. **Payment Trigger:**  
   - If the response passes, the backend calls our Payment Contract's `sendPayment` function (e.g., transferring 0.25 cUSD for a paraphrase task or 0.15 cUSD for factual correction).
   - A confirmation event is emitted and logged.
4. **Feedback & Next Steps:**  
   - The chat displays the evaluation result and payment confirmation.
   - The system then asks if the user would like to complete another task.

---

### 4. Architecture

**Frontend:**  
- **Framework:** React with Vite  
- **Components:**  
  - Chat-based interface (using a custom or third-party chat component)  
  - Task selection and task detail pages (rendered within the chat flow using state management)  
- **Routing:** Managed by react-router-dom (if needed for navigation within the chat flow)

**Backend:**  
- **Server:** Node.js (with Express)  
- **AI Evaluation Module:**  
  - Uses OpenAI's GPT‑4o assistant with function calling to evaluate submissions.  
  - Returns structured JSON with decision, score, and feedback.
- **Payment Integration:**  
  - Uses ethers.js to interact with our Solidity Payment Contract on Celo Alfajores.
- **State Management:** Context or session variables to manage chat conversation state.

**Blockchain:**  
- **Network:** Celo Alfajores Testnet  
- **Smart Contract:**  
  - Written in Solidity, the Payment Contract includes functions like `sendPayment()`, and emits events for successful payouts.
  
**Libraries & Frameworks:**  
- React, Vite, react-router-dom  
- Node.js, Express  
- ethers.js for blockchain interactions  
- OpenAI API for GPT‑4o integration  
- dotenv for environment configuration

---

### 5. Feedback & Issues Encountered

- **Prompt Engineering:**  
  - Initially, GPT‑4o responses contained extra text. We refined the prompt and used function calling to enforce structured JSON outputs.
- **Testing Environment:**  
  - Setting up local testing with Celo and simulating token transfers required extra configuration. I need to rebuild the Celo contract interactions using Viem instead of ethers.js.
- **Overall:**  
  - The integration between AI evaluation and payment triggering is promising, though additional work is needed to handle edge cases and building out the full ai agent system.

## AI Evaluation System

### Prompt Engineering & Quality Verification

The system uses a structured approach for AI-powered evaluation:

#### System Prompt Structure
The system prompt establishes the AI as an expert evaluator for specific task types (paraphrase/factCheck), focusing on three key metrics:
- Accuracy
- Clarity
- Completeness

#### Structured Evaluation Output
The evaluation function enforces structured output with:
- Binary decision (Pass/Fail)
- Overall score (0-100)
- Detailed feedback
- Individual criteria scores:
  - Accuracy (0-100): Factual correctness/meaning preservation
  - Clarity (0-100): Writing quality and understandability
  - Completeness (0-100): Coverage of required information

#### Quality Thresholds
Payment triggers only when:
- Decision is "Pass"
- Overall score ≥ 70

#### Agent Thought Process
The system maintains transparency by recording:
- Evaluation reasoning
- Step-by-step analysis plan
- Criticism and improvement suggestions

#### Example Quality Standards
The system uses reference examples to calibrate evaluation:
- Paraphrase task: Preserves meaning while varying structure
- Fact check task: Clear correction with accurate information

#### Error Handling
Failed evaluations are logged with:
- Failure reasoning
- Improvement suggestions
- Error context for debugging

This approach ensures:
- Consistent evaluation across submissions
- Quantifiable quality metrics
- Transparent decision-making
- Actionable feedback for users
- Auditable evaluation process