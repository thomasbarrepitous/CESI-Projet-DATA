from random import randint

import networkx as nx
import matplotlib.pyplot as plt
import json


class VRPGenerator:
    """Classe générant un graphe connexe et utilisable pour le problème VRP.
    Caractérisé par :
    - son réalisme (0 ou 1)
    - un fichier json
    """

    # Liste qui va stocker les données du fichier JSON
    data = []
    # Notre graphe
    G = 0
    # Realisme activé ou désactivé (1 ou 0), définit si les villes sont placées en fonction de leur lat/lng ou
    # aléatoirement
    realisme = 0
    # La variable contenant le path du fichier JSON
    json_file = ''
    # La limite d'arrêtes par sommets
    LIMITE = 5
    BORNEMIN = 0
    BORNEMAX = 10

    def __init__(self, realisme, json_file):
        """Constructeur de notre classe"""
        self.realisme = realisme
        self.json_file = json_file

    def vrp_generate(self):
        # JSON Config
        # On charge le fichier json dans la variable data
        with open(self.json_file) as f:
            self.data = json.load(f)

        self.G = nx.Graph()
        # self.reduire_echantillon(5)

        if self.realisme == 1:
            # On crée le triangle de départ
            for i in range(0, 3):
                self.G.add_node(self.data[i]["name"], pos=(self.lat(i), self.lng(i)))
            self.G.add_edge(self.data[0]["name"], self.data[1]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))
            self.G.add_edge(self.data[2]["name"], self.data[0]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))
            self.G.add_edge(self.data[2]["name"], self.data[1]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))

            self.G = self.vrp_realiste()

            # On dessine notre graphe
            nx.draw(vrp.G, nx.get_node_attributes(vrp.G, 'pos'), node_size=75, with_labels=True)

            # pos = nx.get_node_attributes(vrp.G, 'pos')
            # labels = nx.get_edge_attributes(vrp.G, 'weight')
            # nx.draw_networkx_edge_labels(vrp.G, pos, edge_labels=labels)
            plt.show()
        else:
            for i in range(0, 3):
                self.G.add_node(self.data[i]["name"])

            self.G.add_edge(self.data[0]["name"], self.data[1]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))
            self.G.add_edge(self.data[2]["name"], self.data[0]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))
            self.G.add_edge(self.data[2]["name"], self.data[1]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))

            self.G = self.vrp_standard()

            # On dessine notre graphe
            nx.draw(vrp.G, node_size=75, with_labels=True)
            # pos = nx.get_node_attributes(vrp.G, 'pos')
            # labels = nx.get_edge_attributes(vrp.G, 'weight')
            # nx.draw_networkx_edge_labels(vrp.G, pos, edge_labels=labels)
        return self.G;

    def vrp_standard(self):
        # Pour tous les sommets à partir de 3 dans notre JSON
        for j in range(3, len(self.data)):
            # On génere un nombre d'arrête aléatoire entre 2 et n-1, n étant notre nombre de sommets
            nbr_edge = self.limite_edge(randint(2, len(self.G.node) - 1), self.LIMITE)

            current_node = self.data[j]["name"]

            # On l'ajoute à notre graphe
            self.G.add_node(current_node)

            # On ajoute autant d'arrêtes que la variable nbr_edge
            for n in range(1, nbr_edge + 1):
                rand = randint(0, len(self.G.node) - 1)
                cpt = 0

                for node in self.G:
                    if self.G.has_edge(current_node, node):
                        cpt += 1
                if cpt == len(self.G.node):
                    break;

                while self.G.has_edge(current_node, self.data[rand]["name"]) | rand == j:
                    rand = randint(0, len(self.G.node) - 1)

                node_cible = self.data[rand]["name"]
                self.G.add_edge(current_node, node_cible, weight=randint(self.BORNEMIN, self.BORNEMAX))
        return self.G;

    def vrp_realiste(self):
        # Pour tous les sommets à partir de 3 dans notre JSON
        for j in range(3, len(self.data)):
            # On génere un nombre d'arrête aléatoire entre 2 et n-1, n étant notre nombre de sommets
            nbr_edge = self.limite_edge(randint(2, len(self.G.node) - 1), self.LIMITE)

            current_node = self.data[j]["name"]

            # On l'ajoute à notre graphe
            self.G.add_node(current_node, pos=(self.lat(j), self.lng(j)))

            # On ajoute autant d'arrêtes que la variable nbr_edge
            for n in range(1, nbr_edge + 1):
                rand = randint(0, len(self.G.node) - 1)
                cpt = 0

                for node in self.G:
                    if self.G.has_edge(current_node, node):
                        cpt += 1
                if cpt == len(self.G.node):
                    break;

                while self.G.has_edge(current_node, self.data[rand]["name"]) | rand == j:
                    rand = randint(0, len(self.G.node) - 1)

                node_cible = self.data[rand]["name"]
                self.G.add_edge(current_node, node_cible, weight=randint(self.BORNEMIN, self.BORNEMAX))
        return self.G;

    # Fonction qui va recupère la position dans la liste en latitude
    def lat(self, i):
        latitude = self.data[i]["lat"]
        return float(latitude);

    # Fonction qui va recupère la position dans la liste en longitude
    def lng(self, i):
        longitude = self.data[i]["lng"]
        return float(longitude);

    # Fonction qui limite le nombre d'arrêtes possible
    def limite_edge(self, n, limite):
        if n >= limite:
            return n;
        return randint(2, limite);

    # Fonction utilisé pour réduire la taille de la liste
    def reduire_echantillon(self, taille_data):
        while len(self.data) > taille_data:
            self.data.pop(1)
        return self.data;

    def show_graph(self):
        plt.show()
        return 0;

#####
# Change les axes juste pour voir
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()

# On instance l'objet et on génère le graphe
vrp = VRPGenerator(0, 'E:\Desktop\Dev\Projet DATA\CESI-Projet-DATA/villes.json')
vrp.vrp_generate()
