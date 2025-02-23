# Akashic

## Former Participation in Celo Hackathons

We are a new project on Celo.

## Goal for this Proof of Ship

Launch a fully functional POC allowing projects to sign up and create campaigns on Akashic.


## Detailed description of the work you did during the contest

### Campaign & Donation Management

#### Campaign Enhancements
- Added a dedicated campaign page and improvements for campaign updates and clicks.
- Integrated the campaign creation function with the frontend and introduced a listing feature to display campaigns.

#### Donation Flow
- Introduced a donation flow that ties in campaign data, streamlining how users contribute.
- Updated payment handling by switching from ETH to USDC, and added treasury address management to support financial operations.

#### Rounds & Mapping

##### Rounds Functionality
- Implemented updates to the rounds process, including a new post-approval step and refined mapping between rounds and campaigns.

##### User Experience & Visual Improvements

#### Search & Navigation
- Added a search function to help users easily find campaigns or related data.

#### Visual Enhancements
- Rolled out visual fixes and design updates, including network toast notifications that provide real-time feedback.
- Introduced a comment feature to foster interaction and engagement.

#### Administrative & Dashboard Features

##### Admin Tools
- Patched the admin routes and introduced an admin page to simplify backend management.
- Fixed issues with the admin approval function for smoother operation.

##### User Dashboard
- Addressed and resolved issues in the user dashboard to enhance overall usability.

#### Backend & Database Improvements

##### Query & Database Enhancements
- Optimized queries for better performance.
- Enhanced database integration by adding support for Prisma, saving campaign details, pulling images from the database, and generally improving data handling.

#### Miscellaneous Fixes

#### Code & Build Quality
- Removed unused code, fixed build errors, and resolved various breakages to maintain a clean and stable codebase.


## Problem

Akashic addresses the challenge of preserving the cultural heritage and multimedia expressions of refugees and displaced communities. These communities often lose access to their cultural artifacts, oral histories, music, and artistic expressions due to forced migration, conflict, and displacement. Traditional archives may fail to capture the nuanced, multimedia nature of this cultural heritage, or they may be inaccessible to displaced individuals. Furthermore, the lack of financial support and recognition for creators from these communities exacerbates the problem.

**Problem We Are Solving**

Akashic aims to:

•	**Preserve Culture and Identity:** By creating a decentralized archive using IPFS technology, ensuring the survival and accessibility of cultural heritage across borders and through time, which strengthens their sense of identity and cultural pride. 

•	**Empower creators via Income Generation, Financial Independence & Inclusion, and Communication:** Ability to generate a dignified income by monetizing and fundraising their work from a global audience, access to basic financial services via web3 wallets, including the facilitation of payment & remittances, micro-loans, digital identity, etc. Provide a platform for creators to upload, share, retain ownership and control, and monetize their work, directly connecting them to supporters, donors, talent agents, and curators. Provide skills training and workforce development opportunities that enable creators to generate income.

•	**Foster Collaboration, Community-Building, and Cross-Cultural Exchange:** Allow buyers and donors to view and directly support creators’ work while preserving cultural artifacts in a decentralized, tamper-proof manner using Web3 technologies. Enable the discovery of emerging creator talent by media & arts organizations, foundations, galleries (i.e. curators, agents). By engaging a community of global supporters, a network of creators transcend borders, allowing for collaboration, mentorship, and shared projects with other creators, curators, and agents, building a supportive, inclusive and diverse creative community that encourages cross-cultural understanding and building empathy.


## Solution
We help refugees and displaced communities build financial independence and preserve their cultural heritage by providing direct access to global supporters, secure financial services, and tools for community-driven initiatives.

### Key Features:
- Banking the unbanked
- Last mile distribution
- Community Driven Initiatives
- Creator Economy
- Decentralized Archive
- Web3 Wallets



## Architecture
``` mermaid
sequenceDiagram
    participant pa as Protocol Admin/Deployer
    participant cc as Campaign Creator
    participant pla as Platform Admin
    participant gp as GlobalParams Contract
    participant cif as CampaignInfoFactory Contract
    participant tf as TreasuryFactory Contract
    participant aontf as AllOrNothing Treasury Contract
    participant cb as Campaign Backer

    pa->>gp: Initialize GlobalParams
    pa->>cif: Initialize CampaignInfoFactory
    pa->>tf: Initialize TreasuryFactory

    cc->>cif: createCampaign(owner, slug, platform, goal, deadline)
    cif->>cc: Returns CampaignInfo contract (infoAddress)

    pla->>tf: deploy(platform, 0, infoAddress)
    tf->>pla: Returns Treasury Address (AllOrNothing)

    cc->>aontf: addReward(rewardName, reward)
    aontf->>cc: Reward added

    cb->>aontf: pledgeForAReward(backerAddress, rewardName)
    aontf->>cb: Pledge Confirmed

    aontf->>aontf: Check Goal Amount
    alt Goal Met (Successful Campaign)
        aontf->>cc: disburseFees()
        cc->>cc: Fees Disbursed
        cc->>cc: withdraw()
        cc->>cc: Funds Withdrawn
    else Goal Not Met (Unsuccessful Campaign)
        aontf->>cb: claimRefund()
        cb->>cb: Refund Processed
    end

```

## Deployed Contract Addresses on Celo



## Team

**James**- Product Manager
GitHub: https://github.com/positonic
Twitter: [positonic](https://x.com/positonic) 
Past experience: Founder and previous CTO at Toucan, prev Tech lead at Giveth

**Prajjawal**- SR Fullstack Engineer
GitHub: https://github.com/Prajjawalk
Twitter: [Prajjawalk](https://x.com/Prajjawalk) 
Past experience: Core protocol developer at QRL


**Shikhar**- SR Backend Engineer
GitHub: https://github.com/0xshikhar 
Twitter: [0xshikhar ](https://x.com/0xshikhar )
Past experience: 
