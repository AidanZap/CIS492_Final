from enum import Enum

class Type(Enum):
    TV_SHOW = 0
    MOVIE = 1

class Time_Period(Enum):
    NEW = 0
    TWO_THOUSANDS = 1
    PRE_TWO_THOUSANDS = 2

class Rating(Enum):
    ADULT = 0
    TEEN = 1
    KID = 2

class Duration(Enum):
    ONE_OR_TWO_SEASONS = 0
    THREE_OR_MORE_SEASONS = 1
    LESS_THAN_60_MIN = 2
    HOUR_TO_90_MIN = 3
    MORE_THAN_90_MIN = 4