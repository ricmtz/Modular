from evolutionary.diff_evo import DiffEvolution
from utility import Plotter, Saver

ALGORITHM = 'Differential Evolution'


def main():
    max_gen = 2
    pop_size = 10
    weight_f = 0.2
    cross_r = 0.7
    a = DiffEvolution(max_gen, pop_size, weight_f, cross_r)
    print(ALGORITHM.center(50, '-'))
    a.search()
    best = a.get_best()
    print(''.center(50, '-'))
    print('Results: ', best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error(),
                        ALGORITHM)
    Saver.save_results(ALGORITHM,
                       best.get_values(), a.get_error())


if __name__ == '__main__':
    main()
