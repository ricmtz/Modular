import math

import numpy as np
from scipy.linalg import norm

from parameters import Parameter as parm
from parameters import Scaler as sc


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
        return w

    @staticmethod
    def func_i_alpha(r, l, lam, w):
        d_ia = []
        for i in range(len(parm.TIME)):
            ia = parm.get_i_alpha_at(i)
            w = theta = parm.get_theta_at(i)
            d_ia.append(r/l*ia+parm.P*lam/l*w*math.sin(theta)+1/l*parm.U_ALPHA)
        d_ia = np.asarray(d_ia)
        return d_ia

    @staticmethod
    def func_i_beta(r, l, lam, w):
        d_ib = []
        for i in range(len(parm.TIME)):
            ib = parm.get_i_beta_at(i)
            w = theta = parm.get_theta_at(i)
            d_ib.append(r/l*ib+parm.P*lam/l*w *
                        math.cos(theta)+1/l*parm.U_BETA)
        d_ib = np.asarray(d_ib)
        return d_ib

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
        w = (sc.transform(Function.func_w(j, lam))) - 0.6
        ia = (sc.transform(Function.func_i_alpha(r, l, lam, w))) - 0.1
        ib = (sc.transform(Function.func_i_beta(r, l, lam, w))) + 0.1
        return ia, ib, w
