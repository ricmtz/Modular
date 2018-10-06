from models import Algorithm
from physical import HarmonyMem


class Harmony(Algorithm):
    def __init__(self, max_iter, pop_size, consid_r, adjust_r, ran):
        super().__init__()
        self.max_iter = max_iter
        self.pop_size = pop_size
        self.consid_r = consid_r
        self.adjust_r = adjust_r
        self.ran = ran

    def search(self):
        gen = 0
        memory = HarmonyMem(self.pop_size, self.consid_r,
                            self.adjust_r, self.ran)
        self.best = memory.get_best()
        while gen < self.max_iter:
            harm = memory.create_harmony()
            harm.set_error(memory.fitness_function(*harm.get_values()))
            if harm.get_error() < self.best.get_error():
                self.best = harm
            self.error.append(self.best.get_error())
            memory.add_harm(harm)
            print('gen: {}, error:{}'.format(gen, self.best.get_error()))
            gen += 1
