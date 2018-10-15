from probabilistic import CrossEntropy
from utility import Runner


def main():
    max_iter = 2
    num_samples = 50
    num_update = 10
    learning_r = 0.7
    algorithm = CrossEntropy(max_iter, num_samples, num_update, learning_r)
    Runner.run_algorithm(algorithm, 'Cross Entropy')


if __name__ == '__main__':
    main()
