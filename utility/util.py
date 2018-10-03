import numpy as np


def rand_bound(low, high, size=None):
    return np.random.uniform(low, high, size)


def randint_bound(low, high=None, size=None):
    return np.random.randint(low, high, size)


def rand():
    return np.random.rand()


def choice(a, size):
    return np.random.choice(a, size, replace=False)
