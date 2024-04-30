# 1 Inheritance:

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


animal = Animal("Pūkis", 10)
dog = Dog("Rokis", 5, "black")


# 2 Encapsulation:

class Car:
    def __init__(self, make, model, consumption, origin="Europe"):
        self.make = make
        self.model = model
        self._full_model = f"{self.make} {self.model}"
        self.consumption = consumption
        self.origin = origin

    def _convert_to_liters(self):
        return round(235.21 / self.consumption, 2)

    def _convert_to_gallons(self):
        return round(235.2145 / self.consumption, 2)

    def print_consumption(self):
        if self.origin == "USA":
            print(f"{self._full_model} consumption:")
            print(f"{self._convert_to_liters()} l/100 km")
            print("or")
            print(f"{self.consumption} mpg (miles per gallon)")
            print()
        if self.origin == "Europe":
            print(f"{self._full_model} consumption:")
            print(f"{self.consumption} l/100 km")
            print("or")
            print(f"{self._convert_to_gallons()} mpg (miles per gallon)")
            print()


car = Car("Toyota", "Corolla Hybrid", 5)
car2 = Car("Ford", "Mustang Convertible VII GT 5.0 V8 (486 Hp) SelectShift", 18, "USA")

car.print_consumption()
car2.print_consumption()


# Polymorphism:

class Animal:
    def run(self):
        print("I'm running")


class Turtle(Animal):
    def run(self):
        print("I can't run")


animal2 = Animal()
animal3 = Turtle()

animal2.run()
animal3.run()


# Abstraction:

class Man:
    def run(self):
        pass


class Employee(Man):
    def run(self):
        print("I'm running")


emp2 = Employee()
emp2.run()
