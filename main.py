import time

import save
from generation import VRPGenerator
from vrp_solving import Genetic_Algorithm

# Variables
from vrp_solving_constraint import Genetic_algorithm_with_constraint

BORNEMIN = 1
BORNEMAX = 10
TAILLE = 10
N_MUTE = 5  # Doit être inférieur à TAILLE
MUTATION_CHANCE = 0.5

NB_IND = 100  # Bug quand moins d'individu que de villes
NB_ITE = 200

SOMMET_DEPART = 5  # Bug quand sommet_depart est différent de 0

CAPACITE_CAMION = 10
CAPACITE_VILLE_MAX = 10
CAPACITE_VILLE_MIN = 1

path_matrice = '/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/Objets/matrice_ponderation_t=' + str(
    TAILLE) + '_bmin=' + str(
    BORNEMIN) + '_bmax=' + str(BORNEMAX)

path_capacite = '/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/Objets/capacite_t=' + str(TAILLE) + '_cmin=' + str(
    CAPACITE_VILLE_MIN) + '_cmax=' + str(CAPACITE_VILLE_MAX) + '_ccamion=' + str(CAPACITE_CAMION) + '_sdepart=' + str(
    SOMMET_DEPART)


graphe = VRPGenerator(2, '/home/thomas/Bureau/Dev/CESI-Projet-DATA/cities.json', TAILLE, BORNEMIN, BORNEMAX, CAPACITE_VILLE_MIN, CAPACITE_VILLE_MAX, CAPACITE_CAMION, SOMMET_DEPART)
# Realisme / Fichier JSON de villes / NB_VILLES / pondération min / pondération max / Capacité min /  Capacité max / Capacité du camion / Sommet de départ

#On enregistre le graphe sous forme JSON
save.saveGrapheToJson(graphe.G, TAILLE)

#Algorithme de résolution TSP
tsp_solving = Genetic_Algorithm(path_matrice, TAILLE, NB_IND, NB_ITE, N_MUTE, MUTATION_CHANCE, SOMMET_DEPART)
# Objet matrice de pondération / NB_VILLES / Nombre d'individus / Nombre d'itérations / Le nombre N de chemins qui ont une chance de muter / Chance de muter / Sommet de départ


#Algorithme de résolution VRP
vrp_solving = Genetic_algorithm_with_constraint(path_matrice, path_capacite, CAPACITE_CAMION, TAILLE, NB_IND, N_MUTE, MUTATION_CHANCE, NB_ITE, SOMMET_DEPART, CAPACITE_VILLE_MIN, CAPACITE_VILLE_MAX)
# Objet matrice de pondération / chemin de l'objet / capacité du camion / nombre de villes / Nombre individus / Le nombre N de chemins qui ont une chance de muter / Chance de muter / Nombre d'itérations / Sommet de départ / Capacité maximale qu'une ville peut avoir, Capacité minimale qu'une ville peut avoir

graphe.show_graph()
