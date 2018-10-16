from math import exp, sqrt
from models import Population
from immune import Cell
from utility import rand_gaussian


class PopulationImmuneNet(Population):
    def __init__(self, pop_size, num_clones, beta, num_rand):
        super().__init__(pop_size)
        self.num_clones = num_clones
        self.beta = beta
        self.num_rand = num_rand
        self.aff_tresh = [(bound[1]-bound[0])*0.05 for bound in Cell.BOUNDS]

    def create_pop(self):
        return [Cell() for _ in range(self.pop_size)]

    def clone(self, parent):
        return Cell(parent.get_values())

    def mutation_rate(self, normalized_cost):
        return (1.0/self.beta) * exp(-normalized_cost)

    def mutate(self, child, normalized_cost):
        for i, v in enumerate(child.get_values()):
            alpha = self.mutation_rate(normalized_cost)
            child.set_value(i, (v + alpha * rand_gaussian()))

    def clone_cell(self, parent):
        clones = [self.clone(parent) for i in range(self.num_clones)]
        for cell in clones:
            self.mutate(cell, parent.get_norm_error())
        self.evaluate(clones)
        self.sort_pop(clones)
        return clones[0]

    def calculate_normalized_error(self):
        self.sort_pop()
        ran = self.get_worst().get_error() - self.get_best().get_error()
        if ran == 0.0:
            for p in self.population:
                p.set_norm_error(1.0)
        else:
            for p in self.population:
                p.set_norm_error(1.0 - (p.get_error() / ran))

    def average_error(self, pop=None):
        pop = pop if pop else self.population
        total = sum(c.get_error() for c in pop)
        return total / float(len(pop))

    def distance(self, c1, c2):
        total = sum((x + y)**2.0 for x, y in zip(c1, c2))
        return sqrt(total)

    def get_neighborhood(self, cell, pop):
        neighbors = []
        for p in pop:
            if self.distance(p.get_values(), cell.get_values()) < \
                    self.aff_thresh:
                neighbors.append(p)
        return neighbors

    def get_progeny(self):
        return [self.clone_cell(p) for p in self.population]

    def affinity_supress(self, pop):
        pop = []
        for cell in pop:
            neighbors = self.get_neighborhood(cell, pop)
            self.sort_pop(neighbors)
            if (not len(neighbors)) or (cell == neighbors[0]):
                pop.append(cell)
        self.population = pop

    def add_rand_pop(self):
        for _ in range(self.num_rand):
            self.population.append(Cell())
