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


def select_parents(best_p):
    """
    Parameters
    ----------
    best_p : int
    """
    p1, p2 = np.random.choice(best_p, 2, replace=False)
    return [p1, p2]


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
        child['R'][i] = p2['R'][i]
        child['L'][i] = p2['L'][i]
        child['J'][i] = p2['J'][i]
        child['LAM'][i] = p2['LAM'][i]
    return child


def make_crossover(pop, pop_size, problem_size, best_p):
    """
    Parameters
    ----------
    pop : list

    pop_size: int

    problem_size : int

    best_p : int
    """
    children = []
    for i in range(pop_size):
        p1, p2 = select_parents(best_p)
        child = crossover(pop[p1], pop[p2], problem_size)
        children.append(child)
    return children


def mutate(s, problem_size):
    """
    s : dict
    """
    r, l, j, lam = np.random.choice(problem_size, 4)
    s['R'][r] = np.random.uniform(R_MIN, R_MAX)
    s['L'][l] = np.random.uniform(L_MIN, L_MAX)
    s['J'][j] = np.random.uniform(J_MIN, J_MAX)
    s['LAM'][lam] = np.random.uniform(LAM_MIN, LAM_MAX)


def search(pop_size, problem_size, best_p, max_gen, pm):
    """
    pop_size : int

    problem_size : int

    best_p : int

    max_gen : int

    pm : float
    """
    emc = []
    gen = 0
    pop = create_pop(pop_size, problem_size)
    fitness_function(gen, pop)
    best = min(pop, key=lambda p: p['Error'])
    emc.append(best['Error'])
    while gen < max_gen and best['Error'] > 0.1:
        children = make_crossover(pop, pop_size, problem_size, best_p)
        if gen % pm == 0:
            pos = np.random.randint(pop_size)
            mutate(children[pos], problem_size)
        fitness_function(gen, children)
        best = min(children, key=lambda p: p['Error'])
        emc.append(best['Error'])
        pop = children
        print('Gen: {}, Error: {}'.format(gen, best['Error']))
        gen += 1
    return best, emc


def main():
    pop_size = 100
    problem_size = 6
    best_p = 15
    max_gen = 500
    pm = 50
    solution, error = search(pop_size, problem_size, best_p, max_gen, pm)
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
