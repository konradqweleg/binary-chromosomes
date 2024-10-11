from app.selection.selection_method import SelectionMethod


class BestSelection(SelectionMethod):

    def __init__(self, percentage_the_best_to_select):
        self.percentage_the_best_to_select = percentage_the_best_to_select

    def select(self, population, fitness_scores):
        best_chromosomes = []
        number_of_best_chromosomes = int(len(population) * self.percentage_the_best_to_select)

        # Make a copy of fitness_scores to avoid modifying the original list
        fitness_scores_copy = fitness_scores[:]

        for _ in range(number_of_best_chromosomes):
            best_index = fitness_scores_copy.index(min(fitness_scores_copy))
            best_chromosomes.append(population[best_index])
            # Remove the selected chromosome's fitness score to avoid selecting it again
            fitness_scores_copy[best_index] = float('inf')

        return best_chromosomes