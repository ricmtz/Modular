from probabilistic.cross_e import CrossE
from plot import Plotter


def main():
    max_iter = 50
    num_samples = 100
    num_update = 10
    learning_r = 0.7
    a = CrossE(max_iter, num_samples, num_update, learning_r)
    best, error = a.search()
    print(best.get_R(), best.get_L(), best.get_J(), best.get_LAM())
    Plotter.plot_functions(best.get_R(), best.get_L(),
                           best.get_J(), best.get_LAM(), error)


if __name__ == '__main__':
    main()
