from evolutionary.genetic import Genetic
from utility import Plotter


def main():
    pop_size = 80
    best_p = 10
    max_gen = 2
    p_m = 5
    g = Genetic(pop_size, best_p, max_gen, p_m)
    print('Genetic evolution')
    g.search()
    best = g.get_best()
    error = g.get_error()
    print(best.get_values())
    Plotter.plot_result(*best.get_values(), error, 'Genetic')


if __name__ == '__main__':
    main()
