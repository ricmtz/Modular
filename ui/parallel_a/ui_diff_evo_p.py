from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox
from ui.model import Form
from evolutionary import DiffEvoAlgorithm
from utility import Runner

MAX_GEN = 5
POP_SIZE = 30
WEIGHT_F = 0.2
CROSS_R = 0.7
NUM_THREADS = 3


class UIDiffEvolutionParallel(Form):
    def __init__(self):
        super().__init__('Differential Evolution Parallel')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.pop_size = QLineEdit(str(POP_SIZE))
        self.weight_f = QLineEdit(str(WEIGHT_F))
        self.cross_r = QLineEdit(str(CROSS_R))
        self.num_threads = QLineEdit(str(NUM_THREADS))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)
        self.form.addRow(QLabel('Population size:'), self.pop_size)
        self.form.addRow(QLabel('Weighting factor:'), self.weight_f)
        self.form.addRow(QLabel('Crossover rate:'), self.cross_r)
        self.form.addRow(QLabel('Num. threads:'), self.num_threads)

    def run_algorithm(self):
        try:
            max_gen = int(self.max_gen.text())
            pop_size = int(self.pop_size.text())
            weight_f = float(self.weight_f.text())
            cross_r = float(self.cross_r.text())
            num_threads = int(self.num_threads.text())
            algorithm = DiffEvoAlgorithm(
                pop_size, max_gen, weight_f, cross_r, num_threads)
            bests, t_time = Runner.run_algorithm_p(algorithm, self.title)
            self.print_results_p(bests, t_time)
        except ValueError as error:
            QMessageBox.warning(self, 'Value error',
                                'Invalid input:'+str(error))
