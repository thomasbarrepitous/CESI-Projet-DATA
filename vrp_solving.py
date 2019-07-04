import random
from save import readFile

class Genetic_Algorithm:
    """Classe implémentant un algorithme génétique pour la résolution du TSP avec pour variable :
        - fichier JSON
        - un sommet de départ
        - meilleur individu
        - meilleur fitness (meilleure pondération totale d'un chemin
        - taux retenu d'individu retenu dans une population
        - nombre de villes
        - nombre d'individu
        - nombre d'échantillon
        - nombre d'itération maximum
        - nombre d'itération actuel
        
    """

    JSON = ''

    SOMMET_DEPART = 0

    BEST_IND = []
    BEST_FITNESS = 0

    RETAIN_PERCENTAGE = 0.3
    NB_VILLES = 0
    NB_IND = 5
    NB_ECH = round(NB_IND * RETAIN_PERCENTAGE)
    NB_ITE = 10
    ITE = 0

    fitness = []
    population = []
    foo = []

    def __init__(self, json_file_ponderation, nb_villes, nb_ind, nb_ite, retain, sommet):
        """Constructeur de notre classe"""
        self.JSON = json_file_ponderation
        self.NB_VILLES = nb_villes
        self.NB_IND = nb_ind
        self.NB_ITE = nb_ite
        self.NB_ECH = retain
        self.SOMMET_DEPART = sommet

        self.foo = readFile(json_file_ponderation)

        self.population = self.gen_ppl_initial()

        while self.NB_ITE > self.ITE:
            self.ITE += 1
            self.population = self.tri_fitness(self.population)
            self.BEST_IND = self.best_sol(self.population)
            self.population = self.selection_ech(self.population, self.NB_ECH)
            self.population = self.fill_new_pop(self.population)
            print("Meilleur individu : " + str(self.BEST_IND) + ", Somme pondération : " + str(
                self.eval_fitness(self.BEST_IND)) + ", Itération n° : " + str(self.ITE))

    # Etape 1 : On genere une population de base
    def gen_ppl_initial(self):
        ppl = []
        for i in range(0, self.NB_VILLES):
            ppl.append(self.generation_ind())
        return ppl;

    def generation_ind(self):
        chemin = []
        for n in range(0, self.NB_VILLES):
            chemin.append(n)
        random.shuffle(chemin)
        chemin.remove(self.SOMMET_DEPART)
        chemin.insert(0, self.SOMMET_DEPART)
        chemin.insert(self.NB_VILLES, self.SOMMET_DEPART)
        return chemin;

    # Etape 2 : On évalue cette population

    def eval_fitness(self, chemin):
        score = 0
        for index, value in enumerate(chemin):
            if index != len(chemin) - 1:
                value1 = chemin[index]
                value2 = chemin[index + 1]
                score += self.foo[value1][value2]
        return score;

    def tri_fitness(self, liste_entree):
        foo = list(liste_entree)
        N = len(foo)
        for i in range(1, N):
            cle = foo[i]
            j = i - 1
            while j >= 0 and self.eval_fitness(foo[j]) > self.eval_fitness(cle):
                foo[j + 1] = foo[j]  # decalage
                j = j - 1
            foo[j + 1] = cle
        return foo;

    # Etape 3 : On fait muter la population
    def crossover_milieu(self, chemin):
        chemin_crossover = []
        for i in range(0, 2):
            chemin.remove(self.SOMMET_DEPART)
        part1 = chemin[int((len(chemin) / 2)):].copy()
        part2 = chemin[:int((len(chemin) / 2))].copy()
        chemin_crossover += part1
        chemin_crossover += part2
        chemin_crossover.insert(0, self.SOMMET_DEPART)
        chemin_crossover.insert(len((chemin))+1, self.SOMMET_DEPART)
        self.muter(chemin_crossover)
        return chemin_crossover;

    def muter(self, individu):
        gene1 = random.randint(1, self.NB_VILLES - 1)
        gene2 = random.randint(1, self.NB_VILLES - 1)
        individu[gene1], individu[gene2] = individu[gene2], individu[gene1]
        return individu;

    def fill_new_pop(self, ppl):
        new_pop = []
        for i in range(0, self.NB_ECH):
            new_pop.append(ppl[i])
        for x in range(self.NB_ECH, self.NB_IND):
            new_pop.append(self.generation_ind())
        return new_pop;

    def best_sol(self, ppl):
        return ppl[0];

    def selection_ech(self, ppl, nb_ech):
        new_pop = [ppl[0]]
        for i in range(1, nb_ech):
            new_pop.append(self.crossover_milieu(ppl[i]))
        return new_pop;
