from models import Algorithm
from models import Population
import PopulationImmuneNetwork as PIN

class ImmuneNetwork(Algorithm):
    def __init__(self, pop_size, max_gen, beta=100, num_clones=10, ):
        super().__init__()
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.beta = beta

    def search(self):
        gen = 0

        pop = PIN.PopulationImmuneNetwork(self.pop_size)
        pop.evaluate()

        while gen < self.max_gen:
            pop.evaluate()
            pop.calculate_normalized_cost()
            pop.sort_pop()

            if self.best is None or pop.get_best().get_error() < self.best.get_error():
                self.best = pop.get_best()

            progeny = None
            avg_err = pop.get_average_error()

            while True:
                progeny = [clone_cell(beta, num_clones, pop[i]) for i in range(len(pop))]
                if average_cost(progeny) < avgCost:
                    break
            pop = affinity_supress(progeny, aff_thresh)
            [pop.append({"vector": random_vector(search_space)}) for i in range(num_rand)]
            print(f" > gen #{gen+1}, popSize=#{len(pop)}, fitness=#{best['cost']}")
            gen += 1
        return best
