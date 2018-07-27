import numpy as np
import math
from .citizen_s import CitizenS
from parameters import Function as func


class EvolutionS(object):

    def __init__(self, max_gen, pop_size, num_children):
        self.max_gen = max_gen
        self.pop_size = pop_size
        self.num_children = num_children

    def fitness_function(self, i_time, pop):
        for i in pop:
            error = func.calc_error(
                i_time, i.get_R(), i.get_L(),
                i.get_J(), i.get_LAM())
            i.set_error(error)

    def rand_gaussian(self):
        mean = 0.0
        stdev = 1.0
        u1 = u2 = w = 0
        while True:
            u1 = 2 * np.random.rand() - 1
            u2 = 2 * np.random.rand() - 1
            w = u1 * u1 + u2 * u2
            if w < 1:
                break
        w = math.sqrt((-2.0 * math.log10(w)) / w)
        return mean + (u2 * w) * stdev

    def mutate_problem(self, vector, stdevs):
        aux = [0 for _ in range(4)]
        for i in range(4):
            aux[i] = vector[i] + stdevs[i] * self.rand_gaussian()
            if aux[i] < CitizenS.BOUNDS[i][0]:
                aux[i] = CitizenS.BOUNDS[i][0]
            if aux[i] > CitizenS.BOUNDS[i][1]:
                aux[i] = CitizenS.BOUNDS[i][1]
        return aux

    def mutate_strategy(self, stdevs):
        tau = math.sqrt(2.0 * 4.0) ** -1.0
        tau_p = math.sqrt(2.0 * math.sqrt(4.0)) ** -1.0
        aux = [0 for _ in range(4)]
        for i in range(4):
            aux[i] = stdevs[i] * math.exp(tau_p * self.rand_gaussian() +
                                          tau * self.rand_gaussian())
        return aux

    def mutate(self, parent):
        values = self.mutate_problem(
            parent.get_values(), parent.get_strategy())
        strategy = self.mutate_strategy(parent.get_strategy())
        return CitizenS(values, strategy)

    def init_pop(self):
        return [CitizenS() for _ in range(self.pop_size)]

    def search(self):
        gen = 0
        error = []
        pop = self.init_pop()
        self.fitness_function(gen, pop)
        pop.sort(key=lambda x: x.get_error())
        best = pop[0]
        error.append(best.get_error())
        while gen < self.max_gen:
            children = []
            for i in range(self.num_children):
                children.append(self.mutate(pop[i]))
            self.fitness_function(gen, children)
            union = children + pop
            union.sort(key=lambda x: x.get_error())
            if union[0].get_error() < best.get_error():
                best = union[0]
            error.append(best.get_error())
            pop = union[:self.pop_size]
            print('Gen: {}, Error:{}'.format(
                gen, best.get_error()))
            gen += 1
        return best, error
