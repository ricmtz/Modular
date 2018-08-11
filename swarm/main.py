import PSO

PARTICLES = 30
DIMENSIONS = 2
SPACE_BOUNDARIES = [[-5, 5]] * DIMENSIONS
VELOCITY_BOUNDARIES = [[-1, 1]] * DIMENSIONS
GENERATIONS = 40


def cost_function(values):
    result = 0
    for i in range(len(values)):
        result += values[i]**2
    return result


if __name__ == '__main__':
    PSO.PSO(PARTICLES, SPACE_BOUNDARIES, VELOCITY_BOUNDARIES, GENERATIONS, cost_function)
