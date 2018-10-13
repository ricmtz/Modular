from models import Citizen
import random
import numpy as np
from utility import rand_bound


class Particle(Citizen):

    VEL_BOUNDS = [(-1, 1)] * 4
    C1 = 1.0
    C2 = 2.0
    W = 0.5

    def __init__(self):
        super().__init__()
        self.velocity = [rand_bound(self.VEL_BOUNDS[i][0],
                                    self.VEL_BOUNDS[i][1])
                         for i in range(self.P_SIZE)]
        self.best_cost = self.error
        self.best_pos = self.parameters.copy()

    def set_error(self, error):
        self.error = error
        if self.error < self.best_cost or self.best_cost == np.inf:
            self.best_pos = self.parameters.copy()
            self.best_cost = self.error

    def update_velocity(self, best_global_pos):
        for i in range(len(best_global_pos)):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = self.C1 * r1 * \
                (self.best_pos[i] - self.parameters[i])
            vel_social = self.C2 * r2 * \
                (best_global_pos[i] - self.parameters[i])
            self.velocity[i] = self.W * self.velocity[i] + \
                vel_cognitive + vel_social

    def update_position(self):
        for i in range(self.P_SIZE):
            self.set_value(i, (self.parameters[i] + self.velocity[i]))
