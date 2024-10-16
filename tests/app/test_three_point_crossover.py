import random
import time
import unittest

from app.binary_chromosome import BinaryChromosome
from app.bit_length_calculator import BitLengthMatchToPrecision
from app.crossover_method.three_point_crossover import ThreePointCrossover

# Wymiana segmentów następuje w 4 miejscach, na zmianę

class TestThreePointCrossover(unittest.TestCase):

    def setUp(self):
        self.probability_to_crossover = 0.7
        self.two_point_crossover = ThreePointCrossover(self.probability_to_crossover)

        self.lower_bounds = 0
        self.upper_bounds = 1
        self.precision = 0.1
        self.bit_length_calculator = BitLengthMatchToPrecision(self.precision, self.lower_bounds, self.upper_bounds, 1)
        self.chromosomes_to_crossover = [
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [0, 0, 0, 1, 1, 1]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [1, 1, 1, 0, 0, 0]),
        ]
        self.expected_new_population_size = 2


    def test_crossover_expected_size(self):
        new_chromosomes = self.two_point_crossover.crossover(self.chromosomes_to_crossover, self.expected_new_population_size)

        self.assertEqual(len(new_chromosomes), self.expected_new_population_size)
        self.assertIsInstance(new_chromosomes[0], BinaryChromosome)
        self.assertIsInstance(new_chromosomes[1], BinaryChromosome)



    def test_crossover(self):
        random.seed(42)
        new_chromosomes = self.two_point_crossover.crossover(self.chromosomes_to_crossover, self.expected_new_population_size)

        self.assertEqual(len(new_chromosomes), self.expected_new_population_size)
        self.assertEqual(new_chromosomes[0].chromosome_data, [0, 1, 1, 1, 1, 0])
        self.assertEqual(new_chromosomes[1].chromosome_data, [1, 0, 0, 0, 0, 1])

