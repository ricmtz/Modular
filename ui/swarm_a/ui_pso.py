from PyQt5.QtWidgets import QLabel, QLineEdit
from ui.model import Form
from swarm import PSO
from utility import Runner

MAX_GEN = 5
POP_SIZE = 10


class UIPSO(Form):
    def __init__(self):
        super().__init__('PSO')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.pop_size = QLineEdit(str(POP_SIZE))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)
        self.form.addRow(QLabel('Num. particles:'), self.pop_size)

    def run_algorithm(self):
        max_gen = int(self.max_gen.text())
        pop_size = int(self.pop_size.text())
        algorithm = PSO(pop_size, max_gen)
        val, t_time = Runner.run_algorithm(algorithm, self.title)
        self.print_results(val, t_time)
