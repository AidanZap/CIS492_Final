from enum import Enum

class Type(Enum):
    TV_SHOW = 1
    MOVIE = 2

class Time_Period(Enum):
    NEW = 1
    TWO_THOUSANDS = 2
    PRE_TWO_THOUSANDS = 3

class Rating(Enum):
    ADULT = 1
    TEEN = 2
    KID = 3

class Duration(Enum):
    ONE_OR_TWO_SEASONS = 1
    THREE_OR_MORE_SEASONS = 2
    LESS_THAN_60_MIN = 3
    HOUR_TO_90_MIN = 4
    MORE_THAN_90_MIN = 5