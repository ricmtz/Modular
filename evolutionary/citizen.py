from parameters import Parameter as parm


class Citizen(object):

    def __init__(self):
        self._r = parm.get_rand_R()
        self._l = parm.get_rand_L()
        self._j = parm.get_rand_J()
        self._lam = parm.get_rand_LAM()

    def set_R(self, r):
        self._r = r

    def set_L(self, l):
        self._l = l

    def set_J(self, j):
        self._j = j

    def set_LAM(self, lam):
        self._lam = lam

    @staticmethod
    def cross(c1, c2):
        pass
