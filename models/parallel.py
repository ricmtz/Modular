from threading import Thread, RLock
from models import Algorithm


class Parallel(Thread, Algorithm):
    DATA = {}

    def __init__(self, id_a):
        super(Parallel, self).__init__()
        super(Thread, self).__init__()
        super(Algorithm, self).__init__()
        self.id_a = id_a
        self.lock = RLock()

    def export_data(self, pop):
        self.lock.acquire()
        try:
            self.DATA[self.id_a] = pop.copy()
        finally:
            self.lock.release()

    def get_data(self):
        pop = []
        self.lock.acquire()
        try:
            for id_a, ctz in self.DATA.items():
                if id_a != self.id_a:
                    pop.extend(ctz)
        finally:
            self.lock.release()
        return pop

    def run(self):
        raise NotImplementedError
