# Genetic Algorithm GUI

This application provides a graphical user interface (GUI) for configuring and running a genetic algorithm to optimize a given function. The application is built using `tkinter` for the GUI and `matplotlib` for plotting results.

## Features

- **User Input**: Configure various parameters for the genetic algorithm, such as population size, number of epochs, mutation probability, crossover method, selection method, and the function to be optimized.
- **Dynamic UI Elements**: Additional input fields are dynamically shown or hidden based on the selected crossover and selection methods.
- **Running the Algorithm**: Validate input fields, configure the genetic algorithm, and run it with the provided parameters.
- **Results Visualization**: Plot the minimum fitness value, average fitness value, and standard deviation of fitness values over iterations.
- **Results Storage**: Save the results, including the best chromosome value and fitness values over iterations, to a CSV file.
- **New Window for Results**: Display the results, including the time taken and the best chromosome value, in a new window.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/konradqweleg/genetic-algorithm-gui.git
   cd genetic-algorithm-gui
   

## Usage
    Run the application:  
    python gui/main_frame.py
    Configure the genetic algorithm parameters using the GUI.  
    Click the "Start" button to run the algorithm.  
    View the results in the new window and the generated plots.  
## Configuration Parameters
    Begin of the range: The starting value of the range for the variables.
    End of the range: The ending value of the range for the variables.
    Precision: The precision of the variables.
    Population: The size of the population.
    Epochs: The number of iterations the algorithm will run.
    Number of parameters: The number of variables in the function.
    Percentage elite strategy: The percentage of the best individuals to retain in each generation.
    Cross probability: The probability of crossover.
    Mutation probability: The probability of mutation.
    Inversion probability: The probability of inversion.
    Selection method: The method used for selecting individuals for reproduction.
    Crossover method: The method used for crossover.
    Mutation method: The method used for mutation.
    Function to calculate: The function to be optimized.
    Optimization type: The type of optimization (minimization or maximization).
## Results
    The results of the algorithm, including the best chromosome value and fitness values over iterations, are saved to a CSV file in the results directory. Plots of the minimum fitness value, average fitness value, and standard deviation of fitness values over iterations are also saved as images in the results directory.  
## License
    This project is licensed under the MIT License.