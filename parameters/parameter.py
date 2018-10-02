from scipy.io import loadmat
import numpy as np
# from sklearn.preprocessing import MinMaxScaler
from .scaler import Scaler as sc

T_SAMPLES = 3500
FILE_PARAM = loadmat('mediciones.mat')


class Parameter(object):

    # I_ALPHA_S = MinMaxScaler(feature_range=(-1, 1))
    # I_BETA_S = MinMaxScaler(feature_range=(-1, 1))
    # THETA_S = MinMaxScaler(feature_range=(-1, 1))
    # CI_S = MinMaxScaler(feature_range=(-1, 1))

    TIME = np.asarray(FILE_PARAM['time'][0][:T_SAMPLES])
    # Stator current
    I_ALPHA = np.asarray(FILE_PARAM['ia'][0][:T_SAMPLES])
    I_ALPHA = sc.transform(I_ALPHA)
    # Stator current
    I_BETA = np.asarray(FILE_PARAM['ib'][0][:T_SAMPLES])
    I_BETA = sc.transform(I_BETA)
    # Speed
    THETA = np.asarray(FILE_PARAM['vel'][0][:T_SAMPLES])
    THETA = sc.transform(THETA)
    # Load torque
    CI = np.asarray(FILE_PARAM['ic'][0][:T_SAMPLES])
    CI = sc.transform(CI)

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
