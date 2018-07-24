from scipy.io import loadmat
import numpy as np


class Parameter(object):
    FILE_PARAM = loadmat('mediciones.mat')

    I_ALPHA = FILE_PARAM['ia'][0]  # Stator current
    I_BETA = FILE_PARAM['ib'][0]  # Stator current
    CI = FILE_PARAM['ic'][0]  # Load torque
    THETA = FILE_PARAM['vel'][0]  # Speed

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

    @staticmethod
    def get_rand_R():
        return np.random.uniform(Parameter.R_MIN, Parameter.R_MAX)

    @staticmethod
    def get_rand_L():
        return np.random.uniform(Parameter.L_MIN, Parameter.L_MAX)

    @staticmethod
    def get_rand_J():
        return np.random.uniform(Parameter.J_MIN, Parameter.J_MAX)

    @staticmethod
    def get_rand_LAM():
        return np.random.uniform(Parameter.LAM_MIN, Parameter.LAM_MAX)

    @staticmethod
    def get_i_alpha(time):
        return Parameter.I_ALPHA[time]

    @staticmethod
    def get_i_beta(time):
        return Parameter.I_BETA[time]

    @staticmethod
    def get_ci(time):
        return Parameter.CI[time]

    @staticmethod
    def get_theta(time):
        return Parameter.THETA[time]


def main():
    print(Parameter.I_ALPHA)


if __name__ == '__main__':
    main()
