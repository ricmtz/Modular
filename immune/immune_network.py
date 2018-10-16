from models import Algorithm
from immune import PopulationImmuneNet


class ImmuneNetwork(Algorithm):
    def __init__(self, max_gen, pop_size, num_clones, beta, num_rand):
        super().__init__()
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.num_clones = num_clones
        self.beta = beta
        self.num_rand = num_rand

    def search(self):
        gen = 0
        pop = PopulationImmuneNet(
            self.pop_size, self.num_clones, self.beta, self.num_rand)
        while gen < self.max_gen:
            pop.evaluate()
            pop.calculate_normalized_error()
            pop.sort_pop()
            if self.best is None or \
                    pop.get_best().get_error() < self.best.get_error():
                self.best = pop.get_best()
            self.error.append(self.best.get_error())
            progeny = None
            avg_err = pop.average_error()
            while True:
                progeny = pop.get_progeny()
                if pop.average_error(progeny) < avg_err:
                    break
            pop.affinity_supress(progeny)
            pop.add_rand_pop()
            print('gen: {}, error:{}'.format(gen, self.best.get_error()))
            gen += 1
