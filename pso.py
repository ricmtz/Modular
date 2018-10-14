from swarm import PSO
from utility import Plotter, Saver

ALGORITHM = 'PSO'


def main():
    pop_size = 10
    max_gen = 2
    a = PSO(pop_size, max_gen)
    print(ALGORITHM.center(50, '-'))
    a.search()
    best = a.get_best()
    print(''.center(50, '-'))
    print('Results: ', best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error(), ALGORITHM)
    Saver.save_results(ALGORITHM, best.get_values(), a.get_error())


if __name__ == '__main__':
    main()
