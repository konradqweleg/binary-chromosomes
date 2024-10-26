import unittest

from app.binary_chromosome import BinaryChromosome
from app.bit_length_calculator import BitLengthMatchToPrecision
from app.selection.roulette_wheel_selection import RouletteWheelSelection


class TestRouletteWheelSelection(unittest.TestCase):
    def setUp(self):
        self.percentage_to_select = 0.5
        self.lower_bounds = 0
        self.upper_bounds = 1
        self.precision = 0.1
        self.bit_length_calculator = BitLengthMatchToPrecision(self.precision, self.lower_bounds, self.upper_bounds, 1)
        self.selection_method = RouletteWheelSelection(self.percentage_to_select)  # optimization_type="minimization" optimization_type="maximization"
        self.chromosomes = [
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [1, 1, 0, 1, 1, 1]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [1, 1, 1, 0, 0, 0]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [0, 1, 0, 1, 1, 1]),
            BinaryChromosome(self.bit_length_calculator, self.lower_bounds, self.upper_bounds, 1, [1, 1, 1, 0, 1, 0]),
        ]

    def test_selection_expected_size(self):
        fitness_scores = [-1, 5, -3, -4]
        new_chromosomes = self.selection_method.select(self.chromosomes, fitness_scores)

        self.assertEqual(2, len(new_chromosomes))
        self.assertIsInstance(new_chromosomes[0], BinaryChromosome)
        self.assertIsInstance(new_chromosomes[1], BinaryChromosome)

    def test_for_minimization(self):

        self.selection_method = RouletteWheelSelection(self.percentage_to_select
                                                       )
        fitness_scores = [0, 1, -1, -2]
        selection_counts = {0: 0, 1: 0, 2: 0, 3: 0}

        for _ in range(1000):
            selected_chromosomes = self.selection_method.select(self.chromosomes, fitness_scores,optimization_type="minimization")
            for chromosome in selected_chromosomes:
                index = self.chromosomes.index(chromosome)
                selection_counts[index] += 1

        self.assertGreater(selection_counts[2], selection_counts[0])
        self.assertGreater(selection_counts[3], selection_counts[0])
        self.assertGreater(selection_counts[2], selection_counts[1])
        self.assertGreater(selection_counts[3], selection_counts[1])

    def test_for_maximization(self):
        self.selection_method = RouletteWheelSelection(self.percentage_to_select)
        fitness_scores = [9, -93, 17, 0]
        selection_counts = {0: 0, 1: 0, 2: 0, 3: 0}

        for _ in range(1000):
            selected_chromosomes = self.selection_method.select(self.chromosomes, fitness_scores)
            for chromosome in selected_chromosomes:
                index = self.chromosomes.index(chromosome)
                selection_counts[index] += 1

        self.assertGreater(selection_counts[0], selection_counts[1])
        self.assertGreater(selection_counts[2], selection_counts[1])
        self.assertGreater(selection_counts[0], selection_counts[3])
        self.assertGreater(selection_counts[2], selection_counts[3])
