import random
from app.selection.selection_method import SelectionMethod


class RouletteWheelSelection(SelectionMethod):
    def select(self, population, fitness_scores):
        print("\n")
        print("Selecting method [roulette wheel selection]")
        print("Chromosomes: " + str([str(chromosome) for chromosome in population]))
        print("Fitness scores: " + str(fitness_scores))

        total_fitness = sum(fitness_scores)
        selection_probs = [score / total_fitness for score in fitness_scores]
        print("Selection probabilities: " + str(selection_probs))

        selected_index = random.choices(range(len(population)), weights=selection_probs, k=1)[0]
        selected_chromosome = population[selected_index]

        print(f"Selected chromosome: {str(selected_chromosome)} with fitness score {fitness_scores[selected_index]}")

        return selected_chromosome