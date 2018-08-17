import numpy as np
from parameters import Parameter as parm


class CitizenM(object):

    def __init__(self, bitstring=None, vector=None, bounds=parm.get_bounds(),
                 num_bits=64,):
        if not bitstring:
            self.bitstring = self.__rand_bitstring(num_bits)
        else:
            self.bitstring = bitstring
        if not vector:
            self.vector = self.__decode(bounds)
        else:
            self.vector = vector
        self.error = np.inf

    def __rand_bitstring(self, num_bits):
        return ['0' if np.random.rand() < .5 else '1' for _ in range(num_bits)]

    def __decode(self, bounds, bits_per_param=16):
        vector = []
        for i, bounds in enumerate(bounds):
            off, r_sum = i*bits_per_param, 0.0
            param = list(reversed(self.bitstring[off:off+bits_per_param]))
            for j in range(len(param)):
                r_sum += (float(param[j])*(2.0**float(j)))
            r_min, r_max = bounds
            vector.append(
                r_min + ((r_max-r_min)/(
                    (2.0**float(bits_per_param))-1.0)) * r_sum)
        return vector

    def set_error(self, error):
        self.error = error

    def get_error(self):
        return self.error

    def get_values(self):
        return self.vector

    def get_bitstring(self):
        return self.bitstring
