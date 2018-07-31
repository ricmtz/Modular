from stochastic.random_s import RandomSearch
from plot import Plotter


def main():
    max_gen = 50
    g = RandomSearch(max_gen)
    best, error = g.search()
    print(best.get_R(), best.get_L(), best.get_J(), best.get_LAM())
    Plotter.plot_functions(best.get_R(), best.get_L(),
                           best.get_J(), best.get_LAM(), error)


if __name__ == '__main__':
    main()
