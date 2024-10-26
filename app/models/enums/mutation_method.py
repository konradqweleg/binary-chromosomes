from enum import Enum

class MutationMethod(Enum):
    ONE_POINT = 'one point'
    TWO_POINT = 'two point'
    BOUNDARY = 'boundary'
    BIT_FLIP = 'bit flip'