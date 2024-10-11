import random

from app.crossover_method.crossover_method import CrossoverMethod


class ThreePointCrossover(CrossoverMethod):
    def crossover(self, parent1, parent2):
        points = sorted(random.sample(range(1, len(parent1.genes)), 3))
        child1_genes = (parent1.genes[:points[0]] + parent2.genes[points[0]:points[1]] +
                        parent1.genes[points[1]:points[2]] + parent2.genes[points[2]:])
        child2_genes = (parent2.genes[:points[0]] + parent1.genes[points[0]:points[1]] +
                        parent2.genes[points[1]:points[2]] + parent1.genes[points[2]:])
        return parent1.__class__(child1_genes), parent2.__class__(child2_genes)