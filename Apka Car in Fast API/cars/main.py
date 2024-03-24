from fastapi import FastAPI, Query
from pydantic import BaseModel

from cars import Cars
from repository import Repository

app = FastAPI()


class CarDetails(BaseModel):
    combustion: int = 10
    tank_fuel: float = 10
    max_fuel: int = 20


repository = Repository()
cars = Cars(repository)


@app.post("/create_car/{car_id}")
async def create_car(car_id: int, car: CarDetails):
    return cars.add(car_id, car.dict())


@app.get("/get_car/{car_id}")
async def get_car_by_id(car_id: int):
    return repository.get(car_id)


@app.put("/refuel_car/{car_id}")
async def refuel_car(car_id: int, fuel: int | None = Query(default=1)):
    return cars.refuel(car_id, fuel)


@app.put("/drive/{car_id}")
async def drive(car_id: int, kilometers: int | None = None):
    return cars.drive(car_id, kilometers)
