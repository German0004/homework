# Створіть ієрархію класів транспортних засобів. У загальному класі опишіть загальні всім транспортних засобів поля,
# у спадкоємцях – специфічні їм. Створіть кілька екземплярів. Виведіть інформацію щодо кожного транспортного засобу


# Базовий клас для транспортних засобів
class Transport:
    def __init__(self, name, max_speed, capacity):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity

    def get_info(self):
        return f"Name: {self.name}, Max Speed: {self.max_speed} km/h, Capacity: {self.capacity} people"

# Клас для автомобілів
class Car(Transport):
    def __init__(self, name, max_speed, capacity, num_doors):
        super().__init__(name, max_speed, capacity)
        self.num_doors = num_doors

    def get_info(self):
        return super().get_info() + f", Number of Doors: {self.num_doors}"

# Клас для велосипедів
class Bicycle(Transport):
    def __init__(self, name, max_speed, capacity, type_bike):
        super().__init__(name, max_speed, capacity)
        self.type_bike = type_bike

    def get_info(self):
        return super().get_info() + f", Type: {self.type_bike}"

# Клас для літаків
class Airplane(Transport):
    def __init__(self, name, max_speed, capacity, range_km):
        super().__init__(name, max_speed, capacity)
        self.range_km = range_km

    def get_info(self):
        return super().get_info() + f", Range: {self.range_km} km"

# Створення екземплярів класів
car = Car("Toyota Camry", 240, 5, 4)
bicycle = Bicycle("Giant Escape 3", 25, 1, "Road")
airplane = Airplane("Boeing 747", 920, 660, 13800)

# Виведення інформації про кожен транспортний засіб
print(car.get_info())
print(bicycle.get_info())
print(airplane.get_info())


# Цей код створює ієрархію класів для транспортних засобів і визначає специфічні атрибути для кожного типу.
