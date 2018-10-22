import time
from utility import Plotter, Saver

WIDTH_TXT = 50
FILL_CHR = '-'


class Runner:
    @staticmethod
    def run_algorithm(algorithm, name=''):
        print(name.center(WIDTH_TXT, FILL_CHR))
        start = time.time()
        algorithm.search()
        finish = time.time()
        best = algorithm.get_best()
        total_time = time.strftime('%M:%S', time.gmtime(finish - start))
        print(''.center(WIDTH_TXT, FILL_CHR))
        print('Results'.center(WIDTH_TXT, FILL_CHR))
        print(
            'R:{}, L:{}, J:{}, Lambda:{}'.format(*best.get_values()))
        print('Time: {}'.format(total_time))
        print(''.center(WIDTH_TXT, FILL_CHR))
        Plotter.plot_result(*best.get_values(), algorithm.get_error(), name)
        Saver.save_results(name, best.get_values(),
                           algorithm.get_error(), total_time)
        return best.get_values(), total_time

    @staticmethod
    def run_algorithm_p(algorithm, name=''):
        print(name.center(WIDTH_TXT, FILL_CHR))
        start = time.time()
        algorithm.search()
        finish = time.time()
        bests = algorithm.get_bests()
        total_time = time.strftime('%M:%S', time.gmtime(finish - start))
        print(''.center(WIDTH_TXT, FILL_CHR))
        print('Results'.center(WIDTH_TXT, FILL_CHR))
        for i, best in bests.items():
            print('id: {}, R:{}, L:{}, J:{}, Lambda:{}'.format(
                i, *best.get_values()))
        print('Time: {}'.format(total_time))
        print(''.center(WIDTH_TXT, FILL_CHR))
        best = min(bests.values(), key=lambda x: x.get_error())
        Plotter.plot_result_p(*best.get_values(), algorithm.get_errors(), name)
        return bests, total_time
