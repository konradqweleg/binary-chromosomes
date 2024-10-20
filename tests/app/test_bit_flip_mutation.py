import random
import unittest
from app.binary_chromosome import BinaryChromosome
from app.bit_length_calculator import BitLengthMatchToPrecision
from app.mutation.bit_flip_mutation import BitFlipMutation


class TestBitFlipMutation(unittest.TestCase):

    def setUp(self):
        self.lower_bounds = 0
        self.upper_bounds = 1
        self.precision = 0.1
        self.bit_length_calculator = BitLengthMatchToPrecision(self.precision, self.lower_bounds, self.upper_bounds, 1)

        self.chromosomes = [
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [0, 1, 0, 1]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [1, 0, 1, 0]),
        ]
        self.mutation = BitFlipMutation(0.5)

    def test_mutate(self, ):
        random.seed(42)
        new_chromosomes = self.mutation.mutate(self.chromosomes)

        self.assertEqual(len(new_chromosomes), len(self.chromosomes))
        self.assertEqual(new_chromosomes[0].chromosome_data, [0, 0, 1, 0])
        self.assertEqual(new_chromosomes[1].chromosome_data, [1, 0, 1, 1])


if __name__ == '__main__':
    unittest.main()
