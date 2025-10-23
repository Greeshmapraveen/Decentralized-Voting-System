# Aggregate votes per pc_type
votes_pct = df.groupby('pc_type')['totvotpoll'].sum().reset_index()
votes_pct = votes_pct.sort_values('totvotpoll', ascending=False)

# Pie chart
plt.figure(figsize=(6,6))
plt.pie(votes_pct['totvotpoll'], labels=votes_pct['pc_type'], autopct='%1.1f%%', colors=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title("Votes by Constituency Type (pc_type)")
plt.show()
