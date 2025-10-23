# Group by constituency and year, sum electors
electors_year_pc = df.groupby(['pc_name', 'year'], as_index=False)['electors'].sum()

# For each constituency, find the year with highest electors
max_electors_per_pc = electors_year_pc.loc[electors_year_pc.groupby('pc_name')['electors'].idxmax()]

max_electors_per_pc.head(10)
