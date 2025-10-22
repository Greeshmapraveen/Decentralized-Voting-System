# 🗳️ Decentralized Voting System using Blockchain & Python

## 📘 Overview
This project implements a **secure and transparent decentralized voting system** using **Blockchain technology** and **Python**.  
It ensures that every vote is uniquely recorded, tamper-proof, and verifiable, making the election process more reliable and efficient.

The blockchain structure guarantees:
- ✅ **Transparency** — all votes are visible on the public ledger.
- 🔒 **Security** — immutable records prevent vote manipulation.
- ⚙️ **Automation** — smart-like behavior simulated via Python logic.
- 🌍 **Scalability** — capable of handling multiple constituencies and years.

---

## 📂 Dataset Information

| Feature | Description |
|----------|--------------|
| `st_name` | State name |
| `year` | Election year |
| `pc_no` | Parliamentary constituency number |
| `pc_name` | Constituency name |
| `pc_type` | Constituency type (GEN/SC/ST) |
| `cand_name` | Candidate name |
| `cand_sex` | Gender of candidate |
| `partyname` | Party name |
| `partyabbre` | Party abbreviation |
| `totvotpoll` | Total votes polled |
| `electors` | Number of electors |

**Dataset Size:** 73,081 × 11  
**Source:** Public Election Data (cleaned and preprocessed for analysis)

---

## 🧮 Phases of Implementation

### 🔹 Phase 1 – Dataset Preprocessing
- Loaded the dataset in Python using Pandas.  
- Cleaned missing and duplicate entries.  
- Extracted relevant fields (year, constituency, party, candidate, etc.).
- Generated synthetic voter data for simulation.

### 🔹 Phase 2 – Blockchain Creation
- Implemented a custom `Block` and `Blockchain` class in Python.  
- Each block contains:
  - Voter ID
  - Candidate Name
  - Constituency Name
  - Timestamp
  - Previous Block Hash
- Verified the entire chain for consistency after each transaction.

### 🔹 Phase 3 – Voting Simulation & Accuracy
- Generated synthetic votes mapped to constituencies.  
- Added votes as transactions to the blockchain.  
- Verified and calculated **vote recording accuracy (≥97%)**.

> 🟢 Final Model Accuracy Achieved: **100.00%**

### 🔹 Phase 4 – Visualization & Analysis
Using **Matplotlib** and **Seaborn** for results visualization:
- 📊 **Party-wise vote distribution**
- 👩‍🦰👨‍🦱 **Gender representation per constituency**
- 🗓️ **Year-wise elector analysis**
- 🔗 **Blockchain structure graph (NetworkX)**

---

## 📊 Visual Results (Sample Graphs)

### 1️⃣ Party-wise Vote Distribution
![Party Votes Graph](graphs/party_votes.png)

### 2️⃣ Gender Representation per Constituency
![Gender Graph](graphs/gender_by_constituency.png)

### 3️⃣ Year-wise Highest Electors per Party
![Yearly Electors Graph](graphs/year_party_electors.png)

### 4️⃣ Blockchain Chain Visualization
![Blockchain Structure](graphs/blockchain_chain.png)

---

## ⚙️ Technologies Used

| Category | Tools / Libraries |
|-----------|------------------|
| Language | Python |
| Libraries | Pandas, Matplotlib, Seaborn, NetworkX |
| Framework | Jupyter / Google Colab |
| Version Control | Git & GitHub |
| Storage | Blockchain Simulation (JSON-based) |

---

## 💻 Execution Steps

1. **Open Google Colab**
   - Upload your dataset (`election_data.csv`)
   - Run the provided Python notebook cells in order.
2. **Run Blockchain Simulation**
   - Generates blocks for each vote.
   - Prints verification status and accuracy.
3. **Generate Visualizations**
   - Run the graph cells for gender, party, and year insights.
4. **Export & Upload**
   - Export graphs as `.png` to the `/graphs` folder.
   - Push your final project to GitHub.

---

## 🧑‍💻 Team Members

| Name | Role | Responsibility |
|------|------|----------------|
| **Harshitha Uppalapadu** | Python Developer | Blockchain logic & accuracy testing |
| **Greeshma** | Python Developer | Deployment & UI simulation |
| **Emmanuel** | Python Developer | Frontend dashboard integration |
| **Jakker** | Python Developer | Data preprocessing & visualization |

---

## 🧠 Challenges Faced
- Handling large dataset with over 73K records.
- Ensuring blockchain immutability and unique voter IDs.
- Maintaining vote accuracy above 97%.
- Visualizing large-scale data across multiple years.

---

## 🚀 Future Enhancements
- Integrate **Smart Contracts** for automatic verification.
- Add **User Authentication (Aadhar / OTP)**.
- Deploy as a **Web App using Flask or React**.
- Use **IPFS or Ethereum Blockchain** for real-world decentralization.

---

## 🏁 Conclusion
This project demonstrates how **blockchain technology** can be leveraged to build a **transparent, secure, and decentralized voting system**.  
It ensures **trust**, **accountability**, and **efficiency** in democratic processes — a step toward the future of digital governance. 🌐

---

> 📧 For any queries: **harshithauppalapadu@gmail.com**

