from .candidate import Candidate
from parameters import Function as func


class RandomSearch(object):

    def __init__(self, max_iter):
        self.max_iter = max_iter

    def fitness_func(self, i_time, candidate):
        error = func.calc_error(i_time, candidate.get_R(
        ), candidate.get_L(), candidate.get_J(), candidate.get_LAM())
        candidate.set_error(error)

    def search(self):
        best = None
        gen = 0
        error = []
        while gen <= self.max_iter:
            candidate = Candidate()
            self.fitness_func(gen, candidate)
            if best is None or candidate.get_error() < best.get_error():
                best = candidate
            error.append(best.get_error())
            print('gen:{}, error: {}'.format(gen, best.get_error()))
            gen += 1
        return best, error
