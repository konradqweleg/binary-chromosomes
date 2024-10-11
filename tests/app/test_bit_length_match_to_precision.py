import unittest
from app.bit_length_calculator.bit_length_match_to_precision import BitLengthMatchToPrecision


class BitLengthMatchToPrecisionTests(unittest.TestCase):

    def test_bit_length_for_range_minus_ten_to_ten_with_precision_ten_to_power_minus_six_should_require_twenty_five_bits(
            self):
        bits_calculator = BitLengthMatchToPrecision()
        bits_calculator.set_precision(10 ** -6)
        bits_calculator.set_bounds(-10, 10)
        self.assertEqual(25, bits_calculator.calculate_bit_length())

    def test_bit_length_for_range_zero_to_ten_with_precision_ten_to_power_minus_three_should_require_fourteen_bits(
            self):
        bits_calculator = BitLengthMatchToPrecision()
        bits_calculator.set_precision(10 ** -3)
        bits_calculator.set_bounds(0, 10)
        self.assertEqual(14, bits_calculator.calculate_bit_length())

    def test_bit_length_for_range_minus_one_to_zero_with_precision_ten_to_power_minus_two_should_require_seven_bits(
            self):
        bits_calculator = BitLengthMatchToPrecision()
        bits_calculator.set_precision(10 ** -2)
        bits_calculator.set_bounds(-1, 0)
        self.assertEqual(7, bits_calculator.calculate_bit_length())


if __name__ == '__main__':
    unittest.main()
