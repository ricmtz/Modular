from models import Population
from physical import CitizenMem
from utility import rand, choice


class PopulationMem(Population):
    def __init__(self, pop_size, p_cross, p_mut, max_local_gens,
                 p_local, bits_per_param=16):
        super().__init__(pop_size)
        self.p_cross = p_cross
        self.p_mut = p_mut
        self.max_local_gens = max_local_gens
        self.p_local = p_local
        self.bits_per_param = bits_per_param

    def create_pop(self):
        return [CitizenMem() for _ in range(self.pop_size)]

    def binary_tournament(self):
        i, j = choice(self.pop_size, 2)
        return self.population[i] if self.population[i].get_error() < \
            self.population[j].get_error() else self.population[j]

    def point_mutation(self, bitstring):
        child = []
        for i in range(len(bitstring)):
            bit = bitstring[i]
            child.append(("0" if bit == "1" else "1")
                         if rand() < self.p_mut else bit)
        return child

    def crossover(self, parent1, parent2):
        if rand() >= self.p_cross:
            return parent1
        child = []
        for i in range(len(parent1)):
            child.append(parent1[i] if rand() < 0.5 else parent2[i])
        return child

    def reproduce(self, selected):
        children = []
        for i, p1 in enumerate(selected):
            p2 = selected[i+1] if ((i % 2) == 0) else selected[i-1]
            p2 = selected[0] if i == len(selected)-1 else p2
            child = self.crossover(
                p1.get_bitstring(), p2.get_bitstring())
            child = self.point_mutation(child)
            children.append(CitizenMem(bitstring=child))
            if len(children) >= self.pop_size:
                break
        return children

    def bitclimber(self, child):
        current = child
        for i in range(self.max_local_gens):
            candidate = CitizenMem(
                bitstring=self.point_mutation(current.get_bitstring()))
            candidate.set_error(self.fitness_function(*candidate.get_values()))
            current = candidate if (
                candidate.get_error() <= current.get_error()) else current
        return current

    def replace_pop(self, pop):
        self.population.clear()
        for child in pop:
            if rand() < self.p_local:
                child = self.bitclimber(child)
            self.population.append(child)
