import numpy as np
from scipy.io import loadmat


SAMPLES = 3600
FILE_PARAM = loadmat('mediciones.mat')

# Search space of the parameters
R_MIN = 0.4
R_MAX = 1.2
L_MIN = 0.00010
L_MAX = 0.00020
J_MIN = 0.00015
J_MAX = 0.00030
LAM_MIN = 0.1090
LAM_MAX = 0.1107


def get_param(name):
    return np.asarray(FILE_PARAM[name][0][:SAMPLES]).reshape(-1, 1)


class Parameter:
    # Parameters from file.
    TIME = get_param('time')
    I_ALPHA = get_param('ia')
    I_BETA = get_param('ib')
    THETA = get_param('vel')
    CI = get_param('ic')

    P = 2  # Poles number
    U_ALPHA = 5  # Estandor's voltage
    U_BETA = 5  # Estandor's voltage
    F = 0.9  # Friction coefficient

    BOUNDS = [(R_MIN, R_MAX), (L_MIN, L_MAX),
              (J_MIN, J_MAX), (LAM_MIN, LAM_MAX)]

    @staticmethod
    def get_bounds():
        return Parameter.BOUNDS

    @staticmethod
    def get_i_alpha_at(time):
        return Parameter.I_ALPHA[time]

    @staticmethod
    def get_i_beta_at(time):
        return Parameter.I_BETA[time]

    @staticmethod
    def get_ci_at(time):
        return Parameter.CI[time]

    @staticmethod
    def get_theta_at(time):
        return Parameter.THETA[time]

    @staticmethod
    def get_length():
        return len(Parameter.TIME)
