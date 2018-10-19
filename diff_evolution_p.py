from evolutionary import DiffEvoAlgorithm
from utility import Runner


def main():
    max_gen = 25
    pop_size = 10
    weight_f = 0.2
    cross_r = 0.7
    num_threads = 5
    algorithm = DiffEvoAlgorithm(
        pop_size, max_gen, weight_f, cross_r, num_threads)
    Runner.run_algorithm_p(algorithm, 'Differential Evolution Parallel')


if __name__ == '__main__':
    main()
