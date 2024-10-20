from app.selection.selection_method import SelectionMethod
import logging


class BestSelection(SelectionMethod):

    def __init__(self, percentage_the_best_to_select):
        self.percentage_the_best_to_select = percentage_the_best_to_select
        self.logger = logging.getLogger(__name__)

    def select(self, population, fitness_scores):
        self.logger.debug('Selecting method [best selection]')
        self.logger.debug("Chromosomes: " + str([str(chromosome) for chromosome in population]))
        self.logger.debug("Fitness scores: " + str(fitness_scores))
        best_chromosomes = []
        number_of_best_chromosomes = int(len(population) * self.percentage_the_best_to_select)
        self.logger.debug(f"Number of best chromosomes: {number_of_best_chromosomes}")

        fitness_scores_copy = fitness_scores[:]

        for _ in range(number_of_best_chromosomes):
            best_index = fitness_scores_copy.index(min(fitness_scores_copy))
            best_chromosomes.append(population[best_index])
            fitness_scores_copy[best_index] = float('inf')
            self.logger.debug(
                f"Best chromosome: {str(population[best_index])} with fitness score {fitness_scores[best_index]}")

        return best_chromosomes

    def __str__(self):
        return "Best selection"
