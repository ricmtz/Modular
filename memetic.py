from physical import Memetic
from utility import Plotter, Saver

ALGORITHM = 'Memetic'


def main():
    problem_size = 4
    max_gens = 2
    pop_size = 20
    p_cross = 0.98
    p_mut = 1.0/float(problem_size*16)
    max_local_gens = 20
    p_local = 0.5
    a = Memetic(max_gens, pop_size, p_cross, p_mut, max_local_gens, p_local)
    print(ALGORITHM.center(50, '-'))
    a.search()
    best = a.get_best()
    print(''.center(50, '-'))
    print('Results: ', best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error(), ALGORITHM)
    Saver.save_results(ALGORITHM, best.get_values(), a.get_error())


if __name__ == '__main__':
    main()
