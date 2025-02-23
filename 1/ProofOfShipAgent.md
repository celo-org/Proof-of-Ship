# Proof of Ship Agent

## Link to your project's GitHub repository

- [https://github.com/juliangay/celo-proof-of-ship](https://github.com/juliangay/celo-proof-of-ship)

## Team Members GitHub username	

- [juliangay](https://github.com/juliangay)

## Former Participation in Celo Hackathons	

- None

## Monthly Goal for this Proof of Ship	

This is the first month of the buildathon, so the focus is on setting up the foundation for the project, ensuring a smooth development process, and delivering an initial working prototype. Below is a breakdown of the high-level tasks accomplished each week:

### Week 1: Project Setup & Ideation ###

- Finalize the project's scope, goals, and key functionalities.
- Set up the GitHub repository and project management tools (issues, milestones, Kanban board).
- Define the smart contract architecture and key technical components.
- Research and select the best tools and frameworks (e.g., Celo SDK, smart contract language).
- Establish development workflows (CI/CD pipeline, testing strategy).

### Week 2: Smart Contract Development & Backend Integration ###

- Implement the initial version of the Proof of Ship scripts and smart contract.
- Deploy the contract on a Celo testnet for early testing.
- Begin backend development (APIs, account management, authentication).

### Week 3: Frontend Development & User Flows ###

- Develop the initial frontend UI using Streamlit.
- Implement progress dashboard for project submissions.
- Conduct internal testing of the end-to-end flow.
- Gather feedback from early testers and iterate based on findings.

### Week 4: Final Testing, Refinements & Documentation ###

- Conduct extensive testing (unit, integration, and user acceptance testing).
- Fix critical bugs and optimize contract gas usage.
- Improve UI/UX based on user feedback.
- Write clear documentation for project setup, deployment, and usage.
- Prepare a demo video and project submission materials for the buildathon.

### Detailed description of the work you did this month during the contest	

Initial scripts associated with the MVP that enables validation of Proof of Ship submissions:

- Reporting of public github repo submissions, 
- Tracking smart contract deployments on mainnet and alfajores 
- Reporting Farcaster cast activity associated with Proof of Ship 
- Minting of Proof of Ship Soulbound NFT to recognize contributors 
- Distribution of Proof of Ship rewards to eligible addresses via SAFE wallet	

## Problem	

- Each month the Celo builder community is contributing to the Proof of Ship buildathon. This is a great way to recognize the contributions of the community and to incentivize participation. However, there is no way to track the progress of the buildathon or the contributions of the community. 	

## Solution	

- Create a dashboard to track the progress of the buildathon and the contributions of the community.
- Make it easy for contributors to submit their Proof of Ship submissions and for judges to review them.
- Recognize ongoing contributions to the Proof of Ship buildathon via the minting of a Soulbound NFT to contributors.
- Streamline project submissions and publications via an AI agent that helps contributors publish their Proof of Ship submissions to Farcaster and Twitter.

## Architecture	

- Dashboard: Streamlit application that allows contributors to submit their Proof of Ship submissions and for judges to review them.
- Agent: Python application that uses the Celo SDK to interact with the Celo blockchain.
- Agent: Replit agent that allows judges to review Proof of Ship submissions and to distribute rewards.
- Agent: Replit agent that helps contributors submit their Proof of Ship submissions.
- Agent: Replit agent that publishes Proof of Ship submissions to Farcaster and Twitter.

## Deployed Contract Addresses on Celo	

Soulbound TokenContract Address on Celo Alfajores Testnet:	

- [0x3ac1eb269df27294e8e3e68f0c699480f4f6b8ba](https://alfajores.celoscan.io/address/0x3ac1eb269df27294e8e3e68f0c699480f4f6b8ba)