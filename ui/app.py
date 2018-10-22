from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from ui import (UIEvolutionary, UIImmune, UIPhysical,
                UIProbabilistic, UIStochastic, UISwarm, UIParallel)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Algoritmos evolutivos'
        self.left = 50
        self.top = 50
        self.width = 720
        self.height = 540
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.tabs.resize(300, 200)
        self.tabs.addTab(UIEvolutionary(), 'Evolutionary')
        self.tabs.addTab(UIImmune(), 'Immune')
        self.tabs.addTab(UIPhysical(), 'Physical')
        self.tabs.addTab(UIProbabilistic(), 'Probabilistic')
        self.tabs.addTab(UIStochastic(), 'Stochastic')
        self.tabs.addTab(UISwarm(), 'Swarm')
        self.tabs.addTab(UIParallel(), 'Parallel')
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
