from models import Parallel
from evolutionary import PopulationGen


class GeneticParallel(Parallel):

    def __init__(self, pop_size, best_p, max_gen, p_m, id_a):
        super().__init__(id_a)
        self.pop_size = pop_size
        self.best_p = best_p
        self.max_gen = max_gen
        self.p_m = p_m

    def run(self):
        gen = 0
        pop = PopulationGen(self.pop_size, self.best_p, self.p_m)
        pop.evaluate()
        pop.sort_pop()
        self.best = pop.get_best()
        self.error.append(self.best.get_error())
        self.export_data(pop.get_best_pop())
        while gen < self.max_gen:
            best_pop = self.get_data()
            pop.make_crossover(best_pop)
            pop.evaluate()
            pop.sort_pop()
            self.best = pop.get_best()
            self.error.append(self.best.get_error())
            self.export_data(pop.get_best_pop())
            print('id: {}, Gen: {}, Error: {}'.format(
                self.id_a, gen, self.best.get_error()))
            gen += 1
