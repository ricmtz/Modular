import matplotlib.pyplot as plt

from parameters import Function as func
from parameters import Parameter as parm


class Plotter(object):
    @staticmethod
    def plot_result(r, l, j, lam, error, title=''):
        plt.suptitle(title)
        ia, ib, w = func.calc_values(r, l, j, lam)
        Plotter.__plot_ia(ia)
        Plotter.__plot_ib(ib)
        Plotter.__plot_w(w)
        Plotter.__plot_error(error)
        plt.show()

    @staticmethod
    def __plot_ia(ia):
        ia_plt = plt.subplot(2, 2, 1)
        ia_plt.set_title('Alpha')
        ia_plt.plot(parm.TIME, parm.I_ALPHA, 'r-')
        ia_plt.plot(parm.TIME, ia, 'b-')

    @staticmethod
    def __plot_ib(ib):
        ax2 = plt.subplot(2, 2, 2)
        ax2.set_title('Beta')
        ax2.plot(parm.TIME, parm.I_BETA, 'r-')
        ax2.plot(parm.TIME, ib, 'b-')

    @staticmethod
    def __plot_w(w):
        ax3 = plt.subplot(2, 2, 3)
        ax3.set_title('W')
        ax3.plot(parm.TIME, parm.THETA, 'r-')
        ax3.plot(parm.TIME, w, 'b-')

    @staticmethod
    def __plot_error(error):
        ax4 = plt.subplot(2, 2, 4)
        ax4.set_title('Evolucion')
        ax4.plot(range(len(error)), error, 'r-')
        ax4.semilogy()
