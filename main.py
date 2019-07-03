import time

from generation import VRPGenerator
from vrp_solving import Genetic_Algorithm

# Variables
BORNEMIN = 1
BORNEMAX = 10
TAILLE = 2000

# Bug quand moins d'individu que de villes
NB_IND = 100
NB_ITE = 100
#Doit être inférieur à TAILLE
RETAIN = 5
SOMMET_DEPART = 0

start_time = time.time()

vrp = VRPGenerator(2, '/home/thomas/Bureau/Dev/CESI-Projet-DATA/cities.json', TAILLE, BORNEMIN,
                   BORNEMAX)  # Realisme / JSON / NB_VILLES / BORNEMIN / BORNEMAX

print(time.time() - start_time)

solving = Genetic_Algorithm \
    ('/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/matrice_ponderation_t=' + str(TAILLE) + '_bmin=' + str
        (BORNEMIN) + '_bmax=' + str(BORNEMAX), vrp.TAILLE_DATA, NB_IND, NB_ITE, RETAIN,
                            0)  # Fichier d'instance / NB_VILLES / NB_IND / NB_ITE / RETAIN / SOMMET_DEPART

print(time.time() - start_time)

#vrp.show_graph()
