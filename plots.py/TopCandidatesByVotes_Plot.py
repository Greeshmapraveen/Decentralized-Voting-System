# Convert tally Counter to DataFrame for plotting
tally_df = pd.DataFrame(tally.items(), columns=['candidate', 'votes']).sort_values(by='votes', ascending=False)

# Plot top 10 candidates
top10_df = tally_df.head(10)

plt.figure(figsize=(12,6))
sns.barplot(x='votes', y='candidate', data=top10_df, palette='viridis')
plt.title("Top 10 Candidates by Recorded Votes")
plt.xlabel("Number of Votes")
plt.ylabel("Candidate")
plt.tight_layout()
plt.show()
