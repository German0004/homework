# Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від класу Shape. Перевизначте
# їх методи. Створіть екземпляри відповідних класів за скористайтеся всіма методами. В результаті повинно з’явитися зображення.
# Перегляньте їх.


# Базовий клас Shape
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def volume(self):
        pass


# Клас Cone, який успадковує клас Shape
class Cone(Shape):
    def __init__(self, name, radius, height):
        super().__init__(name)
        self.radius = radius
        self.height = height

    def area(self):
        return 3.14 * self.radius * (self.radius + (self.radius ** 2 + self.height ** 2) ** 0.5)

    def volume(self):
        return 3.14 * self.radius ** 2 * (self.height / 3)


# Клас Paraboloid, який успадковує клас Shape
class Paraboloid(Shape):
    def __init__(self, name, radius, height):
        super().__init__(name)
        self.radius = radius
        self.height = height

    def area(self):
        return 2 * 3.14 * self.radius * (self.radius + self.height)

    def volume(self):
        return (1 / 2) * 3.14 * self.radius ** 2 * self.height


# Створення екземплярів відповідних класів
cone = Cone("Cone", 5, 10)
paraboloid = Paraboloid("Paraboloid", 3, 6)

# Використання методів
print(f"Area of {cone.name}: {cone.area()}")
print(f"Volume of {cone.name}: {cone.volume()}")

print(f"Area of {paraboloid.name}: {paraboloid.area()}")
print(f"Volume of {paraboloid.name}: {paraboloid.volume()}")