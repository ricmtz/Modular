from utility import rand_bound
from models import Citizen


class CitizenStrat(Citizen):

    def __init__(self, params=None, strategy=None):
        super().__init__(params)
        self.strategy = strategy if strategy else [rand_bound(
            0, (self.BOUNDS[i][1] - CitizenStrat.BOUNDS[i][0]) * 0.05)
            for i in range(self.P_SIZE)]

    def set_strategy(self, strategy):
        self.strategy = strategy[:]

    def get_strategy(self):
        return self.strategy
