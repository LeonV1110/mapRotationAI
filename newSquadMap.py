from enum import Enum

class Waterness(Enum):
    LandLocked = 0
    Coast = 1
    Delta = 2
    Island = 3

class Biome(Enum):
    Snow = 0
    Green = 1
    Arid = 2
    Dessert = 3

class Urbanness(Enum):
    Wild = 0
    Rural = 1
    Suburb = 2 # Not full town, but big town part
    Urban = 3
    DownTown = 4

class Forestness(Enum):
    Field = 0
    SparceForest = 1
    Forest = 2
    DenseForest = 3
    Jungle = 4

class Mountainness(Enum):
    Flat = 0 #NL
    Hilly = 1
    BigHill = 2
    Mountain = 3



class SquadMap(Enum):
    AlBasrah                = 0     , Waterness.LandLocked  , Biome.Dessert , Urbanness.Suburb  , Forestness.Field          , Mountainness.Flat
    Anvil                   = 1     , Waterness.LandLocked  , Biome.Dessert , Urbanness.Rural   , Forestness.Field          , Mountainness.Mountain
    Belaya                  = 2     , Waterness.LandLocked  , Biome.Snow    , Urbanness.Rural   , Forestness.Forest         , Mountainness.Hilly
    BlackCoast              = 3     , Waterness.Delta       , Biome.Green   , Urbanness.Rural   , Forestness.Forest         , Mountainness.BigHill
    Chora                   = 4     , Waterness.LandLocked  , Biome.Dessert , Urbanness.Rural   , Forestness.Field          , Mountainness.Flat
    Fallujah                = 5     , Waterness.LandLocked  , Biome.Dessert , Urbanness.DownTown, Forestness.Field          , Mountainness.Flat
    FoolsRoad               = 6     , Waterness.LandLocked  , Biome.Green   , Urbanness.Wild    , Forestness.DenseForest    , Mountainness.BigHill
    GooseBay                = 7     , Waterness.Coast       , Biome.Snow    , Urbanness.Rural   , Forestness.DenseForest    , Mountainness.BigHill
    Gorodok                 = 8     , Waterness.LandLocked  , Biome.Green   , Urbanness.Rural   , Forestness.SparceForest   , Mountainness.Hilly
    Harju                   = 9     , Waterness.Delta       , Biome.Green   , Urbanness.Suburb  , Forestness.DenseForest    , Mountainness.BigHill
    JensensRange            = 10    , Waterness.LandLocked  , Biome.Dessert , Urbanness.Wild    , Forestness.Field          , Mountainness.Flat
    Kamdesh                 = 11    , Waterness.LandLocked  , Biome.Arid    , Urbanness.Rural   , Forestness.Forest         , Mountainness.Hilly
    Kohat                   = 12    , Waterness.LandLocked  , Biome.Dessert , Urbanness.Rural   , Forestness.Field          , Mountainness.Mountain
    Kokan                   = 13    , Waterness.LandLocked  , Biome.Dessert , Urbanness.Rural   , Forestness.Field          , Mountainness.Flat
    Lashkar                 = 14    , Waterness.LandLocked  , Biome.Arid    , Urbanness.Rural   , Forestness.DenseForest    , Mountainness.Mountain
    Logar                   = 15    , Waterness.LandLocked  , Biome.Dessert , Urbanness.Suburb  , Forestness.SparceForest   , Mountainness.BigHill
    Manicouagan             = 16    , Waterness.LandLocked  , Biome.Green   , Urbanness.Rural   , Forestness.DenseForest    , Mountainness.Mountain
    Mestia                  = 17    , Waterness.LandLocked  , Biome.Green   , Urbanness.Rural   , Forestness.Forest         , Mountainness.BigHill
    Mutaha                  = 18    , Waterness.LandLocked  , Biome.Dessert , Urbanness.Urban   , Forestness.Field          , Mountainness.Flat
    Narva                   = 19    , Waterness.LandLocked  , Biome.Green   , Urbanness.DownTown, Forestness.Field          , Mountainness.Flat
    PacificProvingGrounds   = 20    , Waterness.Island      , Biome.Green   , Urbanness.Wild    , Forestness.Jungle         , Mountainness.Hilly
    Sanxian                 = 21    , Waterness.Island      , Biome.Green   , Urbanness.Rural   , Forestness.Jungle         , Mountainness.Hilly #NOT RELEASED YET
    Skorpo                  = 22    , Waterness.Delta       , Biome.Green   , Urbanness.Rural   , Forestness.DenseForest    , Mountainness.Mountain
    Sumari                  = 23    , Waterness.LandLocked  , Biome.Dessert , Urbanness.DownTown, Forestness.Field          , Mountainness.Flat
    Tallil                  = 24    , Waterness.LandLocked  , Biome.Dessert , Urbanness.Rural   , Forestness.Field          , Mountainness.Flat
    Yehorivka               = 25    , Waterness.LandLocked  , Biome.Green   , Urbanness.Suburb  , Forestness.SparceForest   , Mountainness.BigHill