from stochastic import RandomSearch
from utility import Runner


def main():
    max_gen = 50
    algorithm = RandomSearch(max_gen)
    Runner.run_algorithm(algorithm, 'Random Search')


if __name__ == '__main__':
    main()
