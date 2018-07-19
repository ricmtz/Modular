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


def create_pop(pop_size: int, problem_size: int) -> list:
    population = []
    for _ in range(pop_size):
        population.append(create_solution(problem_size))
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
        if w < 1:
            break
    w = math.sqrt((-2.0 * math.log10(w)) / w)
    return mean + (u2 * w) * stdev


def generate_sample(problem_size, means, stdevs):
    """
    Parameters
    ----------.
    problem_size : int

    means : dict

    stdevs : dict
    """
    aux = {
        'R': np.zeros(problem_size),
        'L': np.zeros(problem_size),
        'J': np.zeros(problem_size),
        'LAM': np.zeros(problem_size)
    }
    for i in range(problem_size):
        aux['R'][i] = random_gaussian(means['R'][i], stdevs['R'][i])
        aux['R'][i] = R_MIN if aux['R'][i] < R_MIN else aux['R'][i]
        aux['R'][i] = R_MAX if aux['R'][i] > R_MAX else aux['R'][i]
        aux['L'][i] = random_gaussian(means['L'][i], stdevs['L'][i])
        aux['L'][i] = L_MIN if aux['L'][i] < L_MIN else aux['L'][i]
        aux['L'][i] = L_MAX if aux['L'][i] > L_MAX else aux['L'][i]
        aux['J'][i] = random_gaussian(means['J'][i], stdevs['J'][i])
        aux['J'][i] = J_MIN if aux['J'][i] < J_MIN else aux['J'][i]
        aux['J'][i] = J_MAX if aux['J'][i] > J_MAX else aux['J'][i]
        aux['LAM'][i] = random_gaussian(means['LAM'][i], stdevs['LAM'][i])
        aux['LAM'][i] = LAM_MIN if aux['LAM'][i] < LAM_MIN else aux['LAM'][i]
        aux['LAM'][i] = LAM_MAX if aux['LAM'][i] > LAM_MAX else aux['LAM'][i]
    return aux


def mean_attr(samples, i, param):
    """
    Parameters
    ----------
    samples : list

    i : int

    param : string
    """
    r = 0
    for s in samples:
        r += s[param][i]
    return (r / float(len(samples)))


def stdev_attr(samples, mean, i, param):
    """
    Parameters
    ----------
    samples : list

    mean : float

    i : int

    param : string
    """
    r = 0
    for s in samples:
        r += (s[param][i] - mean) ** 2
    return math.sqrt(r / float(len(samples)))


def update_distribution(samples, alpha, problem_size, means, stdevs):
    """
    Parameters
    ----------
    samples: list

    alpha : float

    problem_size : int

    means : dict

    stdevs : dict
    """
    for i in range(problem_size):
        means['R'][i] = (alpha * means['R'][i] +
                         ((1.0 - alpha) * mean_attr(samples, i, 'R')))
        stdevs['R'][i] = (alpha * stdevs['R'][i] +
                          ((1.0 - alpha) * stdev_attr(samples,
                                                      means['R'][i], i, 'R')))
        means['L'][i] = (alpha * means['L'][i] +
                         ((1.0 - alpha) * mean_attr(samples, i, 'L')))
        stdevs['L'][i] = (alpha * stdevs['L'][i] +
                          ((1.0 - alpha) * stdev_attr(samples,
                                                      means['L'][i], i, 'L')))
        means['J'][i] = (alpha * means['J'][i] +
                         ((1.0 - alpha) * mean_attr(samples, i, 'J')))
        stdevs['J'][i] = (alpha * stdevs['J'][i] +
                          ((1.0 - alpha) * stdev_attr(samples,
                                                      means['J'][i], i, 'J')))
        means['LAM'][i] = (alpha * means['LAM'][i] +
                           ((1.0 - alpha) * mean_attr(samples, i, 'LAM')))
        stdevs['LAM'][i] = (alpha * stdevs['LAM'][i] +
                            ((1.0 - alpha) * stdev_attr(samples,
                                                        means['LAM'][i],
                                                        i, 'LAM')))


def search(problem_size, max_iter, num_samples, num_update, learning_r):
    """
    Parameters
    ----------
    problem_size : int

    max_iter : int

    num_samples : int

    num_update : int

    learning_r : float
    """
    error = []
    means = create_solution(problem_size)
    stdevs = {
        'R': np.full(problem_size, R_MAX - R_MIN),
        'L': np.full(problem_size, L_MAX - L_MIN),
        'J': np.full(problem_size, J_MAX - J_MIN),
        'LAM': np.full(problem_size, LAM_MAX - LAM_MIN)
    }
    best = None
    for i in range(max_iter):
        samples = [generate_sample(problem_size, means, stdevs)
                   for _ in range(num_samples)]
        fitness_function(i, samples)
        samples.sort(key=lambda s: s['Error'])
        if best is None or samples[0]['Error'] < best['Error']:
            best = samples[0]
        error.append(best['Error'])
        selected = samples[:num_update]
        update_distribution(selected, learning_r, problem_size, means, stdevs)
        print('Gen:{}, Error:{}'.format(i, best['Error']))
    return best, error


def main():
    problem_size = 6
    max_iter = 100
    num_samples = 100
    num_update = 20
    learning_r = 0.0007
    solution, error = search(problem_size, max_iter,
                             num_samples, num_update, learning_r)
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
            w.append(w_function(i, solution['J'][i], solution['LAM'][i]))
            ia.append(i_alpha_function(
                j, solution['R'][i], solution['L'][i], solution['LAM'][i]))
            ib.append(i_beta_function(
                j, solution['R'][i], solution['L'][i], solution['LAM'][i]))
        ax1.plot(time, ia, 'b-')
        ax2.plot(time, ib, 'b-')
        ax3.plot(time, w, 'b-')
    ax4.plot(range(len(error)), error, 'r-')
    ax4.set_title('Evolucion')
    plt.show()


if __name__ == '__main__':
    main()
