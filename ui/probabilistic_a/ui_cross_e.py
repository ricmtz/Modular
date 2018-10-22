from PyQt5.QtWidgets import QLabel, QLineEdit
from ui.model import Form
from probabilistic import CrossEntropy
from utility import Runner

MAX_GEN = 5
NUM_SAMPLES = 50
NUM_UPDATE = 10
LEARNING_R = 0.7


class UICrossEntropy(Form):
    def __init__(self):
        super().__init__('Cross Entropy')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.num_samples = QLineEdit(str(NUM_SAMPLES))
        self.num_update = QLineEdit(str(NUM_UPDATE))
        self.learning_r = QLineEdit(str(LEARNING_R))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)
        self.form.addRow(QLabel('Num. samples:'), self.num_samples)
        self.form.addRow(QLabel('NUM. update:'), self.num_update)
        self.form.addRow(QLabel('Learning rate:'), self.learning_r)

    def run_algorithm(self):
        max_gen = int(self.max_gen.text())
        num_samples = int(self.num_samples.text())
        num_update = int(self.num_update.text())
        learning_r = float(self.learning_r.text())
        algorithm = CrossEntropy(max_gen, num_samples, num_update, learning_r)
        val, t_time = Runner.run_algorithm(algorithm, self.title)
        self.print_results(val, t_time)
