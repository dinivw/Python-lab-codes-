import networkx as nx

tsv_file = "string_interactions_short.tsv"

#creating an empty graph
G = nx.Graph()

with open(tsv_file) as file:
    for line in file:
        if "#" not in line:
            line = line.strip().split('\t')
            G.add_edge(line[0],line[1])



print(G.degree())
print(G.degree('ERF24'))




