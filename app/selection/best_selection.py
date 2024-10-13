from app.selection.selection_method import SelectionMethod


class BestSelection(SelectionMethod):

    def __init__(self, percentage_the_best_to_select):
        self.percentage_the_best_to_select = percentage_the_best_to_select

    def select(self, population, fitness_scores):
        print("\n")
        print("Selecting method [best selection]")
        print("Chromosomes: " + str([str(chromosome) for chromosome in population]))
        print("Fitness scores: " + str(fitness_scores))
        best_chromosomes = []
        number_of_best_chromosomes = int(len(population) * self.percentage_the_best_to_select)
        print(f"Selecting {number_of_best_chromosomes} best chromosomes")

        fitness_scores_copy = fitness_scores[:]

        for _ in range(number_of_best_chromosomes):
            best_index = fitness_scores_copy.index(min(fitness_scores_copy))
            best_chromosomes.append(population[best_index])
            fitness_scores_copy[best_index] = float('inf')
            print(f"Best chromosome: {str(population[best_index])} with fitness score {fitness_scores[best_index]}")

        return best_chromosomes