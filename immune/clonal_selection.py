from models import Algorithm
from immune import PopulationClonal


class ClonalSelection(Algorithm):
    def __init__(self, max_gens, pop_size, clone_factor, num_rand):
        super().__init__()
        self.max_gens = max_gens
        self.pop_size = pop_size
        self.clone_factor = clone_factor
        self.num_rand = num_rand

    def search(self):
        gen = 0
        pop = PopulationClonal(self.pop_size, self.clone_factor, self.num_rand)
        pop.evaluate()
        pop.sort_pop()
        self.best = pop.get_best()
        self.error.append(self.best.get_error())
        for gen in range(self.max_gens):
            clones = pop.clone_and_hypermutate()
            pop.evaluate(clones)
            pop.select_best_pop(clones)
            pop.random_insertion()
            if pop.get_best().get_error() <= self.best.get_error():
                self.best = pop.get_best()
            self.error.append(self.best.get_error())
            print('gen: {},  error: {}'.format(gen, self.best.get_error()))
            gen += 1
