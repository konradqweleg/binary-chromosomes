import random

from app.crossover_method.crossover_method import CrossoverMethod


class GranularCrossover(CrossoverMethod):
    def crossover(self, parent1, parent2):
        granularity = 3  # Example granularity
        child1_genes = []
        child2_genes = []
        for i in range(0, len(parent1.genes), granularity):
            if random.random() < 0.5:
                child1_genes.extend(parent1.genes[i:i+granularity])
                child2_genes.extend(parent2.genes[i:i+granularity])
            else:
                child1_genes.extend(parent2.genes[i:i+granularity])
                child2_genes.extend(parent1.genes[i:i+granularity])
        return parent1.__class__(child1_genes), parent2.__class__(child2_genes)