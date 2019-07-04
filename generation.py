from random import randint, randrange, shuffle

import networkx as nx
import matplotlib.pyplot as plt
import json
from save import saveInstance


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
    TAILLE_DATA = 0

    DEPART = 0
    C_MIN = 1
    C_MAX = 10


    graphe = 0

    def __init__(self, realisme, json_file, taille, bornemin, bornemax, c_min, c_max, c_camion, s_depart):
        """Constructeur de notre classe"""
        self.realisme = realisme
        self.json_file = json_file
        self.TAILLE_DATA = taille
        self.BORNEMIN = bornemin
        self.BORNEMAX = bornemax
        self.DEPART = s_depart
        self.C_MIN = c_min
        self.C_MAX = c_max

        self.graphe = self.vrp_generate()

        matrice_instance = self.gen_matrice_ponderation()
        capacite = self.generate_capacite()

        #Enregistre matrice_ponderation.txt
        file = open('/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/Texte/matrice_ponderation_t=' + str(
            taille) + '_bmin=' + str(bornemin) + '_bmax=' + str(bornemax) + '.txt', 'w')
        file.write(str(matrice_instance))
        file.close()

        # Enregistre capacite.txt
        file = open('/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/Texte/capacite_t=' + str(taille) + '_cmin=' + str(
            c_min) + '_cmax=' + str(c_max) + '_ccamion=' + str(c_camion) + '_sdepart=' + str(s_depart) + '.txt', 'w')
        file.write(str(capacite))
        file.close()

        saveInstance(self.graphe,
                     '/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/Objets/graphe_t=' + str(taille) + '_bmin=' + str(
                         bornemin) + '_bmax=' + str(bornemax))

        saveInstance(matrice_instance,
                     '/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/Objets/matrice_ponderation_t=' + str(
                         taille) + '_bmin=' + str(bornemin) + '_bmax=' + str(bornemax))

        saveInstance(capacite, '/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/Objets/capacite_t=' + str(
            taille) + '_cmin=' + str(
            c_min) + '_cmax=' + str(c_max) + '_ccamion=' + str(c_camion) + '_sdepart=' + str(s_depart))



    def vrp_generate(self):
        # JSON Config
        # On charge le fichier json dans la variable data
        with open(self.json_file) as f:
            self.data = json.load(f)

        self.G = nx.Graph()
        self.reduire_echantillon(self.TAILLE_DATA)

        if self.realisme == 1:
            # On crée le triangle de départ
            for i in range(0, 3):
                self.G.add_node(self.data[i]["name"], pos=(self.lat(i), self.lng(i)))
            self.G.add_edge(self.data[0]["name"], self.data[1]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))
            self.G.add_edge(self.data[2]["name"], self.data[0]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))
            self.G.add_edge(self.data[2]["name"], self.data[1]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))

            self.G = self.vrp_realiste()

            # On dessine notre graphe
            nx.draw(self.G, nx.get_node_attributes(self.G, 'pos'), node_size=75, with_labels=True)
        elif self.realisme == 0:
            for i in range(0, 3):
                self.G.add_node(self.data[i]["name"])

            self.G.add_edge(self.data[0]["name"], self.data[1]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))
            self.G.add_edge(self.data[2]["name"], self.data[0]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))
            self.G.add_edge(self.data[2]["name"], self.data[1]["name"], weight=randint(self.BORNEMIN, self.BORNEMAX))

            self.G = self.vrp_standard()

            # On dessine notre graphe
            nx.draw(self.G, node_size=75, with_labels=True)
        elif self.realisme == 2:
            for n in range(0, len(self.data)):
                current_node = self.data[n]["name"]
                self.G.add_node(current_node)

            self.G = self.vrp_complet()

            nx.draw(self.G, node_size=75, with_labels=True)
        return self.G;

    def vrp_complet(self):
        for i in range(0, len(self.data)):
            current_node = self.data[i]["name"]
            for j in range(0, len(self.data)):
                node_cible = self.data[j]["name"]
                self.G.add_edge(current_node, node_cible, weight=randint(self.BORNEMIN, self.BORNEMAX))
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

    def generate_capacite(self):
        capacite_ville = []
        for n in range(1, len(self.data)):
            capacite_ville.append(randrange(self.C_MIN, self.C_MAX))
        shuffle(capacite_ville)
        capacite_ville.insert(self.DEPART, 0)
        return capacite_ville;

    def gen_matrice_ponderation(self):
        foo = []
        for i in range(0, self.TAILLE_DATA):
            chemin = []
            for j in range(0, self.TAILLE_DATA):
                if i == j:
                    chemin.append(0)
                else:
                    chemin.append(randint(self.BORNEMIN, self.BORNEMAX))
            foo.append(chemin)
        return foo;

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
