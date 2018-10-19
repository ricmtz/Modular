from models import Parallel
from evolutionary import PopulationDif
from random import sample


class DiffEvoParallel(Parallel):

    def __init__(self, pop_size, max_gen, wf, cr, id_a):
        super().__init__(id_a)
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.wf = wf
        self.cr = cr

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
