import numpy as np
from parameters import Parameter as parm


class CitizenS(object):

    BOUNDS = [(parm.R_MIN, parm.R_MAX), (parm.L_MIN, parm.L_MAX),
              (parm.J_MIN, parm.J_MAX), (parm.LAM_MIN, parm.LAM_MAX)]

    def __init__(self, values=None, strategy=None):
        if values:
            self._values = values[:]
        else:
            self._values = [parm.get_rand(CitizenS.BOUNDS[i])
                            for i in range(4)]
        if strategy:
            self._strategy = strategy[:]
        else:
            self._strategy = [np.random.uniform(
                0, (CitizenS.BOUNDS[i][1] - CitizenS.BOUNDS[i][0]) * 0.05)
                for i in range(4)]
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

    def set_strategy(self, strategy):
        self._strategy = strategy[:]

    def get_strategy(self):
        return self._strategy
