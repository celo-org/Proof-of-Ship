# Project Name
Employee.ai

## Short Description
🚀 Introducing Employee AI! Automate your digital tasks, on-chain activities, and social media posting effortlessly with our virtual agents. #AIAgents #AI #Automation #Web3

## Links

-  [Video](https://youtu.be/6s1ZxTkVgrM)
-  [Presentation](https://www.canva.com/design/DAGgAKvKkRc/y90PmscJnCth_EdpOQ0WmA/edit?utm_content=DAGgAKvKkRc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Description of work done in the last month

I was able to develop a working prototype using Coinbase Agentkit [Demo video](). Thereafter, I started improving the system by setting up a dedicated backend for server so that I can easily develop my custom agents and not be restricted to Coinbase Agentkit. 
- Frontend Landing page and chat UI
  - Authentication using Privy Auth
- Backend setup and deployment
  - Twitter Agent service
  - Celo API Service
  - Langchain service
  - Graphql endpoint configuration


## Problem
Some of the problems Employee.ai aims to solve include
1. Friction when using multiple AI tools
2. Difficulty in analyzing the current market state
3. Challenges trying to get quick answers on Web3 niched topics

## Solution
With the increase in awareness of the potentials of artificial intelligence (AI) Employee.ais aims to:

1. Leverage AI for automating tasks on the blockchain
2. Get current chain activities such as top performing tokens, whale purchase, etc
3. Aggregate news that may influence the crypto market
4. Ease the process needed to place an order in the crypto market by analyzing prompts and making decisions accordingly
5. Provide quick answers to niche web3 topics


## Architecture

Employee.ai is composed of three main stacks

1. **Frontend Stack:**

   - **Next.js:** User friendly interface to enable users chat with the ai.
   - **Privy Auth:** Used for authentication of users into the app.

2. **Agent Stack:**

   - **Langchain:** Manage different models and can be used to create custom agents
   - **CDP AgentKit:** Provides the agents and a set of actions that can be plugged in to give the llm more capabilities

3. **API Stack:**

   - **Backend APIs:** Provides REST endpoints for frontend communication with the user's desired ai agent. Powered with Nest.js backend
     - LLM models
     -  API Services e.g Twitter, Celo, Lemonade, Whatsapp
     -  Postgres Database - managing conversations memory of the agents
     -  Privy Sever wallets service to power agents onchain transactions
   - **Database** PostgresDB for management of conversations
   - **Privy Server Wallets:** For AI Agent's wallet. We can fund it and ask it to perform some transactions on the wallet.


## Github Repo 

- https://github.com/philix27/employee_ai


## Team

- Eligbue Felix



## Goal for this Proof of Ship

What are you planning to achieve. Be as detailed as possible. Try to break it down into weekly milestones. 
- `Feb 2 - 8`: 
  - [X] Design User interface of App
  - [x] Build Landing page
  - [x] Build Dashboard 
    - [x] Frontend: Develop Chat screen
    - [x] Frontend: Develop AI Management window
  - [x] Frontend: Deploy to vercel
  - [x] Frontend: Sign in with Privy
  - [x] Frontend: Wagmi setup, to work with Privy Auth
  
- `Feb 9 - 15`: 
  - [x] Setup Nest.js Backend
  - [x] Deploy to railway
  - [x] Setup Graphql configurations
  - [x] Setup Prisma configurations for database
  - [x] Setup Postgres container
- `Feb 16 - 22`: 
  - [ ] Backend: ChatConversations Modules - 
  - [ ] Backend: ChatMessage Modules
  - [ ] Backend: PlatformAccount Modules
  - [ ] Backend: Posts Modules
  - [ ] Backend: Services for Twitter Agentkit
  - [ ] Frontend: Consume graphql endpoint - Setup config
    - [ ]  Frontend: Run basic llm based chat with AI 
  
- `Feb 23 - Mar 1`: 
  - [ ] Backend: Services for Langchain DeepSeek and OpenAI
  - [ ] Backend: Services for Celo Blockchain APIs
  - [ ] Backend: Celo Agent construct
    - [ ] Pull onchain transactions
    - [ ] Check wallet balance
- `Mar 2 - Mar 8`: 
  - [ ] Pull data from `(The graph)[https://thegraph.com/] 
  - [ ] Generate Server Wallet for users using Privy
  - [ ] Testing



## Former Participation in Celo Hackathons

-  [Mobarter - P2P offramping app](https://github.com/philix27/mobarter-app)
-  [Pocket Ramp - Off ramping solution](https://github.com/philix27/pocket)
-  [Supa Save - Locked savings dApp](https://github.com/philix27/supa-save1)
-  [Rampage](https://github.com/philix27/rampage)
-  [Xpensa - Personal Finance manager](https://github.com/philix27/Xpensa)



## Deployed Contract Addresses on Celo

### Mainnet
- Contracts should be verified
- 0x5bFD6ea1Bae8f8b99Ee5ADbE9844108F1Fff359e
- 0x72D8025739315424725aCA52d83E7A59fB2d4A3e
- 0xf8FE71E2D44b8c18757d16e3C272d9591CE48d79
- 0xaDC89ab1516f104CfE2200fE1daA40C33DCf97b9 - BetaLyf
- 0x6e73346d7a77915FdaE2D556F112993f51E1fCa4
- 0xCffe2E2053b73F46023ac69f274F93A72854C3c0
- 0x13bf40c7561350790032A535905Da36E893Ef0E2
- 0x3C235a7AED6Fc77e799f9aeb9bFD652FE2465928
- 0xb80094df09f1949F43279e1aFab67449fC75712F

### Testnet
- 0x9f507BF2163b9EcaB85530AD0CD7c947456c17e3
- 0x34fE8A68b50EaaD07e67FB37919D2F8de78Cc4f0
- 0x47245FdA51fDFbaBbe807351eb6bBB3816567d77
- 0x8d1aE51Acef6c671b659f5aC3916e9b211560CD0
- 0x47245FdA51fDFbaBbe807351eb6bBB3816567d77
- 0x1098E00cba3b65bacc1a80c565e6beaA6D5504EC
- 0x7235C0aDC7111247dD8d5F10C01b23B71947f6d1
- 0x25aCe6dc2B4e4b76d906341ce511A53590B35492
- 0xceCA706fEC4a17085D79580Ae4F9078d5Cc214a3
- 0x613D66e96eaf4D6028410Cd50615C6a37a57aCCB
- 0x911F492164817fE994Fba17F356a5A8C737ab85E



