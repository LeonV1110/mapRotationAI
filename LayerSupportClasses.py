from enum import Enum

class Faction(Enum):
    ADF     = 0
    BAF     = 1
    CAF     = 2
    USA     = 3
    USMC    = 4
    
    PLA     = 5
    PLANMC  = 6
    RGF     = 7
    VDV     = 8
    
    MEA     = 9
    TLF     = 10
    
    INS     = 11
    IMF     = 12

class Gamemode(Enum):
    RAAS = 0
    AAS = 1
    Invasion = 2
    TC = 3
    Insurgency = 4
    Destruction = 5
    Skirmish = 6
    Tank = 7
    Seed = 8
    TA = 9
    Training = 10

class Size(Enum):
    Tiny    = 0
    Small   = 1
    Medium  = 3
    Large   = 4
    Huge    = 5

