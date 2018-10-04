from models import Population
from models import Citizen
from utility import randint_bound, choice, rand, rand_bound


class PopulationGen(Population):
    def __init__(self, pop_size, best_pop, p_m):
        super().__init__(pop_size)
        self.best_pop = best_pop
        self.p_m = p_m

    def create_pop(self):
        return [Citizen() for _ in range(self.pop_size)]

    def make_crossover(self):
        children = []
        for _ in range(self.best_pop, self.pop_size):
            p1, p2 = self.select_parents()
            child = self.cross(self.population[p1], self.population[p2])
            self.mutate(child)
            children.append(child)
        self.population = self.population[:self.best_pop] + children
        # self.evaluate()
        # self.sort_pop()

    def cross(self, p1, p2):
        v_p1 = p1.get_values()
        v_p2 = p2.get_values()
        cut_p = randint_bound(1, 3)
        v_child = v_p1[:cut_p] + v_p2[cut_p:]
        return Citizen(v_child)

    def select_parents(self):
        return choice(self.best_pop, 2)

    def mutate(self, citizen):
        if (rand() * 100) < self.p_m:
            pos = randint_bound(4)
            citizen.get_values()[pos] = rand_bound(*Citizen.BOUNDS[pos])
