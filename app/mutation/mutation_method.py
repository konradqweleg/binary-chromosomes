from abc import ABC, abstractmethod

class MutationMethod(ABC):

    @abstractmethod
    def mutate(self, chromosomes_to_mutate):
        pass