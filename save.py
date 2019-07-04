import json
import pickle
from networkx.readwrite import json_graph


def saveInstance(x, path):
    with open(
            path,
            'wb') as instanceFile:
        pickledFile = pickle.Pickler(instanceFile)
        pickledFile.dump(x)


def readFile(path):
    with open(path, 'rb') as fileRead:
        unpickler = pickle.Unpickler(fileRead)
        data = unpickler.load()
    return data


def saveGrapheToJson(graphe, taille):
    #La librairie networkx inclut des fonctions pour sérialiser un graphe en fichier JSON, graph_node_link_data permet
    # de transformer notre graphe en JSON.
    data = json_graph.node_link_data(graphe)

    with open("/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/JSON/Graphe_t=" + str(taille) +".json", 'w') as out_file:
        json.dump(data, out_file, sort_keys=True, indent=4)

