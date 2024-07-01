# Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

class Car:
    def __init__(self, make, model, year):
        self._make = make  # Приватне поле для виробника
        self._model = model  # Приватне поле для моделі
        self._year = year  # Приватне поле для року випуску

    # Методи для отримання значень приватних полів (getters)
    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    # Методи для встановлення значень приватних полів (setters)
    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_year(self, year):
        self._year = year


# Приклад використання класу Car
car1 = Car("Toyota", "Camry", 2023)

# Використання методів для доступу до даних (getters)
print(car1.get_make())  # Виведе: Toyota
print(car1.get_model())  # Виведе: Camry
print(car1.get_year())  # Виведе: 2023

# Використання методів для зміни даних (setters)
car1.set_make("Honda")
car1.set_model("Accord")
car1.set_year(2022)

print(car1.get_make())  # Виведе: Honda (після зміни)
print(car1.get_model())  # Виведе: Accord (після зміни)
print(car1.get_year())  # Виведе: 2022 (після зміни)