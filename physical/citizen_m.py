from utility import rand
from models import Citizen


class CitizenMem(Citizen):

    def __init__(self, params=None, bitstring=None, num_bits=64):
        self.bitstring = bitstring if bitstring else self.__rand_bitstring(
            num_bits)
        super().__init__(params if params else self.__decode())

    def __rand_bitstring(self, num_bits):
        return ['0' if rand() < 0.5 else '1' for _ in range(num_bits)]

    def __decode(self, bits_per_param=16):
        vector = []
        for i, bounds in enumerate(self.BOUNDS):
            off, r_sum = i*bits_per_param, 0.0
            param = list(reversed(self.bitstring[off:off+bits_per_param]))
            for j in range(len(param)):
                r_sum += (float(param[j])*(2.0**float(j)))
            r_min, r_max = bounds
            vector.append(
                r_min + ((r_max-r_min)/(
                    (2.0**float(bits_per_param))-1.0)) * r_sum)
        return vector

    def get_bitstring(self):
        return self.bitstring
