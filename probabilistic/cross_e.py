import math
import numpy as np
from .means import Means
from parameters import Function as func
from parameters import Parameter as parm

BOUNDS = [(parm.R_MIN, parm.R_MAX), (parm.L_MIN, parm.L_MAX),
          (parm.J_MIN, parm.J_MAX), (parm.LAM_MIN, parm.LAM_MAX)]


class CrossE(object):

    def __init__(self, max_iter, num_samples, num_uptade, l_r):
        self.max_iter = max_iter
        self.num_samples = num_samples
        self.num_uptade = num_uptade
        self.l_r = l_r
        self._means = [parm.get_rand(BOUNDS[i]) for i in range(4)]
        self._stdevs = [BOUNDS[i][1] - BOUNDS[i][0] for i in range(4)]

    def fitness_function(self, i_time, pop):
        for i in pop:
            error = func.calc_error(
                i_time, i.get_R(), i.get_L(),
                i.get_J(), i.get_LAM())
            i.set_error(error)

    def generate_sample(self):
        aux = [0 for _ in range(4)]
        for i in range(4):
            aux[i] = np.random.normal(self._means[i], self._stdevs[i])
            if (aux[i] < BOUNDS[i][0]):
                aux[i] = BOUNDS[i][0]
            if (aux[i] > BOUNDS[i][1]):
                aux[i] = BOUNDS[i][1]
        return Means(aux)

    def mean_attr(self, samples, i):
        res = 0
        for s in samples:
            res += s.get(i)
        return (res / float(self.num_samples))

    def stdev_attr(self, samples, mean, i):
        res = 0
        for s in samples:
            res += ((s.get(i) - mean) ** 2.0)
        return math.sqrt(res/float(self.num_samples))

    def update_distribution(self, samples):
        for i in range(4):
            self._means[i] = (self.l_r * self._means[i] +
                              ((1.0 - self.l_r) * self.mean_attr(samples, i)))
            self._stdevs[i] = (self.l_r * self._stdevs[i] +
                               ((1.0 - self.l_r) * self.stdev_attr(samples, self._means[i], i)))

    def search(self):
        best = None
        error = []
        for i in range(self.max_iter):
            samples = [self.generate_sample()
                       for _ in range(self.num_samples)]
            self.fitness_function(i, samples)
            samples.sort(key=lambda x: x.get_error())
            if best is None or samples[0].get_error() < best.get_error():
                best = samples[0]
            error.append(best.get_error())
            selected = samples[:self.num_uptade]
            self.update_distribution(selected)
            print('Gen:{}, Error:{}'.format(i, best.get_error()))
        return best, error
