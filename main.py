from generation import VRPGenerator
from vrp_solving import Genetic_Algorithm


vrp = VRPGenerator(2, '/home/thomas/Bureau/Dev/Generation_ville/villes.json', 5, 1, 10) #Realisme / JSON / NB_VILLES / BORNEMIN / BORNEMAX
vrp.vrp_generate()
solving = Genetic_Algorithm(vrp)

vrp.show_graph()