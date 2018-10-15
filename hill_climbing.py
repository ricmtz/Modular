from stochastic import HillClimbing
from utility import Runner


def main():
    max_gen = 100
    algorithm = HillClimbing(max_gen)
    Runner.run_algorithm(algorithm, 'Hill Climbing')


if __name__ == '__main__':
    main()
