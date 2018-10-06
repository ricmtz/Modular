import numpy as np
from parameters import Parameter as parm


class Harmony(object):
    BOUNDS = [parm.get_bounds()]

    def __init__(self, values=None):
        if values:
            self._values = values[:]
        else:
            self._values = [parm.get_rand(Harmony.BOUNDS[i]) for i in range(4)]
        self._error = np.inf

    def set_R(self, r):
        self._values[0] = r

    def get_R(self):
        return self._values[0]

    def set_L(self, l):
        self._values[1] = l

    def get_L(self):
        return self._values[1]

    def set_J(self, j):
        self._values[2] = j

    def get_J(self):
        return self._values[2]

    def set_LAM(self, lam):
        self._values[3] = lam

    def get_LAM(self):
        return self._values[3]

    def set_error(self, error):
        self._error = error

    def get_error(self):
        return self._error

    def set_values(self, values):
        self._values = values[:]

    def get_values(self):
        return self._values
