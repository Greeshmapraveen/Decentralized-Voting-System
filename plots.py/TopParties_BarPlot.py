# Aggregate votes per party
votes_party = df.groupby('partyname')['totvotpoll'].sum().reset_index()
votes_party = votes_party.sort_values('totvotpoll', ascending=False)

# Bar plot
plt.figure(figsize=(12,6))
sns.barplot(x='totvotpoll', y='partyname', data=votes_party.head(10), palette='magma')
plt.title("Top 10 Parties by Total Votes")
plt.xlabel("Total Votes")
plt.ylabel("Party Name")
plt.tight_layout()
plt.show()
