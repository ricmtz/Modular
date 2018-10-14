from physical import Harmony
from utility import Plotter, Saver

ALGORITHM = 'Harmony Search'


def main():
    max_gen = 20
    mem_size = 20
    consid_r = 0.95
    adjust_r = 0.7
    rang = 0.05
    a = Harmony(max_gen, mem_size, consid_r, adjust_r, rang)
    print(ALGORITHM.center(50, '-'))
    a.search()
    best = a.get_best()
    print(''.center(50, '-'))
    print('Results: ', best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error(), ALGORITHM)
    Saver.save_results(ALGORITHM, best.get_values(), a.get_error())


if __name__ == '__main__':
    main()
