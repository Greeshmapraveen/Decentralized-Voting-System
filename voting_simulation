bc = Blockchain()
registry = VoterRegistry()

# Register all voters
for _, row in voters_df.iterrows():
    registry.register(row['voter_id'])

print("Voters registered:", len(registry.registry))

# Cast votes
recorded = 0
rejected = 0
for _, r in votes_df.iterrows():
    voter_id = r['voter_id']
    candidate = r['candidate_name']
    pc = r['pc_name']
    voter_hash = hashlib.sha256(voter_id.encode()).hexdigest()

    if not registry.is_registered(voter_hash) or registry.has_voted(voter_hash):
        rejected += 1
        continue

    vote_data = {'voter_hash': voter_hash, 'candidate': candidate, 'pc_name': pc, 'timestamp': str(datetime.now(timezone.utc))}
    bc.add_block(vote_data)
    registry.mark_voted(voter_hash)
    recorded += 1

print(f"Votes processed: recorded={recorded}, rejected={rejected}, total_submitted={len(votes_df)}")

# Verify blockchain
valid, msg = bc.is_chain_valid()
print("Chain verification:", valid, msg)
