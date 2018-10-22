from PyQt5.QtWidgets import QLabel, QLineEdit
from ui.model import Form
from physical import Harmony
from utility import Runner

MAX_GEN = 5
MEM_SIZE = 20
CONSID_R = 0.95
ADJUST_R = 0.7
RANG = 0.05


class UIHarmony(Form):
    def __init__(self):
        super().__init__('Harmony Search')

    def generate_fields(self):
        self.max_gen = QLineEdit(str(MAX_GEN))
        self.mem_size = QLineEdit(str(MEM_SIZE))
        self.consid_r = QLineEdit(str(CONSID_R))
        self.adjust_r = QLineEdit(str(ADJUST_R))
        self.rang = QLineEdit(str(RANG))
        self.form.addRow(QLabel('Max. generations:'), self.max_gen)
        self.form.addRow(QLabel('Memory size:'), self.mem_size)
        self.form.addRow(QLabel('Considering rate:'), self.consid_r)
        self.form.addRow(QLabel('Adjustment rate:'), self.adjust_r)
        self.form.addRow(QLabel('Range:'), self.rang)

    def run_algorithm(self):
        max_gen = int(self.max_gen.text())
        mem_size = int(self.mem_size.text())
        consid_r = float(self.consid_r.text())
        adjust_r = float(self.adjust_r.text())
        rang = float(self.rang.text())
        algorithm = Harmony(max_gen, mem_size, consid_r, adjust_r, rang)
        val, t_time = Runner.run_algorithm(algorithm, self.title)
        self.print_results(val, t_time)
