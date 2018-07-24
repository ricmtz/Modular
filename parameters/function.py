from parameter import Parameter as parm
import math


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
        return w*.002

    @staticmethod
    def i_alpha_function(i_time, r, l, lam):
        """
        Parameters
        ----------
        i_time : int

        r : float

        l : float

        lam : float
        """
        ia = parm.get_i_alpha(i_time)
        w = theta = parm.get_theta(i_time)
        d_ia = r/l*ia+parm.P*lam/l*w*math.sin(theta)+1/l*parm.U_ALPHA
        return d_ia

    @staticmethod
    def i_beta_function(i_time, r, l, lam):
        """
        Parameters
        ----------
        i_time : int

        r : float

        l : float

        lam : float
        """
        ib = parm.get_i_beta(i_time)
        w = theta = parm.get_theta(i_time)
        d_ib = r/l*ib+parm.P*lam/l*w*math.cos(theta)+1/l*parm.U_BETA
        return d_ib


def main():
    print(Function.func_w(0, 0.0015, 0.1090))


if __name__ == '__main__':
    main()
