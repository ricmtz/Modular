from models import Population
from swarm import Particle


class Particles(Population):
    def __init__(self, pop_size):
        super().__init__(pop_size)

    def create_pop(self):
        return [Particle() for i in range(self.pop_size)]

    def get_best_pos_global(self):
        self.sort_pop()
        return self.population[0].get_values().copy()

    def update_particles(self, best_pos_global):
        for p in self.population:
            p.update_velocity(best_pos_global)
            p.update_position()
