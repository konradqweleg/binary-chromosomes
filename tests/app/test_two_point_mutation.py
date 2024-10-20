import unittest
import random

from app.binary_chromosome import BinaryChromosome
from app.bit_length_calculator import BitLengthMatchToPrecision
from app.mutation.two_point_mutation import TwoPointMutation


class TestTwoPointMutation(unittest.TestCase):

    def setUp(self):
        self.lower_bounds = 0
        self.upper_bounds = 1
        self.precision = 0.1
        self.bit_length_calculator = BitLengthMatchToPrecision(self.precision, self.lower_bounds, self.upper_bounds, 1)


        self.chromosomes = [
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [random.randint(0, 1) for _ in range(10)])
            for _ in range(1000)
        ]
        self.mutation = TwoPointMutation(0.5)



    def test_two_point_mutation_distribution(self):
        mutated_count = 0
        unchanged_count = 0


        new_chromosomes = self.mutation.mutate(self.chromosomes)

        for original, mutated in zip(self.chromosomes, new_chromosomes):

            bit_differences = sum(1 for o_bit, m_bit in zip(original.chromosome_data, mutated.chromosome_data) if o_bit != m_bit)

            if bit_differences == 2:
                mutated_count += 1
            elif bit_differences == 0:
                unchanged_count += 1
            else:
                self.fail(f"Expected exactly 2 bits to mutate, but found {bit_differences} mutated bits in chromosome: {original.chromosome_data} -> {mutated.chromosome_data}")

        self.assertAlmostEqual(mutated_count / 1000, 0.5, delta=0.1)  # Allow a delta of 10%
        self.assertAlmostEqual(unchanged_count / 1000, 0.5, delta=0.1)  # Allow a delta of 10%

if __name__ == '__main__':
    unittest.main()
