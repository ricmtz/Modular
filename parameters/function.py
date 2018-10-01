import math
from scipy.linalg import norm
from .parameter import Parameter as parm
import numpy as np


class Function(object):

    @staticmethod
    def func_w(j, lam):
        """
        Parameters
        ----------
        j : float

        lam : float
        """
        w = []
        for i in range(len(parm.TIME)):
            ia = parm.get_i_alpha(i)
            ib = parm.get_i_beta(i)
            theta = parm.get_theta(i)
            ci = parm.get_ci(i)
            w.append(-(lam/j*(-ia * math.sin(parm.P)*theta + ib *
                              math.cos(parm.P)*theta) - parm.F/j *
                       theta - ci/j))
        w = np.asarray(w)
        return w

    @staticmethod
    def func_i_alpha(r, l, lam, w):
        """
        Parameters
        ----------
        r : float

        l : float

        lam : float
        """
        d_ia = []
        for i in range(len(parm.TIME)):
            ia = parm.get_i_alpha(i)
            w = theta = parm.get_theta(i)
            d_ia.append(r/l*ia+parm.P*lam/l*w*math.sin(theta)+1/l*parm.U_ALPHA)
        d_ia = np.asarray(d_ia)
        return d_ia

    @staticmethod
    def func_i_beta(r, l, lam, w):
        """
        Parameters
        ----------
        r : float

        l : float

        lam : float
        """
        d_ib = []
        for i in range(len(parm.TIME)):
            ib = parm.get_i_beta(i)
            w = theta = parm.get_theta(i)
            d_ib.append(r/l*ib+parm.P*lam/l*w *
                        math.cos(theta)+1/l*parm.U_BETA)
        d_ib = np.asarray(d_ib)
        return d_ib

    @staticmethod
    def calc_error(r, l, j, lam):
        """
        Parameters
        ----------
        r : float

        l : float

        j : float

        lam : float
        """
        ia = parm.I_ALPHA
        ib = parm.I_BETA
        w = parm.THETA
        iap, ibp, wp = Function.calc_values(r, l, j, lam)
        error = (norm(ia) - norm(iap)) + \
            (norm(ib) - norm(ibp)) + (norm(w - wp))
        return (error ** 2)/parm.get_length()

    @staticmethod
    def calc_values(r, l, j, lam):
        w = (parm.THETA_S.fit_transform(
            Function.func_w(j, lam).reshape(-1, 1))) - 0.5
        ia = (parm.I_ALPHA_S.fit_transform(
            Function.func_i_alpha(r, l, lam, w).reshape(-1, 1)))
        ib = (parm.I_BETA_S.fit_transform(
            Function.func_i_beta(r, l, lam, w).reshape(-1, 1)))
        return ia, ib, w
