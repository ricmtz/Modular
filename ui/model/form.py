from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QFormLayout,
                             QLabel, QPlainTextEdit, QPushButton, QHBoxLayout)
from PyQt5.QtGui import QFont


class Form(QWidget):
    def __init__(self, title=''):
        super().__init__()
        self.title = title
        self.initUI()

    def initUI(self):
        # Layouts
        self.main_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.form = QFormLayout()
        # Widgets
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)
        font_o = QFont()
        font_o.setBold(True)
        font_o.setPointSize(10)
        self.name = QLabel(self.title)
        self.name.setFont(font)
        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        self.output.setFont(font_o)
        self.run = QPushButton('Run Algorithm')
        self.clear = QPushButton('Clear')
        self.run.setMinimumSize(100, 30)
        self.clear.setMinimumSize(100, 30)
        self.generate_fields()
        # Setup main layout
        self.main_layout.addWidget(self.name)
        self.main_layout.addLayout(self.form)
        self.main_layout.addWidget(self.output)
        self.main_layout.addLayout(self.h_layout)
        # Setup h layout
        self.h_layout.addStretch()
        self.h_layout.addWidget(self.clear)
        self.h_layout.addWidget(self.run)
        self.setLayout(self.main_layout)
        # Conecting button.
        self.run.clicked.connect(self.run_algorithm)
        self.clear.clicked.connect(self.clear_output)
        self.show()

    def generate_fields(self):
        raise NotImplementedError

    def run_algorithm(self):
        raise NotImplementedError

    def clear_output(self):
        self.output.clear()

    def print_results(self, values, t_time):
        self.output.appendPlainText('Results:')
        self.print_values(values)
        self.output.appendPlainText('Time: {}'.format(t_time))
        self.output.appendPlainText('')

    def print_results_p(self, bests, t_time):
        self.output.appendPlainText('Results:')
        for i, best in bests.items():
            self.output.appendPlainText('Thread: {}'.format(i))
            self.print_values(best.get_values())
        self.output.appendPlainText('Time: {}'.format(t_time))
        self.output.appendPlainText('')

    def print_values(self, values):
        self.output.appendPlainText('R: {}'.format(values[0]))
        self.output.appendPlainText('L: {}'.format(values[1]))
        self.output.appendPlainText('J: {}'.format(values[2]))
        self.output.appendPlainText('Lam: {}'.format(values[3]))
