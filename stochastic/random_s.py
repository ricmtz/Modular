from models import Citizen
from models import Algorithm
from parameters import Function as func


class RandomSearch(Algorithm):

    def __init__(self, max_iter):
        super().__init__()
        self.max_iter = max_iter

    def evaluate(self, candidate):
        error = func.calc_error(*candidate.get_values())
        candidate.set_error(error)

    def search(self):
        gen = 0
        while gen <= self.max_iter:
            candidate = Citizen()
            self.evaluate(candidate)
            if self.best is None or \
                    candidate.get_error() < self.best.get_error():
                self.best = candidate
            self.error.append(self.best.get_error())
            print('gen:{}, error: {}'.format(gen, self.best.get_error()))
            gen += 1
