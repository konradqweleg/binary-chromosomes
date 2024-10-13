import unittest
from app.bit_length_calculator.bit_length_match_to_precision import BitLengthMatchToPrecision


class BitLengthMatchToPrecisionTests(unittest.TestCase):

    def test_bit_length_for_range_minus_ten_to_ten_with_precision_ten_to_power_minus_six_should_require_twenty_five_bits_for_one_variable(
            self):

        bits_calculator = BitLengthMatchToPrecision(10 ** -6, -10, 10, 1)
        self.assertEqual(bits_calculator.calculate_bit_length(), 25)

    def test_bit_length_for_range_zero_to_ten_with_precision_ten_to_power_minus_three_should_require_fourteen_bits_for_one_variable(
            self):
        bits_calculator = BitLengthMatchToPrecision(10 ** -3, 0, 10, 1)
        self.assertEqual(bits_calculator.calculate_bit_length(), 14)

    def test_bit_length_for_range_minus_one_to_zero_with_precision_ten_to_power_minus_two_should_require_seven_bits_for_one_variable(
            self):
        bits_calculator = BitLengthMatchToPrecision(10 ** -2, -1, 0, 1)
        self.assertEqual(bits_calculator.calculate_bit_length(), 7)

    def test_bit_length_for_range_minus_ten_to_ten_with_precision_ten_to_power_minus_six_should_require_fifty_bits_for_two_variable(
            self):
        bits_calculator = BitLengthMatchToPrecision(10 ** -6, -10, 10, 2)
        self.assertEqual(bits_calculator.calculate_bit_length(), 50)


if __name__ == '__main__':
    unittest.main()