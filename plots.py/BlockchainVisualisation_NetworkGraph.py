N = 20  # last 20 blocks
G_small = nx.DiGraph()
for i in range(len(bc.chain)-N, len(bc.chain)):
    G_small.add_edge(bc.chain[i-1].index, bc.chain[i].index)

plt.figure(figsize=(10,4))
pos = nx.spring_layout(G_small, seed=42)
nx.draw(G_small, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, arrows=True)
plt.title(f"Blockchain Structure (Last {N} Blocks)")
plt.show()
