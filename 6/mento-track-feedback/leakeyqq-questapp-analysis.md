# Analysis Report: leakeyqq/questapp

Generated: 2025-08-22 18:06:07

## Project Scores

| Criteria | Score (0-10) | Justification |
|-----------------------------|--------------|---------------|
| Mento SDK Integration Quality | 0.0/10 | No evidence of `@mento-protocol/mento-sdk` usage or its methods for quotes, swaps, or exchange discovery. |
| Broker Contract Usage | 0.0/10 | No direct interactions with Mento Broker contracts (e.g., `getAmountOut`, `swapIn`, `getExchangeProviders`) were found. The project uses standard ERC20 `transferFrom` after user approval. |
| Oracle Implementation | 1.0/10 | The project uses cUSD, which is a Mento-managed stablecoin (evidenced by `StableTokenABI` containing `getExchangeRegistryId`). However, the application code does not actively query Mento oracles (`SortedOracles`, `medianRate()`) for real-time rates or data validation. It implicitly relies on the stablecoin's peg. |
| Swap Functionality | 0.0/10 | No Mento Protocol-specific swap functionality (e.g., cUSD to CELO, cUSD to cEUR) is implemented within the application. Fiat-to-crypto on-ramping is handled by a third-party service (Pretium/Swypt), not Mento. |
| Code Quality & Architecture | 6.5/10 | Good overall architecture (Next.js, Express, Mongoose, Wagmi, Viem). Decent error handling with custom modals and retry logic for transactions. However, the codebase explicitly notes missing tests, contribution guidelines, and CI/CD. Documentation is sparse for critical logic. |
| **Overall Technical Score** | 4.0/10 | The project effectively leverages Celo's stablecoin infrastructure (Mento-managed assets like cUSD, USDT, USDC) and demonstrates solid general Web3 development practices, including multi-chain support (Solana) and Celo-specific gas handling. However, its direct integration with Mento Protocol's advanced features (SDK, Broker, Oracle for dynamic operations) is absent. The score reflects a well-built Web3 application that passively uses Mento assets, rather than actively integrating with the protocol's core functionalities. |

## Project Summary
- **Primary purpose/goal related to Mento Protocol**: The project, "Questpanda," aims to connect brands with content creators for promotional video quests, with rewards paid in stable assets. Its primary goal related to Mento Protocol is the *utilization of Mento-managed stablecoins* (primarily cUSD, but also USDT and USDC on Celo) for prize pools and creator rewards, leveraging their stability and presence within the Celo ecosystem.
- **Problem solved for stable asset users/developers**: For brands, it provides a simple way to fund marketing campaigns using readily available stable assets on Celo (and Solana). For creators, it offers a clear path to earn stable asset rewards. For developers, it demonstrates how to integrate stablecoin payments and manage associated gas fees within a Celo/Solana dApp, including a third-party fiat-to-crypto on-ramp solution.
- **Target users/beneficiaries within DeFi/stable asset space**: Brands looking for digital marketing, content creators seeking monetization opportunities, and developers building on Celo who need to integrate stablecoin payments and potentially cross-chain stable asset liquidity.

## Technology Stack
- **Main programming languages identified**: TypeScript (81.17%), JavaScript (13.17%), Solidity (4.91%), CSS (0.76%).
- **Mento-specific libraries and frameworks used**: None explicitly. The project relies on the underlying Celo blockchain's support for Mento stablecoins.
- **Smart contract standards and patterns used**: ERC20 (for stable tokens), Ownable, ReentrancyGuard (in custom QuestPanda contract).
- **Frontend/backend technologies supporting Mento integration**:
    -   **Frontend**: Next.js, React, Shadcn UI, Wagmi, Viem for Celo blockchain interaction. `@divvi/referral-sdk` for Celo-based referral tracking. Web3Auth for wallet management. Solana Web3.js for Solana interaction.
    -   **Backend**: Express.js, Mongoose (MongoDB ORM), Axios (for external API calls), `ethers.js`, `web3.js` (for Celo blockchain interaction), `@solana/web3.js`, `bs58` (for Solana interaction). Cloudinary for image management.

## Architecture and Structure
- **Overall project structure**: The project follows a typical full-stack architecture with a `client` (Next.js frontend) and a `server` (Express.js backend). Smart contracts are in a `smart-contract` directory.
- **Key components and their Mento interactions**:
    -   `client/contexts/useWeb3.tsx`: Centralizes Web3 interactions, including cUSD (Mento stablecoin) balance checks, approvals, and transfers. It also handles gas fee pre-filling on Celo, which is crucial for transactions involving cUSD.
    -   `client/app/brand/quests/create/page.tsx`: Orchestrates the creation of quests, including handling stable asset deposits (cUSD, USDT, USDC on Celo/Solana) and approvals.
    -   `client/components/payment-modal.tsx`: Provides a UI for selecting payment methods for quest prize pools, including cUSD, USDT, USDC on Celo/Solana, and a fiat-to-crypto (M-Pesa to USDT on Celo) on-ramp.
    -   `server/controllers/questController.js`: Handles the backend logic for quest creation, storing details like `onchain_id`, `rewardToken`, and `network`.
    -   `server/controllers/celoFeesController.js`: Manages gas fee sponsorship for Celo transactions, which directly supports operations involving cUSD.
    -   `server/controllers/swyptController.js`: Integrates with third-party APIs (Pretium/Swypt) for fiat-to-crypto on-ramping, depositing USDT to Celo.
- **Smart contract architecture (Mento-related contracts)**: The project uses a custom `QuestPanda` smart contract (defined by `questpanda-abi.json`). This contract is responsible for creating quests, holding prize pools, and rewarding creators. It interacts with ERC20 tokens (like cUSD) by calling their `approve` and `safeTransferFrom` methods. It does not directly implement Mento-specific logic but relies on the ERC20 standard supported by Mento stablecoins.
- **Mento integration approach (SDK vs direct contracts)**: The project does *not* use the Mento SDK or directly interact with Mento Broker or Oracle contracts. Its integration with Mento Protocol is indirect, through the use of Mento-managed stablecoins (cUSD, USDT, USDC) as standard ERC20 tokens on the Celo network.

## Security Analysis
- **Mento-specific security patterns**: Due to the lack of direct Mento SDK/contract integration, Mento-specific security patterns (e.g., slippage protection for Mento swaps, oracle data validation for Mento rates) are not directly applicable or implemented by the dApp.
- **Input validation for swap parameters**: Not applicable for Mento swaps as they are not implemented. For the fiat on-ramp, basic input validation for phone numbers is present.
- **Slippage protection mechanisms**: Not applicable for Mento swaps. For ERC20 transfers (e.g., `approveSpending`), the amount is fixed, so slippage is not a concern.
- **Oracle data validation**: No explicit oracle data validation is performed by the dApp, as it doesn't query Mento oracles. It relies on the inherent stability and peg maintenance of Mento stablecoins.
- **Transaction security for Mento operations**:
    -   **Token Approvals**: The `approveSpending` function in `useWeb3.tsx` uses `IERC20Metadata.safeTransferFrom` in the `QuestPanda` contract, which is a standard and secure pattern for ERC20 token transfers.
    -   **Gas Management**: The `prefillGas_v2` function in `useWeb3.tsx` and `customFundFeesOnWallet` in `celoFeesController.js` attempt to manage gas fees by pre-funding the user's wallet. This helps ensure transactions (including those with cUSD) don't fail due to insufficient gas, but it relies on a trusted backend service. Retry logic for nonce and underpriced transactions is a good practice.
    -   **Reentrancy Protection**: The `QuestPanda` smart contract inherits `ReentrancyGuard`, which is a critical security measure for contracts handling token transfers.

## Functionality & Correctness
- **Mento core functionalities implemented**: The project uses Mento-managed stablecoins (cUSD, USDT, USDC on Celo) as payment tokens. The `cUSD-abi.json` includes `getExchangeRegistryId`, confirming cUSD's Mento origin. However, no active Mento functionalities like dynamic swaps or oracle queries are implemented.
- **Swap execution correctness**: No Mento-specific swaps are executed. The fiat-to-crypto on-ramp relies on a third-party (Pretium/Swypt) for correctness.
- **Error handling for Mento operations**: Error handling is present for general Web3 transactions (e.g., wallet connection issues, transaction failures, insufficient balance) which would apply to cUSD transfers. Custom alert/confirm modals (`useAlert`, `useConfirm`) provide user feedback.
- **Edge case handling for rate fluctuations**: Not applicable as the dApp does not perform dynamic Mento swaps or directly interact with price oracles. It assumes the stablecoins maintain their peg. For the M-Pesa on-ramp, an exchange rate is fetched, but rate fluctuations are handled by the third-party provider.
- **Testing strategy for Mento features**: The codebase explicitly states "Missing tests" as a weakness. No dedicated testing strategy for any Mento-related features (or any features in general) is evident.

## Code Quality & Architecture
- **Code organization for Mento features**: Mento-related stablecoin interactions are encapsulated within `client/contexts/useWeb3.tsx` and related ABI files. This is a clear separation of concerns.
- **Documentation quality for Mento integration**: Code comments are sparse in critical Web3 interaction files (`useWeb3.tsx`). There is no dedicated documentation explaining the Mento integration strategy or assumptions.
- **Naming conventions for Mento-related components**: Names like `cUSDTokenAddress`, `QuestPandaABI` are clear.
- **Complexity management in swap logic**: The logic for handling multiple stable assets and networks (Celo and Solana) in `create/page.tsx` and `payment-modal.tsx` is reasonably well-managed, but the "swap" part (fiat-to-crypto) is offloaded to a third-party. The on-chain logic for `QuestPanda` is relatively simple (ERC20 transfers).

## Dependencies & Setup
- **Mento SDK and library management**: No Mento SDK is explicitly used, so no dependency management is needed for it.
- **Installation process for Mento dependencies**: Not applicable.
- **Configuration approach for Mento networks**: `cUSDTokenAddress` is hardcoded for Celo mainnet. RPC URLs for Celo and Solana are configured via environment variables (`NEXT_PUBLIC_CELO_RPC`, `NEXT_PUBLIC_SOLANA_MAINNET_RPC_URL`).
- **Deployment considerations for Mento integration**: The project is designed for deployment on Vercel (frontend) and a Node.js server (backend). It relies on environment variables for API keys, contract addresses, and RPC URLs, which is standard practice.

## Mento Protocol Integration Analysis

### 1. **Mento SDK Usage**
- **File Path**: Not applicable (no usage found).
- **Implementation Quality**: N/A (No implementation).
- **Code Snippet**: N/A.
- **Security Assessment**: N/A.

### 2. **Broker Contract Integration**
- **File Path**: Not applicable (no direct interaction found).
- **Implementation Quality**: N/A (No implementation).
- **Code Snippet**: N/A.
- **Security Assessment**: N/A.

### 3. **Oracle Integration (SortedOracles)**
- **File Path**: `client/contexts/cusd-abi.json`
- **Implementation Quality**: Basic (Passive reliance).
- **Code Snippet**: The `cusd-abi.json` contains the `getExchangeRegistryId` function, which is a Mento-specific method for Mento stablecoins to identify their associated Mento Exchange.
  ```json
  {
    "constant": true,
    "inputs": [],
    "name": "getExchangeRegistryId",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
  ```
  However, the application code does not actively call this function or any other oracle functions to fetch real-time rates or perform dynamic operations based on Mento's oracle data. It simply uses cUSD as a stable ERC20 token.
- **Security Assessment**: No direct oracle interaction means no direct oracle-related vulnerabilities (e.g., stale data, manipulation). However, the dApp implicitly trusts the cUSD peg, which is maintained by Mento's stability mechanism. Any issues with the Mento peg would directly impact the dApp's value proposition.

### 4. **Stable Asset & Token Integration**
- **File Path**:
    - `client/README.md` (mentions cUSD)
    - `client/package.json` (`@divvi/referral-sdk` implies Celo/cUSD ecosystem)
    - `client/contexts/CurrencyContext.tsx` (determines `cUSD` vs `USD`)
    - `client/contexts/cusd-abi.json` (cUSD ABI)
    - `client/contexts/questpanda-abi.json` (QuestPanda contract ABI, handles `address token`)
    - `client/contexts/useWeb3.tsx` (core logic for cUSD, USDT, USDC on Celo/Solana)
    - `client/app/brand/quests/create/page.tsx` (UI for depositing cUSD, USDT, USDC)
    - `client/components/payment-modal.tsx` (Payment UI for various stable assets)
    - `server/controllers/celoFeesController.js` (CELO gas funding for Celo transactions)
    - `server/controllers/solFeesController.js` (SOL gas funding for Solana transactions)
    - `server/controllers/swyptController.js` (Fiat-to-USDT on-ramp on Celo)
- **Implementation Quality**: Advanced (Robust support for multiple stable assets across Celo and Solana).
- **Code Snippet**:
    - `client/contexts/useWeb3.tsx`:
    ```typescript
    const cUSDTokenAddress = "0x765DE816845861e75A25fCA122bb6898B8B1282a"; // Celo Mainnet cUSD
    // ...
    const checkContractAddress = (tokenSymbol: string) => {
        if(tokenSymbol.toLowerCase() == 'cusd'){
            let address = '0x765DE816845861e75A25fCA122bb6898B8B1282a'
            return address as `0x${string}`;
        }else if(tokenSymbol.toLowerCase() == 'usdt'){
            let address = '0x48065fbBE25f71C9282ddf5e1cD6D6A887483D5e'
            return address as `0x${string}`;
        } // ... and USDC
    };
    // ...
    await walletClient.writeContract({
        address: tokenContractAddress,
        abi: StableTokenABI.abi,
        functionName: "approve",
        account: walletClient.account.address,
        args: [spenderAddress, amountInWei],
    });
    // ...
    await walletClient.writeContract({
        address: QuestPandaContract,
        abi: QuestPandaABI,
        functionName: "createQuestAsBrand",
        account: walletClient.account.address,
        args: [amountInWei, tokenContractAddress]
    });
    ```
    - `client/app/brand/quests/create/page.tsx`:
    ```typescript
    // ... inside handlePaymentAndSubmit
    const {
        celo: { cUSDBalance, USDTBalance: celoUSDTBalance, USDCBalance: celoUSDCBalance },
        solana: { USDTBalance: solUSDTBalance, USDCBalance: solUSDCBalance },
    } = await checkCombinedTokenBalances();

    // Prioritization logic for payment token
    if (Number(cUSDBalance) >= Number(prizePool)) {
        await completeQuestCreation("cusd", 'celo');
    } else if (Number(celoUSDTBalance) >= Number(prizePool)) {
        await completeQuestCreation("usdt", 'celo');
    } // ... and other tokens/networks
    ```
- **Security Assessment**:
    -   **Token Approvals**: Uses the `approve` and `transferFrom` pattern for ERC20 tokens, which is standard. The `QuestPanda` contract uses `SafeERC20` for robust token interactions.
    -   **Multi-currency/Multi-chain**: Robust handling of different stablecoins and blockchain networks (Celo/Solana) is implemented, reducing the risk of asset mismatch.
    -   **Hardcoded Addresses**: Celo token addresses (cUSD, USDT, USDC) are hardcoded in `useWeb3.tsx`, which is acceptable for widely used tokens but requires careful verification.
    -   **Solana Integration**: Uses `bs58` for private key decoding and standard SPL token operations. The backend funds Solana transaction fees, mitigating user UX issues.

### 5. **Advanced Mento Features**
- **File Path**: Not applicable.
- **Implementation Quality**: N/A (No implementation).
- **Code Snippet**: N/A.
- **Security Assessment**: N/A.

### 6. **Implementation Quality Assessment**
- **Architecture**: Clean separation of concerns between frontend (Next.js components, contexts) and backend (Express routes, controllers, models). Modular design is evident in `useWeb3.tsx` and API controllers.
- **Error Handling**: Basic `try-catch` blocks are used. Custom `useAlert` and `useConfirm` hooks provide a consistent UI for user feedback. Transaction functions (`approveSpending`, `createQuest`, `customFundFeesOnWallet`) include retry mechanisms for common blockchain errors (nonce, gas, underpriced transactions), which enhances robustness.
- **Gas Optimization**: The `prefillGas_v2` function actively estimates and funds gas fees on Celo, which is a key optimization for Celo's fee market and user experience, especially for MiniPay users.
- **Security**:
    -   Authentication middleware (`requireAuth`) protects API routes.
    -   Input validation for quest creation and submission (`express-validator`).
    -   The `QuestPanda` smart contract utilizes `ReentrancyGuard` and `SafeERC20` for common smart contract vulnerabilities.
    -   The backend service for gas funding introduces a trust component, but the transaction is ultimately signed by the user.
    -   Solana private key handling from Web3Auth is done securely via `getED25519Key` and `bs58`.
- **Testing**: "Missing tests" is a noted weakness, indicating a lack of unit, integration, or end-to-end tests, which is a significant risk for a production-ready dApp.
- **Documentation**: READMEs provide high-level overviews. Code comments are present but could be more comprehensive for complex Web3 logic in `useWeb3.tsx` and controllers.

## Mento Integration Summary

### Features Used:
- **Mento-managed Stablecoins**: The project extensively uses cUSD, USDT, and USDC as primary stable assets for quest prize pools and rewards. These tokens operate on the Celo blockchain and are part of the Mento Protocol ecosystem.
- **Celo Ecosystem Integration**: The project integrates deeply with the broader Celo ecosystem, including:
    -   Celo native token (CELO) for gas fees, with custom gas pre-filling logic.
    -   MiniPay wallet detection and auto-connection.
    -   Farcaster Mini App detection.
    -   `@divvi/referral-sdk` for referral tracking, which operates on Celo.
- **Cross-chain Stable Asset Support**: The project supports USDT and USDC on the Solana blockchain in addition to Celo, demonstrating an understanding of stable asset liquidity beyond a single chain.
- **Fiat On-Ramp**: Integration with a third-party service (Pretium/Swypt) for M-Pesa to USDT (Celo) on-ramping, providing a fiat gateway to stable assets.

### Implementation Quality:
- **Code Organization**: Web3 interaction logic is well-organized within `useWeb3.tsx` and related ABI files, promoting modularity.
- **Error Handling**: Robust error handling is present for blockchain interactions, including retry logic for common transaction issues. Custom UI components (`useAlert`, `useConfirm`) enhance user experience during errors.
- **Security Practices**: The custom smart contract uses standard OpenZeppelin contracts for `Ownable` and `ReentrancyGuard` and `SafeERC20` for secure token interactions. Backend API routes are authenticated.
- **Architectural Decisions**: The choice of Next.js for the frontend and a dedicated Node.js backend allows for efficient data fetching, server-side rendering, and API management. The integration of Wagmi/Viem provides a modern and type-safe approach to Celo interactions.

### Best Practices Adherence:
- **Adherence to ERC20 Standards**: The project adheres to ERC20 standards for token transfers and approvals, which is fundamental for Mento stablecoins.
- **Celo Gas Fee Management**: The custom gas pre-filling mechanism is a good practice for improving user experience on Celo, especially for MiniPay users who might not hold CELO directly.
- **Missing Documentation and Testing**: A significant deviation from best practices is the explicit lack of a test suite and comprehensive documentation, which are crucial for the reliability and maintainability of a blockchain application.

## Recommendations for Improvement
- **High Priority**:
    -   **Implement Comprehensive Testing**: Develop unit, integration, and end-to-end tests for all critical blockchain interactions, especially for `useWeb3.tsx` functions (`approveSpending`, `createQuest`, `rewardCreator`) and smart contract logic. This is essential for verifying correctness and preventing regressions.
    -   **Mento Protocol SDK Integration**: For deeper integration, consider using the official `@mento-protocol/mento-sdk` to actively query Mento Exchanges for optimal swap routes or to fetch real-time oracle rates. This would allow the dApp to offer dynamic pricing or facilitate direct swaps within the application.
- **Medium Priority**:
    -   **Detailed Code Documentation**: Add more comprehensive inline comments and JSDoc for complex functions, especially in `useWeb3.tsx` and API controllers, explaining the rationale behind design choices and potential edge cases.
    -   **Slippage Protection for Transfers**: While not a "swap," if the project ever introduces variable-rate scenarios or external liquidity interactions beyond the current fixed-price model, implement slippage protection for token transfers to safeguard users against unexpected price movements.
    -   **Event-Driven Updates**: Implement a more robust event-driven architecture for tracking on-chain events (e.g., `QuestCreatedByBrand`, `CreatorRewardedByBrand`) to ensure the frontend and backend are always in sync with the blockchain state, rather than relying solely on polling or manual refreshes.
- **Low Priority**:
    -   **Mento Exchange Discovery**: Even without direct swaps, the dApp could use `getExchangeRegistryId` from the cUSD token to display information about the underlying Mento Exchange, enhancing transparency.
    -   **UI Feedback for On-Ramp Status**: Improve real-time feedback for the M-Pesa on-ramp process, perhaps by actively polling the Pretium/Swypt status and updating the UI, rather than relying on a simple "initiated" state.

## Technical Assessment from Senior Blockchain Developer Perspective
The project demonstrates a solid foundational architecture for a Web3 application on Celo, with commendable efforts in managing multi-chain stable assets and addressing Celo-specific UX challenges like gas fees. The `useWeb3` hook is well-designed to abstract complex blockchain interactions, and the backend effectively supports these operations. However, the current implementation *passively consumes* Mento-managed stablecoins rather than *actively integrating* with the Mento Protocol's dynamic features. Production readiness is hampered by the stated lack of a test suite, which introduces significant risk for a project handling financial transactions. To evolve into an innovative Mento-centric application, direct engagement with the Mento SDK for dynamic swaps, liquidity provision, or robust oracle integration would be crucial. As it stands, it's a functional stablecoin-powered dApp with a good base, but limited Mento Protocol-specific innovation.

---

## Project Analysis Summary

| GitHub Repository | Mento Implementation | Senior Developer Rating (1-10) |
|------------------|---------------------|-------------------------------|
| https://github.com/leakeyqq/questapp | Uses Mento-managed stablecoins (cUSD, USDT, USDC on Celo) for quest rewards and prize pools. Implements custom gas funding for Celo transactions. No direct Mento SDK, Broker, or Oracle integration. | 4.0/10 |

### Key Mento Features Implemented:
- **Stable Asset Usage**: cUSD (primary), USDT, USDC on Celo are used as ERC20 tokens for value transfer.
- **Celo Gas Sponsorship**: Custom backend-driven gas funding for Celo transactions, which implicitly supports transactions involving Mento stablecoins.

### Technical Assessment:
Questpanda presents a well-structured Next.js and Express.js dApp with multi-chain stable asset support (Celo and Solana). It effectively handles stablecoin payments and Celo gas mechanics, demonstrating solid Web3 development. However, its Mento Protocol integration is limited to passive consumption of Mento-managed stablecoins, lacking active use of Mento SDK, broker, or oracle features, which restricts its innovation in the Mento ecosystem.

## GitHub Metrics
### Repository Metrics
- Stars: 0
- Watchers: 1
- Forks: 2
- Open Issues: 6
- Total Contributors: 2
- Created: 2025-04-09T20:31:28+00:00
- Last Updated: 2025-08-14T19:55:57+00:00

### Top Contributor Profile
- Name: Leakey Njeru
- Github: https://github.com/leakeyqq
- Company: N/A
- Location: N/A
- Twitter: N/A
- Website: N/A

### Language Distribution
- TypeScript: 81.17%
- JavaScript: 13.17%
- Solidity: 4.91%
- CSS: 0.76%

### Codebase Breakdown
- **Strengths**: Active development (updated within the last month), comprehensive README documentation.
- **Weaknesses**: Limited community adoption (0 stars, 2 forks), no dedicated documentation directory, missing contribution guidelines, missing license information, missing tests, no CI/CD configuration.
- **Missing or Buggy Features**: Test suite implementation, CI/CD pipeline integration, configuration file examples, containerization.