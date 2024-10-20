from abc import abstractmethod, ABC


class BitLengthCalculator(ABC):
    """
    Interface for bit length calculator.
    """

    @abstractmethod
    def calculate_bit_length(self):
        """
        Calculates the minimum number of bits required to achieve a given precision for a single variable.
        :return: Number of bits required to represent the value.
        """
        pass
