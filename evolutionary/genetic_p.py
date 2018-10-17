from threading import Thread, RLock
from models import Algorithm
from evolutionary import PopulationGen


class GeneticParallel(Thread, Algorithm):

    BEST_CITIZENS = {}

    def __init__(self, pop_size, best_p, max_gen, p_m, id_a):
        super(GeneticParallel, self).__init__()
        super(Thread, self).__init__()
        super(Algorithm, self).__init__()
        self.pop_size = pop_size
        self.best_p = best_p
        self.max_gen = max_gen
        self.p_m = p_m
        self.id_a = id_a
        self.lock = RLock()

    def export_best_citizens(self, pop):
        self.lock.acquire()
        try:
            self.BEST_CITIZENS[self.id_a] = pop
        finally:
            self.lock.release()

    def get_best_citizens(self):
        pop = []
        self.lock.acquire()
        try:
            for id_a, ctz in self.BEST_CITIZENS.items():
                if id_a != self.id_a:
                    pop.extend(ctz)
            self.BEST_CITIZENS[self.id_a]
        finally:
            self.lock.release()
        return pop

    def run(self):
        gen = 0
        pop = PopulationGen(self.pop_size, self.best_p, self.p_m)
        pop.evaluate()
        pop.sort_pop()
        self.best = pop.get_best()
        self.error.append(self.best.get_error())
        self.export_best_citizens(pop.get_best_pop())
        while gen < self.max_gen:
            best_pop = self.get_best_citizens()
            pop.make_crossover(best_pop)
            pop.evaluate()
            pop.sort_pop()
            self.best = pop.get_best()
            self.error.append(self.best.get_error())
            self.export_best_citizens(pop.get_best_pop())
            print('id: {}, Gen: {}, Error: {}'.format(
                self.id_a, gen, self.best.get_error()))
            gen += 1
