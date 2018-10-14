from evolutionary.evolution_s import EvolutionStrat
from utility import Runner


def main():
    max_gen = 2
    pop_size = 30
    num_children = 20
    algorithm = EvolutionStrat(max_gen, pop_size, num_children)
    Runner.run_algorithm(algorithm, 'Evolution Strategies')


if __name__ == '__main__':
    main()
