import logging
import random
from app.selection.selection_method import SelectionMethod


class TournamentSelection(SelectionMethod):

    def __init__(self, percentage_the_best_to_select, tournament_size):
        self.tournament_size = tournament_size
        self.percentage_the_best_to_select = percentage_the_best_to_select
        self.logger = logging.getLogger(__name__)

    def select(self, population, fitness_scores):
        self.logger.debug("Selecting method [tournament selection]")
        self.logger.debug("Chromosomes: " + str([str(chromosome) for chromosome in population]))
        self.logger.debug("Fitness scores: " + str(fitness_scores))

        best_chromosomes = []
        number_of_best_chromosomes = int(len(population) * self.percentage_the_best_to_select)
        self.logger.debug(
            f"Selecting {number_of_best_chromosomes} chromosomes using tournament selection with tournament size {self.tournament_size}")

        for _ in range(number_of_best_chromosomes):
            tournament_indices = random.sample(range(len(population)), self.tournament_size)
            tournament_participants = [population[i] for i in tournament_indices]
            tournament_fitness_scores = [fitness_scores[i] for i in tournament_indices]

            best_tournament_index = tournament_fitness_scores.index(min(tournament_fitness_scores))
            best_chromosome = tournament_participants[best_tournament_index]
            best_chromosomes.append(best_chromosome)

            self.logger.debug(f"Tournament participants: {[str(chromosome) for chromosome in tournament_participants]}")
            self.logger.debug(f"Tournament fitness scores: {tournament_fitness_scores}")
            self.logger.debug(
                f"Selected chromosome: {str(best_chromosome)} with fitness score {tournament_fitness_scores[best_tournament_index]}")

        return best_chromosomes

    def __str__(self):
        return "Tournament selection"