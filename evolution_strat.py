from evolutionary.evolution_s import EvolutionStrat
from utility import Plotter, Saver

ALGORITHM = 'Evolution Strategies'


def main():
    max_gen = 2
    pop_size = 30
    num_children = 20
    a = EvolutionStrat(max_gen, pop_size, num_children)
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
