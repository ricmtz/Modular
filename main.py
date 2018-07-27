from evolutionary.genetic import Genetic
from plot import Plotter


def main():
    pop_size = 100
    best_p = 15
    max_gen = 200
    p_m = 5
    g = Genetic(pop_size, best_p, max_gen, p_m)
    best, error = g.search()
    print(best.get_R(), best.get_L(), best.get_J(), best.get_LAM())
    Plotter.plot_functions(best.get_R(), best.get_L(),
                           best.get_J(), best.get_LAM(), error)


if __name__ == '__main__':
    main()
