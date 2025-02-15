# Nyfa App

## Overview
A Next.js-based Web3 application that automatically mints PNG crypto asset reports called `NoFAs` as NFTs on the Celo network. The reports include market cap, news headlines, sentiment, and other information.

## Core Features

### 1. Crypto API Calls
- Select one of the over 17,000 cryptocurrencies
- Call CoinGecko and CryptonewsAPI APIs

### 2. HTML 2 Canvas 
- Grab the generate report, a `NoFA - Not Financial Advice`
- Generate a PNG with the said information

### 3. IPFS Upload
- Upload the generated PNG to Pinata
- Get back a link to the IPFS-stored file `ipfs://`

### 4. Smart Contract Components
1. ERC71URIStorage
   - Create NFTs based on the NoFAs
   - Link NFTs with metadata


### 5. Frontend Components

#### Crypto Report Generation
Create your NoFA
  * Select crypto
  * Make background API calls

#### Save to Pinata
- Button display with `Save your PNG, then create an NFT`
- API calls to Pinata to save the image and metadata

#### Wallet Integration
- Connect wallet from `RainbowKit`


## Technical Architecture

### Frontend Flow
1. User Journey
   ```
   Creator creates an account
   ↓
   They are authenticated using Supabase Anon Auth
   ↓
   They can create a NoFA which is saved to Supabase Postgres Database
   ```
2. NoFA Creation
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
NoFA NFT Creation
   ```
   Creator saves the PNG to Pinata
   ↓
   Pinata returns an IPFS link 
   ↓
   Creator creates NFT, which uses the IPFS link as metadata to the PNG
   ```

## Data Structures

### Creator Object
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


### NoFA Object
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

### NewsItem Object
```typescript
 interface NewsItem {
    title: string;
    image_url: string;
    news_url: string;
    sentiment:"Positive" | "Negative" | "Neutral";
}
```


### Headline Object
```typescript
interface Headline {
  title: string | null | undefined;
  imageURL: string | null | undefined;
  link: string | null | undefined;
  sentiment: "Positive" | "Negative" | "Neutral" | null;
}
```

## Long-Term Plan

### Month 1: RainbowKit Integration and Celo Alfajores Contract Deployment
- Move from Coinbase's `OnchainKit` to `RainbowKit`
- Optimize for MiniPay
- Deploy NFT contract to Celo Alfajores

### Month 2: Add Paywall
- Charge for each NFT creation, and each NoFA generation

### Month 3: Introduce Nyla - AI
- Create an SDK integrate with Nyfa that will serve as an AI agent
- Make SDK available for all to use
