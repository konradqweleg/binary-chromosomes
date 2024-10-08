# Binary Chromosome Implementation for Multivariable Functions

This project provides an implementation of a binary chromosome designed for optimizing functions of multiple variables. The binary chromosome serves as a fundamental component in genetic algorithms, where it encodes potential solutions to optimization problems.

## Overview

In this implementation, a binary chromosome represents a solution in a binary format, enabling efficient encoding of multiple variables. This approach facilitates the exploration of the solution space, allowing for the application of genetic operators such as selection, crossover, and mutation.

## Features

- **Binary Encoding**: Each variable is encoded as a sequence of bits, enabling the representation of a wide range of values.
- **Multivariable Support**: The chromosome can encode multiple variables, making it suitable for complex optimization problems.
- **Genetic Algorithm Integration**: The implementation is designed to be used within genetic algorithms, allowing for the evolution of solutions over generations.

## Usage

To use this implementation, you can follow these steps:

1. **Initialize the Chromosome**: Create a new binary chromosome with the desired number of variables.
2. **Set Variable Ranges**: Define the range for each variable to ensure proper encoding.
3. **Apply Genetic Operators**: Use selection, crossover, and mutation to evolve the population of chromosomes.
4. **Evaluate Fitness**: Implement a fitness function to assess the quality of each chromosome in solving the optimization problem.

## Example

Here's a simple example demonstrating how to create a binary chromosome:

```python
# Example of creating a binary chromosome
chromosome = BinaryChromosome(num_variables=3, variable_ranges=[(0, 10), (0, 5), (0, 20)])
