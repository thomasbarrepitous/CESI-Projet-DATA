from random import randint

import networkx as nx
import matplotlib.pyplot as plt
import json


def lat(i):
    latitude = data[i]["lat"]
    return float(latitude);


def lng(i):
    longitude = data[i]["lng"]
    return float(longitude);


def limite_edge(n, limite):
    if n >= limite:
        return n;
    return randint(2, limite);


def reduire_echantillon(data, taille_data):
    while len(data) > taille_data:
        data.pop(1)
    return data;


# JSON Config
with open('villes.json') as f:
    data = json.load(f)

LIMITE = 5

plt.gca().invert_yaxis()
plt.gca().invert_xaxis()

G = nx.Graph()

#data = reduire_echantillon(data, 10)

for i in range(0, 3):
    G.add_node(data[i]["name"], pos=(lat(i), lng(i)))

G.add_edge(data[0]["name"], data[1]["name"])
G.add_edge(data[2]["name"], data[0]["name"])
G.add_edge(data[2]["name"], data[1]["name"])


#Pour tous les sommets à partir de 3 dans notre JSON
for j in range(3, len(data)):
    #On génere un nombre d'arrête aléatoire entre 2 et n-1, n étant notre nombre de sommets
    nbr_edge = limite_edge(randint(2, len(G.node) - 1),LIMITE)

    current_node = data[j]["name"]

    #On l'ajoute à notre graphe
    G.add_node(current_node, pos=(lat(j), lng(j)))


    #On ajoute autant d'arrêtes que la variable nbr_edge
    #rand = j
    for n in range(2, nbr_edge):
    #   while rand == j:
        rand = randint(0, len(G.node) - 1)

        node_cible = data[rand]["name"]
        G.add_edge(current_node, node_cible)

        #Peuvent faire des noeuds sur eux mêmes, je vais le corriger

nx.draw(G, nx.get_node_attributes(G, 'pos'), node_size=75, with_labels=True)
plt.show()

print(G.node)
print(data)

