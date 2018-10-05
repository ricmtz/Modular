from evolutionary import PopulationGen


class Genetic(object):

    def __init__(self, pop_size, best_p, max_gen, p_m):
        self.pop_size = pop_size
        self.best_p = best_p
        self.max_gen = max_gen
        self.p_m = p_m
        self.best = None
        self.error = []

    def get_error(self):
        return self.error

    def get_best(self):
        return self.best

    def search(self):
        gen = 0
        self.error.clear()
        pop = PopulationGen(self.pop_size, self.best_p, self.p_m)
        pop.evaluate()
        pop.sort_pop()
        self.best = pop.get_best()
        self.error.append(self.best.get_error())
        while gen < self.max_gen:
            pop.make_crossover()
            pop.evaluate()
            pop.sort_pop()
            self.best = pop.get_best()
            self.error.append(self.best.get_error())
            print('Gen: {}, Error: {}'.format(gen, self.best.get_error()))
            gen += 1
