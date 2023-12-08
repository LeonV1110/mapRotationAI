from enum import Enum
import SquadMap

class Alliance(Enum):
    Blue    = "1"
    Red     = "2"
    Green   = "3"
    Brown   = "4" # INS + IMF

class Faction(Enum):
    ADF     = "10", Alliance.Blue
    BAF     = "11", Alliance.Blue
    CAF     = "12", Alliance.Blue
    USA     = "13", Alliance.Blue
    USMC    = "14", Alliance.Blue
    
    PLA     = "15", Alliance.Red
    PLANMC  = "16", Alliance.Red
    RGF     = "17", Alliance.Red
    VDV     = "18", Alliance.Red
    
    MEA     = "19", Alliance.Green
    TGF     = "20", Alliance.Green # kalkoen faction
    
    INS     = "21", Alliance.Brown
    IMF     = "22", Alliance.Brown

    def getNum(self):
        return self.value[0]
    
    def getAlliance(self):
        return self.value[1]
    
    def getFactionCode(self) -> str:
        return self.getNum() + self.getAlliance().value

class Gamemode(Enum):
    RAAS        = "10"
    AAS         = "11"
    Invasion    = "12"
    TC          = "13"
    Insurgency  = "14"
    Destruction = "15"
    Skirmish    = "16"
    Tank        = "17" #Basically AAS but lots of tanks
    Seed        = "18"
    TA          = "19"
    
class Size(Enum):
    Tiny    = "1"
    Small   = "2"
    Medium  = "3"
    Large   = "4"
    Huge    = "5"

class Vehicles(Enum):
    Tank    = "1"
    T_IFV   = "2"
    W_IFV   = "3"
    APC     = "4"
    Jeep    = "5"
    Heli    = "6"
    Misc    = "7"

class Lighting(Enum):
    Afternoon       = "10"
    ClearSunnyDay   = "11"
    Cloud           = "12"
    Dawn            = "13"
    Day             = "14"
    Daytime         = "15"
    Evening         = "16"
    Fog             = "17"
    Foggy           = "18"
    FoggyDay        = "19"
    MidDay          = "20"
    Midday          = "21"
    Moonlit         = "22"
    Morning         = "23"
    Night           = "24"
    Overcast        = "25"
    OvercastDay     = "26"
    Rainstorm       = "27"
    Sandstorm       = "28"
    Storm           = "29"
    Stormy          = "30"
    Sunny           = "31"
    Sunnyday        = "32"
    Sunrise         = "33"
    Sunset          = "34"

class Layer:
    faction1: Faction
    faction1Tickets: int #number of starting tickets devided by 10
    faction2: Faction
    faction2Tickets: int #number of starting tickets devided by 10
    
    map: SquadMap
    gamemode: Gamemode
    vehicles: Vehicles
    spicyFactor: int #int between 0 and 9
    bugged: bool 
    size: Size
    lighting: Lighting
    version: str # needs to be a 2 digit number
    #Squad is stupid and doesn't use actual int for only some layers, so issue for later Leon to translate that.

    name: str

    def __init__(self, fac1, fac1tick, fac2, fac2tick, map, gamemode, vehicles, spicyFactor, bugged, size, lighting, version) -> None:
        self.faction1 = fac1
        self.faction1Tickets = fac1tick
        self.faction2 = fac2
        self.faction2Tickets = fac2tick
        self.map = map
        self.gamemode = gamemode
        self.vehicles = vehicles
        self.spicyFactor = spicyFactor
        self.bugged = bugged
        self.size = size
        self.lighting = lighting
        self.version = version

    def barcodify(self) -> int:
        faction1Code = self.faction1.getFactionCode()
        faction1TicketsCode = str(self.faction1Tickets)
        faction2Code = self.faction2.getFactionCode()
        faction2TicketsCode = str(self.faction2Tickets)

        factionsCode = faction1Code + faction1TicketsCode + faction2Code + faction2TicketsCode

        mapCode = self.map.getMapcode()
        gamemodeCode = self.gamemode.value
        vehiclesCode = self.vehicles.value
        spicyFactorCode = str(self.spicyFactor)
        buggedCode = str(int(self.bugged))
        sizeCode = self.size.value
        lightingCode = self.lighting.value
        version = self.version
        
        res = mapCode + gamemodeCode + version + factionsCode + sizeCode + vehiclesCode + buggedCode + spicyFactorCode + lightingCode
        return int(res)
    
    def readBarcode(barcode:int):
        pass
    


    
def test():
    fac1 = Faction.USA
    fac1tick = 30
    fac2 = Faction.RGF
    fac2tick = 30
    map = SquadMap.SquadMap.Manicouagan
    gamemode = Gamemode.RAAS
    vics = Vehicles.Tank
    spicyFactor = 0
    bugged = False
    size = Size.Large
    lighting = Lighting.Stormy
    version = '03'
    layer = Layer(fac1, fac1tick, fac2, fac2tick, map, gamemode, vics, spicyFactor, bugged, size, lighting, version)

    barcode = layer.barcodify()
    print(barcode)

test()
print("Disatrict You Stink")


#You cant make