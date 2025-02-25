# Project Name

EventChain

## Link to your project's GitHub repository

[https://github.com/Chigozie0706/eventchain](https://github.com/Chigozie0706/eventchain)

## Team Members GitHub username

- https://github.com/Chigozie0706

## Former Participation in Celo Hackathons

Nill

## Goal for This Proof of Ship

The goal is to develop a decentralized event management platform on the Celo blockchain. The dApp will allow users to:

- Create an event.
- View a list of events created by themselves and others.
- Join an event.
- View detailed event information.
- Delete an event (only if they are the owner).
- Purchase tickets using Mento stablecoins (cUSD, cEUR, cCOP)

### Weekly Milestones

**Week 1:**

- Set up the smart contract for event creation, listing, and deletion.
- Implement event ownership validation for deletion.
- Deploy the initial smart contract on the Celo testnet.

**Week 2:**

- Develop the front end with React.js and integrate the smart contract.
- Implement event listing and detailed views.
- Allow users to join events.

**Week 3:**

- Implement purchase tickets using Mento stablecoins (cUSD, cEUR, cCOP)
- Finalize UI/UX improvements.
- Test smart contract interactions thoroughly.
- Deploy the dApp and verify contracts on Celo.

**Week 4:**

- Bug fixes and optimizations.
- Prepare documentation and finalize submission.

Here's a more detailed version of your description with additional depth, competitor mention, and technical details:

---

## **Detailed Description of the Work Done During the Contest**

During the contest, I developed and deployed a decentralized event management platform on the **Celo blockchain**, enabling users to create, manage, and attend events securely. The platform leverages **smart contracts for transparency, ownership validation, and trustless transactions**.

### **Key Features Implemented:**

- **Smart Contract Development:** Created and deployed Solidity smart contracts for event creation, ticketing, and ownership validation.
- **Frontend Integration:** Built a responsive **Next.js** frontend that interacts seamlessly with the blockchain.
- **Event Management:** Users can **create, list, and delete events**, ensuring full control over event data.
- **Ticket Purchase with cUSD:** Integrated a secure payment system using **Celo's stablecoin (cUSD)** for ticket transactions.
- **Ownership Validation:** Implemented access control to **prevent unauthorized event deletion** and ensure only event creators can modify their events.
- **Smart Contract Testing & Deployment:** Conducted unit tests on smart contracts and deployed them on **Celo Alfajores Testnet** for real-world testing.

---

## **Problem**

Traditional event management platforms like **Eventbrite** and **Meetup** are **centralized**, meaning event organizers and attendees rely on third-party services to create, manage, and purchase tickets. This model introduces:

- **Lack of transparency:** Users must trust platforms with event data and payments.
- **High fees:** Third-party services charge processing fees for ticket sales.
- **Data Ownership Issues:** Event creators do not have full control over their event details and attendee lists.

---

## **Solution**

A **decentralized event management platform** that allows users to create, join, and manage events while maintaining full ownership. Key benefits of our approach:

- **Transparency:** All event and ticketing data is stored on-chain, ensuring verifiability.
- **Trustless Transactions:** Users purchase tickets via smart contracts using **cUSD**, eliminating the need for intermediaries.
- **Decentralized Ownership:** Event creators have full control over their events, preventing censorship or data manipulation.

---

## **Competitors & Differentiation**

| Feature                       | Eventbrite                         | Meetup              | Decentralized Event Platform (Built on Celo) |
| ----------------------------- | ---------------------------------- | ------------------- | -------------------------------------------- |
| Centralized or Decentralized? | Centralized                        | Centralized         | **Decentralized**                            |
| Transaction Fees?             | High                               | Subscription-based  | **Minimal (gas fees only)**                  |
| Payment Options               | Traditional (Credit/Debit, PayPal) | Subscription-based  | **Crypto (cUSD on Celo)**                    |
| Ownership Control             | Platform Controlled                | Platform Controlled | **User-Owned**                               |
| Transparency                  | Limited                            | Limited             | **Fully Transparent (On-Chain)**             |

Our platform leverages **blockchain technology to eliminate middlemen**, providing a more transparent, secure, and user-controlled event management experience.

---

## **Architecture**

### **Technology Stack:**

- **Frontend:** [Next.js](https://nextjs.org/) (React framework)
- **Blockchain:** [Celo](https://celo.org/) smart contracts written in Solidity
- **Smart Contract Interaction:** [ethers.js](https://docs.ethers.org/)
- **Payment Processing:** Celo's stablecoin (cUSD)
- **Wallet Integration:** [MetaMask](https://metamask.io/) for authentication and transactions
- **Storage:** On-chain event data (no centralized database)
- **Package Manager:** [pnpm](https://pnpm.io/) for dependency management

### **High-Level System Flow:**

1. **Event Creation:** Users submit event details, which are stored on-chain via a Solidity smart contract.
2. **Event Listing:** The frontend fetches and displays active events from the blockchain.
3. **Ticket Purchase:** Attendees buy tickets using **cUSD** via the smart contract.
4. **Ownership Validation:** Only event creators can modify or delete their events.
5. **Smart Contract Execution:** The blockchain processes event-related transactions transparently.

---

## **Challenges & Solutions**

### **1. Smart Contract Event Deletion Not Updating Frontend**

**Issue:** When an event was deleted, the frontend didn't update automatically.  
**Solution:** Implemented state updates after transactions and refetched event data upon deletion.

### **2. Handling Blockchain Transactions in UI**

**Issue:** Users needed better feedback when transactions were pending.  
**Solution:** Integrated **loading states, success/error toasts**, and transaction status updates using `react-hot-toast`.

### **3. Gas Fee Optimization**

**Issue:** High gas fees for transactions.  
**Solution:** Optimized contract functions to **minimize gas costs** and used efficient data structures.

---

## **Future Improvements**

- **Support for More Cryptocurrencies:** Expand payment options beyond cUSD.
- **Ticket Reselling & Transfer:** Allow users to resell or transfer event tickets securely via smart contracts.
- **Social Features:** Add attendee profiles and event discussions.

---

## Deployed Contract Addresses on Celo

- 0xBa26366767eA843A656853d348c763c41f9D67Ca
- [Celo explorer](https://alfajores.celoscan.io/address/0xBa26366767eA843A656853d348c763c41f9D67Ca)

## Contracts Should Be Verified

[Celo explorer](https://alfajores.celoscan.io/address/0xBa26366767eA843A656853d348c763c41f9D67Ca)

## Team

- Chigozie0706

## Short Description (that fits into a tweet)

**Decentralized Event Platform on Celo** – Create, manage, and attend events seamlessly with blockchain. Buy tickets securely using cUSD, ensure transparency, and experience trustless event management. 🚀 #Celo #Web3 #Blockchain #Events

## link to all assets you provide

![Image](https://github.com/user-attachments/assets/b796ae16-92c8-4592-a55f-25cc575a3c10)
![Image](https://github.com/user-attachments/assets/c37491ec-c0d8-43cd-980e-8086c04e5994)
![Image](https://github.com/user-attachments/assets/1317079a-d067-4d99-ae08-0ca5c731e4e0)
![Image](https://github.com/user-attachments/assets/c89c9386-51ea-4116-b3d2-6acd2c463626)
![Image](https://github.com/user-attachments/assets/33a042eb-2f1e-4cfd-b3ed-00e90c318ae8)
![Image](https://github.com/user-attachments/assets/c784d079-1c17-4b95-a32d-6b396e21e19e)

## Link to Video explaining your work

[https://www.loom.com/share/ddc7d558f69b49f389badebc2174a425](https://www.loom.com/share/ddc7d558f69b49f389badebc2174a425)

## Link to your Presentation

[Slide](https://www.canva.com/design/DAGf-vn5bL4/GpTakYkJ6L9RTarjzrD4vg/view?utm_content=DAGf-vn5bL4&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h596c558439)
