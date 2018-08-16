# This program will ask for some input from a user to build a small-world
# network. Then it will visualize that network.

# import all the packages we'll need
import networkx as nx
import matplotlib.pyplot as plt

print "Hi there! We'll be making a small-world network today, but I need your help!"

nodes = -1
while nodes < 0:
    print "How many nodes should I put in the network? "
    nodes = int(raw_input())

    if nodes < 0:
        print "You can't have negative nodes! Try again."

neighbors = -1
while (neighbors < 0) | (neighbors > nodes):
    print "How many neighbors should each node have? "
    neighbors = int(raw_input())

    if neighbors < 0:
        print "You can't have negative neighbors! Try again."
    elif neighbors > nodes:
        print "You can't have more nodes than neighbors! Try again."

p = 10
while (0 > p) | (p > 1):
    print "What rewiring probability do you want? "
    p = float(raw_input())

    if 0 > p:
        print "Not acceptable. Try again!"
    elif p > 1:
        print "Not acceptable. Try again!"

G = nx.watts_strogatz_graph(nodes,neighbors,p)

pos = nx.circular_layout(G)

nx.draw_networkx_nodes(G,pos,node_size = 20)
nx.draw_networkx_edges(G,pos)

plt.axis("off")

plt.show()
