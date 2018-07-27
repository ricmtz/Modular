import math
from scipy.linalg import norm
from .parameter import Parameter as parm


class Function(object):

    @staticmethod
    def func_w(i_time, j, lam):
        """
        Parameters
        ----------
        i_time: int

        j : float

        lam : float
        """
        ia = parm.get_i_alpha(i_time)
        ib = parm.get_i_beta(i_time)
        theta = parm.get_theta(i_time)
        ci = parm.get_ci(i_time)
        w = lam/j*(-ia * math.sin(parm.P)*theta + ib *
                   math.cos(parm.P)*theta) - parm.F/j * theta - ci/j
        return w*.0001 - 0.04

    @staticmethod
    def func_i_alpha(i_time, r, l, lam, w):
        """
        Parameters
        ----------
        i_time : int

        r : float

        l : float

        lam : float
        """
        ia = parm.get_i_alpha(i_time)
        theta = parm.get_theta(i_time)
        d_ia = r/l*ia+parm.P*lam/l*w*math.sin(theta)+1/l*parm.U_ALPHA
        return d_ia*.0001 - 4.1

    @staticmethod
    def func_i_beta(i_time, r, l, lam, w):
        """
        Parameters
        ----------
        i_time : int

        r : float

        l : float

        lam : float
        """
        ib = parm.get_i_beta(i_time)
        theta = parm.get_theta(i_time)
        d_ib = r/l*ib+parm.P*lam/l*w*math.cos(theta)+1/l*parm.U_BETA
        return d_ib*.0001 - 4.1

    @staticmethod
    def calc_error(i_time, r, l, j, lam):
        """
        Parameters
        ----------
        i_time : int

        r : float

        l : float

        j : float

        lam : float
        """
        ia = parm.get_i_alpha(i_time)
        ib = parm.get_i_beta(i_time)
        w = parm.get_theta(i_time)
        wp = Function.func_w(i_time, j, lam)
        iap = Function.func_i_alpha(i_time, r, l, lam, wp)
        ibp = Function.func_i_beta(i_time, r, l, lam, wp)
        error = (norm(ia) - norm(iap)) + \
            (norm(ib) - norm(ibp)) + (norm(w - wp))
        return error ** 2
