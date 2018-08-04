import numpy as np
from .citizen import Citizen
from parameters import Parameter as parm
from parameters import Function as func


class Genetic(object):

    def __init__(self, pop_size, best_p, max_gen, p_m):
        self.pop_size = pop_size
        self.best_p = best_p
        self.max_gen = max_gen
        self.p_m = p_m

    def fitness_func(self, i_time, pop):
        for i in pop:
            error = func.calc_error(i_time, *i.get_values())
            i.set_error(error)

    def create_pop(self):
        return [Citizen() for _ in range(self.pop_size)]

    def select_parents(self):
        return np.random.choice(self.best_p, 2, replace=False)

    def crossover(self, p1, p2):
        v_p1 = p1.get_values()
        v_p2 = p2.get_values()
        cut_p = np.random.randint(1, 3)
        v_child = v_p1[:cut_p] + v_p2[cut_p:]
        return Citizen(v_child)

    def make_crossover(self, pop):
        children = []
        for _ in range(self.best_p, self.pop_size):
            p1, p2 = self.select_parents()
            child = self.crossover(pop[p1], pop[p2])
            children.append(child)
        return pop[:self.best_p] + children

    def mutate(self, citizen):
        pos = np.random.randint(4)
        aux = parm.get_rand(Citizen.BOUNDS[pos])
        if pos == 0:
            citizen.set_R(aux)
        elif pos == 1:
            citizen.set_L(aux)
        elif pos == 2:
            citizen.set_J(aux)
        elif pos == 3:
            citizen.set_LAM(aux)

    def search(self):
        gen = 0
        best = None
        error = []
        pop = self.create_pop()
        self.fitness_func(gen, pop)
        pop.sort(key=lambda x: x.get_error())
        best = pop[0]
        error.append(best.get_error())
        while gen < self.max_gen:
            children = self.make_crossover(pop)
            if np.random.rand() * 100 < self.p_m:
                pos = np.random.randint(self.best_p, self.pop_size)
                print('--------Mutation------')
                print(children[pos].get_values())
                self.mutate(children[pos])
                print(children[pos].get_values())
                print('----------------------')
            self.fitness_func(gen, children[self.best_p:])
            children.sort(key=lambda x: x.get_error())
            best = children[0]
            error.append(best.get_error())
            pop = children
            print('Gen: {}, Error: {}'.format(gen, best.get_error()))
            gen += 1
        return best, error
