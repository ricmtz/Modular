from PyQt5.QtWidgets import QTabWidget
from ui.stochastic_a import UIAdaptativeRandomS, UIHillClimbing, UIRandomSearch


class UIStochastic(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addTab(UIAdaptativeRandomS(), 'Adaptative random search')
        self.addTab(UIHillClimbing(), 'Hill climbing')
        self.addTab(UIRandomSearch(), 'Random search')
