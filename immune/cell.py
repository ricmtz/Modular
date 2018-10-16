from models import Citizen
import numpy as np


class Cell(Citizen):
    def __init__(self, params=None):
        super().__init__(params)
        self.norm_error = np.inf

    def get_norm_error(self):
        return self.norm_error

    def set_norm_error(self, norm_error):
        self.norm_error = norm_error
