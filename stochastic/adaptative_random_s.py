import numpy as np
from models import Algorithm, Citizen
from parameters import Function as func
from parameters import Parameter as parm
from utility import rand_bound


class AdaptativeRandomS(Algorithm):
    def __init__(self, max_gen, init_fac, s_factor, l_factor, iter_mult,
                 max_no_impr):
        super().__init__()
        self.max_gen = max_gen
        self.init_fac = init_fac
        self.s_factor = s_factor
        self.l_factor = l_factor
        self.iter_mult = iter_mult
        self.max_no_impr = max_no_impr
        self.bounds = parm.get_bounds()

    def evaluate(self, candidate):
        error = func.calc_error(*candidate.get_values())
        candidate.set_error(error)

    def take_step(self, current, step_size):
        position = Citizen()
        for i in range(Citizen.P_SIZE):
            minimum = min([self.bounds[i][0],
                           current.get_value(i) - step_size[i]])
            maximum = max([self.bounds[i][1],
                           current.get_value(i) + step_size[i]])
            value = rand_bound(minimum, maximum)
            position.set_value(i, value)
        return position

    def large_step_size(self, gen, step_size):
        if (gen > 0) and (gen % self.iter_mult == 0):
            result = step_size * self.l_factor
        else:
            result = step_size * self.s_factor
        return result

    def take_steps(self, current, step_size, big_stepsize):
        step = self.take_step(current, step_size)
        self.evaluate(step)
        big_step = self.take_step(current, big_stepsize)
        self.evaluate(big_step)
        return step, big_step

    def search(self):
        step_size = np.array([(self.bounds[i][1] - self.bounds[i][0])
                              * self.init_fac for i in range(Citizen.P_SIZE)])
        current = Citizen()
        self.evaluate(current)
        count = 0
        gen = 0
        while gen < self.max_gen:
            big_stepsize = self.large_step_size(gen, step_size)
            step, big_step = self.take_steps(current, step_size, big_stepsize)
            if step.get_error() <= current.get_error() or \
                    big_step.get_error() <= current.get_error():
                if big_step.get_error() <= step.get_error():
                    step_size, current = big_stepsize, big_step
                else:
                    current = step
                count = 0
            else:
                count += 1
                if count >= self.max_no_impr:
                    count = 0
                    step_size = (step_size/self.s_factor)
            self.best = current
            self.error.append(current.get_error())
            print("iteration:{}, error:{}".format(gen, current.get_error()))
            gen += 1
