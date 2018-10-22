from PyQt5.QtWidgets import QLabel, QLineEdit
from ui.model import Form
from immune import ImmuneNetwork
from utility import Runner

MAX_GEN = 5
POP_SIZE = 30
NUM_CLONES = 10
BETA = 100
NUM_RAND = 2


class UIImmuneNetwork(Form):
    def __init__(self):
        super().__init__('Immune Network')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.pop_size = QLineEdit(str(POP_SIZE))
        self.num_clones = QLineEdit(str(NUM_CLONES))
        self.beta = QLineEdit(str(BETA))
        self.num_rand = QLineEdit(str(NUM_RAND))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)
        self.form.addRow(QLabel('Population size:'), self.pop_size)
        self.form.addRow(QLabel('Num. clones:'), self.num_clones)
        self.form.addRow(QLabel('Beta:'), self.beta)
        self.form.addRow(QLabel('Num. random insertions:'), self.num_rand)

    def run_algorithm(self):
        max_gen = int(self.max_gen.text())
        pop_size = int(self.pop_size.text())
        num_clones = int(self.num_clones.text())
        beta = int(self.beta.text())
        num_rand = int(self.num_rand.text())
        algorithm = ImmuneNetwork(
            max_gen, pop_size, num_clones, beta, num_rand)
        val, t_time = Runner.run_algorithm(algorithm, self.title)
        self.print_results(val, t_time)
