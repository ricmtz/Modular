from stochastic import AdaptativeRandomS
from utility import Runner


def main():
    max_gen = 10
    init_factor = 0.05
    s_factor = 1.3
    l_factor = 3.0
    iter_mult = 10
    max_no_impr = 30
    algorithm = AdaptativeRandomS(
        max_gen, init_factor, s_factor, l_factor, iter_mult, max_no_impr)
    Runner.run_algorithm(algorithm, 'Adaptative Random Search')


if __name__ == '__main__':
    main()
