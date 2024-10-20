import math
import logging
from app.bit_length_calculator import BitLengthCalculator


class BitLengthMatchToPrecision(BitLengthCalculator):
    def __init__(self, precision, lower_bound, upper_bound, num_variables):
        self.precision = precision
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.num_variables = num_variables
        self.logger = logging.getLogger(__name__)

    def calculate_bit_length(self):
        self.logger.debug(
            "Calculating bit length with precision: %s, lower_bound: %s, upper_bound: %s, num_variables: %s",
            self.precision, self.lower_bound, self.upper_bound, self.num_variables)

        if self.precision is None:
            raise ValueError("Precision must be set before calculating bit length.")
        if self.lower_bound is None or self.upper_bound is None:
            raise ValueError("Bounds must be set before calculating bit length.")

        range_size = self.upper_bound - self.lower_bound
        if range_size <= 0:
            raise ValueError("Upper bound must be greater than lower bound.")

        required_values = range_size / self.precision
        self.logger.debug("Range size: %s, Required values: %s", range_size, required_values)

        bit_length = math.ceil(math.log2(required_values))
        self.logger.debug("Bit length for one variable: %s", bit_length)

        bit_length_for_all_variables = bit_length * self.num_variables
        self.logger.debug("Total bit length for all variables: %s", bit_length_for_all_variables)

        return bit_length_for_all_variables