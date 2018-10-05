import math
from evolutionary import CitizenStrat
from models import Population
from utility import rand_gaussian


class PopulationStrat(Population):

    def __init__(self, pop_size, num_children):
        super().__init__(pop_size)
        self.num_children = num_children

    def create_pop(self):
        return [CitizenStrat() for _ in range(self.pop_size)]

    def mutate_problem(self, vector, stdevs):
        aux = [0 for _ in range(CitizenStrat.P_SIZE)]
        for i in range(CitizenStrat.P_SIZE):
            aux[i] = vector[i] + stdevs[i] * self.rand_gaussian()
            if aux[i] < CitizenStrat.BOUNDS[i][0]:
                aux[i] = CitizenStrat.BOUNDS[i][0]
            if aux[i] > CitizenStrat.BOUNDS[i][1]:
                aux[i] = CitizenStrat.BOUNDS[i][1]
        return aux

    def mutate_strategy(self, stdevs):
        tau = math.sqrt(2.0 * float(CitizenStrat.P_SIZE)) ** -1.0
        tau_p = math.sqrt(2.0 * math.sqrt(float(CitizenStrat.P_SIZE))) ** -1.0
        aux = [0 for _ in range(CitizenStrat.P_SIZE)]
        for i in range(CitizenStrat.P_SIZE):
            aux[i] = stdevs[i] * math.exp(tau_p * rand_gaussian() +
                                          tau * rand_gaussian())
        return aux

    def mutate(self, parent):
        params = self.mutate_problem(
            parent.get_values(), parent.get_strategy())
        strategy = self.mutate_strategy(parent.get_strategy())
        return CitizenStrat(params, strategy)
