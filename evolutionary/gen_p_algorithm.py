from evolutionary import GeneticParallel
from models import AlgorithmP


class GenParallelAlgorithm(AlgorithmP):
    def __init__(self, pop_size, best_p, max_gen, p_m, num_threads=3):
        super().__init__()
        self.pop_size = pop_size
        self.best_p = best_p
        self.max_gen = max_gen
        self.p_m = p_m
        self.num_threads = num_threads

    def search(self):
        for i in range(self.num_threads):
            t = GeneticParallel(self.pop_size, self.best_p,
                                self.max_gen, self.p_m, i)
            t.start()
            self.threads.append(t)
        for t in self.threads:
            t.join()
