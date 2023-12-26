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
    lighting: Lighting
    vehicles: Vehicles

    map: SquadMap
    layer: int

    def __init__(self, f1, f1t, f2, f2t, gm, s, v, m ,l) -> None:
        self.faction1 = f1
        self.faction1Tickets = f1t
        self.faction2 = f2
        self.faction2Tickets = f2t

        self.gamemode = gm
        self.size = s
        self.vehicles = v
        self.map = m
        self.lighting = l

        

    def __eq__(self, other) -> bool:
        return (self.map, self.layer) == (other.map, other.layer)