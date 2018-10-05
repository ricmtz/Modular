from evolutionary.evolution_s import EvolutionStrat
from utility import Plotter


def main():
    max_gen = 2
    pop_size = 30
    num_children = 20
    a = EvolutionStrat(max_gen, pop_size, num_children)
    a.search()
    best = a.get_best()
    print(best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error(),
                        'Evolution Strategies')


if __name__ == '__main__':
    main()
