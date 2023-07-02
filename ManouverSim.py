import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph for movement
G = nx.DiGraph()

# Nodes represent locations, with their positions as attributes
G.add_node('Alpha', pos=(0, 0))
G.add_node('Bravo', pos=(1, 0))
G.add_node('Charlie', pos=(0, 1))
G.add_node('Delta', pos=(1, 1))

# Edges represent possible movements, with the cost as an attribute
G.add_edge('Alpha', 'Bravo', cost=1)
G.add_edge('Alpha', 'Charlie', cost=1.5)
G.add_edge('Bravo', 'Delta', cost=2)
G.add_edge('Charlie', 'Delta', cost=1)

# Find the shortest path from Alpha to Delta
path = nx.shortest_path(G, 'Alpha', 'Delta', 'cost')
print('Shortest path:', path)

# Plot the graph with Matplotlib using draw_networkx
pos = nx.get_node_attributes(G, 'pos')
nx.draw_networkx(G, pos)
plt.show()
