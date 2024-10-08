import math
from app.bit_length_calculator import BitLengthCalculator


class BitLengthMatchToPrecision(BitLengthCalculator):
    def __init__(self):
        self.precision = None
        self.lower_bound = None
        self.upper_bound = None

    def set_precision(self, precision):
        self.precision = precision

    def set_bounds(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def calculate_bit_length(self):
        if self.precision is None:
            raise ValueError("Precison must be set before calculating bit length.")
        if self.lower_bound is None or self.upper_bound is None:
            raise ValueError("Bounds must be set before calculating bit length.")

        range_size = self.upper_bound - self.lower_bound
        if range_size <= 0:
            raise ValueError("Upper bound must be greater than lower bound.")

        required_values = range_size / self.precision

        bit_length = math.ceil(math.log2(required_values))

        return bit_length
