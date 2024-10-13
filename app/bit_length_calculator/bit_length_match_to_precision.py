import math
from app.bit_length_calculator import BitLengthCalculator


class BitLengthMatchToPrecision(BitLengthCalculator):
    def __init__(self, precision, lower_bound, upper_bound, num_variables):
        self.precision = precision
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.num_variables = num_variables

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

        bit_length_for_all_variables = bit_length * self.num_variables
        return bit_length_for_all_variables
