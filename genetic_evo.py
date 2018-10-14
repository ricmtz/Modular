from evolutionary.genetic import Genetic
from utility import Runner


def main():
    pop_size = 80
    best_p = 10
    max_gen = 2
    p_m = 5
    algorithm = Genetic(pop_size, best_p, max_gen, p_m)
    Runner.run_algorithm(algorithm, 'Genetic Evolution')


if __name__ == '__main__':
    main()
