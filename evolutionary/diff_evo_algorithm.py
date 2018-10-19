from evolutionary import DiffEvoParallel
from models import AlgorithmP


class DiffEvoAlgorithm(AlgorithmP):
    def __init__(self, pop_size, max_gen, wf, cr, num_threads=3):
        super().__init__()
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.wf = wf
        self.cr = cr
        self.num_threads = num_threads

    def search(self):
        for i in range(self.num_threads):
            t = DiffEvoParallel(self.pop_size, self.max_gen,
                                self.wf, self.cr, i)
            t.start()
            self.threads.append(t)
        for t in self.threads:
            t.join()
