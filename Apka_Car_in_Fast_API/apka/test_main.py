from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_car():
    car = {"combustion": 10, "tank_fuel": 10, "max_fuel": 20}
    response = client.post("/create_car/1", json=car)
    response.status_code == 200
    assert response.json() == {"combustion": 10, "tank_fuel": 10, "max_fuel": 20}


def test_refuel_car_to_full_tank_fuel():
    response = client.put("/refuel_car/1?fuel=10")
    assert response.json() == {"combustion": 10, "tank_fuel": 20, "max_fuel": 20}


def test_refuel_when_tank_fuel_is_full():

    response = client.put("/refuel_car/1?fuel=20")
    assert response.json() == {"detail": "Próbujesz zatankować za dużo"}


# def test_drive_car_when_tank_fuel_is_full():
#     resposne = client.put("/drive/1?kilometers=200")
#     assert resposne.json() == {"Dojechałeś do celu"}


def test_try_to_refuel_car_more_than_max_tank_fuel_capacity():
    response = client.put("/refuel_car/1?fuel=21")
    assert response.json() == {"detail": "Próbujesz zatankować za dużo"}


def test_try_to_use_more_gas_than_max_tank_fuel():
    resposne = client.put("/drive/1?kilometers=250")
    assert resposne.json() == {"detail": "Zabrakło paliwa"}
