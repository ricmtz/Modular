from models import Population
import CitizenImmuneNetwork as CTN

class PopulationImmuneNetwork(Population):
    def __init__(self, pop_size):
        super().__init__(pop_size)

    def create_pop(self):
        return [CTN.CitizenImmuneNetwork() for i in range(self.pop_size)]

    def get_worst(self):
        return self.population[-1]

    def calculate_normalized_error(self):
        self.sort_pop()
        diff = self.get_best().get_error() - self.get_worst().get_error()
        self.set_normalized_errors(diff)

    def set_normalized_errors(diff):
        if diff == 0.0:
            for citizen in self.population:
                citizen.set_normalized_error(1.0)
        else:
            for citizen in self.population:
                citizen.set_normalized_error(1.0 - (citizen.get_error() / diff))

    def get_average_error():
        sum = 0.0
        for citizen in self.population:
            sum += citizen.get_error()
        return sum / float(len(self.population))

    def clone_cells(beta, num_clones):
        cloned_pop = []
        for cell_index in range(len(self.population)):
            cloned_pop.append(self.clone_cell(beta, num_clones, self.population[cell_index]))

    def clone_cell(beta, num_clones, parent):
        return CTN.CitizenImmuneNetwork(parent.parameters)

    def mutate_cells(pop, beta, norm_err):
        for cell in pop:
            cell.mutate(beta, norm_err)
