from scipy.io import loadmat
from scipy.linalg import norm
import numpy as np
import math

FILE_PARAM = loadmat('mediciones.mat')

I_ALPHA = FILE_PARAM['ia']  # Stator current
I_BETA = FILE_PARAM['ib']  # Stator current
CI = FILE_PARAM['ic']  # Load torque
W = FILE_PARAM['vel']  # Speed

P = 2  # Poles number
U_ALPHA = 0.05  # Estandor's voltage
U_BETA = 0.05  # Estandor's voltage
F = 0.0001  # Friction coefficient

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
    w = W[0][i_time]
    return ((r/l)*ia+(P*lam/l)*w*math.sin(w)+(1/l)*U_ALPHA)


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
    w = W[0][i_time]
    return ((r/l)*ib+(P*lam/l)*w*math.cos(w)+(1/l)*U_BETA)


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
    ia = I_ALPHA[0][i_time]
    ib = I_BETA[0][i_time]
    w = W[0][i_time]
    iap = i_alpha_function(i_time, r, l, lam)
    ibp = i_beta_function(i_time, r, l, lam)
    wp = w_function(i_time, j, lam)
    return abs((norm(ia) - norm(iap)) + (norm(ib) - norm(ibp))
               + (norm(w - wp)))


def fitness_function(i_time, pop):
    """
    Parameters
    ----------
    i_time: int

    pop : list
    """
    for i in pop:
        i['Error'] = calc_error(i_time, i['R'], i['L'], i['J'], i['LAM'])


def create_pop(pop_size, problem_size):
    """
    Parameters
    ----------
    pop_size : int

    problem_size : int
    """
    population = []
    for _ in range(pop_size):
        temp_s = {}
        temp_s['R'] = (np.random.uniform(R_MIN, R_MAX, problem_size))
        temp_s['L'] = (np.random.uniform(L_MIN, L_MAX, problem_size))
        temp_s['J'] = (np.random.uniform(J_MIN, J_MAX, problem_size))
        temp_s['LAM'] = (np.random.uniform(LAM_MIN, LAM_MAX, problem_size))
        population.append(temp_s)
    return population
    pass


def select_parents(pop, pop_size):
    """
    Parameters
    ----------
    pop : list

    pop_size : int
    """
    pass


def crossover(p1, p2, problem_size):
    """
    Parameters
    ----------
    p1 : dict

    p2 : dict

    problem_size : int
    """
    cut = np.random.randint(int(problem_size*.2), int(problem_size*.8))
    child = {'R': np.zeros(problem_size),
             'L': np.zeros(problem_size),
             'J': np.zeros(problem_size),
             'LAM': np.zeros(problem_size)
             }
    for i in range(cut):
        child['R'][i] = p1['R'][i]
        child['L'][i] = p1['L'][i]
        child['J'][i] = p1['J'][i]
        child['LAM'][i] = p1['LAM'][i]
    for i in range(cut, problem_size):
        child['R'][i] = p1['R'][i]
        child['L'][i] = p1['L'][i]
        child['J'][i] = p1['J'][i]
        child['LAM'][i] = p1['LAM'][i]
    return child


def make_crossover(pop, problem_size):
    """
    Parameters
    ----------
    pop : list

    problem_size : int
    """
    pass


def mutate(s):
    """
    s : dict
    """
    pass


def main(pop_size, problem_size, pm):
    """
    pop_size : int

    problem_size : int

    pm : float
    """
    pass


if __name__ == '__main__':
    main()
