from evolutionary import GenParallelAlgorithm
from utility import Runner


def main():
    pop_size = 20
    best_p = 10
    max_gen = 2
    p_m = 5
    num_threads = 5
    algorithm = GenParallelAlgorithm(
        pop_size, best_p, max_gen, p_m, num_threads)
    Runner.run_algorithm_p(algorithm, 'Genetic Evolution Parallel')


if __name__ == '__main__':
    main()
