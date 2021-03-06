from models import Population
from models import Citizen
from utility import randint_bound, choice, rand


class PopulationGen(Population):
    def __init__(self, pop_size, best_pop, p_m):
        super().__init__(pop_size)
        self.best_pop = best_pop
        self.p_m = p_m

    def create_pop(self):
        return [Citizen() for _ in range(self.pop_size)]

    def make_crossover(self, pop=[]):
        children = []
        for _ in range(self.best_pop, self.pop_size):
            child = []
            if pop:
                p1, p2 = self.select_parents(len(pop))
                child = self.cross(pop[p1], pop[p2])
            else:
                p1, p2 = self.select_parents()
                child = self.cross(self.population[p1], self.population[p2])
            self.mutate(child)
            children.append(child)
        self.population = self.population[:self.best_pop] + children

    def cross(self, p1, p2):
        v_p1 = p1.get_values()
        v_p2 = p2.get_values()
        cut_p = randint_bound(1, 3)
        v_child = v_p1[:cut_p] + v_p2[cut_p:]
        return Citizen(v_child)

    def select_parents(self, len_pop=0):
        return choice(len_pop if len_pop else self.best_pop, 2)

    def mutate(self, citizen):
        if (rand() * 100) < self.p_m:
            pos = randint_bound(4)
            citizen.set_value(pos)

    def get_best_pop(self):
        return self.population[:self.best_pop]
