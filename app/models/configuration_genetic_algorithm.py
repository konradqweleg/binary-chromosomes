from app.bit_length_calculator import BitLengthMatchToPrecision
from app.crossover_method.crossover_method import CrossoverMethod
from app.crossover_method.granular_crossover import GranularCrossover
from app.crossover_method.one_point_crossover import OnePointCrossover
from app.crossover_method.three_point_crossover import ThreePointCrossover
from app.crossover_method.two_point_crossover import TwoPointCrossover
from app.crossover_method.uniform_crossover import UniformCrossover
from app.genetic_algorithm import GeneticAlgorithm
from app.models.enums.cross_method import CrossoverMethod
from app.models.enums.function_to_calculate import FunctionToCalculate
from app.models.enums.mutation_method import MutationMethod
from app.models.enums.selection_method import SelectionMethod
from app.mutation.boundary_mutation import BoundaryMutation
from app.mutation.one_point_mutation import OnePointMutation
from app.mutation.two_point_mutation import TwoPointMutation
from app.other_operations.inversion_operator import InversionOperator
from app.selection.best_selection import BestSelection
from app.selection.roulette_wheel_selection import RouletteWheelSelection
from app.selection.tournament_selection import TournamentSelection


class ConfigurationGeneticAlgorithm:
    def configuration(self, form_data):
        bit_length_match_precision = BitLengthMatchToPrecision(form_data.precision, form_data.begin_of_the_range,
                                                               form_data.end_of_the_range, form_data.num_variable)
        selection_method = self._get_selection_method(form_data)
        crossover_method = self._get_crossover_method(form_data)
        mutation_method =  self._get_mutation_method(form_data)
        fitness_function_method = self._get_fitness_function(form_data)
        return GeneticAlgorithm(bit_length_match_precision, form_data.population, form_data.begin_of_the_range,
                         form_data.end_of_the_range, form_data.epochs, selection_method, crossover_method,
                         mutation_method, form_data.num_variable, fitness_function_method,
                                form_data.elite_strategy,InversionOperator(form_data.inversion_probability))

    def _get_selection_method(self, form_data):
        match form_data.selection_method:
            case SelectionMethod.ROULETTE_WHEEL_SELECTION:
                return RouletteWheelSelection(
                    form_data.percentage_the_best_to_select, form_data.optimization_type)
            case SelectionMethod.BEST_SELECTION:
                return BestSelection(form_data.percentage_the_best_to_select)
            case SelectionMethod.TOURNAMENT_SELECTION:
                return TournamentSelection(
                    form_data.percentage_the_best_to_select, form_data.tournament_size)

    def _get_crossover_method(self, form_data):
        match form_data.crossover_method:
            case CrossoverMethod.ONE_POINT:
                return OnePointCrossover(form_data.cross_probability)
            case CrossoverMethod.TWO_POINTS:
                return TwoPointCrossover(form_data.cross_probability)
            case CrossoverMethod.THREE_POINTS:
                return ThreePointCrossover
            case CrossoverMethod.GRANULAR_CROSSOVER:
                return GranularCrossover(form_data.cross_probability,
                                         form_data.block_size, form_data.probability_to_crossover_block)
            case CrossoverMethod.UNIFORM_CROSSOVER:
                return UniformCrossover(form_data.cross_probability,
                                        form_data.probability_to_crossover_gene)

    def _get_mutation_method(self, form_data):
        match form_data.mutation_method:
            case MutationMethod.ONE_POINT:
                return OnePointMutation(form_data.mutation_probability)
            case MutationMethod.TWO_POINT:
                return TwoPointMutation(form_data.mutation_probability)
            case MutationMethod.BOUNDARY:
                return BoundaryMutation(form_data.mutation_probability)

    def _get_fitness_function(self, form_data):
        match form_data.fitness_function:
            case FunctionToCalculate.SZWEFEL:
                return None