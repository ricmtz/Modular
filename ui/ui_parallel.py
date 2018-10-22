from PyQt5.QtWidgets import QTabWidget
from ui.parallel_a import UIGeneticParallel, UIDiffEvolutionParallel


class UIParallel(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addTab(UIGeneticParallel(), 'Genetic')
        self.addTab(UIDiffEvolutionParallel(), 'Differential')
