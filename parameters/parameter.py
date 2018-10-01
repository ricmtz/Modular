from scipy.io import loadmat
import numpy as np


class Parameter(object):
    FILE_PARAM = loadmat('mediciones.mat')

    TIME = np.asarray(FILE_PARAM['time'][0][1000:3500])
    I_ALPHA = np.asarray(FILE_PARAM['ia'][0][1000:3500])  # Stator current
    I_BETA = np.asarray(FILE_PARAM['ib'][0][1000:3500])  # Stator current
    CI = np.asarray(FILE_PARAM['ic'][0][1000:3500])  # Load torque
    THETA = np.asarray(FILE_PARAM['vel'][0][1000:3500])  # Speed

    P = 2  # Poles number
    U_ALPHA = 5  # Estandor's voltage
    U_BETA = 5  # Estandor's voltage
    F = 0.9  # Friction coefficient

    # Search space of the parameters
    R_MIN = 0.4
    R_MAX = 1.2
    L_MIN = 0.00010
    L_MAX = 0.00020
    J_MIN = 0.00015
    J_MAX = 0.00030
    LAM_MIN = 0.1090
    LAM_MAX = 0.1107

    BOUNDS = [(R_MIN, R_MAX), (L_MIN, L_MAX),
              (J_MIN, J_MAX), (LAM_MIN, LAM_MAX)]

    @staticmethod
    def get_rand(bounds):
        return np.random.uniform(*bounds)

    @staticmethod
    def get_bounds():
        return Parameter.BOUNDS

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

    @staticmethod
    def get_length():
        return len(Parameter.TIME)
