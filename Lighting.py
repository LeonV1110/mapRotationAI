from enum import Enum

class Weather(Enum):
    Sunny = 0
    Cloudy = 1
    Rainy = 2
    Stormy = 3

class Visibility(Enum): #fog, sandstorms, ect...
    Low = 0
    Medium = 1
    High = 2

class Time(Enum):
    Morning = 0
    Midday = 1
    Afternoon = 2
    Evening = 3
    Night = 4

class Lighting:
    weather : Weather
    visibility: Visibility
    time: Time
    
    def __init__(self, weather, visibility, time) -> None:
        self.weather = weather
        self.visibility = visibility
        self.time = time

    def __eq__(self, other):
        return (self.weather, self.visibility, self.time) == (other.weather, other.visibility, other.time)