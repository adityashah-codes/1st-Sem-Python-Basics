class car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def details(self):
        return f"The {self.color} car has {self.mileage} miles"

car_1 = car("blue", 20000)
car_2 = car("red", 30000)
        
print(car_1.details())
print(car_2.details())

for car in (car_1, car_2):
    print(car.details())