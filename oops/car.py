class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0

    def accelerate(self, increase):
        self.speed += increase
        print(f"The {self.color} {self.brand} accelerates to {self.speed} km/h.")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"The {self.color} {self.brand} slows down to {self.speed} km/h.")


my_car = Car("Toyota", "red")
my_car.accelerate(30)
my_car.brake(10)
