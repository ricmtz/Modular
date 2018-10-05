import numpy as np
from utility import rand_bound
from parameters import Parameter as parm


class Citizen(object):

    BOUNDS = parm.get_bounds()
    P_SIZE = 4

    def __init__(self, params=None):
        self.parameters = params if params \
            else [rand_bound(*self.BOUNDS[i]) for i in range(self.P_SIZE)]
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
