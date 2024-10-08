from abc import abstractmethod, ABC


class BitLengthCalculator(ABC):
    """
    Interfejs dla kalkulatora długości bitów.
    """

    @abstractmethod
    def set_precision(self, precision):
        """
        Ustawia precyzję.
        :param precision: Precyzja.
        """
        pass

    @abstractmethod
    def set_bounds(self, lower_bound, upper_bound):
        """
        Ustawia dolną i górną granicę przedziału.
        :param lower_bound: Dolna granica przedziału.
        :param upper_bound: Górna granica przedziału.
        """
        pass

    @abstractmethod
    def calculate_bit_length(self):
        """
        Oblicza minimalną liczbę bitów wymaganą do osiągnięcia danej precyzji dla jednej zmiennej.
        :return: Liczba bitów wymagana do reprezentacji wartości.
        """
        pass