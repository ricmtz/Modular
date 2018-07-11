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


def random_gaussian(mean=0.0, stdev=1.0):
    """
    Parameters
    ----------
    mean : float

    stdev : float
    """
    u1 = u2 = w = 0
    while True:
        u1 = 2 * np.random.rand() - 1
        u2 = 2 * np.random.rand() - 1
        w = u1 * u1 + u2 * u2
        if w >= 1:
            break
    w = math.sqrt((-2.0 * math.log(w)) / w)
    return mean + (u2 * w) * stdev


def generate_sample():
    """
    """
    pass


def mean_attr():
    """
    """
    pass


def stdev_attr():
    """
    """
    pass


def update_distribution():
    """
    """
    pass


def search():
    """
    """
    pass


def main():
    pass


if __name__ == '__main__':
    main()
