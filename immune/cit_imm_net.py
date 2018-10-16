from models import Citizen


class CitizenImmuneNetwork(Citizen):
    def __init__(self, params=None):
        super().__init__(params)

    def mutate(beta, norm_err):
        for index, param in enumerate(self.parameters):
            alpha = self.mutation_rate(beta, norm_err)
            self.parameters[index] = param + alpha + rand_gaussian()

    def mutation_rate(beta, norm_err):
        return (1.0/beta) * exp(-normalized_cost)
