from PyQt5.QtWidgets import QTabWidget
from ui.physical_a import UIHarmony, UIMemetic


class UIPhysical(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addTab(UIHarmony(), 'Harmony search')
        self.addTab(UIMemetic(), 'Memetic')
