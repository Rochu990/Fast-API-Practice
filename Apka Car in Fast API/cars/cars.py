from car import Car
from typing import Tuple
from car import Status


class Cars:

    def __init__(self, repository):
        self.repository = repository

    def refuel(self, id: int, fuel: int) -> Tuple[Car, Status]:
        car = self.repository.get(id)
        car = Car(**car)
        result = car.refuel(fuel)
        self.repository.add(id, car.to_dict())
        return car, result

    def add(self, id: int, car: int) -> dict:
        return self.repository.add(id, car)

    def drive(self, id: int, kilometers: int) -> dict:
        car = self.repository.get(id)
        car = Car(**car)
        car.drive(kilometers)
        self.repository.add(id, car.to_dict())
        return car
