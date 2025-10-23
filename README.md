# 🗳️ Decentralized Voting System using Blockchain & Python

## 📘 Overview
This project implements a **secure and transparent decentralized voting system** using **Blockchain technology** and **Python**.  
It ensures that every vote is uniquely recorded, tamper-proof, and verifiable, making the election process more reliable and efficient.

The blockchain guarantees:  
- ✅ **Transparency** — all votes are visible on the immutable ledger  
- 🔒 **Security** — blocks are cryptographically linked using SHA-256  
- ⚙️ **Automation** — Python simulates blockchain validation and consensus  
- 🌍 **Scalability** — handles multiple constituencies, parties, and years  

---

## 📂 Dataset Information

| Feature | Description |
|----------|-------------|
| `st_name` | State name |
| `year` | Election year |
| `pc_no` | Parliamentary constituency number |
| `pc_name` | Constituency name |
| `pc_type` | Constituency type (GEN / SC / ST) |
| `cand_name` | Candidate name |
| `cand_sex` | Gender of candidate |
| `partyname` | Party name |
| `partyabbre` | Party abbreviation |
| `totvotpoll` | Total votes polled |
| `electors` | Number of electors |

**Dataset Size:** 73,081 × 11  
**Source:** Public Election Data (cleaned and preprocessed for simulation)

---

## 🧮 Phases of Implementation

### 🔹 Phase 1 – Dataset Preprocessing
- Loaded the dataset in Python using **Pandas**  
- Cleaned missing and duplicate entries  
- Extracted relevant fields (year, constituency, candidate, party, electors)  
- Generated synthetic voter data to simulate voting

---

### 🔹 Phase 2 – Blockchain Creation
- Implemented custom **Block** and **Blockchain** classes in Python  
- Each block contains:
  - Voter ID (hashed)
  - Candidate Name
  - Constituency Name
  - Timestamp
  - Previous Block Hash  
- Verified chain integrity after each transaction

---

### 🔹 Phase 3 – Voting Simulation & Accuracy
- Registered synthetic voters using **hashed voter IDs**  
- Simulated votes according to the dataset’s `totvotpoll`  
- Added votes as **blocks in the blockchain**  
- Checked for double voting and invalid votes  
- Calculated **vote recording accuracy**  

> 🟢 **Vote Recording Accuracy Achieved:** 100.00%  
> 🔐 **Blockchain Verification:** Chain is valid and consistent  

**Sample Top 10 Candidates by Recorded Votes:**
Dadala Ramanayya: 44
None Of The Above: 43
Bompalli Ramanna: 35
Gorre Ramesh: 35
Ram Prasad Das: 34

---

### 🔹 Phase 4 – Visualization & Analytics
Using **Matplotlib**, **Seaborn**, and **NetworkX**, generated insights:

- 📊 **Party-wise vote distribution**
- 👩‍🦰👨‍🦱 **Gender representation per constituency**
- 🗓️ **Year-wise elector analysis**
- 🔗 **Blockchain structure graph (last N blocks)**

---

## 📊 Visual Results (Sample Graphs)

### 1️⃣ Party-wise Vote Distribution
Displays top parties by total votes.

![Party Votes Graph](graphs/party_votes.png)

---

### 2️⃣ Gender Representation per Constituency
Stacked bar chart comparing total votes of male vs female candidates.

![Gender Graph](VotesByCandidateGenderInEachConstituency.png)

---

### 3️⃣ Year-wise Highest Electors per Party
Shows the year in which each party had the highest number of electors.

![Yearly Electors Graph](graphs/year_party_electors.png)

---

### 4️⃣ Blockchain Chain Visualization
Network graph displaying links between the last N blocks.

![Blockchain Structure](graphs/blockchain_chain.png)

---

## ⚙️ Technologies Used

| Category | Tools / Libraries |
|-----------|------------------|
| Language | Python |
| Data Handling | Pandas |
| Blockchain & Hashing | hashlib, json, datetime |
| Visualization | Matplotlib, Seaborn |
| Graph Representation | NetworkX |
| IDE / Environment | Jupyter Notebook / Google Colab |
| Version Control | Git & GitHub |

---

## 💻 Execution Steps

1. **Upload Dataset**
   - Upload `indian-national-level-election.csv` to Colab or Jupyter

2. **Run Notebook**
   - Execute all cells sequentially  
   - Blockchain will initialize and add votes as blocks

3. **Verify Blockchain**
   - Prints vote recording accuracy and validation status

4. **Generate Visualizations**
   - Run the graphing cells for party, gender, and year insights  
   - Save `.png` graphs to `/graphs` folder

---

## 🧑‍💻 Team Members

| Name | Role | Responsibility |
|------|------|----------------|
| **Harshitha Uppalapadu** | Python Developer | Blockchain logic & accuracy testing |
| **Greeshma** | Python Developer | Deployment & UI simulation |
| **Emmanuel** | Python Developer | Data preprocessing & visualization |
| **Jakker** | Python Developer | Dashboard & graph generation |

---

## 🧠 Challenges Faced
- Handling **large dataset** with 73K+ records  
- Ensuring **blockchain immutability** and unique voter IDs  
- Preventing double voting and maintaining **100% accuracy**  
- Visualizing constituency, party, and gender data across years

---

## 🚀 Future Enhancements
- Integrate **Smart Contracts** for automatic verification  
- Add **User Authentication (Aadhaar / OTP)**  
- Deploy as **Web App using Flask, Streamlit, or React**  
- Store blockchain data on **IPFS or Ethereum** for real-world decentralization

---

## 🏁 Conclusion
This project demonstrates how **blockchain technology** can be used to create a **transparent, secure, and decentralized voting system**.  
It ensures **trust, accountability, and efficiency**, providing a foundation for future digital democracy solutions. 🌐

---

> 📧 Contact: **harshithauppalapadu@gmail.com**

---

## ✅ Project Folder Structure
📁 Decentralized-Voting-System/
├── main_voting_system.ipynb
├── indian-national-level-election.csv
├── requirements.txt
├── README.md
└── /graphs/
├── party_votes.png
├── gender_by_constituency.png
├── year_party_electors.png
└── blockchain_chain.png

**requirements.txt**
pandas
matplotlib
seaborn
networkx



