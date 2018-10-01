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
        return w*.0005 - 0.05

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
            theta = parm.get_theta(i)
            d_ia = r/l*ia+parm.P*lam/l*w*math.sin(theta)+1/l*parm.U_ALPHA
        d_ia = np.asarray(d_ia)
        return d_ia*.0005 - 4

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
            theta = parm.get_theta(i)
            d_ib = r/l*ib+parm.P*lam/l*w * \
                math.cos(theta)+1/l*parm.U_BETA
        d_ib = np.asarray(d_ib)
        return d_ib*.0005 - 4

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
        w = Function.func_w(j, lam)
        ia = Function.func_i_alpha(r, l, lam, w)
        ib = Function.func_i_beta(r, l, lam, w)
        return ia, ib, w
