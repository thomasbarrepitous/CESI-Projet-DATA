import pickle


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

#"/home/thomas/Bureau/Dev/CESI-Projet-DATA/DATASET/graphe"