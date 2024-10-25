from dataclasses import dataclass

from app.models.enums.cross_method import CrossoverMethod
from app.models.enums.function_to_calculate import FunctionToCalculate
from app.models.enums.mutation_method import MutationMethod
from app.models.enums.selection_method import SelectionMethod


@dataclass
class BinaryChromosomesConfigurationData:
    mutation_method : MutationMethod
    cross_method : CrossoverMethod
    selection_method : SelectionMethod
    inversion_probability : float
    mutation_probability : float
    cross_probability : float
    elite_strategy : float
    population : int
    end_of_the_range : int
    begin_of_the_range : int
    epochs : int
    precision : float
    num_variable: int
    function_to_calculate: FunctionToCalculate
    percentage_the_best_to_select : float
    roulette_wheel_selection_percentage_chromosomes_to_select : float
    block_size : int
    probability_to_crossover_block : float
    probability_to_crossover_gene : float
    optimization_type : str
    tournament_size : int