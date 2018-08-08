import numpy as np
from .harmony import Harmony
from parameters import Function as func
from parameters import Parameter as parm


class HarmonyA(object):

    def __init__(self, max_iter, mem_size, consid_r, adjust_r, ran):
        self.max_iter = max_iter
        self.mem_size = mem_size
        self.consid_r = consid_r
        self.adjust_r = adjust_r
        self.ran = ran

    def fitness_function(self, i_time, solution):
        error = func.calc_error(i_time, *solution.get_values())
        solution.set_error(error)

    def create_rand_harmony(self):
        harm = Harmony()
        self.fitness_function(0, harm)
        return harm

    def initialize_harmony_memory(self, factor=3):
        memory = [self.create_rand_harmony()
                  for _ in range(self.mem_size * factor)]
        memory.sort(key=lambda x: x.get_error())
        return memory[:self.mem_size]

    def create_harmony(self, memory):
        vector = [0 for _ in range(4)]
        for i in range(4):
            if np.random.rand() < self.consid_r:
                value = memory[np.random.randint(
                    self.mem_size)].get_values()[i]
                if np.random.rand() < self.adjust_r:
                    value = value + self.ran * np.random.uniform(-1, 1)
                if value < Harmony.BOUNDS[i][0]:
                    value = Harmony.BOUNDS[i][0]
                if value > Harmony.BOUNDS[i][1]:
                    value = Harmony.BOUNDS[i][1]
                vector[i] = value
            else:
                vector[i] = parm.get_rand(Harmony.BOUNDS[i])
        return Harmony(vector)

    def search(self):
        gen = 0
        error = []
        memory = self.initialize_harmony_memory()
        best = memory[0]
        while gen < self.max_iter:
            harm = self.create_harmony(memory)
            self.fitness_function(gen, harm)
            if harm.get_error() < best.get_error():
                best = harm
            error.append(best.get_error())
            memory.append(harm)
            memory.sort(key=lambda x: x.get_error())
            memory.pop()
            print('gen: {}, error:{}'.format(gen, best.get_error()))
            gen += 1
        return best, error
