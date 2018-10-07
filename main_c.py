from probabilistic import CrossEntropy
from utility import Plotter


def main():
    max_iter = 2
    num_samples = 50
    num_update = 10
    learning_r = 0.7
    a = CrossEntropy(max_iter, num_samples, num_update, learning_r)
    a.search()
    best = a.get_best()
    print(best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error())


if __name__ == '__main__':
    main()
