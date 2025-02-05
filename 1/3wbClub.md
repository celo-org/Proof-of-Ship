# Project Name
3 Wheeler Bike Club

## Former Participation in Celo Hackathons
N/A

## Link to your repository. It needs to be **Open Source**.
https://github.com/3-Wheeler-Bike-Club

## Goal for this Proof of Ship
We are getting ready to pilot our community driven platform for 3 wheelers bikers. Last month we demoed the membership payment & credit score feature of platform to a group of 3 wheelers bikers & at the first celo builder showcase event(https://www.youtube.com/live/M3x0cBvVz8E?si=QQ9SfaMki_Gdj42t) and we got a lot of positive feedback. This month as we get closer to the pilot, we are looking to finalize the MVP, our main focus is rolling out the 3 wheeler bike P2P finance feature where anyone can buy or add a 3wheeler bike to the platform and start a hire purchase agreement with credit worthy member. Below is a more itemized list of the feature flow we are looking to achieve in the next 2-3 weeks.
#### Week 1:
- Purchase or pre-order a 3 wheeler bike from the platform w/ offchain + onchain payment options
- Registration of 3 wheeler w/ local government authority eg. DVLA in Ghana(offline) + Onboard the 3 wheeler bike on the platform w/ pink slip attestation
#### Week 2:
- Application submission to ride a 3 wheeler bike w/ KYC(offchain)
- Assign a credit worthy member after in-person interview by union chairman & gurantor assurance(offchain)
#### Week 3:
- Initiate a hire purchase agreement between the financer & driver w/ hire purchase agreement attestation + attest all IOU invoices w/due weekly dates
- Payment of hire purchase receipts w/ attestation of receipt and credit scores


### Detailed description of the work you did during the contest
- TBD
- TBD

## Problem
We see the opportunity to create a community where drivers contribute to a shared foundation, helping each other grow and succeed, improving the quality of work & life. This is a community that is driven by the members, for the members to root out & solve the challenges of their local communities.

## Solution
A membership platform designed to create a community of Keke/Pragia/TukTuk drivers that:
- Contribute weekly membership dues to a pool.
- Build reputation based on weekly contributions.
- Vote & Propose membership pool budgets.
- Own motorcycle after 93 weeks of micro-payments.

## Architecture
- ethSign Protocol: attestations
- privy: authentication & wallet management
- Pooltogether: membership contribution pool where the yield goes to prizes for members based on credit scores/contributions
- viem/wagmi: type-safe smart contract interactions
- Celo: blockchain infrastructure
- Paystack: payment processing for membership dues
- NextJS: frontend & backendfor the platform
- TailwindCSS: styling
- shadcn/ui: components
- framer-motion: animations
- Mongoose: database for offchain attestations

## Deployed Contract Addresses on Celo
For now we do not have any deployed contracts on celo. What we do have instead are Schemas and Attestations depolyed w/ ethSign Protocol on celo. Here is a list of the deployed schemas and attestations:
#### KYC
- ID Badge Schema - https://scan.sign.global/schema/onchain_evm_42220_0x8 
#### MEMBERSHIP
- Membership Invoice Schema ( linked to ID Badge ) - https://scan.sign.global/schema/onchain_evm_42220_0x9
- Membership Receipt Schema( linked to Invoice ) -https://scan.sign.global/schema/onchain_evm_42220_0xa
- Membership Credit Score Badge Schema( linked to ID Badge ) - https://scan.sign.global/schema/onchain_evm_42220_0x12
#### OWNERSHIP
- Pink Slip Schema - https://scan.sign.global/schema/onchain_evm_42220_0x18
- Hire Purchase Schema ( linked to ID Badge ) - https://scan.sign.global/schema/onchain_evm_42220_0xd
- Hire Purchase Invoice Schema ( linked to Hire Purchase ) - https://scan.sign.global/schema/onchain_evm_42220_0xe
- Hire Purchase Receipt Schema( linked to Hire Purchase Invoice ) - https://scan.sign.global/schema/onchain_evm_42220_0xf 
- Ownership Credit Score Badge Schema( linked to ID Badge ) - https://scan.sign.global/schema/onchain_evm_42220_0x10

## Team
- https://github.com/tickether
- https://github.com/ciphertextk
- https://github.com/Anitapounds