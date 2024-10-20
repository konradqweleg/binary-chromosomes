from abc import ABC, abstractmethod

class Operation(ABC):

    @abstractmethod
    def apply(self, chromosomes):
        pass