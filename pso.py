from swarm import PSO
from utility import Runner


def main():
    pop_size = 10
    max_gen = 2
    algorithm = PSO(pop_size, max_gen)
    Runner.run_algorithm(algorithm, 'PSO')


if __name__ == '__main__':
    main()
