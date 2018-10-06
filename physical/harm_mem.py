from models import Population
from physical import CitizenHar
from utility import rand, randint_bound, rand_bound


class HarmonyMem(Population):
    def __init__(self, pop_size, consid_r, adjust_r, ran):
        super().__init__(pop_size)
        self.consid_r = consid_r
        self.adjust_r = adjust_r
        self.ran = ran

    def create_pop(self, factor=3):
        memory = [self.create_rand_harmony()
                  for _ in range(self.pop_size * factor)]
        self.sort_pop(memory)
        return memory[:self.pop_size]

    def create_rand_harmony(self):
        harm = CitizenHar()
        harm.set_error(self.fitness_function(*harm.get_values()))
        return harm

    def create_harmony(self):
        harmony = CitizenHar()
        for i in range(CitizenHar.P_SIZE):
            if rand() < self.consid_r:
                pos = randint_bound(self.pop_size)
                value = self.population[pos].get_value(i)
                if rand() < self.adjust_r:
                    value = value + self.ran * rand_bound(-1, 1)
                harmony.set_value(i, value)
            else:
                harmony.set_value(i)
        return harmony

    def add_harm(self, harm):
        self.population.append(harm)
        self.sort_pop()
        self.population.pop()
