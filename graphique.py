import networkx as nx
import matplotlib.pyplot as plt

from lecture import *


class Node():
    def __init__(self, type, id, coords):
        self.type = type
        self.id = id
        self.coords = coords
    def __repr__(self):
        return f"{self.type}{self.id}"


instance = lire_instances("Kiro-large.json")

# Ajout des noeuds

G_clients = nx.Graph()

pre_clients = instance["clients"]
clients = [Node("I", client["id"], coords=client["coordinates"]) for client in pre_clients]
clients_pos = {client:client.coords for client in clients}

G_clients.add_nodes_from(clients)

G_sites = nx.Graph()

pre_sites = instance["sites"]
sites = [Node("S", site["id"], coords=site["coordinates"]) for site in pre_sites]
sites_pos = {site:site.coords for site in sites}

G_sites.add_nodes_from(sites)

# Tracé

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
# pos = clients_pos
# pos.update(sites_pos)
nx.draw(G_clients, pos=clients_pos,  with_labels = False, node_color='lightblue', ax = ax)
nx.draw(G_sites, pos=sites_pos,  with_labels = True, node_color='red', ax = ax)

print(len(sites))
plt.show()