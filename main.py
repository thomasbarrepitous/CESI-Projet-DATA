import time

import save
from generation import VRPGenerator
from vrp_solving import Genetic_Algorithm

# Variables
from vrp_solving_constraint import Genetic_algorithm_with_constraint

BORNEMIN = 1
BORNEMAX = 10
TAILLE = 10

NB_IND = 100  # Bug quand moins d'individu que de villes
NB_ITE = 200
RETAIN = 5  # Doit être inférieur à TAILLE
SOMMET_DEPART = 1 #Bug quand sommet_depart est différent de 0

CAPACITE_CAMION = 20

path_matrice = '/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/matrice_ponderation_t=' + str(TAILLE) + '_bmin=' + str(BORNEMIN) + '_bmax=' + str(BORNEMAX)


start_time = time.time()

#vrp = VRPGenerator(2, '/home/thomas/Bureau/Dev/CESI-Projet-DATA/cities.json', TAILLE, BORNEMIN,
#                   BORNEMAX)  # Realisme / JSON / NB_VILLES / BORNEMIN / BORNEMAX

print(time.time() - start_time)

solving = Genetic_Algorithm \
    (path_matrice, TAILLE, NB_IND, NB_ITE, RETAIN,
     SOMMET_DEPART)  # Fichier d'instance / NB_VILLES / NB_IND / NB_ITE / RETAIN / SOMMET_DEPART

print(time.time() - start_time)

solving = Genetic_algorithm_with_constraint(path_matrice, CAPACITE_CAMION, TAILLE, NB_IND, RETAIN, NB_ITE, SOMMET_DEPART)

print(time.time() - start_time)

#vrp.show_graph()
