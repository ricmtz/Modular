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

    def get_error(self):
        return self.error

    def set_error(self, error):
        self.error = error

    @staticmethod
    def create_citizen(params):
        return Citizen(params)
