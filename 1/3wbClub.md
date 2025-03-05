# Project Name
3 Wheeler Bike Club

## Logo
![3-Wheeler](https://i.ibb.co/1R7dngG/3-Wheeler-Logo-Horizontal-4x.png)


## Description
Membership Club for 3 Wheeler(TukTuk/Pragia/Keke) Bikers built on the pillars of Ownership, Community & Governance. 🛺💨

## Former Participation in Celo Hackathons
N/A

## Link to your repository. It needs to be **Open Source**.
https://github.com/3-Wheeler-Bike-Club

## Goal for this Proof of Ship
We are getting ready to pilot our community-driven platform for 3-wheeler bikers. Last month we demoed the membership payment & credit score feature of platform to a group of 3 wheelers bikers & at the first celo builder showcase event(https://www.youtube.com/live/M3x0cBvVz8E?si=QQ9SfaMki_Gdj42t) and we got a lot of positive feedback. This month as we get closer to the pilot, we are looking to finalize the MVP, our main focus is rolling out the 3 wheeler bike P2P finance feature where anyone can buy or add a 3wheeler bike to the platform and start a hire purchase agreement with credit worthy member. Below is a more itemized list of the feature flow we are looking to achieve in the next 2-3 weeks.
#### Week 1:
- Purchase or pre-order a 3 wheeler bike from the platform w/ offchain + onchain payment options
- Registration of 3 wheeler w/ local government authority eg. DVLA in Ghana(offline) + Onboard the 3 wheeler bike on the platform w/ pink slip attestation
#### Week 2:
- Application submission to ride a 3 wheeler bike w/ KYC(offchain)
- Assign a credit worthy member after in-person interview by union chairman & guarantorassurance(offchain)
#### Week 3:
- Initiate a hire purchase agreement between the financier & driver w/ hire purchase agreement attestation + attest all IOU invoices w/due weekly dates
- Payment of hire purchase receipts w/ attestation of receipt and credit scores


### Detailed description of the work you did during the contest
#### Week 1
1. Purchase or pre-order a 3 wheeler bike from the platform w/ offchain + onchain payment options
   - visual foundation of the peer-to-peer 3 wheeler bike financing feature + basic repo setup(https://github.com/3-Wheeler-Bike-Club/3-wheeler-bike-club-fleet-app/commit/7634d4c1461f48f80b278b3665598ae771b59f28)
   - complete business logic + integrated paystack payment gate + order submission to 3wb Team to complete procurement, registration & driver assignment of 3-wheeler(https://github.com/3-Wheeler-Bike-Club/3-wheeler-bike-club-fleet-app/commit/8e69fc77b62b6412346ed94b992d8906e44702fb)

2. Registration of 3 wheeler w/ local government authority eg. DVLA in Ghana(offline) + Onboard the 3 wheeler bike on the platform w/ pink slip attestation
   - remodel admin dashboard flow to receive order submission & match w/ driver submission after pink slip registration(https://github.com/3-Wheeler-Bike-Club/3-wheeler-bike-club-team-app/commit/0071009622160949bde5ab400b1ae4fe228dcba4)
   - add procured 3-wheelers to the platform w/ basic information for DVLA registration(https://github.com/3-Wheeler-Bike-Club/3-wheeler-bike-club-team-app/commit/94811b2c02800e836f4ad9e0b2c816f2db53baed)
   - storing offline vehicle registration data onchain w/ ethSign attestation(https://github.com/3-Wheeler-Bike-Club/3-wheeler-bike-club-team-app/commit/98961562223ad26c71921fe34e4a7f8caf32d9ed)

#### Week 2
1. Application submission to ride a 3 wheeler bike w/ KYC(offchain) 
   - create membership badge attestation on init signup, submit interest to drive for in-person KYC(https://github.com/3-Wheeler-Bike-Club/3-wheeler-bike-club-members-app-pwa/commit/2902b23d8c27c66c41cda7ea80ce6d84dc20530a)
   - upload in-person KYC documents offchain + revoke then attest new membership badge to reflect KYC passed(https://github.com/3-Wheeler-Bike-Club/3-wheeler-bike-club-team-app/commit/74adacec8d125f18ffcc8bc4953f1eb167270136)

2. Assign a credit worthy member after in-person interview by union chairman & guarantorassurance(offchain)
   - display all verified drivers for final approval and assignment of 3-wheeler(https://github.com/3-Wheeler-Bike-Club/3-wheeler-bike-club-team-app/commit/285d8d91b6cf252df04203f77ee34f5dd607749f)

#### Week 3
1. Initiate a hire purchase agreement between the financier & driver w/ hire purchase agreement attestation + attest all IOU invoices w/due weekly dates
   - TBD
   - TBD

2. Payment of hire purchase receipts w/ attestation of receipt and credit scores
   - TBD
   - TBD
## Problem
We see the opportunity to create a community where drivers contribute to a shared foundation, helping each other grow and succeed, improving the quality of work & life. This is a community that is driven by the members, for the members to root out & solve the challenges of their local communities.

## Solution
A membership platform designed to create a community of Keke/Pragia/TukTuk drivers that:
- Contribute weekly membership dues to a pool.
- Build reputation based on weekly contributions.
- Vote & Propose membership pool budgets.
- Own a motorcycle after 93 weeks of micro-payments.

## Demo
https://youtu.be/N-w2wbuJPNA

## Deck
https://tinyurl.com/Deck3WB

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
For now we do not have any deployed contracts on celo. What we do have instead are Schemas and Attestations deployed w/ ethSign Protocol on celo. Here is a list of the deployed schemas and attestations:
#### KYC
- ID Badge Schema - https://scan.sign.global/schema/onchain_evm_42220_0x609 
#### MEMBERSHIP
- Membership Invoice Schema ( linked to ID Badge ) - https://scan.sign.global/schema/onchain_evm_42220_0x9
- Membership Receipt Schema( linked to Invoice ) -https://scan.sign.global/schema/onchain_evm_42220_0xa
- Membership Credit Score Badge Schema( linked to ID Badge ) - https://scan.sign.global/schema/onchain_evm_42220_0x12
#### OWNERSHIP
- Pink Slip Schema - https://scan.sign.global/schema/onchain_evm_42220_0x47c
- Hire Purchase Schema ( linked to ID Badge ) - https://scan.sign.global/schema/onchain_evm_42220_0x548
- Hire Purchase Invoice Schema ( linked to Hire Purchase ) - https://scan.sign.global/schema/onchain_evm_42220_0x547
- Hire Purchase Receipt Schema( linked to Hire Purchase Invoice ) - https://scan.sign.global/schema/onchain_evm_42220_0xf 
- Ownership Credit Score Badge Schema( linked to ID Badge ) - https://scan.sign.global/schema/onchain_evm_42220_0x10

## Team
- https://github.com/tickether
- https://github.com/ciphertextk
- https://github.com/Anitapounds