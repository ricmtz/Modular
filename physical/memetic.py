import numpy as np
from parameters import Function as func
from .cictizen_m import CitizenM


class Memetic(object):
    def __init__(self, max_gens, search_space, pop_size, p_cross, p_mut,
                 max_local_gens, p_local, bits_per_param=16):
        self.max_gens = max_gens
        self.bounds = search_space
        self.pop_size = pop_size
        self.p_cross = p_cross
        self.p_mut = p_mut
        self.max_local_gens = max_local_gens
        self.p_local = p_local
        self.bits_per_param = bits_per_param

    def fitness_function(self, i_time, citizen):
        error = func.calc_error(i_time, *citizen.get_values())
        citizen.set_error(error)

    def binary_tournament(self, pop):
        i, j = np.random.randint(len(pop)), np.random.randint(len(pop))
        while j == i:
            j = np.random.randint(len(pop))
        return pop[i] if pop[i].get_error() < pop[j].get_error() else pop[j]

    def point_mutation(self, bitstring, rate):
        if not rate:
            rate = 1.0/len(bitstring)
        child = []
        for i in range(len(bitstring)):
            bit = bitstring[i]
            child.append(("0" if bit == "1" else "1")
                         if np.random.rand() < rate else bit)
        return child

    def crossover(self, parent1, parent2, rate):
        if np.random.rand() >= rate:
            return parent1
        child = []
        for i in range(len(parent1)):
            child.append(parent1[i] if np.random.rand() < 0.5 else parent2[i])
        return child

    def reproduce(self, selected):
        children = []
        for i, p1 in enumerate(selected):
            p2 = selected[i+1] if ((i % 2) == 0) else selected[i-1]
            p2 = selected[0] if i == len(selected)-1 else p2
            child = self.crossover(
                p1.get_bitstring(), p2.get_bitstring(), self.p_cross)
            child = self.point_mutation(child, self.p_mut)
            children.append(CitizenM(child))
            if len(children) >= self.pop_size:
                break
        return children

    def bitclimber(self, child, i_time):
        current = child
        for i in range(self.max_local_gens):
            candidate = CitizenM(self.point_mutation(
                current.get_bitstring(), self.p_mut))
            self.fitness_function(i_time, candidate)
            current = candidate if (
                candidate.get_error() <= current.get_error()) else current
        return current

    def search(self):
        error = []
        pop = [CitizenM() for _ in range(self.pop_size)]
        for candidate in pop:
            self.fitness_function(0, candidate)
        best = sorted(pop, key=lambda x: x.get_error())[0]
        for gen in range(self.max_gens):
            selected = [self.binary_tournament(
                pop) for i in range(self.pop_size)]
            children = self.reproduce(selected)
            for cand in children:
                self.fitness_function(gen, cand)
            pop = []
            for child in children:
                if np.random.rand() < self.p_local:
                    child = self.bitclimber(child, gen)
                pop.append(child)
            pop.sort(key=lambda x: x.get_error())
            best = pop[0] if pop[0].get_error() <= best.get_error() else best
            error.append(best.get_error())
            print(f"gen={gen}, f={best.get_error()}, b={best.get_bitstring()}")
        return best, error
