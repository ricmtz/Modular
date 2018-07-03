from scipy.io import loadmat
import numpy as np
import math

FILE_PARAM = loadmat('mediciones.mat')

I_ALPHA = FILE_PARAM['ia']  # Stator current
I_BETA = FILE_PARAM['ib']  # Stator current
CI = FILE_PARAM['ic']  # Load torque
W = FILE_PARAM['vel']  # Speed

P = 2  # Poles number
U_ALPHA = 5  # Estandor's voltage
U_BETA = 5  # Estandor's voltage
F = 0.5  # Friction coefficient

# Search space of the parameters
R_MIN = 0.4
R_MAX = 1.2
L_MIN = 0.00010
L_MAX = 0.00020
J_MIN = 0.00015
J_MAX = 0.00030
LAM_MIN = 0.1090
LAM_MAX = 0.1107


def w_function(i_time, j, lam):
    """
    Parameters
    ----------
    i_time: int

    j : numpy.array

    lam : numpy.array
    """
    ia = I_ALPHA[0][i_time]
    w = W[0][i_time]
    ci = CI[0][i_time]
    return (lam/j)*(-ia * math.sin(P*w)) - (F/j) * w - (ci/j)


def i_alpha_function(i_time, r, l, lam):
    """
    Parameters
    ----------
    i_time : int

    r : numpy.array

    l : numpy.array

    lam : numpy.array
    """
    ia = I_ALPHA[0][i_time]
    ua = U_ALPHA[0][i_time]
    w = W[0][i_time]
    return ((r/l)*ia+(P*lam/l)*w*math.sin(w)+(1/l)*ua)


def i_beta_function(i_time, r, l, lam):
    """
    Parameters
    ----------
    i_time : int

    r : numpy.array

    l : numpy.array

    lam : numpy.array
    """
    ib = I_BETA[0][i_time]
    ub = U_BETA[0][i_time]
    w = W[0][i_time]
    return ((r/l)*ib+(P*lam/l)*w*math.cos(w)+(1/l)*ub)


def calc_error(i_time, r, l, j, lam):
    """
    Parameters
    ----------
    i_time : int

    r : numpy.array

    l : numpy.array

    j : numpy.array

    lam : numpy.array
    """
    print(w_function(i_time, j, lam))
    pass


def fitness_function(i_time, population_in):
    """
    Parameters
    ----------
    i_time: int

    population_in : list

    """
    for i in population_in:
        i['error'] = calc_error(i_time, i['R'], i['L'], i['J'], i['LAM'])


def create_pop(pop_size: int, problem_size: int) -> list:
    population = []
    for _ in range(pop_size):
        temp_s = {}
        temp_s['R'] = (np.random.uniform(R_MIN, R_MAX, problem_size))
        temp_s['L'] = (np.random.uniform(L_MIN, L_MAX, problem_size))
        temp_s['J'] = (np.random.uniform(J_MIN, J_MAX, problem_size))
        temp_s['LAM'] = (np.random.uniform(LAM_MIN, LAM_MAX, problem_size))
        population.append(temp_s)
    return population


def random_vector():
    pass


def de_rand_1_bin():
    pass


def select_parents():
    pass


def create_children():
    pass


def select_population():
    pass


def search(max_gen: int, pop_size: int, problem_size: int,
           wf: float, cr: float) -> list:
    pop = create_pop(pop_size, problem_size)
    fitness_function(0, pop)
    pass


def main():
    problem_size = 3
    max_gen = len(FILE_PARAM['time'][0])
    pop_size = 5
    weight_f = 0.8
    cross_f = 0.9
    best = search(max_gen, pop_size, problem_size, weight_f, cross_f)
    print(best)


if __name__ == '__main__':
    main()
