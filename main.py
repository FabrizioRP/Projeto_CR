import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import igraph as ig

# Tudo por enquanto é provisorio e é só pra testar

a = pd.read_csv("test.csv") # Lê o csv do grafo

g = nx.Graph() # Cria o objeto grafo

# contando os RAs unicos
#cout = []
#c = 0

#for i in range((int)(a.size / 2)):
#    if a.loc[i][1] not in cout:
#        c+=1
#        cout+= [a.loc[i][1]]

#print(c)

# Cria os vertices dos RAs no grafo
for i in range((int)(a.size / 2)):
    g.add_node(a.loc[i][0], bipartite = 0)
    g.add_node(a.loc[i][1], bipartite = 1)
    g.add_edge(a.loc[i][0], a.loc[i][1])

# nx.draw(g)

G = ig.Graph.from_networkx(g)
fig, ax = plt.subplots()
ig.plot(G, target=ax, vertex_size=3, layout = G.layout("kk"))
plt.show()
print(g)