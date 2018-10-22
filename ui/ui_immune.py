from PyQt5.QtWidgets import QTabWidget
from ui.immune_a import UIClonalSelection, UIImmuneNetwork


class UIImmune(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addTab(UIClonalSelection(), 'Clonal selection')
        self.addTab(UIImmuneNetwork(), 'Immune network')
