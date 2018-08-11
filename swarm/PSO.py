import Particle as Prt
import util


class PSO:
    def __init__(self, population_quantity, space_boundaries, velocity_boundaries, generations, cost_function):
        best_cost_global = -1
        best_pos_global = []

        population = []
        for i in range(population_quantity):
            population.append(Prt.Particle(space_boundaries, velocity_boundaries))

        gen = 0
        while gen < generations:
            for i in range(population_quantity):
                population[i].evaluate(cost_function)

                if population[i].cost < best_cost_global or best_cost_global == -1:
                    best_pos_global = population[i].position.copy()
                    best_cost_global = population[i].cost

            for i in range(population_quantity):
                population[i].update_velocity(best_pos_global)
                population[i].update_position(space_boundaries)

            util.plot_population(population, space_boundaries, gen+1 >= generations)
            print(f"> Gen={gen+1}, Fitness={best_cost_global}")

            gen += 1
