from typing import Tuple

from car import Car, DriveStatus, FuelStatus


class Cars:

    def __init__(self, repository):
        self.repository = repository

    def refuel(self, id: int, fuel: int) -> Tuple[Car, FuelStatus]:
        car = self.repository.get(id)
        car = Car(**car)
        result = car.refuel(fuel)
        self.repository.add(id, car.to_dict())
        return car, result

    def add(self, id: int, car: dict) -> dict:
        return self.repository.add(id, car)

    def drive(self, id: int, kilometers: int) -> Tuple[Car, DriveStatus]:
        car = self.repository.get(id)
        car = Car(**car)
        result = car.drive(kilometers)
        self.repository.add(id, car.to_dict())
        return car, result
    
    def get(self, id: int) -> dict:
        return self.repository.get(id)
