import math

import numpy as np
from scipy.linalg import norm

from parameters import Parameter as parm


SCALER = 0.00014


class Function(object):

    @staticmethod
    def func_w(j, lam):
        w = []
        for i in range(len(parm.TIME)):
            ia = parm.get_i_alpha_at(i)
            ib = parm.get_i_beta_at(i)
            theta = parm.get_theta_at(i)
            ci = parm.get_ci_at(i)
            w.append(-(lam/j*(-ia * math.sin(parm.P)*theta + ib *
                              math.cos(parm.P)*theta) - parm.F/j *
                       theta - ci/j))
        w = np.asarray(w)
        return w * SCALER

    @staticmethod
    def func_i_alpha(r, l, lam):
        ia_p = []
        for i in range(len(parm.TIME)):
            ia = parm.get_i_alpha_at(i)
            w = theta = parm.get_theta_at(i)
            ia_p.append(r/l*ia+parm.P*lam/l*w*math.sin(theta)+1/l*parm.U_ALPHA)
        ia_p = np.asarray(ia_p)
        return ia_p * SCALER

    @staticmethod
    def func_i_beta(r, l, lam):
        ib_p = []
        for i in range(len(parm.TIME)):
            ib = parm.get_i_beta_at(i)
            w = theta = parm.get_theta_at(i)
            ib_p.append(r/l*ib+parm.P*lam/l*w *
                        math.cos(theta)+1/l*parm.U_BETA)
        ib_p = np.asarray(ib_p)
        return ib_p * SCALER

    @staticmethod
    def calc_error(r, l, j, lam):
        ia = parm.I_ALPHA
        ib = parm.I_BETA
        w = parm.THETA
        iap, ibp, wp = Function.calc_values(r, l, j, lam)
        error = (norm(ia) - norm(iap)) + \
            (norm(ib) - norm(ibp)) + (norm(w - wp))
        return (error ** 2)/parm.get_length()

    @staticmethod
    def calc_values(r, l, j, lam):
        w = Function.func_w(j, lam)
        ia = Function.func_i_alpha(r, l, lam) - 6
        ib = Function.func_i_beta(r, l, lam) - 6
        return ia, ib, w
