from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox
from ui.model import Form
from immune import ClonalSelection
from utility import Runner

MAX_GEN = 5
POP_SIZE = 30
CLONE_F = 0.1
NUM_RAND = 2


class UIClonalSelection(Form):
    def __init__(self):
        super().__init__('Clonal Selection')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.pop_size = QLineEdit(str(POP_SIZE))
        self.clone_f = QLineEdit(str(CLONE_F))
        self.num_rand = QLineEdit(str(NUM_RAND))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)
        self.form.addRow(QLabel('Population size:'), self.pop_size)
        self.form.addRow(QLabel('Clone factor:'), self.clone_f)
        self.form.addRow(QLabel('Num. random insertions:'), self.num_rand)

    def run_algorithm(self):
        try:
            max_gen = int(self.max_gen.text())
            pop_size = int(self.pop_size.text())
            clone_f = float(self.clone_f.text())
            num_rand = int(self.num_rand.text())
            algorithm = ClonalSelection(max_gen, pop_size, clone_f, num_rand)
            val, t_time = Runner.run_algorithm(algorithm, self.title)
            self.print_results(val, t_time)
        except ValueError as error:
            QMessageBox.warning(self, 'Value error',
                                'Invalid input:'+str(error))
