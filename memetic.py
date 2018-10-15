from physical import Memetic
from utility import Runner


def main():
    problem_size = 4
    max_gens = 2
    pop_size = 20
    p_cross = 0.98
    p_mut = 1.0/float(problem_size*16)
    max_local_gens = 20
    p_local = 0.5
    algorithm = Memetic(max_gens, pop_size, p_cross,
                        p_mut, max_local_gens, p_local)
    Runner.run_algorithm(algorithm, 'Memetic')


if __name__ == '__main__':
    main()
