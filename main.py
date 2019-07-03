from generation import VRPGenerator
from vrp_solving import Genetic_Algorithm


vrp = VRPGenerator(2, '/home/thomas/Bureau/Dev/CESI-Projet-DATA/villes.json', 5, 1, 10) #Realisme / JSON / NB_VILLES / BORNEMIN / BORNEMAX
vrp.vrp_generate()
solving = Genetic_Algorithm('',vrp, vrp.TAILLE_DATA, 10, 100, 3, 2) #Fichier d'instance / Graphe / NB_VILLES / NB_IND / NB_ITE / RETAIN / SOMMET_DEPART

vrp.show_graph()