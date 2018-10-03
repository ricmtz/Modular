from numpy.random import uniform
from parameters import Parameter as parm

class Citizen(object):
    """docstring for Citizen."""

    BOUNDS = [(parm.R_MIN, parm.R_MAX), (parm.L_MIN, parm.L_MAX),
              (parm.J_MIN, parm.J_MAX), (parm.LAM_MIN, parm.LAM_MAX)]

    def __init__(self, params=[]):
        super(Citizen, self).__init__()
        self.parameters = params if params \
        else [uniform(*bound) for bound in self.BOUNDS]
