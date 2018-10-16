from models import Population
from immune import Antibody
from utility import rand
from math import exp, floor


class PopulationClonal(Population):
    def __init__(self, pop_size, clone_factor, num_rand):
        super().__init__(pop_size)
        self.c_f = clone_factor
        self.num_rand = num_rand

    def create_pop(self):
        return [Antibody() for _ in range(self.pop_size)]

    def point_mutation(self, bitstring, rate):
        child = []
        for i in range(len(bitstring)):
            bit = bitstring[i]
            child.append(("0" if bit == "1" else "1")
                         if rand() < rate else bit)
        return child

    def calculate_mutation_rate(self, antibody, mutate_factor=-2.5):
        return exp(mutate_factor * antibody.get_affinity())

    def get_num_clones(self):
        return floor(self.pop_size * self.c_f)

    def calculate_affinity(self):
        self.sort_pop()
        ran = self.population[-1].get_error() - self.population[0].get_error()
        if ran == 0.0:
            for p in self.population:
                p.set_affinity(1.0)
        else:
            for p in self.population:
                p.set_affinity(1.0 - (p.get_error() / ran))

    def clone_and_hypermutate(self):
        clones = []
        num_c = self.get_num_clones()
        self.calculate_affinity()
        for antibody in self.population:
            m_rate = self.calculate_mutation_rate(antibody)
            for i in range(num_c):
                clones.append(Antibody(self.point_mutation(
                    antibody.get_bitstrig(), m_rate)))
        return clones

    def select_best_pop(self, pop):
        self.evaluate(pop)
        self.population += pop
        self.sort_pop()
        self.population = self.population[:self.pop_size]

    def random_insertion(self):
        if self.num_rand != 0:
            rands = [Antibody() for _ in range(self.num_rand)]
            self.select_best_pop(rands)
