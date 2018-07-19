from scipy.io import loadmat
from scipy.linalg import norm
import numpy as np
import math
import matplotlib.pyplot as plt

FILE_PARAM = loadmat('mediciones.mat')

I_ALPHA = FILE_PARAM['ia']  # Stator current
I_BETA = FILE_PARAM['ib']  # Stator current
CI = FILE_PARAM['ic']  # Load torque
THETA = FILE_PARAM['vel']  # Speed

P = 2  # Poles number
U_ALPHA = 0.00005  # Estandor's voltage
U_BETA = 0.00005  # Estandor's voltage
F = 0.001  # Friction coefficient

# Search space of the parameters
R_MIN = 0.0004
R_MAX = 0.0012
L_MIN = 0.0010
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
    ib = I_BETA[0][i_time]
    theta = THETA[0][i_time]
    ci = CI[0][i_time]
    w = lam/j*(-ia * math.sin(P)*theta + ib *
               math.cos(P)*theta) - F/j * theta - ci/j
    return w*.002


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
    w = theta = THETA[0][i_time]
    d_ia = r/l*ia+P*lam/l*w*math.sin(theta)+1/l*U_ALPHA
    return d_ia


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
    w = theta = THETA[0][i_time]
    d_ib = r/l*ib+P*lam/l*w*math.cos(theta)+1/l*U_BETA
    return d_ib


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
    w = THETA[0][i_time]
    wp = w_function(i_time, j, lam)
    iap = i_alpha_function(i_time, r, l, lam)
    ibp = i_beta_function(i_time, r, l, lam)
    error = (norm(ia) - norm(iap)) + (norm(ib) - norm(ibp)) + (norm(w - wp))
    return error ** 2


def fitness_function(i_time, pop):
    """
    Parameters
    ----------
    i_time: int

    pop : list
    """
    for i in pop:
        error = 0
        i_size = len(i['R'])
        error += calc_error(i_time, i['R'], i['L'], i['J'], i['LAM'])
        i['Error'] = math.sqrt(error)/i_size


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


def de_rand_1_bin(p0, p1, p2, p3, problem_size, wf, cr):
    """
    Parameters
    ----------
    p0 : dict

    p1 : dict

    p2 : dict

    p3 : dict

    problem_size : int

    wf : float

    cr : float
    """
    cut = np.random.randint(problem_size)
    sp = {'R': np.zeros(problem_size),
          'L': np.zeros(problem_size),
          'J': np.zeros(problem_size),
          'LAM': np.zeros(problem_size)
          }
    for i in range(problem_size):
        if i == cut or np.random.rand() < cr:
            sp['R'][i] = p3['R'][i] + wf * (p1['R'][i] - p2['R'][i])
            sp['R'][i] = sp['R'][i] if sp['R'][i] < R_MAX else R_MAX
            sp['R'][i] = sp['R'][i] if sp['R'][i] > R_MIN else R_MIN
            sp['L'][i] = p3['L'][i] + wf * (p1['L'][i] - p2['L'][i])
            sp['L'][i] = sp['L'][i] if sp['L'][i] < L_MAX else L_MAX
            sp['L'][i] = sp['L'][i] if sp['L'][i] > L_MIN else L_MIN
            sp['J'][i] = p3['J'][i] + wf * (p1['J'][i] - p2['J'][i])
            sp['J'][i] = sp['J'][i] if sp['J'][i] < J_MAX else J_MAX
            sp['J'][i] = sp['J'][i] if sp['J'][i] > J_MIN else J_MIN
            sp['LAM'][i] = p3['LAM'][i] + wf * (p1['LAM'][i] - p2['LAM'][i])
            sp['LAM'][i] = sp['LAM'][i] if sp['LAM'][i] < LAM_MAX else LAM_MAX
            sp['LAM'][i] = sp['LAM'][i] if sp['LAM'][i] > LAM_MIN else LAM_MIN
        else:
            sp['R'][i] = p0['R'][i]
            sp['L'][i] = p0['L'][i]
            sp['J'][i] = p0['J'][i]
            sp['LAM'][i] = p0['LAM'][i]
    return sp


def select_parents(pop, current):
    """
    Parameters
    ----------
    pop : list

    current: int
    """
    p1, p2, p3 = np.random.randint(len(pop), size=3)
    while (p1 == current):
        p1 = np.random.randint(len(pop))
    while (p2 == current or p2 == p1):
        p2 = np.random.randint(len(pop))
    while (p3 == current or p3 == p1 or p3 == p2):
        p3 = np.random.randint(len(pop))
    return [p1, p2, p3]


def create_children(pop, problem_size, wf, cr):
    """
    Parameters
    ----------
    pop : list

    problem_size : int

    wf : float

    cr : float
    """
    children = []
    for i, p0 in enumerate(pop):
        p1, p2, p3 = select_parents(pop, i)
        children.append(de_rand_1_bin(p0, pop[p1], pop[p2], pop[p3],
                                      problem_size, wf, cr))
    return children


def select_population(parents, children, pop_size):
    """
    Parameters
    ---------
    parents : list

    children : list

    pop_size : int
    """
    n_pop = []
    for i in range(pop_size):
        n_pop.append(parents[i] if parents[i]['Error'] <=
                     children[i]['Error'] else children[i])
    return n_pop


def search(max_gen: int, pop_size: int, problem_size: int,
           wf: float, cr: float) -> list:
    error = []
    gen = 0
    pop = create_pop(pop_size, problem_size)
    fitness_function(gen, pop)
    best = min(pop, key=lambda p: p['Error'])
    error.append(best['Error'])
    while gen < max_gen and best['Error'] > 0.1:
        children = create_children(pop, problem_size, wf, cr)
        fitness_function(gen, children)
        pop = select_population(pop, children, pop_size)
        pop.sort(key=lambda p: p['Error'])
        if pop[0]['Error'] < best['Error']:
            best = pop[0]
        print('Gen: {}, fitness: {}'.format(gen, best['Error']))
        error.append(best['Error'])
        gen += 1
    return best, error


def main():
    problem_size = 6
    max_gen = 300
    pop_size = 100
    weight_f = 0.8
    cross_r = 0.9
    solution, error = search(
        max_gen, pop_size, problem_size, weight_f, cross_r)
    print(solution)
    time = FILE_PARAM['time'][0][:60]
    ax1 = plt.subplot(2, 2, 1)
    ax2 = plt.subplot(2, 2, 2)
    ax3 = plt.subplot(2, 2, 3)
    ax4 = plt.subplot(2, 2, 4)
    ax1.plot(time, I_ALPHA[0][:60], 'r-')
    ax1.set_title('Alpha')
    ax2.plot(time, I_BETA[0][:60], 'r-')
    ax2.set_title('Beta')
    ax3.plot(time, THETA[0][:60], 'r-')
    ax3.set_title('W')
    for i in range(problem_size):
        ia = []
        ib = []
        w = []
        for j in range(len(time)):
            ia.append(i_alpha_function(
                j, solution['R'][i], solution['L'][i], solution['LAM'][i]))
            ib.append(i_beta_function(
                j, solution['R'][i], solution['L'][i], solution['LAM'][i]))
            w.append(w_function(i, solution['J'][i], solution['LAM'][i]))
        ax1.plot(time, ia, 'b-')
        ax2.plot(time, ib, 'b-')
        ax3.plot(time, w, 'b-')
    ax4.plot(range(len(error)), error, 'r-')
    ax4.set_title('Evolucion')
    plt.show()


if __name__ == '__main__':
    main()
