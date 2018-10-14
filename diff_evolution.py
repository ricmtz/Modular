from evolutionary.diff_evo import DiffEvolution
from utility import Runner


def main():
    max_gen = 2
    pop_size = 10
    weight_f = 0.2
    cross_r = 0.7
    algorithm = DiffEvolution(max_gen, pop_size, weight_f, cross_r)
    Runner.run_algorithm(algorithm, 'Differential Evolution')


if __name__ == '__main__':
    main()
