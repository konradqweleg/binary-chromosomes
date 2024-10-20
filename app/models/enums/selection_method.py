from enum import Enum

class SelectionMethod(Enum):
    ROULETTE_WHEEL_SELECTION = 'Roulette wheel selection'
    BEST_SELECTION = 'Best selection'
    TOURNAMENT_SELECTION = 'Tournament selection'