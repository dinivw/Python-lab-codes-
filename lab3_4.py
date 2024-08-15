import networkx as nx
tsv_file = "string_interactions_short.tsv"

G = nx.Graph()
with open(tsv_file) as file:
    for line in file:
        if "#" not in line:
            line = line.strip().split('\t')
            G.add_edge(line[0], line[1], combined_score=line[12])



count = 0
neighbors = G.neighbors("ERF24")

for i in neighbors:
    if G.edges[('ERF24',i)]['combined_score'] > str(0.7):
        count += 1

print(count)








