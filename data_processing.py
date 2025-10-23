# Upload your dataset to Colab first
DATAFILE = '/content/indian-national-level-election.csv'
df = pd.read_csv(DATAFILE)
print("Dataset loaded, rows:", len(df))

# Unique candidate-constituency
candidates_df = df[['pc_name', 'cand_name', 'partyname', 'totvotpoll', 'electors']].drop_duplicates().reset_index(drop=True)
print("Unique candidate-constituency rows:", len(candidates_df))

# Generate one voter per vote in dataset → ensures accuracy ~100%
voter_rows = []
for idx, row in df.iterrows():
    voter_id = f"{row['pc_name']}_V{idx+1:06d}"
    voter_rows.append({'voter_id': voter_id, 'pc_name': row['pc_name']})

voters_df = pd.DataFrame(voter_rows)
print("Synthetic voters generated:", len(voters_df))

# Simulated votes: use candidate and totvotpoll
votes_rows = []
for idx, row in df.iterrows():
    voter_id = f"{row['pc_name']}_V{idx+1:06d}"
    votes_rows.append({'voter_id': voter_id, 'candidate_name': row['cand_name'], 'pc_name': row['pc_name']})

votes_df = pd.DataFrame(votes_rows)
print("Simulated votes generated:", len(votes_df))

# Optional: save sample files
voters_df.to_csv('voters_sample.csv', index=False)
candidates_df.to_csv('candidates_sample.csv', index=False)
votes_df.to_csv('votes_sample.csv', index=False)
