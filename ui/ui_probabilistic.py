from PyQt5.QtWidgets import QTabWidget
from ui.probabilistic_a import UICrossEntropy


class UIProbabilistic(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addTab(UICrossEntropy(), 'Cross Entropy')
