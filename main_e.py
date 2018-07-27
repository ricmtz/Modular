from evolutionary.evolution_s import EvolutionS
from plot import Plotter


def main():
    max_gen = 100
    pop_size = 30
    num_children = 20
    a = EvolutionS(max_gen, pop_size, num_children)
    best, error = a.search()
    print(best.get_R(), best.get_L(), best.get_J(), best.get_LAM())
    Plotter.plot_functions(best.get_R(), best.get_L(),
                           best.get_J(), best.get_LAM(), error)


if __name__ == '__main__':
    main()
