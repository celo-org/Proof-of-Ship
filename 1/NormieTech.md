
# Normie Tech

## GitHub repository 

**[Normie.Tech Github](https://github.com/normiedottech/normie.tech)**

## Team Members GitHub username
**[dipanshuhappy](https://github.com/dipanshuhappy)**

**[Nithin-Varma](https://github.com/Nithin-Varma)**

**[arrytiwari](https://github.com/arrytiwari)**

## Former Participation in Celo Hackathons

- Links should go here if any

## Monthly Goal for this Proof of Ship

- Build Webhooks.
- Onboard X Customers

### Detailed description of the work you did this month during the contest

- Link to PR for feature 1
- Link to PR for feature 2

## Problem
Web3 businesses lose 85% of potential customers who want to pay with cards but can’t navigate crypto wallets, KYC hurdles, or volatile settlements.

**For Users**: Painful on-ramps, KYC delays, waiting for crypto deposits, and multi-step transfers.

**For Web3 Businesses**: Difficulty accepting payments from web2 users due to crypto complexities.

## Solution
[Normie.tech](https://normie.tech/) accept card payments from your customers and auto-convert them to instant stablecoin settlements for you, no crypto complexity for your customers.

### Why It Matters:
**For Web3 Businesses**: Tap into 4B+ card users, slash payment friction, and grow revenue 20-30% faster.

**For Web2Users**: Pay with cards they already trust. 

**No Wallets + No KYC = No Worries**

🚀 Turn payment barriers into growth engines.

## Flow Chart

```mermaid
flowchart LR
    A[User Signup & Onboarding] --> B[Dashboard]
    B --> C[Create Payment Link]
    C --> D{Select Settlement Option}
    D -- Instant Settlement --> E[Generate Payment Link Instant]
    D -- Withdraw Later --> F[Generate Payment Link Withdraw Later]
    E & F --> G[Share Payment Link with Customer]
    G --> H[Customer Clicks Payment Link]
    H --> I[Redirect to PayPal Checkout]
    I --> J[Customer Pays via PayPal / Card]
    J --> K{Payment Successful?}
    K -- No --> L[Payment Failed]
    K -- Yes --> M{Settlement Type?}
    M -- Instant Settlement --> N[Process Fees & Transfer Funds to Payout Address]
    M -- Withdraw Later --> O[Hold Funds Until Manual Withdrawal]
```

## Architecture Diagram
```mermaid
flowchart TD
    %% Entities
    WB[Web3 Business]
    NT[Normie.tech Platform]
    PP[Payment Processor PayPal]
    C[Customer]
    NL[Normie Liquidity/Reserves]

    %% Flow: Onboarding & URL sharing
    WB -- "Onboarded; receives Checkout URL" --> NT
    WB -- "Shares Checkout URL" --> C

    %% Flow: Payment process
    C -- "Clicks URL & Pays (Card/PayPal)" --> PP
    PP -- "Processes payment & sends confirmation" --> NT

    %% Flow: Settlement
    NT -- "Calculate fees & trigger settlement event" --> NL
    NL -- "Disburse net funds" --> WB

```

## Sequence Diagram
```mermaid
sequenceDiagram
    participant WB as Web3 Business
    participant NT as normie.tech
    participant C as Customer
    participant PP as Payment Processor (PayPal)
    
    %% Onboarding & URL Generation
    WB->>NT: Request Onboarding
    NT-->>WB: Acknowledge Confirmation
    WB->>NT: Request Checkout URL
    NT-->>WB: Provide Checkout URL
    
    %% URL Sharing & Payment Initiation
    WB->>C: Share Checkout URL
    C->>PP: Click URL & Redirect to PayPal
    PP->>C: Display Payment Form
    C->>PP: Submit Payment Details
    
    %% Payment Processing & Notification
    PP->>PP: Process Payment
    PP-->>NT: Send Payment Confirmation
    
    %% Settlement Process
    NT->>NT: Calculate Fees & Determine Net Amount
    NT->>WB: Transfer Net Funds from Liquidity/Reserves
```
## Deployed Contract Addresses on Celo

We dont have any contract addresses which deployed on chain......
???????????????????
- Contract Address on Celo or Celo Alfajores Testnet.
- NOTE: Our AI Agent Judge tracks transactions on deployed contracts. Contracts are required in order to receive monthly rewards.  