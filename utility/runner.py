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
        print('R:{}, L:{}, J:{}, Lambda:{}'.format(*best.get_values()))
        print('Time: {}'.format(total_time))
        print(''.center(WIDTH_TXT, FILL_CHR))
        Plotter.plot_result(*best.get_values(), algorithm.get_error(), name)
        Saver.save_results(name, best.get_values(),
                           algorithm.get_error(), total_time)
