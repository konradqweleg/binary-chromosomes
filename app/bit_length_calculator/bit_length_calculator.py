from abc import abstractmethod, ABC


class BitLengthCalculator(ABC):
    """
    Interfejs dla kalkulatora długości bitów.
    """
    @abstractmethod
    def calculate_bit_length(self):
        """
        Oblicza minimalną liczbę bitów wymaganą do osiągnięcia danej precyzji dla jednej zmiennej.
        :return: Liczba bitów wymagana do reprezentacji wartości.
        """
        pass