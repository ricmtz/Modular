from PyQt5.QtWidgets import QTabWidget
from ui.evo_a import UIGenetic, UIDiffEvolution, UIEvolutionStrat


class UIEvolutionary(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addTab(UIGenetic(), 'Genetic')
        self.addTab(UIDiffEvolution(), 'Differential')
        self.addTab(UIEvolutionStrat(), 'Evolutionary')
