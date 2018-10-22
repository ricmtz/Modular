from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox
from ui.model import Form
from evolutionary import GenParallelAlgorithm
from utility import Runner

POP_SIZE = 20
BEST_P = 10
MAX_GEN = 5
P_M = 5
NUM_THREADS = 3


class UIGeneticParallel(Form):
    def __init__(self):
        super().__init__('Genetic evolution parallel')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.pop_size = QLineEdit(str(POP_SIZE))
        self.best_pop = QLineEdit(str(BEST_P))
        self.p_m = QLineEdit(str(P_M))
        self.num_threads = QLineEdit(str(NUM_THREADS))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)
        self.form.addRow(QLabel('Population size:'), self.pop_size)
        self.form.addRow(QLabel('Best population:'), self.best_pop)
        self.form.addRow(QLabel('Percent mutant:'), self.p_m)
        self.form.addRow(QLabel('Num. threads:'), self.num_threads)

    def run_algorithm(self):
        try:
            pop_size = int(self.pop_size.text())
            best_p = int(self.best_pop.text())
            max_gen = int(self.max_gen.text())
            p_m = float(self.p_m.text())
            num_threads = int(self.num_threads.text())
            algorithm = GenParallelAlgorithm(
                pop_size, best_p, max_gen, p_m, num_threads)
            bests, t_time = Runner.run_algorithm_p(algorithm, self.title)
            self.print_results_p(bests, t_time)
        except ValueError as error:
            QMessageBox.warning(self, 'Value error',
                                'Invalid input:'+str(error))
