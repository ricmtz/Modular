import numpy as np
from models import Citizen
from utility import rand


class Antibody(Citizen):
    def __init__(self, bitstring='', params=[], bits_per_param=32):
        self.bits_per_param = bits_per_param
        self.bitstring = bitstring if bitstring else self.random_bitstring()
        self.affinity = np.inf
        super().__init__(self.decode(self.bitstring))

    def random_bitstring(self):
        return ['0' if rand() < 0.5 else '1'
                for i in range(self.P_SIZE * self.bits_per_param)]

    def decode(self, bitstring):
        vector = []
        for i, bounds in enumerate(self.BOUNDS):
            off, r_sum = i*self.bits_per_param, 0.0
            param = list(reversed(bitstring[off:off+self.bits_per_param]))
            for j in range(len(param)):
                r_sum += (float(param[j])*(2.0**float(j)))
            r_min, r_max = bounds
            vector.append(
                r_min + ((r_max-r_min) /
                         ((2.0**float(self.bits_per_param))-1.0)) * r_sum)
        return vector

    def get_bitstrig(self):
        return self.bitstring

    def get_affinity(self):
        return self.affinity

    def set_affinity(self, affinity):
        self.affinity = affinity
