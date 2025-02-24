# Project Name
### Simplifinance
A platform of decentralized pools for short-term lending and borrowing services. At Simplifi, we provide a groundbreaking approach to peer-to-peer group lending and borrowing that combines inclusivity, transparency, and control. While other lending platforms rely on centralized liquidity pools with predetermined and algorithm-driven interest rates, Simplifi flips the script.

## Link to your project's GitHub repository 	

__[](https://github.com/bobeu/simplifinance_bot_miniapp)__

## Team Members GitHub username	
- __[Github](https://github.com/bobeu)__

## Former Participation in Celo Hackathons
- None

## Monthly Goal for this Proof of Ship	
Following the research we conducted, we want to create excellent user experience via intuitive easy-to-use interface, protocols, and techologies, our goal is to convert Simplifinance to a user-friendly Celo-AI-Safe-powered deFi app to reduce deployment and interaction costs, improve and smooth UI/UX, and better code optimization leveraging bot and miniApp, AI models/agents, Safe protocol, and the Celo blockchain. We have set out the following milestones to help us achieve the set goal. 

Tasks | 1 | 2 | 3 | 4 | Status
----- | - | - | - | - | ------
**Wk 1** | Team brainstoring session | Idea workout and finalization | Planning, technology research, and feature design | | :heavy_check_mark:
**Wk 2** | Project setup & Restructing | Buidl and implementation | Feature serialization and Smart wallet integration | First iteration | :heavy_check_mark:
**Wk 3** | AI integration | Second iteration | Code optimization| | :orange_circle:
**Wk 4** | Feedbacks and improvement | Rounding Up | Final iteration | Submission | 

**LD**
:heavy_check_mark: | **Completed**
------------------ | -------------
:orange_circle: | **Ongoing**
:red_circle: | **Canceled**


## Detailed description of the work you did during the contest
- __[PR-1](https://github.com/celo-org/Proof-of-Ship/pull/19)__
- __[PR-2](https://github.com/celo-org/Proof-of-Ship/pull/25)__
- __[PR-3](https://github.com/celo-org/Proof-of-Ship/pull/27)__
- __[PR-4](https://github.com/celo-org/Proof-of-Ship/pull/29)__
- __[PR-4](https://github.com/celo-org/Proof-of-Ship/pull/44)__

## Problem
- High interest rate monopoly.
- Centralized and rigid liquidity pattern.
- Low transparency and financial exclusion (especially for the lower class of users).

## Solution
- Near-zero interest loans via peer-funding mechanism.
- User-driven liquidity pool through our FlexPool design.
- Enhanced flexibility and inclusion for all class of users.
- Trust and transparency.
- Expandable liquidity.

By blending traditional group lending practices with blockchain tecehnology, Simplifi creates a financial solution that's transparent, inclusive, and uniquely user-focused.

## Architecture

This project is in two phases
    - a web-app - Action-based
    - mini-app - Agentic. 
    
We started to build the second phase in this this contest. From the webApp, users can use action-based such as clicking a button or sending an event-based action to get result from the protocol while the AI-Assist part is plainly conversational. With a text prompt, users will able to get similar results as the action-based.

We used the following technologies to integrate an agent into the app.

- Safe protocol : Our agent leverage the Safe wallet via the SDK to manage pooled funds instead of an internally generated smart contracts. Although, there are a few trade-offs but we chose to use this method since we're able to significantly reduce deployment cost. On the part of the users, the cost of interacting with the smart contracts reduced by around 50%. This is an achievement we're excited about. The only challenge we had was determining the owners of the safe wallet due to the flow of activities.

- LLM : We chose OpenAi over others due to it's simplicity and robust sdk infrastructures. We use OpenAi to analyse users' intent when they visit the app by simply typing some characters. The agent decide which function to run and when to do so.

- Our smart contracts are currently deployed on the Celo Alfajores since we're actively making a lot of changes. Celo blockchain serves as our core database, even though we had tested with other network, we chose Celo in order to benefit from the cheap transaction cost, scalabiity and EVM security features.

## Deployed Contract Addresses on Celo

- Factory - __0x99D39170E2807D26E71C721bbb414f4a913eA2c4__ (Unverified)
- Stablecoin (test) - __0xF0046e26E286f966F77fFC6F408eD00949092Ccd__ (Unverified)

`NB`: We are yet to very these contracts as they are undergoing frequest changes.

## Commits

- __[1](https://github.com/bobeu/simplifi_proof_of_ship/commit/f1e04091efce2358fdbb6771bfa2510e7b50043a)__

- __[2](https://github.com/bobeu/simplifi_proof_of_ship/commit/e2eead19451c0c15379975bf27379406b97745cb)__

__[3](https://github.com/bobeu/simplifi_proof_of_ship/commit/990ee8131843ed5bdbeca54e86207c33d0070925)__


## Video
__[Youtube]()__

## Slide
__[Google](https://docs.google.com/presentation/d/1r4jqqVc-oMhMBpJAXiN9u0VSnVNS2uC3M0hgdH1c-Bg/edit?usp=sharing https://docs.google.com/presentation/d/1r4jqqVc-oMhMBpJAXiN9u0VSnVNS2uC3M0hgdH1c-Bg/edit?usp=sharing )__

## Team
- Isaac J
    - __[Github](https://github.com/bobeu)__
    - __[Email](mailto:bobmatea27@gmail.com)__
    - __[LinkedIn](https://www.linkedin.com/in/isaac-j-a6764a169)__
    - __[Project - Proof of ship](https://github.com/bobeu/simplifinance_bot_miniapp)__