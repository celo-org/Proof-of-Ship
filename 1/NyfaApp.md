# Nyfa App

## Overview
A Next.js-based Web3 application that automatically mints PNG crypto asset reports called `NoFAs` as NFTs on the Celo network. The reports include market cap, news headlines, sentiment, and other information.

## Solution & Vision
Nyfa captures a moment in a cryptocurrency's lifetime, similar to what [carbon](https://carbon.now.sh/) does for code snippets. Users can generate and download shareable PNGs containing crypto asset reports, which can then be minted as NFTs.

## Contract Deployment
NoFA NFT Contract Address (Celo Alfajores): `0x7f5b1F68079b885512f6338C17466d53BC5A213C`

## Core Features

### 1. Cryptocurrency Data Integration
- Access to over 17,000 cryptocurrencies
- Integration with CoinGecko and CryptonewsAPI
- Real-time market data and news sentiment analysis

### 2. Report Generation
- Creation of `NoFA` (Not Financial Advice) reports
- PNG generation using HTML2Canvas
- Customizable report layouts

### 3. IPFS Integration
- Seamless upload to Pinata
- IPFS-based storage with permanent links
- Decentralized file management

### 4. NFT Implementation
- ERC721URIStorage-based smart contract
- Metadata linking with IPFS content
- Automated minting process

### 5. User Interface
- Intuitive crypto selection
- Background API processing
- Pinata integration for storage
- RainbowKit wallet connectivity

## Technical Architecture

### Frontend Flow
1. User Authentication
   ```
   Creator creates an account
   ↓
   They are authenticated using Supabase Anon Auth
   ↓
   They can create a NoFA which is saved to Supabase Postgres Database
   ```

2. NoFA Creation Process
   ```
   Creator selects a coin
   ↓
   The coin id is used to call CoinGecko API for data
   ↓
   The coin id is also used to call CryptoNewsAPI for news headlines and sentiment
   ↓
   The NoFA is created using the fetched data
   ↓
   A user can see that information
   ```

### Smart Contract Flow
```
Creator saves the PNG to Pinata
↓
Pinata returns an IPFS link 
↓
Creator creates NFT, which uses the IPFS link as metadata to the PNG
```

## Data Models

### Creator
```typescript
interface Creator {
    id: string;
    authId: string;
    userWalletAddress: string;
    privyWalletAddress: string;
    privyWalletId: string;
    timeCreated: string;
}
```

### NoFA
```typescript
interface NoFA {
    id: string | null;
    coinId: string
    creatorAuthId: string | null | undefined; 
    txnHash: string | null | undefined;
    ipfsURI: string | null | undefined;
    coinImageURI: string | null | undefined;
    marketCap: number | null | undefined;
    totalSupply: number | null | undefined;
    circulatingSupply: number | null | undefined;
    headlines: Headline[] | null | undefined;
    timeCreated: string | null | undefined;
}
```

### News Components
```typescript
interface NewsItem {
    title: string;
    image_url: string;
    news_url: string;
    sentiment: "Positive" | "Negative" | "Neutral";
}

interface Headline {
    title: string | null | undefined;
    imageURL: string | null | undefined;
    link: string | null | undefined;
    sentiment: "Positive" | "Negative" | "Neutral" | null;
}
```

## Roadmap

### Month 1: Wallet Integration & Testing
- Migration from Coinbase's `OnchainKit` to `RainbowKit`
- MiniPay optimization
- Celo Alfajores testnet deployment

### Month 2: Monetization
- Implementation of NFT minting fees
- NoFA generation payment system
- Revenue model optimization

### Month 3: AI Integration (Nyla)
- Development of Nyfa SDK with AI capabilities
- Public SDK release
- AI-powered feature expansion