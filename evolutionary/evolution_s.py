

class EvolutionStrat(object):

    def __init__(self, max_gen, pop_size, num_children):
        self.max_gen = max_gen
        self.pop_size = pop_size
        self.num_children = num_children

    def search(self):
        gen = 0
        error = []
        pop = self.init_pop()
        self.fitness_function(gen, pop)
        pop.sort(key=lambda x: x.get_error())
        best = pop[0]
        error.append(best.get_error())
        while gen < self.max_gen:
            children = []
            for i in range(self.num_children):
                children.append(self.mutate(pop[i]))
            self.fitness_function(gen, children)
            union = children + pop
            union.sort(key=lambda x: x.get_error())
            if union[0].get_error() < best.get_error():
                best = union[0]
            error.append(best.get_error())
            pop = union[:self.pop_size]
            print('Gen: {}, Error:{}'.format(
                gen, best.get_error()))
            gen += 1
        return best, error
