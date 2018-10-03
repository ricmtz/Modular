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
        i_size = len(i['solution']['R'])
        error += calc_error(i_time, i['solution']['R'], i['solution']
                            ['L'], i['solution']['J'], i['solution']['LAM'])
        i['Error'] = math.sqrt(error)/i_size


def create_solution(problem_size):
    """
    Parameters
    ----------
    problem_size : int
    """
    temp_s = {}
    temp_s['R'] = (np.random.uniform(R_MIN, R_MAX, problem_size))
    temp_s['L'] = (np.random.uniform(L_MIN, L_MAX, problem_size))
    temp_s['J'] = (np.random.uniform(J_MIN, J_MAX, problem_size))
    temp_s['LAM'] = (np.random.uniform(LAM_MIN, LAM_MAX, problem_size))
    return temp_s


def create_strategy(problem_size):
    temp_s = {}
    temp_s['R'] = (np.random.uniform(0, R_MAX - R_MIN * 0.05, problem_size))
    temp_s['L'] = (np.random.uniform(0, L_MAX - L_MIN * 0.05, problem_size))
    temp_s['J'] = (np.random.uniform(0, J_MAX - J_MIN * 0.05, problem_size))
    temp_s['LAM'] = (np.random.uniform(
        0, LAM_MAX - LAM_MIN * 0.05, problem_size))
    return temp_s


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
        if w < 1:
            break
    w = math.sqrt((-2.0 * math.log10(w)) / w)
    return mean + (u2 * w) * stdev


def mutate_problem(problem_size, vector, stdevs):
    """
    Parameters
    ----------.
    problem_size : int

    vector : dict

    stdevs : dict
    """
    aux = {
        'R': np.zeros(problem_size),
        'L': np.zeros(problem_size),
        'J': np.zeros(problem_size),
        'LAM': np.zeros(problem_size)
    }
    for i in range(problem_size):
        aux['R'][i] = vector['R'][i] + stdevs['R'][i] * random_gaussian()
        aux['R'][i] = R_MIN if aux['R'][i] < R_MIN else aux['R'][i]
        aux['R'][i] = R_MAX if aux['R'][i] > R_MAX else aux['R'][i]
        aux['L'][i] = vector['L'][i] + stdevs['L'][i] * random_gaussian()
        aux['L'][i] = L_MIN if aux['L'][i] < L_MIN else aux['L'][i]
        aux['L'][i] = L_MAX if aux['L'][i] > L_MAX else aux['L'][i]
        aux['J'][i] = vector['J'][i] + stdevs['J'][i] * random_gaussian()
        aux['J'][i] = J_MIN if aux['J'][i] < J_MIN else aux['J'][i]
        aux['J'][i] = J_MAX if aux['J'][i] > J_MAX else aux['J'][i]
        aux['LAM'][i] = vector['LAM'][i] + stdevs['LAM'][i] * random_gaussian()
        aux['LAM'][i] = LAM_MIN if aux['LAM'][i] < LAM_MIN else aux['LAM'][i]
        aux['LAM'][i] = LAM_MAX if aux['LAM'][i] > LAM_MAX else aux['LAM'][i]
    return aux


def mutate_strategy(stdevs, problem_size):
    tau = math.sqrt(2.0 * float(problem_size)) ** -1.0
    tau_p = math.sqrt(2.0 * math.sqrt(float(problem_size))) ** -1.0
    aux = {
        'R': np.zeros(problem_size),
        'L': np.zeros(problem_size),
        'J': np.zeros(problem_size),
        'LAM': np.zeros(problem_size)
    }
    for i in range(problem_size):
        aux['R'][i] = stdevs['R'][i] * \
            math.exp(tau_p*random_gaussian() + tau * random_gaussian())
        aux['L'][i] = stdevs['L'][i] * \
            math.exp(tau_p*random_gaussian() + tau * random_gaussian())
        aux['J'][i] = stdevs['J'][i] * \
            math.exp(tau_p*random_gaussian() + tau * random_gaussian())
        aux['LAM'][i] = stdevs['LAM'][i] * \
            math.exp(tau_p*random_gaussian() + tau * random_gaussian())
    return aux


def mutate(parent, problem_size):
    child = {}
    child['solution'] = mutate_problem(
        problem_size, parent['solution'], parent['strategy'])
    child['strategy'] = mutate_strategy(parent['strategy'], problem_size)
    return child


def init_pop(problem_size, pop_size):
    pop = []
    for i in range(pop_size):
        aux = {
            'solution': create_solution(problem_size),
            'strategy': create_strategy(problem_size)
        }
        pop.append(aux)
    return pop


def search(max_gen, pop_size, problem_size, num_children):
    gen = 0
    error = []
    pop = init_pop(problem_size, pop_size)
    fitness_function(gen, pop)
    pop.sort(key=lambda x: x['Error'])
    best = pop[0]
    error.append(best['Error'])
    while gen < max_gen:
        children = []
        for i in range(num_children):
            children.append(mutate(pop[i], problem_size))
        fitness_function(gen, children)
        union = children + pop
        union.sort(key=lambda x: x['Error'])
        if union[0]['Error'] < best['Error']:
            best = union[0]
        error.append(best['Error'])
        pop = union[:pop_size]
        print('Gen: {}, Error:{}'.format(gen, best['Error']))
        gen += 1
    return best['solution'], error


def main():
    max_gen = 100
    pop_size = 30
    problem_size = 6
    num_children = 20
    solution, error = search(max_gen, pop_size, problem_size, num_children)
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
