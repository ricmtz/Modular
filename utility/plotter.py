import matplotlib.pyplot as plt

from parameters import Function as func
from parameters import Parameter as parm


class Plotter(object):
    @staticmethod
    def plot_result(r, l, j, lam, error, title=''):
        time = parm.TIME
        plt.suptitle(title)
        ax1 = plt.subplot(2, 2, 1)
        ax2 = plt.subplot(2, 2, 2)
        ax3 = plt.subplot(2, 2, 3)
        ax4 = plt.subplot(2, 2, 4)
        ax1.plot(time, parm.I_ALPHA, 'r-')
        ax1.set_title('Alpha')
        ax2.plot(time, parm.I_BETA, 'r-')
        ax2.set_title('Beta')
        ax3.plot(time, parm.THETA, 'r-')
        ax3.set_title('W')
        ax4.plot(range(len(error)), error, 'r-')
        ax4.set_title('Evolucion')
        ax4.semilogy()
        ia, ib, w = func.calc_values(r, l, j, lam)
        ax1.plot(time, ia, 'b-')
        ax2.plot(time, ib, 'b-')
        ax3.plot(time, w, 'b-')        
        plt.show()
