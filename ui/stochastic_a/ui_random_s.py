from PyQt5.QtWidgets import QLabel, QLineEdit
from ui.model import Form
from stochastic import RandomSearch
from utility import Runner

MAX_GEN = 25


class UIRandomSearch(Form):
    def __init__(self):
        super().__init__('Random Search')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)

    def run_algorithm(self):
        max_gen = int(self.max_gen.text())
        algorithm = RandomSearch(max_gen)
        val, t_time = Runner.run_algorithm(algorithm, self.title)
        self.print_results(val, t_time)
