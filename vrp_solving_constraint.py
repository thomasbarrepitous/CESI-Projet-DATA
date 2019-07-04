import random

import save


class Genetic_algorithm_with_constraint:
    MUTATION_CHANCES = 0.5
    capacite = 0
    depart = 0
    nb_ville = 0
    nb_ind = 0
    nb_ech = 0
    foo = [[0, 2, 3, 4, 5, 1, 2, 3, 4],
           [2, 0, 1, 2, 3, 4, 1, 2, 1],
           [1, 2, 0, 5, 3, 4, 1, 2, 3],
           [5, 4, 3, 0, 1, 2, 1, 2, 3],
           [3, 2, 1, 5, 0, 1, 2, 3, 3],
           [2, 5, 4, 1, 3, 0, 1, 1, 5],
           [1, 2, 3, 4, 5, 1, 0, 3, 4],
           [2, 3, 5, 4, 1, 2, 3, 0, 1],
           [5, 3, 2, 4, 1, 2, 3, 4, 0]]
    capacite_ville = []
    population = []
    best_ind = []

    def __init__(self, json_file, capacite, nb_ville, nb_ind, nb_ech, nb_ite, sommet_depart):
        self.nb_ite = nb_ite
        self.capacite = capacite
        self.nb_ville = nb_ville
        self.nb_ind = nb_ind
        self.nb_ech = nb_ech
        self.generate_capacite_ville()
        self.population = self.gen_ppl_initiale()
        self.etape = 0
        self.depart = sommet_depart
        self.matrice_ponderation = save.readFile(json_file)
        self.MUTATION_CHANCES = mutation * 100


        while True:
            if self.nb_ite > self.etape:
                self.etape += 1
                self.population = self.tri_ponderation_totale(self.population)
                self.best_ind = self.calcul_capacite_cumulee(self.best_sol(self.population))
                self.population = self.selection_ech(self.population)
                self.population = self.fill_new_pop(self.population)
                print("Meilleur individu : " + str(self.best_ind) + ", pondération totale : " + str(
                    self.fitness(self.best_ind)) + ", nombre d'itération(s) : " + str(
                    self.etape) + ", camions nécessaires : " + str(self.nombre_tournee(self.best_ind)))
            else:
                break

    def generate_capacite_ville(self):
        for n in range(1, self.nb_ville):
            self.capacite_ville.append(random.randrange(1, 6))
        random.shuffle(self.capacite_ville)
        self.capacite_ville.insert(0, self.depart)
        print("capacite_ville : " + str(self.capacite_ville))

    def gen_ppl_initiale(self):
        for i in range(0, self.nb_ind):
            self.population.append(self.generation_ind())
        return self.population;

    def generation_ind(self):
        chemin = []
        for n in range(0, self.nb_ville):
            chemin.append(n)
        random.shuffle(chemin)
        chemin.remove(self.depart)
        chemin.insert(0, self.depart)
        chemin.insert(self.nb_ville, self.depart)
        return chemin;

    def division_k_camions(self):
        for x in range(0, len(self.population)):
            self.population[x] = self.calcul_capacite_cumulee(self.population[x])

    def calcul_capacite_cumulee(self, chemin):
        capacite_cumul = 0
        new_chemin = []
        for x in range(0, len(chemin) - 1):
            new_chemin.append(chemin[x])
            capacite_cumul += self.capacite_ville[chemin[x]]
            if capacite_cumul + self.capacite_ville[chemin[x + 1]] > self.capacite:
                new_chemin.append(self.depart)
                capacite_cumul = 0
        new_chemin.append(self.depart)
        return new_chemin;

    def nombre_tournee(self, chemin):
        nb_tournee = 0
        for x in range(0, len(chemin)):
            if chemin[x] == self.depart:
                nb_tournee += 1
        return nb_tournee - 1;

    def tri_ponderation_totale(self, chemin):
        A = list(chemin)
        N = len(A)
        for i in range(1, N):
            cle = A[i]
            j = i - 1
            while j >= 0 and self.fitness(A[j]) > self.fitness(cle):
                A[j + 1] = A[j]  # decalage
                j = j - 1
            A[j + 1] = cle
        return A;

    def fitness(self, chemin):
        score = 0
        chemin = self.calcul_capacite_cumulee(chemin)
        for index, value in enumerate(chemin):
            if index != len(chemin) - 1:
                value1 = chemin[index]
                value2 = chemin[index + 1]
                score += self.matrice_ponderation[value1][value2]
        return score;

    def best_sol(self, liste):
        return liste[0];

    def selection_ech(self, liste):
        new_pop = [liste[0]]
        for i in range(1, self.nb_ech):
            new_pop.append(self.mutation(self.crossover(new_pop[0], liste[i])))
        new_pop[0].insert(0, self.depart)
        new_pop[0].insert(self.nb_ville, self.depart)
        return new_pop;

    def crossover(self, chromosome1, chromosome2):
        div = 3
        liste_manquante = []
        chromosome_crossover = []
        for i in range(0, self.nombre_tournee(chromosome2) + 1):
            chromosome2.remove(self.depart)
        for i in range(0, self.nombre_tournee(chromosome1) + 1):
            chromosome1.remove(self.depart)
        c1_part1 = chromosome1[0:int((len(chromosome1)) / div)]
        c1_part2 = chromosome1[int((len(chromosome1)) / div):int(len(chromosome1) - int((len(chromosome1)) / div))]
        c1_part3 = chromosome1[int(len(chromosome1) - int((len(chromosome1)) / div)):]
        c2_part1 = chromosome2[0:int((len(chromosome2)) / div)]
        c2_part2 = chromosome2[int((len(chromosome2)) / div):int(len(chromosome2) - int((len(chromosome2)) / div))]
        c2_part3 = chromosome2[int(len(chromosome2) - int((len(chromosome2)) / div)):]
        for i in range(0, len(c2_part3)):
            if c2_part3[i] not in c1_part2:
                liste_manquante.append(c2_part3[i])
        for i in range(0, len(c2_part1)):
            if c2_part1[i] not in c1_part2:
                liste_manquante.append(c2_part1[i])
        for i in range(0, len(c2_part2)):
            if c2_part2[i] not in c1_part2:
                liste_manquante.append(c2_part2[i])
        for x in range(0, len(c1_part1)):
            chromosome_crossover.append(liste_manquante[x - len(c1_part3)])
        chromosome_crossover.extend(c1_part2)
        for x in range(0, len(c1_part3)):
            chromosome_crossover.append(liste_manquante[x])
        chromosome_crossover.insert(0, self.depart)
        chromosome_crossover.insert(self.nb_ville, self.depart)
        return chromosome_crossover;

    def mutation(self, chromosome_crossover):
        p = random.randint(0, 100)
        if p < MUTATION_CHANCES:
            gene1 = random.randint(1, self.nb_ville - 1)
            gene2 = random.randint(1, self.nb_ville - 1)
            chromosome_crossover[gene1], chromosome_crossover[gene2] = chromosome_crossover[gene2], \
                                                                   chromosome_crossover[gene1]
        # print("apres mutation : " + str(chromosome_crossover))
        return chromosome_crossover;

    def fill_new_pop(self, liste_pop):
        new_pop = []
        for i in range(0, self.nb_ech):
            new_pop.append(liste_pop[i])
        for x in range(self.nb_ech, self.nb_ind):
            new_pop.append(self.generation_ind())
        return new_pop;

    def best_sol(self, liste):
        return liste[0];
