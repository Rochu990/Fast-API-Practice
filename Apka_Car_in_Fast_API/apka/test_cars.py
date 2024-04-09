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



if __name__ == "__main__":
    unittest.main()
