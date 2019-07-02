import random

CHANCE_TO_MUTATE = 0.1
GRADED_RETAIN_PERCENT = 0.2
CHANCE_RETAIN_NONGRATED = 0.05

POPULATION_COUNT = 100
NB_VILLES = 5

GENERATION_COUNT_MAX = 100

GRADED_INDIVIDUAL_RETAIN_COUNT = int(POPULATION_COUNT * GRADED_RETAIN_PERCENT)

MAXIMUM_FITNESS = 10 * NB_VILLES

SOMMET_DEPART = 0


class Genetic_Algorithm:
    """
    """

    BEST_IND = []
    BEST_FITNESS = 0

    fitness = []
    population = []
    vrp = 0
    foo = [[0, 2, 1, 5, 4],
           [1, 0, 9, 3, 7],
           [5, 2, 0, 6, 9],
           [2, 2, 1, 0, 1],
           [3, 2, 3, 3, 0]]

    def __init__(self, vrp):
        """Constructeur de notre classe"""
        self.vrp = vrp
        self.NB_VILLES = vrp.TAILLE_DATA

        self.population = self.gen_ppl_initiale()
        self.population = self.tri_fitness(self.population)

        self.muter([0, 1, 2, 3, 4, 5, 0])

    def launch(self):

        return self.BEST_IND, self.BEST_FITNESS;

    # Etape 1 : On genere une population de base
    def gen_ppl_initiale(self):
        ppl = []
        for i in range(0, self.vrp.TAILLE_DATA):
            ppl.append(self.generation_ind(SOMMET_DEPART))
        return ppl;

    def generation_ind(self, depart):
        chemin = []
        for n in range(0, NB_VILLES):
            chemin.append(n)
        random.shuffle(chemin)
        chemin.remove(0)
        chemin.insert(0, depart)
        chemin.insert(self.NB_VILLES, depart)
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
    def mutation(self, ppl):
        # On trie par rapport à la fitness

        return ppl;

    def muter(self, individu):
        gene1 = random.randint(1, self.vrp.TAILLE_DATA)
        gene2 = random.randint(1, self.vrp.TAILLE_DATA)
        print(individu)
        individu[gene1], individu[gene2] = individu[gene2], individu[gene1]
        print(individu)
        return individu;
