from evolutionary import PopulationStrat


class EvolutionStrat(object):

    def __init__(self, max_gen, pop_size, num_children):
        self.max_gen = max_gen
        self.pop_size = pop_size
        self.num_children = num_children
        self.error = []
        self.best = None

    def get_error(self):
        return self.error

    def get_best(self):
        return self.best

    def search(self):
        gen = 0
        self.error.clear()
        pop = PopulationStrat(self.pop_size, self.num_children)
        pop.evaluate()
        pop.sort_pop()
        self.best = pop.get_best()
        self.error.append(self.best.get_error())
        while gen < self.max_gen:
            children = pop.create_children()
            pop.evaluate(children)
            pop.join_pop(children)
            pop.sort_pop()
            if pop.get_best().get_error() < self.best.get_error():
                self.best = pop.get_best()
            self.error.append(self.best.get_error())
            pop.select_pop()
            print('Gen: {}, Error:{}'.format(
                gen, self.best.get_error()))
            gen += 1
