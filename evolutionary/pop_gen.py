from models import Population
from models import Citizen
from utility import randint_bound


class PopulationGen(Population):
    def __init__(self, pop_size):
        super().__init__(pop_size)

    def create_pop(self):
        return [Citizen() for _ in range(self.pop_size)]

    def make_crossover(self):
        pass

    def cross(self, p1, p2):
        v_p1 = p1.get_values()
        v_p2 = p2.get_values()
        cut_p = randint_bound(1, 3)
        v_child = v_p1[:cut_p] + v_p2[cut_p:]
        return Citizen(v_child)
