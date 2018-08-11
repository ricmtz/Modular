import numpy as np
from .Particle import Particle as Prt


class PSO:
    def __init__(self, population_quantity, space_boundaries,
                 velocity_boundaries, generations, cost_function):
        self.population_quantity = population_quantity
        self.space_boundaries = space_boundaries
        self.velocity_boundaries = velocity_boundaries
        self.generations = generations
        self.cost_function = cost_function

    def search(self):
        error = []
        best_cost_global = np.inf
        best_pos_global = []

        population = []
        for i in range(self.population_quantity):
            population.append(
                Prt(self.space_boundaries, self.velocity_boundaries))

        gen = 0
        while gen < self.generations:
            for i in range(self.population_quantity):
                population[i].evaluate(gen, self.cost_function)

                if population[i].cost < best_cost_global or best_cost_global == np.inf:
                    best_pos_global = population[i].position.copy()
                    best_cost_global = population[i].cost
                error.append(best_cost_global)
            for i in range(self.population_quantity):
                population[i].update_velocity(best_pos_global)
                population[i].update_position(self.space_boundaries)

            print(f"> Gen={gen+1}, Fitness={best_cost_global}")
            gen += 1

        return best_pos_global, error
