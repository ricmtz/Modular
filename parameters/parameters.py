from scipy.io import loadmat


class Parameter(object):
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
