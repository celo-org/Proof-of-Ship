# Project Name - Superflow

## Short Description
One-Click Token Creation and Liquidity Management

## Link to GitHub repository

[Link](https://github.com/distroinfinity/superflow)

## Link to Video



## Link to Deck


## Link to assets



## Team Members GitHub username
[yeah-ssh](https://github.com/yeah-ssh)
[distroinfinty](https://github.com/distroinfinity)

## Former Participation in Celo Hackathons

 Celo Proof-Of-Ship Seaason1.  
 Eth Bangkok Celo Best Open Source Project.

## Monthly Goal for this Proof of Ship
I will be actively participating in Proof-of-Ship Season 2 this month, focusing on:

- Extensive testing of our product on Celo Alfajores to ensure stability and performance.   
- Leveraging access to Alfajores Uniswap V3 contracts for seamless integration and improved functionality.   
- Implementing key enhancements from ScoutsGame to streamline contributions and maintain a smooth workflow.    
- Restructuring the folder architecture to improve organization and remove unnecessary clutter.   
- Developing a lightweight frontend to enhance the usability of our currently terminal-based tool.   


### Detailed description of the work you did this month during the contest
 

## Problem

- Launching tokens and managing liquidity across multiple chains is highly complex, time-intensive, and risky. Projects struggle with security vulnerabilities, fragmented tooling, and inefficient workflows that slow adoption.


## Solution

- SuperFlow removes these barriers by providing an all-in-one, automated solution for:

- Token Generation – One-click ERC20 deployment with secure, audited contracts.  
- Cross-Chain Liquidity – Instant bridging of Celo tokens to major EVM chains.  
- DEX Liquidity Management – Automated pool creation for seamless trading.  


## Architecture

Token Deployment (newToken.js)
- Deploys new ERC-20 tokens using Hardhat & Ethers.js.
Liquidity Pool Setup (createUniswapPools.js)
- Pairs the deployed token with a collateral token.
Creates Uniswap V3 pools using FactoryV3 & Non-Fungible Position Manager.
- Frontend will be built using Reactjs or Nextjs.

## Contracts on Celo Alfajores

- UniswapV3Factory: 0x229Fd76DA9062C1a10eb4193768E192bdEA99572
- NonfungiblePositionManager: 0x0eC9d3C06Bc0A472A80085244d897bb604548824
