import unittest

from car import Car
from cars import Cars
from repository import Repository


class TestCar(unittest.TestCase):

    def test_po_zatankowaniu_do_pelna_paliwa_i_przejechaniu_10_km_zostalo_mi_10_paliwa(self):
        # arrange
        repository = Repository()
        cars = Cars(repository)
        car1 = Car(10, 10, 20)
        cars.add(car1.id, car1.to_dict())
        # act 
        cars.drive(car1.id, 100)
        cars.refuel(car1.id, 10)
        result = cars.get(car1.id)
        # assert
        self.assertEqual(result, {'combustion': 10, 'tank_fuel': 10, 'max_fuel': 20})

    def test_refuel_car_to_full_fuel_tank_and_then_refuel_again(self):
        repository = Repository()
        cars = Cars(repository)
        car1 = Car(10, 10, 20)
        cars.add(car1.id, car1.to_dict())
        cars.refuel(car1.id,10)
        cars.refuel(car1.id,1)
        result = cars.get(car1.id)
        self.assertEqual(result, {'combustion': 10, 'tank_fuel': 20, 'max_fuel': 20})

    def test_drive_with_empty_fuel_tank(self):
        repository = Repository()
        cars = Cars(repository)
        car1 = Car(10, 0, 20)
        cars.add(car1.id, car1.to_dict())
        cars.drive(car1.id, 100)
        result = cars.get(car1.id)
        self.assertEqual(result, {'combustion': 10, 'tank_fuel': 0, 'max_fuel': 20})




if __name__ == "__main__":
    unittest.main()
