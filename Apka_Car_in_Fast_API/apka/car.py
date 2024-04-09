import dataclasses
import uuid


@dataclasses.dataclass
class FuelStatus:
    succes: bool
    msg: str

@dataclasses.dataclass
class DriveStatus:
    succes: bool
    msg: str


class Car:
    def __init__(self, combustion: int, tank_fuel: int, max_fuel: int):
        self.combustion = combustion
        self.tank_fuel = tank_fuel
        self.max_fuel = max_fuel
        self.id = uuid.uuid4()

    def refuel(self, fuel: int) -> FuelStatus:
        self.tank_fuel = self.tank_fuel + fuel
        if self.tank_fuel > self.max_fuel:
            self.tank_fuel = self.max_fuel
            return FuelStatus(False, "Próbujesz zatankować za dużo")
        return FuelStatus(True, "Zatankowano auto")

    def drive(self, kilometers: int) -> DriveStatus:
        fuel = (kilometers / 100) * self.combustion
        self.tank_fuel = self.tank_fuel - fuel
        if self.tank_fuel < 0:
            self.tank_fuel = 0
            return DriveStatus(False, "Zabrakło paliwa")
        return DriveStatus(True, "Dojechałeś do celu")
    
    def to_dict(self):
        return {
            "combustion": self.combustion,
            "tank_fuel": self.tank_fuel,
            "max_fuel": self.max_fuel,
        }
