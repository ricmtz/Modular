from threading import Thread, RLock
from utility import rand
from models import Algorithm


class test(Thread, Algorithm):
    BEST = {}

    def __init__(self, id):
        super(test, self).__init__()
        super(Thread, self).__init__()
        super(Algorithm, self).__init__()
        self.values = []
        self.id = id
        self.lock = RLock()

    def run(self):
        for i in range(3):
            self.mix_best()
            for i in range(5):
                self.values.append(rand())
            self.export_best()

    def export_best(self):
        self.values.sort()
        self.lock.acquire()
        try:
            print('export', self.id, self.values[:2])
            self.BEST[self.id] = self.values[:2]
        finally:
            self.lock.release()

    def mix_best(self):
        print('mix', self.id)
        self.lock.acquire()
        try:
            new_v = []
            for id_i, val in self.BEST.items():
                if id_i != self.id:
                    new_v.extend(val)
            print('nuevos datos', self.id, new_v)
            self.values.extend(new_v)
        finally:
            self.lock.release()


def main():
    threads = []
    for i in range(4):
        thread = test(i)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()
    for t in threads:
        print(t.id, t.values)
        print(t.get_best())
        print('')


if __name__ == '__main__':
    main()
