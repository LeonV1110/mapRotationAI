class Vehicles:
    tanks: int
    atgmIfv: int
    ifv: int
    apc: int
    rwsJeep: int
    jeep: int
    heli: int

    def __init__(self, tanks, atgmIfv, ifv, apc, rwsJeep, jeep, heli) -> None:
        self.tanks = tanks
        self.atgmIfv = atgmIfv
        self.ifv = ifv
        self.apc = apc
        self.rwsJeep = rwsJeep
        self.jeep = jeep
        self.heli = heli
    