from evolutionary.diff_evo import DiffEvolution
from utility import Plotter


def main():
    max_gen = 2
    pop_size = 10
    weight_f = 0.2
    cross_r = 0.7
    a = DiffEvolution(max_gen, pop_size, weight_f, cross_r)
    a.search()
    best = a.get_best()
    print(best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error(),
                        'Differential Evolution')


if __name__ == '__main__':
    main()
