 	
# SaloneLawsAI

## Short Description

Explore the laws of Sierra Leone with AI

## Link to GitHub repository

https://github.com/vtamara/SaloneLawsAI

## Link to Video

No yet

## Link to Deck

No yet

## Link to assets

No yet

## Team Members GitHub username

- vtamara
  - fullstack
  - GitHub: https://github.com/vtamara
  - Twitter: https://x.com/VladimirTamara
  - Farcaster: 

## Former Participation in Celo Hackathons

None

## Monthly Goal for this Proof of Ship

Start

### Detailed description of the work you did this month during the contest

No yet

## Problem

- General public from Sierra Leone need to know, understand easily and apply the laws of their country for example during conflicts
- Lawyers of Sierra Leone need help in finding laws and analyzing them for their cases

## Solution

- Repository of laws
- Training AI model with them to help people and lawyers to explore, analyze and use them


## Architecture

- Backends:
  - Repository of laws
  - AI Trainer: based on open source AI modules Fine Tuning with the repository of laws prepared, continuosly as laws are updated and new laws are added.
  - AI Server: Runs the fine tuned model to answer questions
  - Database of users: KYC information, authentication information including CELO wallet address, usage and payments (we wish to do it as free as possible)
- Frontend. Web application to:
  - Login with wallet and payments
  - Start or continue conversations with the AI server
  - Access to the repository of laws
  

## Contracts on Celo

- Maybe bridges to make payments as easy as possible
