from models import Algorithm
from probabilistic import PopulationCross


class CrossEntropy(Algorithm):

    def __init__(self, max_iter, num_samples, num_uptade, l_r):
        super().__init__()
        self.max_iter = max_iter
        self.num_samples = num_samples
        self.num_uptade = num_uptade
        self.l_r = l_r

    def search(self):
        for i in range(self.max_iter):
            samples = PopulationCross(
                self.num_samples, self.num_uptade, self.l_r)
            samples.evaluate()
            samples.sort_pop()
            if self.best is None or \
                    samples.get_best().get_error() < self.best.get_error():
                self.best = samples.get_best()
            self.error.append(self.best.get_error())
            samples.update_distribution()
            print('Gen:{}, Error:{}'.format(i, self.best.get_error()))
