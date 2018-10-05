from models import Algorithm
from evolutionary import PopulationDif


class DiffEvolution(Algorithm):

    def __init__(self, max_gen, pop_size, wf, cr):
        super().__init__()
        self.max_gen = max_gen
        self.pop_size = pop_size
        self.wf = wf
        self.cr = cr

    def search(self):
        self.error.clear()
        gen = 0
        pop = PopulationDif(self.pop_size, self.wf, self.cr)
        pop.evaluate()
        pop.sort_pop()
        self.best = pop.get_best()
        while gen < self.max_gen:
            children = pop.create_children()
            pop.evaluate(children)
            pop.sort_pop(children)
            pop.select_population(children)
            pop.sort_pop()
            if pop.get_best().get_error() < self.best.get_error():
                self.best = pop.get_best()
            self.error.append(self.best.get_error())
            print('Gen: {}, fitness: {}'.format(gen, self.best.get_error()))
            gen += 1
