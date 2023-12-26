from enum import Enum
class Biome(Enum):
    Desert  = "1"
    Green   = "2"
    Snow    = "3"
    Arid    = "4"
    Island  = "5"

class Environment(Enum):
    Open        = "1"
    Urban       = "2"
    Canyon      = "3"
    Field       = "4"
    Mountain    = "5"
    Forest      = "6"
    Jungle      = "7"
    
class SquadMap(Enum):
    AlBasrah                = "10", Biome.Desert, Environment.Urban
    Anvil                   = "11", Biome.Desert, Environment.Canyon 
    Belaya                  = "12", Biome.Snow, Environment.Forest
    BlackCoast              = "13", Biome.Green, Environment.Forest
    Chora                   = "14", Biome.Desert, Environment.Field
    Fallujah                = "15", Biome.Desert, Environment.Urban
    FoolsRoad               = "16", Biome.Green, Environment.Forest
    GooseBay                = "17", Biome.Snow, Environment.Forest
    Gorodok                 = "18", Biome.Green, Environment.Forest
    Harju                   = "19", Biome.Green, Environment.Forest
    JensensRange            = "10", Biome.Desert, Environment.Open
    Kamdesh                 = "21", Biome.Arid, Environment.Forest
    Kohat                   = "22", Biome.Desert, Environment.Mountain
    Kokan                   = "23", Biome.Desert, Environment.Field
    Lashkar                 = "24", Biome.Arid, Environment.Mountain
    Logar                   = "25", Biome.Desert, Environment.Urban
    Manicouagan             = "26", Biome.Green, Environment.Mountain
    Mestia                  = "27", Biome.Green, Environment.Mountain
    Mutaha                  = "28", Biome.Desert, Environment.Urban
    Narva                   = "29", Biome.Green, Environment.Urban
    PacificProvingGrounds   = "30", Biome.Island, Environment.Jungle
    Sanxian                 = "31", Biome.Island, Environment.Jungle
    Skorpo                  = "32", Biome.Green, Environment.Mountain
    Sumari                  = "33", Biome.Desert, Environment.Urban
    Tallil                  = "34", Biome.Desert, Environment.Open
    Yehorivka               = "35", Biome.Green, Environment.Forest

    def getNum(self):
        return self.value[0]

    def getBiome(self):
        return self.value[1]
    
    def getEnvironment(self):
        return self.value[2]
    
    def getMapcode(self) -> str:
        return self.getNum() + self.getBiome().value + self.getEnvironment().value

def test():
    print(SquadMap.AlBasrah.getBiome())
    print(SquadMap.AlBasrah.getMapcode())
    print(SquadMap.Yehorivka.getMapcode())