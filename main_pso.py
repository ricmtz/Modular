from swarm import PSO
from utility import Plotter


def main():
    pop_size = 10
    max_gen = 2
    a = PSO(pop_size, max_gen)
    a.search()
    best = a.get_best()
    print(best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error(), 'PSO')


if __name__ == '__main__':
    main()
