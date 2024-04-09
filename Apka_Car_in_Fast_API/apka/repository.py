

class Repository:

    def __init__(self):
        self.cars = {}

    def add(self, id: int, car: dict):
        self.cars[id] = car
        return car

    def delete(self, id: int):
        del self.cars[id]

    def get(self, id: int) -> dict:
        return self.cars[id]
