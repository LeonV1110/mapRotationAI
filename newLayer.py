from LayerSupportClasses import Faction, Gamemode, Size
from Vehicles import Vehicles
from newSquadMap import SquadMap
from Lighting import Lighting

class Layer:
    faction1: Faction
    faction1Tickets: int
    faction2: Faction
    faction2Tickets: int

    gamemode: Gamemode
    size: Size
    vehicles: Vehicles

    map: SquadMap
    lighting: Lighting

