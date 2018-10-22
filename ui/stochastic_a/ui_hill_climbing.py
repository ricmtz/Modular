from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox
from ui.model import Form
from stochastic import HillClimbing
from utility import Runner

MAX_GEN = 25


class UIHillClimbing(Form):
    def __init__(self):
        super().__init__('Hill Climbing')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)

    def run_algorithm(self):
        try:
            max_gen = int(self.max_gen.text())
            algorithm = HillClimbing(max_gen)
            val, t_time = Runner.run_algorithm(algorithm, self.title)
            self.print_results(val, t_time)
        except ValueError as error:
            QMessageBox.warning(self, 'Value error',
                                'Invalid input:'+str(error))
