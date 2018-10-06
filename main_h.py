from physical import Harmony
from utility import Plotter


def main():
    max_gen = 20
    mem_size = 20
    consid_r = 0.95
    adjust_r = 0.7
    rang = 0.05
    a = Harmony(max_gen, mem_size, consid_r, adjust_r, rang)
    a.search()
    best = a.get_best()
    print(*best.get_values())
    Plotter.plot_result(*best.get_values(), a.get_error(), 'Harmony Search')


if __name__ == '__main__':
    main()
