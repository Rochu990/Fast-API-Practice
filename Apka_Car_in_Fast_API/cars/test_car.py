import unittest

from car import Car, FuelStatus, DriveStatus


class TestCar(unittest.TestCase):

    def test_refuel(self):
        car = Car(10, 10, 20)
        self.assertEqual(car.refuel(5), FuelStatus(succes=True, msg="Zatankowano auto"))
        self.assertEqual(
            car.refuel(10), FuelStatus(succes=False, msg="Próbujesz zatankować za dużo")
        )

    def test_try_to_refuel_full_tank_fuel(self):
        car = Car(10, 20, 20)
        self.assertEqual(
            car.refuel(5), FuelStatus(succes=False, msg="Próbujesz zatankować za dużo")
        )

    def test_try_to_refuel_empty_fuel_tank(self):
        car = Car(10, 0, 20)
        self.assertEqual(car.refuel(5), FuelStatus(succes=True, msg="Zatankowano auto"))

    def test_drive(self):
        car = Car(10, 10, 20)
        self.assertEqual(car.drive(100), DriveStatus(succes=True, msg='Dojechałeś do celu'))

    def test_drive_with_empty_fuel_tank(self):
        car = Car(10, 0 ,20)
        self.assertEqual(car.drive(100), DriveStatus(succes=False, msg="Zabrakło paliwa"))
    
    def test_use_half_of_fuel(self):
        car = Car(10, 20 ,20)
        self.assertEqual(car.drive(100), DriveStatus(succes=True, msg='Dojechałeś do celu'))

    def test_drive_four_destination_in_the_same_kilometres(self):
        car = Car(10, 20 ,20)
        self.assertEqual(car.drive(50), DriveStatus(succes=True, msg='Dojechałeś do celu'))
        self.assertEqual(car.drive(50), DriveStatus(succes=True, msg='Dojechałeś do celu'))
        self.assertEqual(car.drive(50), DriveStatus(succes=True, msg='Dojechałeś do celu'))
        self.assertEqual(car.drive(50), DriveStatus(succes=True, msg='Dojechałeś do celu'))
    
    def test_not_enought_fuel_in_second_drive(self):
        car = Car(10, 10, 20)
        self.assertEqual(car.drive(100), DriveStatus(succes=True, msg='Dojechałeś do celu'))
        self.assertEqual(car.drive(10), DriveStatus(succes=False, msg="Zabrakło paliwa"))



if __name__ == "__main__":
    unittest.main()
