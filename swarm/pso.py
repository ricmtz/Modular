from swarm import Particles
from models import Algorithm


class PSO(Algorithm):
    def __init__(self, pop_size, max_gen):
        super().__init__()
        self.pop_size = pop_size
        self.max_gen = max_gen

    def search(self):
        best_pos_global = None
        gen = 0
        best_prt = None
        particulas = Particles(self.pop_size)
        while gen < self.max_gen:
            particulas.evaluate()
            best_prt = particulas.get_best()
            if self.best is None or \
                    best_prt.get_error() < self.best.get_error():
                best_pos_global = particulas.get_best_pos_global()
                self.best = best_prt
            self.error.append(self.best.get_error())
            particulas.update_particles(best_pos_global)
            print('Gen={}, Error={}'.format(gen, self.best.get_error()))
            gen += 1
