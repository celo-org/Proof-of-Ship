# Canvassing - Participant: Online Surveys, Paid in Tokens

## Short Description

online surveys that reward participants for answering questions, built on Celo

## Link to GitHub repository
https://github.com/andrewkimjoseph/canvassing-participant.git

## Link to Video
- to be updated upon completion of video demo creation

## Link to Deck
- to be updated upon completion pitch deck creation

## Link to assets
https://github.com/andrewkimjoseph/canvassing-participant/tree/main/assets

## Team Members GitHub username

- Andrew Kim Joseph
  - [GitHub](https://github.com/andrewkimjoseph)
  - [Twitter](https://x.com/andrewkimjoseph)
  - [Farcaster](https://warpcast.com/andrewkimjoseph)

- Benedictors Ogada
  - [Twitter](https://x.com/Ben_Diktos)


## Former Participation in Celo Hackathons

- [Build with Celo 5 project - First Place](https://github.com/andrewkimjoseph/pamoja-app-awg) 
- [Build with Celo 6 project - First Place](https://github.com/andrewkimjoseph/stekcit-bwc) 
- [Build with Celo 7 project - First Place](https://github.com/andrewkimjoseph/canvassing) 
- [Proof of Ship Season 1 - Sixth Place](https://github.com/nyfaapp/celo-nyfa-app)


## Monthly Goal for this Proof of Ship

https://gap.karmahq.xyz/project/canvassing/grants/0x5b0f752718f3595bd2c9d32fc1837fab9890aa243c690a72606a610758609244/milestones-and-updates

## Problem

1. Traditional survey platforms require you to meet a minimum withdrawal threshold (e.g., 5 USD) before you can access your earnings.
2. Most platforms require linking a payment method that demands Know Your Customer (KYC) verification, such as PayPal.
3. Traditional platforms only process payouts during business days/hours, causing delays in receiving your earnings.


## Solution

1. By using stablecoins with more decimal places, we can transfer amounts as small as 0.01 cUSD directly to your account, enabling microtransactions.
2. We use MiniPay, a no-KYC dollar stablecoin wallet that only requires a Google account and phone number to sign up, eliminating invasive verification processes.
3. Our smart contract can process payments anytime through its [processRewardClaimByParticipant] method, allowing instant payouts regardless of time or day (as long as the blockchain is active and the participant has sufficient gas fees).


## Architecture

### Overview
Canvassing is built using Next.js for the frontend and Firebase for backend services. The application combines Web2 and Web3 technologies to create a seamless survey participation and reward system.

### Tech Stack
- **Frontend**: Next.js 13 (App Router)
- **Backend**: Firebase (Authentication, Firestore)
- **Forms**: Tally Forms
- **Blockchain**: Solidity Smart Contracts
- **Web3 Integration**: viem.js

### Flow Diagram

```mermaid
sequenceDiagram
    title dApp Survey Reward System Flow
    
    actor User
    participant Frontend as Frontend UI
    participant Firebase as Firebase Auth/DB
    participant TallyForms as Survey Platform
    participant SmartContract as Blockchain Contract
    participant Webhook as Backend Service
    
    %% User Authentication and Initial Setup
    User->>Frontend: Opens dApp
    Frontend->>Firebase: Request Anonymous Authentication
    Firebase-->>Frontend: Return Auth Token
    Frontend->>Firebase: Create/Update User Account
    Firebase-->>Frontend: Confirm Account Status
    
    %% Display Available Surveys
    Frontend->>Firebase: Fetch Available Surveys
    Firebase-->>Frontend: Return Survey List
    Frontend->>Frontend: Display Survey List
    
    %% Survey Booking Process
    User->>Frontend: Select Survey to Complete
    Frontend->>SmartContract: Book Survey (On-chain Transaction)
    Note right of SmartContract: Locks survey slot for user
    SmartContract-->>Frontend: Emit BookingConfirmed Event
    Frontend->>Frontend: Update UI with Booking Status
    
    %% Survey Completion Flow
    Frontend->>TallyForms: Redirect to Survey with User Parameters
    User->>TallyForms: Complete Survey Questions
    User->>TallyForms: Submit Survey Response
    TallyForms->>Webhook: Trigger Completion Webhook
    
    %% Reward Generation Process
    Webhook->>Firebase: Verify Survey Completion
    Webhook->>Firebase: Store Survey Response Data
    Webhook->>Firebase: Generate Off-chain Signature
    Note right of Webhook: Signature proves valid completion
    Webhook-->>Frontend: Notify Completion Status
    
    %% Reward Claiming Process
    Frontend->>Frontend: Display Claimable Reward
    User->>Frontend: Initiate Reward Claim
    Frontend->>SmartContract: Submit Claim with Signature
    SmartContract->>SmartContract: Verify Signature Validity
    SmartContract->>SmartContract: processRewardClaimByParticipant
    SmartContract-->>User: Transfer Reward Tokens
    
    %% Final Confirmation
    SmartContract-->>Frontend: Emit RewardClaimed Event
    Frontend->>Frontend: Update UI with Reward Status
```

## Contracts on Celo

- to be deployed upon completion of Milestone 4
