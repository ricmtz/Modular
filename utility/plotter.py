import matplotlib.pyplot as plt
import numpy as np

from parameters import Function as func
from parameters import Parameter as parm
from utility import Saver


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
    def plot_result_p(r, l, j, lam, errors, title=''):
        plt.suptitle(title)
        ia, ib, w = func.calc_values(r, l, j, lam)
        Plotter.__plot_ia(ia)
        Plotter.__plot_ib(ib)
        Plotter.__plot_w(w)
        Plotter.__plot_errors(errors)
        plt.show()

    @staticmethod
    def __plot_ia(ia):
        ia_plt = plt.subplot(2, 2, 1)
        ia_plt.set_title('Alpha')
        ia_plt.plot(parm.TIME, parm.I_ALPHA, 'r-', label='Original')
        ia_plt.plot(parm.TIME, ia, 'b-', label='Predict')
        ia_plt.legend()

    @staticmethod
    def __plot_ib(ib):
        ib_plt = plt.subplot(2, 2, 2)
        ib_plt.set_title('Beta')
        ib_plt.plot(parm.TIME, parm.I_BETA, 'r-', label='Original')
        ib_plt.plot(parm.TIME, ib, 'b-', label='Predict')
        ib_plt.legend()

    @staticmethod
    def __plot_w(w):
        w_plt = plt.subplot(2, 2, 3)
        w_plt.set_title('W')
        w_plt.plot(parm.TIME, parm.THETA, 'r-', label='Original')
        w_plt.plot(parm.TIME, w, 'b-', label='Predict')
        w_plt.legend()

    @staticmethod
    def __plot_error(error):
        ax4 = plt.subplot(2, 2, 4)
        ax4.set_title('Evolucion')
        ax4.plot(range(len(error)), error, 'r-')
        ax4.semilogy()

    @staticmethod
    def __plot_errors(errors):
        colors = iter(plt.cm.rainbow(np.linspace(0, 1, len(errors))))
        ax4 = plt.subplot(2, 2, 4)
        ax4.set_title('Evolucion')
        for t, values in errors.items():
            cl = next(colors)
            x = range(len(values))
            plt.plot(x, values, color=cl, label=t)
        ax4.semilogy()
        ax4.legend()

    @staticmethod
    def plot_evolution():
        data = Saver.get_results()
        colors = iter(plt.cm.rainbow(np.linspace(0, 1, len(data))))
        for algorithm, values in data.items():
            cl = next(colors)
            x = range(len(values['evolution']))
            plt.plot(x, values['evolution'], color=cl, label=algorithm)
        plt.semilogy()
        plt.legend()
        plt.show()
