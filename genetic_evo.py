from evolutionary.genetic import Genetic
from utility import Plotter, Saver

ALGORITHM = 'Genetic Evolution'


def main():
    pop_size = 80
    best_p = 10
    max_gen = 2
    p_m = 5
    a = Genetic(pop_size, best_p, max_gen, p_m)
    print(ALGORITHM.center(50, '-'))
    a.search()
    best = a.get_best()
    print(''.center(50, '-'))
    print('Results: ', best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error(), ALGORITHM)
    Saver.get_results(ALGORITHM, best.get_values(), a.get_error())


if __name__ == '__main__':
    main()
