from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox
from ui.model import Form
from evolutionary import EvolutionStrat
from utility import Runner

MAX_GEN = 5
POP_SIZE = 30
NUM_CHILDREN = 20


class UIEvolutionStrat(Form):
    def __init__(self):
        super().__init__('Evolution Strategies')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.pop_size = QLineEdit(str(POP_SIZE))
        self.num_children = QLineEdit(str(NUM_CHILDREN))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)
        self.form.addRow(QLabel('Population size:'), self.pop_size)
        self.form.addRow(QLabel('Num. children:'), self.num_children)

    def run_algorithm(self):
        try:
            max_gen = int(self.max_gen.text())
            pop_size = int(self.pop_size.text())
            num_children = int(self.num_children.text())
            algorithm = EvolutionStrat(max_gen, pop_size, num_children)
            val, t_time = Runner.run_algorithm(algorithm, self.title)
            self.print_results(val, t_time)
        except ValueError as error:
            QMessageBox.warning(self, 'Value error',
                                'Invalid input:'+str(error))
