import networkx as nx
import matplotlib.pyplot as plt

from lecture import *


class Node():
    def __init__(self, type, id, coords):
        self.type = type
        self.id = id
        self.coords = coords
    def __repr__(self):
        return f"{self.type}_{self.id}"


instance = lire_instances("Kiro-tiny.json")


G = nx.Graph()

# Ajout des noeuds

pre_clients = instance["clients"]
clients = [Node("I", client["id"], coords=client["coordinates"]) for client in pre_clients]
clients_pos = {client:client.coords for client in clients}

G.add_nodes_from(clients)

pre_sites = instance["sites"]
sites = [Node("S", site["id"], coords=site["coordinates"]) for site in pre_sites]
sites_pos = {site:site.coords for site in sites}

G.add_nodes_from(sites)

# Tracé

pos = clients_pos
pos.update(sites_pos)
nx.draw(G, pos=pos,  with_labels = True, node_color='lightblue')

plt.show()