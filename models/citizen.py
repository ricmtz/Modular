import numpy as np
from utility import rand_bound
from parameters import Parameter as parm


class Citizen(object):

    BOUNDS = parm.get_bounds()

    def __init__(self, params=[]):
        self.parameters = params if params \
            else [rand_bound(*bound) for bound in self.BOUNDS]
        self.error = np.inf

    def get_values(self):
        return self.parameters

    def set_value(self, param, value=None):
        if value:
            if value < self.BOUNDS[param][0]:
                value = self.BOUNDS[param][0]
            if value > self.BOUNDS[param][1]:
                value = self.BOUNDS[param][1]
            self.parameters[param] = value
        else:
            self.parameters[param] = rand_bound(*self.BOUNDS[param])

    def get_error(self):
        return self.error

    def set_error(self, error):
        self.error = error

    @staticmethod
    def create_citizen(params):
        return Citizen(params)
