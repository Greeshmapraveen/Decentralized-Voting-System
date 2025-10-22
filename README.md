### Decentralized-Voting-System
##Decentralized voting system using Blockchain and Python
👩‍💻 Project Overview

This project simulates a secure and transparent decentralized voting system using Python and Blockchain principles.
It ensures vote integrity, immutability, and transparency by recording every vote as a separate block in a simulated blockchain.
In addition, data visualization and analysis are performed to understand voting trends such as:

Year-wise elector growth

Party-wise dominance

Constituency-wise and gender-wise participation
#🚀 Key Features

Blockchain Simulation:

Each vote is stored as a separate block with hash linkage.

Genesis block initialization and chain verification included.

Data Analysis (Pandas + Matplotlib):

Total votes by party, constituency, and year.

Highest electors per year and per party.

Gender distribution across constituencies.

Graphical Visualization:

📊 Party vs Total Votes

📈 Highest Electors per Year

🧭 Constituency-wise Trends

🪩 Blockchain Graph (Last N Blocks)

#🧩 Technologies Used
Category	Tools/Packages
Programming Language	Python 3.x
Data Handling	Pandas
Visualization	Matplotlib, Seaborn
Blockchain Simulation	Custom Python Classes
IDE Used	VS Code / Jupyter Notebook
Version Control	Git & GitHub
#👨‍💻 Team Members
Name	Role
Harshitha Uppalapadu	Python Developer (Blockchain & Analysis)
Greeshma	Data Visualization & Analytics
Emmanuel	Vote Simulation & Dataset Handling
Jakker	Chain Verification & Graph Exporting
#📅 Daily Work Summary
Date	Task	Status
20 Oct 2025	Dataset loading, Genesis block creation	✅ Completed
21 Oct 2025	Vote simulation, Graph plotting (party/year)	✅ Completed
22 Oct 2025	Blockchain visualization, README preparation	🔄 Ongoing
#⚙️ How It Works

#Initialize Blockchain: Creates a genesis block.

Record Votes: Adds each vote as a new block with timestamp and hash.

Verify Chain: Ensures data immutability through hash validation.

Visualize Results: Uses Pandas and Matplotlib to display analysis graphs.

#📊 Example Visualization
Blockchain Structure (Last 20 Blocks)
N = 20  # last 20 blocks
G_small = nx.DiGraph()
for i in range(len(bc.chain)-N, len(bc.chain)):
    G_small.add_edge(bc.chain[i-1].index, bc.chain[i].index)

plt.figure(figsize=(10,4))
nx.draw(G_small, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, arrows=True)
plt.title(f"Blockchain Structure (Last {N} Blocks)")
plt.show()

#🧠 Insights

The blockchain ensures integrity — no vote can be altered without changing the chain hash.

Party-wise analysis shows vote trends and majorities.

Elector trends help identify participation growth by year.

Gender analysis reflects inclusivity across constituencies.

#📁 Repository Structure
📦 Decentralized-Voting-System
├── dataset.csv
├── voting_system.py
├── blockchain_visuals.ipynb
├── graphs/
│   ├── party_votes.png
│   ├── electors_by_year.png
│   └── gender_by_constituency.png
├── README.md
└── requirements.txt

#💡 Future Enhancements

Integration with a real-time database (e.g., Firebase).

GUI dashboard for live vote visualization.

Voter authentication using hash-based IDs.

#🏁 Conclusion

This project demonstrates how blockchain technology can revolutionize election systems by providing transparency, trust, and decentralization.
The accompanying Python-based data analytics offers deep insights into elector patterns and voting behaviors.
