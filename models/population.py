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

    def evaluate(self):
        for citizen in self.population:
            citizen.set_error(self.fitness_function(*citizen.get_values()))

    def sort_pop(self):
        self.population.sort(key=lambda x: x.get_error())

    def get_best(self):
        return self.population[0]
