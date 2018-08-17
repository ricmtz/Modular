from physical.memetic import Memetic
from parameters import Parameter as parm
from plot import Plotter


def main():
    problem_size = 3
    search_space = parm.get_bounds()
    max_gens = 100
    pop_size = 100
    p_cross = 0.98
    p_mut = 1.0/float(problem_size*16)
    max_local_gens = 20
    p_local = 0.5
    a = Memetic(max_gens, search_space, pop_size,
                p_cross, p_mut, max_local_gens, p_local)
    best, error = a.search()
    print(best.get_values())
    Plotter.plot_functions(*best.get_values(), error)


if __name__ == '__main__':
    main()
