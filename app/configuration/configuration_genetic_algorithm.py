from scipy.constants import precision

from app.bit_length_calculator import BitLengthMatchToPrecision
from app.crossover_method.crossover_method import CrossoverMethod
from app.crossover_method.granular_crossover import GranularCrossover
from app.crossover_method.one_point_crossover import OnePointCrossover
from app.crossover_method.three_point_crossover import ThreePointCrossover
from app.crossover_method.two_point_crossover import TwoPointCrossover
from app.crossover_method.uniform_crossover import UniformCrossover
from app.functions.cec_2014_f1 import Cec2014F1
from app.functions.griewank import Griewank
from app.functions.szwefel import Szwefel
from app.functions.szwefel_custom_impl import SzwefelCustomImpl
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
        population = int(form_data.population)
        begin_of_the_range = int(form_data.begin_of_the_range)
        end_of_the_range = int(form_data.end_of_the_range)
        num_variable = int(form_data.num_variable)
        precision = float(form_data.precision)
        bit_length_match_precision = BitLengthMatchToPrecision(precision, begin_of_the_range,
                                                               end_of_the_range, num_variable)
        selection_method = self._get_selection_method(form_data)
        crossover_method = self._get_crossover_method(form_data)
        mutation_method =  self._get_mutation_method(form_data)
        fitness_function_method = self._get_fitness_function(form_data)
        elitism_rate =  float(form_data.elite_strategy)

        epochs = int(form_data.epochs)
        return GeneticAlgorithm(bit_length_match_precision, population, begin_of_the_range,
                         end_of_the_range, epochs, selection_method, crossover_method,
                         mutation_method, num_variable, elitism_rate,
                                InversionOperator(float(form_data.inversion_probability)),
                                fitness_function_method, form_data.optimization_type)

    def _get_selection_method(self, form_data):
        match form_data.selection_method:
            case SelectionMethod.ROULETTE_WHEEL_SELECTION:
                return RouletteWheelSelection(
                    float(form_data.percentage_the_best_to_select))
            case SelectionMethod.BEST_SELECTION:
                return BestSelection(float(form_data.percentage_the_best_to_select))
            case SelectionMethod.TOURNAMENT_SELECTION:
                return TournamentSelection(
                    float(form_data.percentage_the_best_to_select), int(form_data.tournament_size))

    def _get_crossover_method(self, form_data):
        match form_data.cross_method:
            case CrossoverMethod.ONE_POINT:
                return OnePointCrossover(float(form_data.cross_probability))
            case CrossoverMethod.TWO_POINTS:
                return TwoPointCrossover(float(form_data.cross_probability))
            case CrossoverMethod.THREE_POINTS:
                return ThreePointCrossover
            case CrossoverMethod.GRANULAR_CROSSOVER:
                return GranularCrossover(float(form_data.cross_probability),
                                         int(form_data.block_size), float(form_data.probability_to_crossover_block))
            case CrossoverMethod.UNIFORM_CROSSOVER:
                return UniformCrossover(float(form_data.cross_probability),
                                        float(form_data.probability_to_crossover_gene))

    def _get_mutation_method(self, form_data):
        match form_data.mutation_method:
            case MutationMethod.ONE_POINT:
                return OnePointMutation(float(form_data.mutation_probability))
            case MutationMethod.TWO_POINT:
                return TwoPointMutation(float(form_data.mutation_probability))
            case MutationMethod.BOUNDARY:
                return BoundaryMutation(float(form_data.mutation_probability))

    def _get_fitness_function(self, form_data):
        match FunctionToCalculate(form_data.function_to_calculate):
            case FunctionToCalculate.SCHWEFEL:
                return Szwefel()
            case FunctionToCalculate.GRIEWANK:
                return Griewank()
            case FunctionToCalculate.CEC_2014_F1:
                return Cec2014F1()
            case FunctionToCalculate.CUSTOM_SCHWEFEL:
                return SzwefelCustomImpl()