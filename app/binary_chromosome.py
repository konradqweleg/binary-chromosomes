import math
import random

class BinaryChromosome:

    def __init__(self, bit_length_calculator, lower_bounds, upper_bounds, num_variables, chromosomes=None):
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds
        self.num_variables = num_variables
        self.chromosome_length_calculator = bit_length_calculator

        self.bit_length = self._calculate_bit_length()
        self.max_values = self._calculate_max_values_for_variable(self.bit_length)

        if chromosomes is None:
            self.chromosome_data = self._random_chromosome(self.bit_length)
        else:
            self.chromosome_data = chromosomes

    def _calculate_bit_length(self):
        return self.chromosome_length_calculator.calculate_bit_length()

    def _random_chromosome(self, bit_length):
        return [random.choice([0, 1]) for _ in range(bit_length)]

    def _calculate_max_values_for_variable(self, bit_length):
        return (2 ** (bit_length / self.num_variables)) - 1

    def decode(self):
        real_values = []
        for i in range(self.num_variables):
            start_index = i * self.bit_length // self.num_variables
            end_index = (i + 1) * self.bit_length // self.num_variables

            binary_str = ''.join(str(bit) for bit in self.chromosome_data[start_index:end_index])
            decimal_value = int(binary_str, 2)

            real_value = self.lower_bounds + (decimal_value) * (
                    self.upper_bounds - self.lower_bounds)/ math.pow(2, self.bit_length // self.num_variables)

            real_values.append(real_value)

        return real_values

    def encode(self, real_values):
        for i in range(self.num_variables):
            real_value = real_values[i]

            decimal_value = int(
                ((real_value - self.lower_bounds) / (self.upper_bounds - self.lower_bounds)) * self.max_values
            )

            binary_str = format(decimal_value, f'0{self.bit_length // self.num_variables}b')
            start_index = i * self.bit_length // self.num_variables
            end_index = (i + 1) * self.bit_length // self.num_variables

            self.chromosome_data[start_index:end_index] = [int(bit) for bit in binary_str]

    def __str__(self):
        return "Chromosom: " + str(self.chromosome_data) + ", zakodowana wartość: " + str(self.decode())

    @classmethod
    def copy_with_new_chromosomes(cls, other, new_chromosom_data):
        return cls(other.chromosome_length_calculator, other.lower_bounds, other.upper_bounds, other.num_variables,
                   new_chromosom_data)