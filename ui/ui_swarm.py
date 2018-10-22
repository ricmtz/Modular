from PyQt5.QtWidgets import QTabWidget
from ui.swarm_a import UIPSO


class UISwarm(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addTab(UIPSO(), 'PSO')
