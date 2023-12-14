from enum import Enum

class Weather(Enum):
    Sunny = 0
    Cloudy = 1
    Rainy = 2
    Stormy = 3

class Foggyness(Enum):
    Clear = 0
    Fog = 1 # Also counts for sandstorm

class Time(Enum):
    Morning = 0
    Midday = 1
    Afternoon = 2
    Evening = 3
    Night = 4


class Lighting(Enum):
    pass