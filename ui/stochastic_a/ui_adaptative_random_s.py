from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox
from ui.model import Form
from stochastic import AdaptativeRandomS
from utility import Runner

MAX_GEN = 25
INIT_F = 0.05
S_FACTOR = 1.3
L_FACTOR = 3.0
ITER_MULT = 10
MAX_NO_IMPR = 30


class UIAdaptativeRandomS(Form):
    def __init__(self):
        super().__init__('Adaptative Random Search')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.init_f = QLineEdit(str(INIT_F))
        self.s_factor = QLineEdit(str(S_FACTOR))
        self.l_factor = QLineEdit(str(L_FACTOR))
        self.iter_mult = QLineEdit(str(ITER_MULT))
        self.max_no_impr = QLineEdit(str(MAX_NO_IMPR))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)
        self.form.addRow(QLabel('Init factor:'), self.init_f)
        self.form.addRow(QLabel('Small factor:'), self.s_factor)
        self.form.addRow(QLabel('Large factor:'), self.l_factor)
        self.form.addRow(QLabel('Iter factor:'), self.iter_mult)
        self.form.addRow(QLabel('Max. number of changes:'), self.max_no_impr)

    def run_algorithm(self):
        try:
            max_gen = int(self.max_gen.text())
            init_f = float(self.init_f.text())
            s_factor = float(self.s_factor.text())
            l_factor = float(self.l_factor.text())
            iter_mult = int(self.iter_mult.text())
            max_no_impr = int(self.max_no_impr.text())
            algorithm = AdaptativeRandomS(
                max_gen, init_f, s_factor, l_factor, iter_mult, max_no_impr)
            val, t_time = Runner.run_algorithm(algorithm, self.title)
            self.print_results(val, t_time)
        except ValueError as error:
            QMessageBox.warning(self, 'Value error',
                                'Invalid input:'+str(error))
