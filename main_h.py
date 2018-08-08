from physical.harmony_a import HarmonyA
from plot import Plotter


def main():
    max_gen = 100
    mem_size = 20
    consid_r = 0.95
    adjust_r = 0.7
    rang = 0.05
    a = HarmonyA(max_gen, mem_size, consid_r, adjust_r, rang)
    best, error = a.search()
    print(best.get_R(), best.get_L(), best.get_J(), best.get_LAM())
    Plotter.plot_functions(best.get_R(), best.get_L(),
                           best.get_J(), best.get_LAM(), error)


if __name__ == '__main__':
    main()
