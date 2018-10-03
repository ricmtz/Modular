from evolutionary.genetic import Genetic
from utility.plotter import Plotter


def main():
    pop_size = 80
    best_p = 10
    max_gen = 0
    p_m = 5
    g = Genetic(pop_size, best_p, max_gen, p_m)
    print('Genetic evolution')
    best, error = g.search()
    print(best.get_R(), best.get_L(), best.get_J(), best.get_LAM())
    Plotter.plot_result(best.get_R(), best.get_L(),
                           best.get_J(), best.get_LAM(), error, 'Geetic')


if __name__ == '__main__':
    main()
