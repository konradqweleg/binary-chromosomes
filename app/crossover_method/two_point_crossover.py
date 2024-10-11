import random

from app.crossover_method.crossover_method import CrossoverMethod


class TwoPointCrossover(CrossoverMethod):
    def crossover(self, parent1, parent2):
        point1, point2 = sorted(random.sample(range(1, len(parent1.genes)), 2))
        child1_genes = parent1.genes[:point1] + parent2.genes[point1:point2] + parent1.genes[point2:]
        child2_genes = parent2.genes[:point1] + parent1.genes[point1:point2] + parent2.genes[point2:]
        return parent1.__class__(child1_genes), parent2.__class__(child2_genes)