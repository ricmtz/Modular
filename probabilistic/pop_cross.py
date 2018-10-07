import math

from models import Citizen, Population
from utility import rand_bound


class PopulationCross(Population):
    def __init__(self, pop_size, num_uptade, l_r):
        super().__init__(pop_size)
        self.num_uptade = num_uptade
        self.l_r = l_r
        self.means = self.create_means()
        self.stdevs = self.create_stdevs()

    def create_pop(self):
        return [Citizen() for _ in range(self.pop_size)]

    def create_means(self):
        return [rand_bound(*Citizen.BOUNDS[i]) for i in range(Citizen.P_SIZE)]

    def create_stdevs(self):
        return [Citizen.BOUNDS[i][1] - Citizen.BOUNDS[i][0]
                for i in range(Citizen.P_SIZE)]

    def generate_sample(self):
        sample = Citizen()
        for i in range(Citizen.P_SIZE):
            aux = rand_bound(self.means[i], self.stdevs[i])
            sample.set_value(i, aux)
        return sample

    def mean_attr(self, samples, i):
        res = 0
        for s in samples:
            res += s.get_value(i)
        return (res / float(self.pop_size))

    def stdev_attr(self, samples, mean, i):
        res = 0
        for s in samples:
            res += ((s.get_value(i) - mean) ** 2.0)
        return math.sqrt(res/float(self.pop_size))

    def update_distribution(self):
        samples = self.select_pop()
        for i in range(Citizen.P_SIZE):
            self.means[i] = (self.l_r * self.means[i] +
                             ((1.0 - self.l_r) * self.mean_attr(samples, i)))
            self.stdevs[i] = (self.l_r * self.stdevs[i] +
                              ((1.0 - self.l_r) *
                               self.stdev_attr(samples, self.means[i], i)))

    def select_pop(self):
        return self.population[:self.num_uptade]
