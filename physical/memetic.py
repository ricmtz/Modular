class Memetic(object):
    def __init__(self, max_gens, search_space, pop_size, p_cross, p_mut,
                 max_local_gens, p_local, bits_per_param=16):
        self.max_gens = max_gens
        self.bounds = search_space
        self.pop_size = pop_size
        self.p_cross = p_cross
        self.p_mut = p_mut
        self.max_local_gens = max_local_gens
        self.p_local = p_local
        self.bits_per_param = bits_per_param

    def fitness_function(self, i_time, citizen):
        pass

    def binary_tournament(self, pop):
        pass

    def point_mutation(self):
        pass
    
    def crossover(self, parent1, parent2):
        pass    
    
    def reproduce(self, selected):
        pass
    
    def bit_climber(self, child):
        pass

    def search(self):
        pass
