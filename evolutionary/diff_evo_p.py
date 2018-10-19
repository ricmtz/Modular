from threading import Thread, RLock
from models import Algorithm
from evolutionary import PopulationDif
from random import sample


class DiffEvoParallel(Thread, Algorithm):

    DATA = {}

    def __init__(self, pop_size, max_gen, wf, cr, id_a):
        super(DiffEvoParallel, self).__init__()
        super(Thread, self).__init__()
        super(Algorithm, self).__init__()
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.wf = wf
        self.cr = cr
        self.id_a = id_a
        self.lock = RLock()

    def export_data(self, pop):
        self.lock.acquire()
        try:
            self.DATA[self.id_a] = pop.copy()
        finally:
            self.lock.release()

    def get_data(self):
        pop = []
        self.lock.acquire()
        try:
            for id_a, ctz in self.DATA.items():
                if id_a != self.id_a:
                    pop.extend(ctz)
        finally:
            self.lock.release()
        return pop

    def run(self):
        gen = 0
        pop = PopulationDif(self.pop_size, self.wf, self.cr)
        pop.evaluate()
        pop.sort_pop()
        self.best = pop.get_best()
        while gen < self.max_gen:
            children = pop.create_children()
            self.export_data(children) 
            children.extend(self.get_data())
            children = sample(children, self.pop_size)
            pop.evaluate(children)
            pop.sort_pop(children)
            pop.select_population(children)
            pop.sort_pop()
            if pop.get_best().get_error() < self.best.get_error():
                self.best = pop.get_best()
            self.error.append(self.best.get_error())
            print('id: {}, Gen: {}, Error: {}'.format(
                self.id_a, gen, self.best.get_error()))
            gen += 1
