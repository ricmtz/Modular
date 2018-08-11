import matplotlib.pyplot as plt
import random


def rand_val(min_v, max_v):
    return min_v + ((max_v - min_v) * random.random())


def plot_population(population, bounds, final=False):
    x_range = bounds[0][1] - bounds[0][0]
    y_range = bounds[1][1] - bounds[1][0]

    x_min = bounds[0][0] - x_range * 0.05
    x_max = bounds[0][1] + x_range * 0.05

    y_min = bounds[1][0] - y_range * 0.05
    y_max = bounds[1][1] + y_range * 0.05

    plt.xlim(xmin=x_min, xmax=x_max)
    plt.ylim(ymin=y_min, ymax=y_max)
    plt.grid(True)

    for particle in population:
        plt.plot(particle.position[1], particle.position[0], marker="o", markersize=5)

    plt.draw()
    plt.pause(0.001)

    if not final:
        plt.clf()
