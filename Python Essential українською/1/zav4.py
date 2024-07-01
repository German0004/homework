# Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів, доступних для
# продажу, і функцію продажу заданого автомобіля.


class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price}"


class CarDealership:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def sell_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model:
                self.cars.remove(car)
                return f"Sold: {car}"
        return "Car not found"

    def list_cars(self):
        if not self.cars:
            return "No cars available"
        return "\n".join(str(car) for car in self.cars)


# Приклад використання
if __name__ == "__main__":
    dealership = CarDealership()

    car1 = Car("Toyota", "Corolla", 2020, 20000)
    car2 = Car("Honda", "Civic", 2019, 18000)
    car3 = Car("Ford", "Mustang", 2021, 35000)

    dealership.add_car(car1)
    dealership.add_car(car2)
    dealership.add_car(car3)

    print("Available cars:")
    print(dealership.list_cars())

    print("\nSelling a car:")
    print(dealership.sell_car("Honda", "Civic"))

    print("\nAvailable cars after sale:")
    print(dealership.list_cars())
