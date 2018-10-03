from parameters import Function as func


class Population:
    def __init__(self, pop_size):
        self.population = self.create_pop(pop_size)

    def create_pop(self, pop_size):
        pass

    def cross(self):
        pass

    def fitness_function(self, r, l, j, lam):
        return func.calc_error(r, l, j, lam)

    def evaluate(self, arg):
        for citizen in self.population:
            citizen.set_error(self.fitness_function(*citizen.get_values()))
