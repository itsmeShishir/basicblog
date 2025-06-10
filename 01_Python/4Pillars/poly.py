# Polymorphishm -> many forms
# Overloading -> same name different parameter
# Overriding -> same name same parameter
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    def move(self):
        print("move")

class boat:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    def move(self):
        print("Sail")

class plane:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    def move(self):
        print("Fly")

car1 = Car("Honda", "Civic", 2020)
boat1 = boat("Ferari", "Ferari", 2020)
plane1 = plane("Ferari", "Ferari", 2025)

for i in (car1, boat1, plane1):
    i.move()