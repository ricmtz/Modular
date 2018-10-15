from immune import ClonalSelection
from utility import Runner


def main():
    # algorithm configuration
    max_gens = 3
    pop_size = 15
    clone_factor = 0.1
    num_rand = 2
    # execute the algorithm
    algorithm = ClonalSelection(max_gens, pop_size, clone_factor, num_rand)
    Runner.run_algorithm(algorithm, 'Clonal Selection')


if __name__ == '__main__':
    main()
