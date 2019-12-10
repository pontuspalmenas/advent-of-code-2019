import networkx as nx

G = nx.Graph()

n = []
def parse_line(line):
    p = line.split(')')
    G.add_node(p[0])
    G.add_edge(p[0], p[1])

with open('example') as f:
    for line in f.read().splitlines():	
        parse_line(line)

sum = 0
for n, nbrs in G.adj.items():
    for nbr in nbrs.items():
        sum += 1
print(sum)
print(nx.density(G))


#print(G.number_of_nodes())
#print(G.number_of_edges())
#print(list(G.adj))