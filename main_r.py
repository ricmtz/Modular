from stochastic import RandomSearch
from utility import Plotter


def main():
    max_gen = 50
    g = RandomSearch(max_gen)
    g.search()
    best = g.get_best()
    print(*best.get_values())
    Plotter.plot_result(*best.get_values(), g.get_error(), 'Random Search')


if __name__ == '__main__':
    main()
