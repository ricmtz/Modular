from models import Algorithm, Citizen
from parameters import Function as func
from utility import randint_bound


class HillClimbing(Algorithm):
    def __init__(self, max_gen):
        super().__init__()
        self.max_gen = max_gen

    def evaluate(self, candidate):
        error = func.calc_error(*candidate.get_values())
        candidate.set_error(error)

    def random_neighbor(self, params=[]):
        mutant = Citizen(params)
        pos = randint_bound(Citizen.P_SIZE)
        mutant.set_value(pos)
        return mutant

    def search(self):
        gen = 0
        candidate = Citizen()
        self.evaluate(candidate)
        while gen < self.max_gen:
            neighbor = self.random_neighbor(candidate.get_values())
            self.evaluate(neighbor)
            if neighbor.get_error() <= candidate.get_error():
                candidate = neighbor
            self.best = candidate
            self.error.append(candidate.get_error())
            print('iteration: {}, error: {}'.format(gen,
                                                    candidate.get_error()))
            gen += 1
