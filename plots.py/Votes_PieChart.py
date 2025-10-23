# Pie chart of recorded vs rejected votes
labels = ['Recorded Votes', 'Rejected Votes']
sizes = [recorded, rejected]
colors = ['#4CAF50', '#F44336']

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Vote Recording Accuracy")
plt.show()
