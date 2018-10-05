from models import Population
from models import Citizen
from utility import randint_bound, rand


class PopulationDif(Population):
    def __init__(self, pop_size, wf, cr):
        super().__init__(pop_size)
        self.wf = wf
        self.cr = cr

    def create_pop(self):
        return [Citizen() for _ in range(self.pop_size)]

    def de_rand_1_bin(self, p0, p1, p2, p3):
        cut = randint_bound(Citizen.P_SIZE)
        params = [0 for _ in range(Citizen.P_SIZE)]
        for i in range(4):
            if i == cut or rand() < self.cr:
                aux = p3[i] + self.wf * (p1[i] - p2[i])
                aux = Citizen.BOUNDS[i][0] if (
                    aux < Citizen.BOUNDS[i][0]) else aux
                aux = Citizen.BOUNDS[i][1] if (
                    aux > Citizen.BOUNDS[i][1]) else aux
                params[i] = aux
            else:
                params[i] = p0[i]
        return Citizen(params)

    def select_parents(self, current):
        p1, p2, p3 = randint_bound(self.pop_size, size=3)
        while (p1 == current):
            p1 = randint_bound(self.pop_size)
        while (p2 == current or p2 == p1):
            p2 = randint_bound(self.pop_size)
        while (p3 == current or p3 == p1 or p3 == p2):
            p3 = randint_bound(self.pop_size)
        return p1, p2, p3

    def create_children(self):
        children = []
        for i, p0 in enumerate(self.population):
            p1, p2, p3 = self.select_parents(i)
            child = self.de_rand_1_bin(p0.get_values(),
                                       self.population[p1].get_values(),
                                       self.population[p2].get_values(),
                                       self.population[p3].get_values())
            children.append(child)
        return children

    def select_population(self, children):
        new_pop = []
        for i in range(self.pop_size):
            best = self.population[i] if self.population[i].get_error(
            ) <= children[i].get_error() else children[i]
            new_pop.append(best)
        self.population = new_pop
