from enum import Enum

class CrossoverMethod(Enum):
    ONE_POINT = 'one point'
    TWO_POINTS = 'two points'
    THREE_POINTS = 'three points'
    GRANULAR_CROSSOVER = 'granular crossover'
    UNIFORM_CROSSOVER = 'uniform crossover'