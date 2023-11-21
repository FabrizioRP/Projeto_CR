import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import igraph as ig

bip = []

for i in range(100000): 
    bip+= [i%2]

print(bip)

a = pd.read_csv("test.csv")

g = ig.Graph.DataFrame(edges = a, use_vids = False, directed = False)

ig.plot(g, target='myfile.pdf', vertex_size = 3, layout = g.layout("kk"))

print(g.is_bipartite())