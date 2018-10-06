from physical import PopulationMem
from models import Algorithm


class Memetic(Algorithm):
    def __init__(self, max_gens, pop_size, p_cross, p_mut,
                 max_local_gens, p_local, bits_per_param=16):
        super().__init__()
        self.max_gens = max_gens
        self.pop_size = pop_size
        self.p_cross = p_cross
        self.p_mut = p_mut
        self.max_local_gens = max_local_gens
        self.p_local = p_local
        self.bits_per_param = bits_per_param

    def search(self):
        pop = PopulationMem(self.pop_size, self.p_cross,
                            self.p_mut, self.max_local_gens, self.p_local)
        pop.evaluate()
        pop.sort_pop()
        self.best = pop.get_best()
        for gen in range(self.max_gens):
            selected = [pop.binary_tournament() for i in range(self.pop_size)]
            children = pop.reproduce(selected)
            children = pop.reproduce(selected)
            pop.evaluate(children)
            pop.replace_pop(children)
            pop.sort_pop()
            self.best = pop.get_best() if pop.get_best().get_error() \
                <= self.best.get_error() else self.best
            self.error.append(self.best.get_error())
            print('gen={}, error={}'.format(gen, self.best.get_error()))
