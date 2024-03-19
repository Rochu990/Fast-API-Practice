from cars.car import Car
from cars.cars import Cars
from cars.repository import Repository


def test_test():
    repository = Repository()
    cars = Cars(repository)
    car1 = Car(10, 20, 10)
    cars.add(car1)
    cars.drive(car1.id, 10)
    cars.refuel(car1.id, 10)
