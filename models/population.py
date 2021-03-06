from parameters import Function as func


class Population:
    def __init__(self, pop_size):
        self.pop_size = pop_size
        self.population = self.create_pop()

    def create_pop(self):
        raise NotImplementedError

    def make_crossover(self):
        raise NotImplementedError

    def fitness_function(self, r, l, j, lam):
        return func.calc_error(r, l, j, lam)

    def evaluate(self, pop=None):
        for citizen in pop if pop else self.population:
            citizen.set_error(self.fitness_function(*citizen.get_values()))

    def sort_pop(self, pop=None):
        if pop:
            pop.sort(key=lambda x: x.get_error())
        else:
            self.population.sort(key=lambda x: x.get_error())

    def get_best(self):
        return min(self.population, key=lambda x: x.get_error())

    def get_worst(self):
        return max(self.population, key=lambda x: x.get_error())
