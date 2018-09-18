from parameters.Functions import calc_error

class Population(object):
    """docstring for Population."""
    def __init__(self, pop_size):
        super(Population, self).__init__()
        self.population = self.create_pop(pop_size)

    def create_pop(self, pop_size):
        pass

    def cross(self):
        pass

    def fitness_function(self, r, l, j, lam):
        calc_error(r, l, j, lam)
        pass

    def evaluate(self, arg):
        for citizen in self.population:
            citizen.set_error(self.fitness_function(citizen.get_params()))
