import random

from app.selection.selection_method import SelectionMethod


class RouletteWheelSelection(SelectionMethod):
    def select(self, population, fitness_scores):
        total_fitness = sum(fitness_scores)
        selection_probs = [score / total_fitness for score in fitness_scores]
        selected_index = random.choices(range(len(population)), weights=selection_probs, k=1)[0]
        return population[selected_index]