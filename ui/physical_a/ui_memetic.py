from PyQt5.QtWidgets import QLabel, QLineEdit
from ui.model import Form
from physical import Memetic
from utility import Runner

MAX_GEN = 5
POP_SIZE = 20
P_CROSS = 0.98
MAX_LOCAL_GENS = 20
P_MUT = 1.0/float(64)
P_LOCAL = 0.5


class UIMemetic(Form):
    def __init__(self):
        super().__init__('Memetic')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.pop_size = QLineEdit(str(POP_SIZE))
        self.p_cross = QLineEdit(str(P_CROSS))
        self.max_local_gens = QLineEdit(str(MAX_LOCAL_GENS))
        self.p_mut = QLineEdit(str(P_MUT))
        self.p_local = QLineEdit(str(P_LOCAL))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)
        self.form.addRow(QLabel('Pop. size:'), self.pop_size)
        self.form.addRow(QLabel('Percent crossover:'), self.p_cross)
        self.form.addRow(QLabel('Max. local genes:'), self.max_local_gens)
        self.form.addRow(QLabel('Percent mutation:'), self.p_mut)
        self.form.addRow(QLabel('P. local:'), self.p_local)

    def run_algorithm(self):
        max_gen = int(self.max_gen.text())
        pop_size = int(self.pop_size.text())
        p_cross = float(self.p_cross.text())
        max_local_gens = int(self.max_local_gens.text())
        p_mut = float(self.p_mut.text())
        p_local = float(self.p_local.text())
        algorithm = Memetic(max_gen, pop_size, p_cross,
                            p_mut, max_local_gens, p_local)
        val, t_time = Runner.run_algorithm(algorithm, self.title)
        self.print_results(val, t_time)
