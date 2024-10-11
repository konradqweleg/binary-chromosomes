import unittest
from app.binary_chromosome import BinaryChromosome
from app.bit_length_calculator.bit_length_match_to_precision import BitLengthMatchToPrecision

class TestBinaryChromosome(unittest.TestCase):

    def setUp(self):
        self.bit_length_calculator = BitLengthMatchToPrecision()
        self.lower_bounds = [-10]
        self.upper_bounds = [10]
        self.precision = 0.000001
        self.chromosome = BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, self.precision, 1)

    def test_decode(self):
        self.chromosome.chromosomes = [[0,0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]]
        expected_real_values = -9.0177380738
        actual_real_values = self.chromosome.decode()
        self.assertAlmostEqual(expected_real_values, actual_real_values[0], places=6)

    def test_encode(self):
        real_values = [-9.0177380738]
        self.chromosome.encode(real_values)
        expected_chromosome = [0,0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
        self.assertEqual(self.chromosome.chromosomes[0], expected_chromosome)

if __name__ == '__main__':
    unittest.main()