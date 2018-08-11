from parameters import Parameter as parm
from parameters import Function as func
from plot import Plotter
from swarm.PSO import PSO

PARTICLES = 30
DIMENSIONS = 4
SPACE_BOUNDARIES = parm.get_bounds()
VELOCITY_BOUNDARIES = [[-1, 1]] * DIMENSIONS
GENERATIONS = 40


def cost_function(i_time, values):
    return func.calc_error(i_time, *values)


if __name__ == '__main__':
    print(parm.get_bounds())
    a = PSO(PARTICLES, SPACE_BOUNDARIES,
            VELOCITY_BOUNDARIES, GENERATIONS, cost_function)
    solution, error = a.search()
    Plotter.plot_functions(*solution, error)
