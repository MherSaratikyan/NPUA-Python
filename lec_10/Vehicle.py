class Vehicle:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def print_info(self):
        print(f"Make: {self.__make}")
        print(f"Model: {self.__model}")
        print(f"Construction year: {self.__year}")
