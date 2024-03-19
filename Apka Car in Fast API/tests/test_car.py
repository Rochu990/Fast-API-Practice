import unittest

from car import drive_car, refuel_car


class TestCar(unittest.TestCase):

    def test_refuel(self):
        self.assertEqual(refuel_car(10, 10, 20), 20)
        self.assertEqual(refuel_car(0, 10, 20), 10)

    def test_drive(self):
        self.assertEqual(drive_car(10, 100, 10), 0)


if __name__ == "__main__":
    unittest.main()
