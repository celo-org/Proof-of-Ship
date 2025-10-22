# Analysis Report: leakeyqq/questapp

Generated: 2025-10-07 01:45:38

## Project Scores

| Criteria | Score (0-10) | Justification |
|----------|--------------|---------------|
| Security | 5.5/10 | Authentication is present, but validation is inconsistent. `execSync` in a dev script is concerning if accidentally deployed. Secret management relies on `.env`. |
| Functionality & Correctness | 7.0/10 | Core features for brands and creators seem implemented, including complex Web3 interactions and social media scraping. Explicitly missing tests and some error handling could be more robust. |
| Readability & Understandability | 7.5/10 | Frontend code is well-structured with clear component usage. Backend uses a standard MVC-like pattern. README is excellent. Code comments are sparse in complex areas. |
| Dependencies & Setup | 6.5/10 | Uses modern, well-maintained libraries. Setup is standard for Next.js/Node.js/Solidity. However, critical CI/CD, testing, and license information are missing. |
| Evidence of Technical Usage | 8.0/10 | Demonstrates solid integration of Web3 (Celo, Solana, Web3Auth, Wagmi), external APIs (social media scraping, fiat on/off-ramp), and modern frontend/backend frameworks. |
| **Overall Score** | 7.0/10 | Weighted average. The project demonstrates strong technical capabilities and core functionality, but critical areas like security validation, testing, and DevOps practices need significant improvement. |

---

## Repository Metrics
- Stars: 0
- Watchers: 1
- Forks: 2
- Open Issues: 6
- Total Contributors: 2
- Created: 2025-04-09T20:31:28+00:00
- Last Updated: 2025-10-03T18:28:19+00:00
- Open PRs: 6
- Closed PRs: 34
- Merged PRs: 34
- Total PRs: 40

## Top Contributor Profile
- Name: Leakey Njeru
- Github: https://github.com/leakeyqq
- Company: N/A
- Location: N/A
- Twitter: N/A
- Website: N/A

## Language Distribution
- TypeScript: 82.32%
- JavaScript: 12.61%
- Solidity: 4.4%
- CSS: 0.68%

## Codebase Breakdown
**Strengths:**
- Active development (updated within the last month), indicated by recent commits and PR activity.
- Comprehensive `README.md` documentation, providing a clear overview, features, and how-it-works sections.

**Weaknesses:**
- Limited community adoption (0 stars, 2 forks), suggesting it's primarily a solo or small team project.
- No dedicated documentation directory, which could make it harder to scale documentation.
- Missing contribution guidelines, hindering potential community involvement.
- Missing license information, which is crucial for open-source projects.
- Missing tests, a significant gap in ensuring correctness and maintainability.
- No CI/CD configuration, leading to manual deployment and lack of automated quality checks.

**Missing or Buggy Features:**
- Test suite implementation.
- CI/CD pipeline integration.
- Configuration file examples (though `.env` is used, explicit examples are not mentioned).
- Containerization (e.g., Dockerfiles).

---

## Project Summary
-   **Primary purpose/goal**: Questpanda aims to be an all-in-one platform for brands to launch marketing campaigns (quests) and for content creators to participate in these quests by creating and posting promotional videos on social media, earning rewards in cryptocurrency (cUSD).
-   **Problem solved**: It solves the problem of connecting brands with content creators for digital marketing in a structured, incentivized, and Web3-enabled manner, offering a transparent reward system.
-   **Target users/beneficiaries**:
    *   **Brands**: Businesses looking to launch marketing campaigns and engage content creators for promotional videos.
    *   **Content Creators**: Individuals interested in earning rewards by creating and sharing promotional content on platforms like TikTok, Instagram, and X (Twitter).

---

## Technology Stack
-   **Main programming languages identified**: TypeScript (82.32%), JavaScript (12.61%), Solidity (4.4%), CSS (0.68%).
-   **Key frameworks and libraries visible in the code**:
    *   **Frontend**: Next.js (React framework), Shadcn UI (component library), Tailwind CSS (styling), Wagmi, RainbowKit, Web3Auth (Web3 integration), Axios (HTTP client), `react-hook-form`, `zod` (form management/validation).
    *   **Backend**: Node.js (runtime), Express.js (web framework), Mongoose (MongoDB ODM), `jsonwebtoken` (JWT), `cookie-parser`, `cors`, `dotenv`, `axios`, `cloudinary` (image management), `cheerio` (web scraping, though `scrapecreators.com` API is primary), `@selfxyz/core` (identity verification), `@solana/web3.js`, `@solana/spl-token` (Solana interaction).
    *   **Smart Contracts**: Solidity, OpenZeppelin Contracts (for secure, reusable components), Hardhat (development environment, inferred from `celo-composer` template).
    *   **Other**: `decimal.js` (precise arithmetic).
-   **Inferred runtime environment(s)**: Node.js for both the Next.js frontend (server-side rendering and API routes) and the Express.js backend. Likely deployed in a serverless or containerized environment (Vercel mentioned for frontend, `vercel.json` for backend).

---

## Architecture and Structure
-   **Overall project structure observed**: The project follows a monorepo-like structure, with distinct `client` (Next.js frontend), `server` (Express.js API), `smart-contract` (Solidity contracts), and `celo-composer/minigigs-comp` (a Celo template, which appears to be the foundation for parts of the Web3 integration) directories. This separation of concerns is good for modularity.
-   **Key modules/components and their roles**:
    *   **`client/`**: The main Next.js application, handling user interfaces for brands and creators, wallet connections, and interacting with the backend API. It includes pages for dashboards, quest creation, quest browsing, leaderboards, and identity verification.
    *   **`server/`**: An Express.js application serving as the backend API. It manages user authentication, quest data (creation, submission, approval), creator profiles, social media data scraping, and interactions with external payment/identity APIs.
    *   **`smart-contract/`**: Contains Solidity contracts (`createQuest.sol`, `manageCurrencies.sol`, `rewardCreator.sol`) that define the core on-chain logic for quest creation, prize pool management, and creator rewards.
    *   **`celo-composer/minigigs-comp/`**: Appears to be a boilerplate or template from Celo Composer, providing foundational Web3 setup and documentation for MiniPay integration.
-   **Code organization assessment**:
    *   **Frontend (`client/`)**: Well-organized using Next.js App Router conventions (`app/` directory for pages, `components/` for reusable UI, `contexts/` for global state, `lib/` for utilities/data fetching, `hooks/`). Shadcn UI components provide a consistent design system.
    *   **Backend (`server/`)**: Follows a standard MVC-like pattern with `routes/`, `controllers/`, and `models/` directories. Middleware (`auth.js`) is used for authentication.
    *   **Smart Contracts (`smart-contract/`)**: Clearly separated into logical contracts (`CreateQuest`, `ManageCurrencies`, `RewardCreator`) with inheritance.
    *   **Overall**: The modular structure is good. However, the `celo-composer/minigigs-comp` directory seems somewhat disconnected from the main `client`/`server` logic, acting more as a reference or initial setup.

---

## Security Analysis
-   **Authentication & authorization mechanisms**:
    *   **Authentication**: Uses JWT (JSON Web Tokens) for backend API authentication. Upon wallet connection (via Wagmi/Web3Auth), a `login` endpoint is called which issues a JWT stored in an `httpOnly`, `secure`, `sameSite=strict` cookie.
    *   **Authorization**: The `requireAuth` middleware is used to protect API routes, verifying the JWT and attaching the `userWalletAddress` to the request object. `onlyOwner` modifier in smart contracts for admin functions.
-   **Data validation and sanitization**:
    *   **Frontend**: Client-side validation is present in forms (e.g., `CreateQuestPage.tsx` checks for empty fields).
    *   **Backend**: `express-validator` is used for some API routes (`questController.js`, `brandController.js`), but not consistently across all endpoints (e.g., `approvalController.js` performs manual checks). This inconsistency can lead to vulnerabilities.
    *   **Smart Contracts**: `require` statements are used for basic validation (e.g., `_validateQuestCreation` checks token support and allowance).
-   **Potential vulnerabilities**:
    *   **Inconsistent Backend Validation**: The lack of universal, robust input validation and sanitization on all backend routes (e.g., `approvalController.js` and `creatorController.js` rely on manual checks or lack explicit sanitization) is a significant vulnerability. Malicious input could lead to injection attacks (though Mongoose helps with NoSQL injection), data corruption, or unexpected behavior.
    *   **`execSync` usage**: The `contract.js` file (which appears to be a development/bot script) uses `execSync("git add .")` and `execSync("git commit -m ...")`. If this script were ever to be deployed or run in a production environment with user-controlled input, it would be a critical command injection vulnerability. It's crucial to ensure this is strictly a local dev tool.
    *   **Broken Access Control**: While `requireAuth` is used, the logic within controllers to verify ownership (e.g., `fetchMySingleCreatedQuest` checking `createdByAddress`) needs careful review to ensure no bypasses.
    *   **Sensitive Data Exposure**: Social media scraping APIs (ScrapeCreators) are used, which could potentially expose more data than intended if not carefully managed.
    *   **Reliance on External APIs**: Heavy reliance on `scrapecreators.com` and `pretium.finance` means the project's security is partly dependent on these third-party services.
    *   **Missing CI/CD**: The absence of CI/CD pipelines (as noted in weaknesses) means security checks, linting, and vulnerability scanning are likely not automated, increasing the risk of introducing flaws.
    *   **No Rate Limiting**: No explicit rate limiting middleware is visible, which could make the API susceptible to brute-force attacks or abuse.
-   **Secret management approach**: Environment variables (`.env`) are used for sensitive information like `JWT_SECRET`, `MONGODB_URI`, `CLOUD_API_KEY`, `SCRAPECREATOR_API_KEY`, `PRETIUM_API_KEY`, `SWYPT_API_KEY`, RPC URLs, and contract addresses. This is a standard practice, but proper environment configuration and secure handling in deployment are essential.

---

## Functionality & Correctness
-   **Core functionalities implemented**:
    *   **User Management**: Wallet-based login/logout, user registration (implicit on first login).
    *   **Brand Features**: Create quests (with prize pools, deadlines, social platform requirements, approval flows), view created quests, manage submissions (view, approve/reject), reward creators on-chain.
    *   **Creator Features**: Browse available quests, apply to quests (if approval needed), submit content (video URLs) for quests, view personal dashboard (earnings, completed quests, linked social accounts), identity verification via Self Protocol.
    *   **Wallet Integration**: Connect with Celo/Solana wallets (via Wagmi, RainbowKit, Web3Auth), send/receive cUSD/USDT/USDC, interact with custom smart contracts (approve tokens, create quests, reward creators).
    *   **Social Media Interaction**: Scrape creator profiles and post metrics (views, likes, comments) from TikTok, X (Twitter), Instagram using `scrapecreators.com` API.
    *   **Fiat On/Off-Ramp**: M-Pesa integration via Pretium API for depositing funds (on-ramp) and withdrawing earnings (off-ramp).
    *   **Leaderboard**: Displays top creators based on points earned.
    *   **Discover Creators**: (Currently simulated) for brands to find creators.
-   **Error handling approach**:
    *   **Frontend**: Uses `react-hot-toast` for user feedback on success/failure/warnings. Custom alert/confirm modals (`custom-popup.tsx`, `custom-confirm.tsx`) provide more structured user interaction for critical actions.
    *   **Backend**: `try-catch` blocks are used in controllers to catch errors, returning `500` status codes with error messages. `express-validator` captures validation errors.
    *   **Web3 Interactions**: Specific error handling for wallet connection issues, insufficient funds/allowance, and transaction failures. Retries are implemented for some on-chain operations.
-   **Edge case handling**:
    *   Checks for duplicate quest submissions.
    *   Quest deadline checks (`new Date(quest.endsOn) < new Date()`).
    *   Minimum follower count validation during quest application.
    *   Platform matching for approved creators during submission.
    *   Basic validation for invalid social media URLs.
    *   Checks for insufficient crypto balance for transactions.
    *   M-Pesa payment polling and timeout.
-   **Testing strategy**: The codebase weaknesses explicitly state "Missing tests" and "Test suite implementation". This is a critical gap, as there is no evidence of automated unit, integration, or end-to-end tests to ensure correctness, prevent regressions, or verify edge case handling.

---

## Readability & Understandability
-   **Code style consistency**:
    *   **Frontend**: Generally consistent with modern React/Next.js practices. Uses functional components, hooks, and follows Shadcn UI component patterns. Tailwind CSS classes are consistently applied.
    *   **Backend**: Follows a standard Express.js pattern with clear route, controller, and model files. Variable and function naming are generally descriptive.
    *   **Smart Contracts**: Follows Solidity best practices with clear function names, `require` statements, and OpenZeppelin inheritance.
-   **Documentation quality**:
    *   **`README.md`**: Excellent. It provides a clear, concise, and comprehensive overview of the project's purpose, features, how it works for different user roles, and Web3 integration details. It also includes instructions for setting up the Celo Composer template.
    *   **In-code comments**: Sparse, particularly in the backend controllers and core logic for Web3 interactions and external API calls. More detailed comments would significantly improve understandability for complex flows (e.g., the `useWeb3` hook, social media scraping logic).
    *   **External documentation**: The "No dedicated documentation directory" weakness indicates a lack of broader project documentation (e.g., architecture diagrams, API specifications, contributing guidelines).
-   **Naming conventions**:
    *   Variable and function names are generally descriptive and follow camelCase (`handleQuestCreation`, `submitQuestByCreator`, `prizePoolUsd`).
    *   Component names in the frontend are PascalCase (`QuestCardV2`, `SubmissionForm`).
    *   Smart contract functions follow Solidity conventions.
-   **Complexity management**:
    *   **Frontend**: Manages complexity through component-based architecture, hooks for state and side effects, and custom contexts (`CurrencyContext`, `useWeb3`) for global state. The Web3 interaction logic in `useWeb3.tsx` is complex but encapsulated.
    *   **Backend**: Uses a modular structure with controllers, services (implicit in `controllers`), and models. However, some controller functions (e.g., `pullTwitterData_v2`) are quite long and handle multiple concerns (API calls, database updates, image processing), which could be refactored for better separation.
    *   **Smart Contracts**: Relatively simple and focused, leveraging OpenZeppelin for common patterns, which reduces complexity.

---

## Dependencies & Setup
-   **Dependencies management approach**: `package.json` files are used in both `client` and `server` directories to manage dependencies. `yarn` is implied by `yarn.lock` and `yarn workspace` commands in `celo-composer/minigigs-comp/package.json`. The project uses a wide array of modern and well-known libraries across Web3, frontend, and backend development.
-   **Installation process**:
    *   For the client and server, it would typically involve `npm install` or `yarn` in each directory, followed by setting up `.env` files.
    *   For smart contracts, the `celo-composer` template provides CLI instructions (`npx @celo/celo-composer@latest create`) for setting up Hardhat and deploying contracts.
    *   The overall process seems standard for a JavaScript/Solidity project, but explicit, consolidated setup instructions for the entire monorepo would be beneficial.
-   **Configuration approach**: Configuration is managed primarily through `.env` files for sensitive keys, API endpoints, and contract addresses. This is a standard and secure practice for environment-specific settings.
-   **Deployment considerations**:
    *   The `vercel.json` file in the `server` directory indicates deployment to Vercel for the Express.js backend as a serverless function.
    *   The `client` (Next.js app) is also typically deployed to Vercel.
    *   The `celo-composer/minigigs-comp/README.md` includes a section "Deploy with Vercel," suggesting a clear deployment path for the Web3 frontend.
    *   **Missing**: The project explicitly lacks CI/CD configuration, which is a significant omission for automated testing, building, and deployment, especially in a Web3 project where security and correctness are paramount. Containerization (e.g., Dockerfiles) is also missing, which could simplify deployment consistency across different environments.

---

## Evidence of Technical Usage
The project demonstrates a high level of technical implementation quality across several domains, leveraging a modern and diverse technology stack.

1.  **Framework/Library Integration**
    *   **Next.js (Frontend)**: Uses the App Router, `generateMetadata` for SEO and Farcaster Frame compatibility, and server components/functions for data fetching (`getSingleQuest`). The `cache` utility is used for data fetching optimization. `next.config.mjs` shows experimental features like `webpackBuildWorker` and `turbopack` usage for performance.
    *   **Wagmi/RainbowKit/Web3Auth (Web3 Frontend)**: Provides a robust multi-wallet connection experience. Web3Auth is integrated for social logins and managing private keys for both Ethereum-compatible (Celo) and Solana chains, abstracting wallet complexities for users. This is a sophisticated solution for broader user adoption.
    *   **Solidity/Hardhat (Smart Contracts)**: Employs OpenZeppelin contracts for secure, audited components (Ownable, ReentrancyGuard, SafeERC20), which is a best practice. The contracts define core logic for quests and rewards, demonstrating understanding of ERC-20 token standards.
    *   **Express.js (Backend API)**: Standard RESTful API implementation with modular routes, controllers, and models. Uses `express-validator` for input validation (though inconsistently applied).
    *   **Mongoose (Database)**: Effectively models complex data structures like `Quest` submissions, `Creator` profiles (with nested social media data), and `Wallet` transactions, demonstrating good schema design.
    *   **External API Integration**: Seamlessly integrates with `scrapecreators.com` for fetching real-time social media metrics (Twitter, TikTok, Instagram) and `pretium.finance` for fiat on-ramp (M-Pesa) and off-ramp functionalities. Cloudinary is used for image hosting, including processing profile pictures from social media.
    *   **Referral SDK**: Integration of `@divvi/referral-sdk` in `sendCUSD` indicates a plan for referral tracking and rewarding, showcasing an understanding of growth mechanisms.

2.  **API Design and Implementation**
    *   **RESTful Design**: Endpoints like `/api/quest`, `/api/brand`, `/api/creator` follow RESTful conventions for resource management.
    *   **Endpoint Organization**: Routes are logically grouped by feature (auth, quest, brand, creator, fees, swypt, verification, wallet).
    *   **Request/Response Handling**: JSON is used for requests and responses. Middleware (`requireAuth`) is correctly applied for authentication. Error responses provide relevant messages.

3.  **Database Interactions**
    *   **Data Model Design**: Schemas for `Quest`, `Creator`, `User`, `Wallet`, and payment orders (`SwyptOnrampOrder`, `PretiumOnrampOrder`) are well-defined, capturing necessary data for the platform's functionality, including nested objects for social media data and quest submissions.
    *   **ORM/ODM Usage**: Mongoose is used effectively for interacting with MongoDB. Operations like `find`, `findById`, `findOneAndUpdate`, `updateOne`, `aggregate`, and `$push`/`$set` for nested updates are correctly applied.
    *   **Query Optimization**: `lean().exec()` is frequently used for read-heavy operations to improve performance by returning plain JavaScript objects instead of Mongoose documents.
    *   **Complex Queries**: The `getAllCreators` aggregation pipeline demonstrates the ability to perform more complex data transformations (e.g., `$size` for `questsDoneCount`).

4.  **Frontend Implementation**
    *   **UI Component Structure**: Utilizes Shadcn UI components extensively, ensuring a consistent and modern look and feel. Components are organized logically (e.g., `quest-card-v2`, `submission-form`, `navbar`).
    *   **State Management**: `useState` and `useEffect` hooks are used for local component state. Global state is managed via React Context (`CurrencyContext`) and Wagmi/Web3Auth for wallet-related data. `react-query` is used for server-side state management and caching.
    *   **Responsive Design**: Tailwind CSS is used to create a responsive layout, adapting to different screen sizes.
    *   **Web3 Interaction UI**: Provides clear UI feedback during Web3 transactions (loading states, success/error messages via custom modals and toasts). The `ConnectWalletButton` handles different wallet environments (MiniPay, Valora, Farcaster, Web3Auth).

5.  **Performance Optimization**
    *   **Caching**: `cache` utility from Next.js is used for `getSingleQuest` to memoize data fetching.
    *   **Client-side data fetching**: `useEffect` hooks trigger data fetches on component mount, often with loading states.
    *   **Server-Side Rendering (SSR)**: Next.js App Router implies SSR for initial page loads, improving perceived performance and SEO.
    *   **Asynchronous Operations**: Extensive use of `async/await` for network requests and blockchain interactions to prevent UI blocking.
    *   **Gas Estimation & Prefilling**: The `useWeb3` hook includes logic to estimate gas costs and interact with a backend endpoint (`/api/fees/gas-estimate`) to prefill gas, which is a critical feature for user experience in Web3 apps, especially on chains like Celo.

The project demonstrates a strong grasp of both Web2 and Web3 technical best practices, integrating various technologies effectively to build a complex decentralized application. The evidence of Celo integration is strong, despite the tool's initial report.

---

## Suggestions & Next Steps
1.  **Implement Comprehensive Testing**: Develop a robust test suite covering unit, integration, and end-to-end tests for both frontend and backend. Prioritize critical paths like quest creation, reward distribution, and social media data processing. This is crucial for ensuring correctness, preventing regressions, and building confidence in the platform's reliability.
2.  **Enhance Backend Input Validation & Sanitization**: Systematically review all backend API endpoints and implement thorough input validation and sanitization using `express-validator` (or a similar library). This will significantly reduce the risk of injection attacks, data corruption, and other security vulnerabilities.
3.  **Integrate CI/CD Pipeline**: Set up a CI/CD pipeline (e.g., using GitHub Actions) to automate testing, code quality checks (linting, vulnerability scanning), and deployment. This will improve code quality, speed up development cycles, and ensure consistent deployments.
4.  **Refactor Complex Backend Logic**: Break down overly large or complex controller functions (e.g., in `questController.js` and `creatorController.js`) into smaller, more focused service functions. This will improve readability, maintainability, and testability.
5.  **Add API Documentation and Contribution Guidelines**: Create a dedicated `docs/` directory. Generate API documentation (e.g., OpenAPI/Swagger) for the backend. Add clear contribution guidelines to encourage community involvement and provide a structured way for others to understand and contribute to the project.
6. **Improve Error Handling for Web3 Interactions:** While basic error handling is present, consider more granular error types for Web3 interactions (e.g., `InsufficientFundsError`, `TransactionFailedError`) to provide more specific user feedback and allow for better recovery strategies.