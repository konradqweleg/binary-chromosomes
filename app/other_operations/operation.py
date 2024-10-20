from abc import ABC, abstractmethod


class Operation(ABC):

    @abstractmethod
    def apply(self, chromosomes):
        """
        Applies the operation to the given chromosomes.

        Parameters:
        chromosomes (list): List of chromosomes to apply the operation to.

        Returns:
        list: List of chromosomes after the operation.
        """
        pass
