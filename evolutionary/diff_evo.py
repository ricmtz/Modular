import numpy as np
from .citizen import Citizen
from parameters import Function as func


class DiffEvolution(object):

    def __init__(self, max_gen, pop_size, wf, cr):
        self.max_gen = max_gen
        self.pop_size = pop_size
        self.wf = wf
        self.cr = cr

    def fitness_function(self, i_time, pop):
        for i in pop:
            error = func.calc_error(
                i_time, i.get_R(), i.get_L(), i.get_J(), i.get_LAM())
            i.set_error(error)

    def create_pop(self):
        return [Citizen() for _ in range(self.pop_size)]

    def de_rand_1_bin(self, p0, p1, p2, p3):
        cut = np.random.randint(4)
        sp = [0 for _ in range(4)]
        for i in range(4):
            if i == cut or np.random.rand() < self.cr:
                aux = p3[i] + self.wf * (p1[i] - p2[i])
                aux = Citizen.BOUNDS[i][0] if (
                    aux < Citizen.BOUNDS[i][0]) else aux
                aux = Citizen.BOUNDS[i][1] if (
                    aux > Citizen.BOUNDS[i][1]) else aux
                sp[i] = aux
            else:
                sp[i] = p0[i]
        return Citizen(sp)

    def select_parents(self, current):
        p1, p2, p3 = np.random.randint(self.pop_size, size=3)
        while (p1 == current):
            p1 = np.random.randint(self.pop_size)
        while (p2 == current or p2 == p1):
            p2 = np.random.randint(self.pop_size)
        while (p3 == current or p3 == p1 or p3 == p2):
            p3 = np.random.randint(self.pop_size)
        return p1, p2, p3

    def create_children(self, pop):
        children = []
        for i, p0 in enumerate(pop):
            p1, p2, p3 = self.select_parents(i)
            child = self.de_rand_1_bin(p0.get_values(), pop[p1].get_values(
            ), pop[p2].get_values(), pop[p3].get_values())
            children.append(child)
        return children

    def select_population(self, parents, children):
        new_pop = []
        for i in range(self.pop_size):
            best = parents[i] if parents[i].get_error(
            ) <= children[i].get_error() else children[i]
            new_pop.append(best)
        return new_pop

    def search(self):
        error = []
        gen = 0
        pop = self.create_pop()
        self.fitness_function(gen, pop)
        pop.sort(key=lambda x: x.get_error())
        best = pop[0]
        while gen < self.max_gen:
            children = self.create_children(pop)
            self.fitness_function(gen, children)
            children.sort(key=lambda x: x.get_error())
            pop = self.select_population(pop, children)
            pop.sort(key=lambda x: x.get_error())
            if pop[0].get_error() < best.get_error():
                best = pop[0]
            error.append(best.get_error())
            print('Gen: {}, fitness: {}'.format(gen, best.get_error()))
            gen += 1
        return best, error
