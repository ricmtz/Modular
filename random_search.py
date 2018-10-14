from stochastic import RandomSearch
from utility import Plotter, Saver

ALGORITHM = 'Random Search'


def main():
    max_gen = 50
    a = RandomSearch(max_gen)
    print(ALGORITHM.center(50, '-'))
    a.search()
    best = a.get_best()
    print(''.center(50, '-'))
    print('Results: ', best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error(), ALGORITHM)
    Saver.save_results(ALGORITHM, best.get_values(), a.get_error())


if __name__ == '__main__':
    main()
