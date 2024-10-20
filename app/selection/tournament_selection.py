import random
from app.selection.selection_method import SelectionMethod


class TournamentSelection(SelectionMethod):

    def __init__(self,  percentage_the_best_to_select, tournament_size):
        self.tournament_size = tournament_size
        self.percentage_the_best_to_select = percentage_the_best_to_select

    def select(self, population, fitness_scores):
        print("\n")
        print("Selecting method [tournament selection]")
        print("Chromosomes: " + str([str(chromosome) for chromosome in population]))
        print("Fitness scores: " + str(fitness_scores))

        best_chromosomes = []
        number_of_best_chromosomes = int(len(population) * self.percentage_the_best_to_select)
        print(f"Selecting {number_of_best_chromosomes} chromosomes using tournament selection with tournament size {self.tournament_size}")

        for _ in range(number_of_best_chromosomes):
            # Randomly select individuals for the tournament
            tournament_indices = random.sample(range(len(population)), self.tournament_size)
            tournament_participants = [population[i] for i in tournament_indices]
            tournament_fitness_scores = [fitness_scores[i] for i in tournament_indices]

            # Find the best individual in the tournament (the one with the lowest fitness score)
            best_tournament_index = tournament_fitness_scores.index(min(tournament_fitness_scores))
            best_chromosome = tournament_participants[best_tournament_index]
            best_chromosomes.append(best_chromosome)

            print(f"Tournament participants: {[str(chromosome) for chromosome in tournament_participants]}")
            print(f"Tournament fitness scores: {tournament_fitness_scores}")
            print(f"Selected chromosome: {str(best_chromosome)} with fitness score {tournament_fitness_scores[best_tournament_index]}")

        return best_chromosomes
