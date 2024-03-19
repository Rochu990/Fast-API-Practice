from car import Car


class Cars:

    def __init__(self, repository):
        self.repository = repository

    def refuel(self, id: int, fuel: int) -> dict:
        car = self.repository.get(id)
        car = Car(**car)
        car.refuel(fuel)
        return car

    def add(self, id: int, car: int) -> dict:
        return self.repository.add(id, car)

    def drive(self, id: int, kilometers: int) -> dict:
        car = self.repository.get(id)
        car = Car(**car)
        car.drive(kilometers)
        return car
