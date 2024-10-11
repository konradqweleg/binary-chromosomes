import random

from app.selection.selection_method import SelectionMethod


class TournamentSelection(SelectionMethod):
    def __init__(self, tournament_size):
        self.tournament_size = tournament_size

    def select(self, population, fitness_scores):

        tournament_indices = random.sample(range(len(population)), self.tournament_size)
        tournament_fitness = [fitness_scores[i] for i in tournament_indices]
        best_index = tournament_indices[tournament_fitness.index(min(tournament_fitness))]
        return population[best_index]