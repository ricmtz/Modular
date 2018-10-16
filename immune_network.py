from immune import ImmuneNetwork
from utility import Runner


def main():
    max_gen = 2
    pop_size = 20
    num_clones = 10
    beta = 100
    num_rand = 2
    algorithm = ImmuneNetwork(max_gen, pop_size, num_clones, beta, num_rand)
    Runner.run_algorithm(algorithm, 'Immune Network')


if __name__ == '__main__':
    main()
