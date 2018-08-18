import matplotlib.pyplot as plt

from parameters import Parameter as parm
from parameters import Function as func


class Plotter(object):

    PLT_S = 0
    PLT_E = int(len(parm.I_ALPHA)/5)

    @staticmethod
    def plot_functions(r, l, j, lam, error):
        ia = []
        ib = []
        w = []
        time = parm.TIME[Plotter.PLT_S:Plotter.PLT_E]
        ax1 = plt.subplot(2, 2, 1)
        ax2 = plt.subplot(2, 2, 2)
        ax3 = plt.subplot(2, 2, 3)
        ax4 = plt.subplot(2, 2, 4)
        ax1.plot(time, parm.I_ALPHA[Plotter.PLT_S:Plotter.PLT_E], 'r-')
        ax1.set_title('Alpha')
        ax2.plot(time, parm.I_BETA[Plotter.PLT_S:Plotter.PLT_E], 'r-')
        ax2.set_title('Beta')
        ax3.plot(time, parm.THETA[Plotter.PLT_S:Plotter.PLT_E], 'r-')
        ax3.set_title('W')
        ax4.plot(range(len(error)), error, 'r-')
        ax4.set_title('Evolucion')
        ax4.semilogy()
        for i in range(len(time)):
            ia_v, ib_v, w_v = func.calc_values(i, r, l, j, lam)
            w.append(w_v)
            ia.append(ia_v)
            ib.append(ib_v)
        ax1.plot(time, ia, 'b-')
        ax2.plot(time, ib, 'b-')
        ax3.plot(time, w, 'b-')
        plt.show()
