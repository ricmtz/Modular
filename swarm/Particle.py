import random
import util

C1 = 1.0
C2 = 2.0
W = 0.5


class Particle:
    def __init__(self, space_bounds, vel_bounds):
        self.position = []
        self.velocity = []
        self.cost = -1
        self.best_cost = self.cost

        for i in range(len(space_bounds)):
            self.position.append(util.rand_val(space_bounds[i][0], space_bounds[i][1]))
            self.velocity.append(util.rand_val(vel_bounds[i][0], vel_bounds[i][1]))

        self.best_pos = self.position.copy()

    def evaluate(self, cost_func):
        self.cost = cost_func(self.position)

        if self.cost < self.best_cost or self.best_cost == -1:
            self.best_pos = self.position.copy()
            self.best_cost = self.cost

    def update_velocity(self, best_global_pos):
        for i in range(len(best_global_pos)):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = C1 * r1 * (self.best_pos[i] - self.position[i])
            vel_social = C2 * r2 * (best_global_pos[i] - self.position[i])
            self.velocity[i] = W * self.velocity[i] + vel_cognitive + vel_social

    def update_position(self, space_bounds):
        for i in range(len(space_bounds)):
            self.position[i] = self.position[i] + self.velocity[i]

            if self.position[i] > space_bounds[i][1]:
                self.position[i] = space_bounds[i][1]

            if self.position[i] < space_bounds[i][0]:
                self.position[i] = space_bounds[i][0]
