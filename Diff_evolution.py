from scipy.io import loadmat

FILE_PARAM = loadmat('mediciones.mat')

I_ALPHA = FILE_PARAM['ia']  # Stator current
I_BETA = FILE_PARAM['ib']  # Stator current
CI = FILE_PARAM['ic']  # Load torque
W = FILE_PARAM['vel']  # Speed

P = 2  # Poles number
U_ALPHA = 5  # Estandor's voltage
U_BETA = 5  # Estandor's voltage
F = 0.5  # Friction coefficient


def objective_function():
    pass


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


def search():
    pass


def main():
    pass


if __name__ == '__main__':
    main()
