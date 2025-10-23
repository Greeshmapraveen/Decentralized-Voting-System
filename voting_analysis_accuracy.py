# Tally votes
tally = Counter()
for block in bc.chain[1:]:  # skip genesis
    data = block.data
    tally[data['candidate']] += 1

print("Top 10 candidates by recorded votes:")
for cand, cnt in tally.most_common(10):
    print(f"{cand}: {cnt}")

# Accuracy = recorded / submitted
accuracy = (recorded / len(votes_df)) * 100
print(f"\nVote recording accuracy: {accuracy:.2f}%")  # should be 100%
