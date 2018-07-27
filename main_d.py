from evolutionary.diff_evo import DiffEvolution
from plot import Plotter


def main():
    max_gen = 50
    pop_size = 10
    weight_f = 0.2
    cross_r = 0.7
    a = DiffEvolution(max_gen, pop_size, weight_f, cross_r)
    best, error = a.search()
    print(best.get_R(), best.get_L(), best.get_J(), best.get_LAM())
    Plotter.plot_functions(best.get_R(), best.get_L(),
                           best.get_J(), best.get_LAM(), error)


if __name__ == '__main__':
    main()
