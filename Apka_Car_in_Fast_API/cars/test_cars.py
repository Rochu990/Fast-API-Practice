import unittest

from car import Car
from cars import Cars
from repository import Repository


class TestCar(unittest.TestCase):

    def test_test(self):
        repository = Repository()
        cars = Cars(repository)
        car1 = Car(10, 20, 10)
        cars.add(car1)
        cars.drive(car1.id, 10)
        cars.refuel(car1.id, 10)


if __name__ == "__main__":
    unittest.main()
