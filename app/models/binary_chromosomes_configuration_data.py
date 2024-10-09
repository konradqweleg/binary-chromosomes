from dataclasses import dataclass

from app.models.enums.cross_method import CrossMethod
from app.models.enums.mutation_method import MutationMethod
from app.models.enums.selection_method import SelectionMethod


@dataclass
class BinaryChromosomesConfigurationData:
    mutation_method : MutationMethod
    cross_method : CrossMethod
    selection_method : SelectionMethod
    inversion_probability : float
    mutation_probability : float
    cross_probability : float
    elite_strategy : float
    number_of_bits : int
    population : int
    end_of_the_range : int
    begin_of_the_range : int
    epochs : int