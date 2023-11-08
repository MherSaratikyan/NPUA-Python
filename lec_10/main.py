from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, make, model, year, weight):
        super().__init__(make, model, year)
        self.__weight = weight

    def print_info(self):
        super().print_info()
        print(f"Weight: {self.__weight} kg")

    def move(self):
        print(f"The {self._Vehicle__make} {self._Vehicle__model} is moving")

class Plane(Vehicle):
    def __init__(self, make, model, year, altitude):
        super().__init__(make, model ,year)
        self.__altitude = altitude

    def print_info(self):
        super().print_info()
        print(f"Altitude: {self.__altitude} feets")

    def fly(self):
        print(f"The {self._Vehicle__make} {self._Vehicle__model} is flying")

class Boat(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.__type = type

    def print_info(self):
        super().print_info()
        print(f"Type: {self.__type}")

    def sail(self):
        print(f"The {self.__type} {self._Vehicle__make} {self._Vehicle__model} is sailing")

class RaceCar(Car):
    def __init__(self, make, model, year, weight, max_speed):
        super().__init__(make, model, year, weight)
        self.__max_speed = max_speed
    
    def print_info(self):
        super().print_info()
        print(f"Max speed: {self.__max_speed} mph")
    
#main logic


car = Car("Toyota", "Camry", 2020, 1500)
car.print_info()
car.move()

plane = Plane("Boeing", "747", 2000, 30000)
plane.print_info()
plane.fly()

boat = Boat("Yamaha", "242X", 2018, "Speedboat")
boat.print_info()
boat.sail()


race_car = RaceCar("Ferrari", "F1", 2023, 700, 270)
race_car.print_info()
race_car.move()