import random

from app.crossover_method.crossover_method import CrossoverMethod


class UniformCrossover(CrossoverMethod):
    def crossover(self, parent1, parent2):
        child1_genes = [random.choice(genes) for genes in zip(parent1.genes, parent2.genes)]
        child2_genes = [random.choice(genes) for genes in zip(parent2.genes, parent1.genes)]
        return parent1.__class__(child1_genes), parent2.__class__(child2_genes)