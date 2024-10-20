import random
from app.selection.selection_method import SelectionMethod

class RouletteWheelSelection(SelectionMethod):
    def __init__(self, percentage_chromosomes_to_select, optimization_type='maximization'):
        self.percentage_chromosomes_to_select = percentage_chromosomes_to_select
        self.optimization_type = optimization_type.lower()

        if self.optimization_type not in ['minimization', 'maximization']:
            raise ValueError("optimization_type must be either 'minimization' or 'maximization'")

    def select(self, population, fitness_scores):
        print("\nSelecting method [roulette wheel selection]")
        print("Chromosomes: " + str([str(chromosome) for chromosome in population]))
        print("Fitness scores: " + str(fitness_scores))

        # Adjusting fitness scores to handle negative and positive values
        min_fitness = min(fitness_scores)

        if min_fitness < 0:
            # Shift all fitness scores up by the absolute value of the minimum fitness to ensure all are non-negative
            fitness_scores = [score - min_fitness for score in fitness_scores]



        print("Adjusted fitness scores (after handling negatives): " + str(fitness_scores))

        if self.optimization_type == 'minimization':
            # Invert the fitness scores for minimization, so lower scores become higher probabilities
            max_fitness = max(fitness_scores)
            fitness_scores = [max_fitness - score for score in fitness_scores]


        total_fitness = sum(fitness_scores)
        adjustment = 0.01 * total_fitness
        fitness_scores = [score + adjustment for score in fitness_scores]
        total_fitness = sum(fitness_scores)
        print("Fitness score " + str(fitness_scores))
        # Prevent division by zero if total fitness is zero
        if total_fitness == 0:
            # Jeśli suma fitness wynosi 0, rozpatruj równe prawdopodobieństwa
            print("Total fitness is zero. Assigning equal probabilities to all chromosomes.")
            relative_fitness_scores = [1 / len(population)] * len(population)
        else:
            # Normalize the fitness scores to sum to 1 (creating probabilities)
            relative_fitness_scores = [fitness_score / total_fitness for fitness_score in fitness_scores]

        print("Relative fitness scores: " + str(relative_fitness_scores))
        sum_relative_fitness_scores = sum(relative_fitness_scores)
        print("Sum of relative fitness scores: " + str(sum_relative_fitness_scores))

        selected_chromosomes = []
        for _ in range(int(len(population) * self.percentage_chromosomes_to_select)):
            r = random.random()
            cumulative_probability = 0
            for i in range(len(population)):
                cumulative_probability += relative_fitness_scores[i]
                if r <= cumulative_probability:
                    selected_chromosomes.append(population[i])
                    break

        return selected_chromosomes
