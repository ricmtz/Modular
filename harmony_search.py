from physical import Harmony
from utility import Runner


def main():
    max_gen = 20
    mem_size = 20
    consid_r = 0.95
    adjust_r = 0.7
    rang = 0.05
    algorithm = Harmony(max_gen, mem_size, consid_r, adjust_r, rang)
    Runner.run_algorithm(algorithm, 'Harmony Search')


if __name__ == '__main__':
    main()
