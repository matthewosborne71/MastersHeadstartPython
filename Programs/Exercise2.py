# Write a file that allows a user to build an Erdos-Renyi random graph with
# user input, and then draws the graph for them.

import networkx as nx
import matplotlib.pyplot as plt

print "Hi there friend! We're making an Erdos-Renyi, but I need some help."

nodes = -10
while nodes < 0:
    print "How many nodes do you want? "
    nodes = int(raw_input())

    if nodes < 0:
        print "Sorry! The number of nodes can't be negative. :-("

p = 100
while (p < 0) | (p > 1):
    print "What edge probability friend? "
    p = float(raw_input())

    if (p < 0) | (p > 1):
        print "The probability has to be between 0 and 1! :-["

G = nx.erdos_renyi_graph(nodes,p)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G,pos,node_size = 20)
nx.draw_networkx_edges(G,pos)

plt.axis('off')
plt.show()
