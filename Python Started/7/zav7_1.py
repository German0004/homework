# Створіть прототип програми «Облік кадрів», в якій є можливість перегляду та внесення змін до структури
# (реалізуйте інтерфейс(меню), за допомогою якого можна робити маніпуляції з даними):
# прізвище: name:
#   посада: ... position:
#   досвід роботи: experience:
#   портфоліо: portfolio:
#   коефіцієнт ефективності: efficiency factor:
#   стек технологій: technology stack:
#   зарплата: salary:
# Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим співробітником.


class Employee:
    def __init__(
        self, surname, position, experience, portfolio, efficiency, technologies, salary
    ):
        self.surname = surname
        self.position = position
        self.experience = experience
        self.portfolio = portfolio
        self.efficiency = efficiency
        self.technologies = technologies
        self.salary = salary

    def __str__(self):
        return (
            f"Прізвище: {self.surname}\n"
            f"Посада: {self.position}\n"
            f"Досвід роботи: {self.experience}\n"
            f"Портфоліо: {self.portfolio}\n"
            f"Коефіцієнт ефективності: {self.efficiency}\n"
            f"Стек технологій: {self.technologies}\n"
            f"Зарплата: {self.salary}\n"
        )


class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employees(self):
        for employee in self.employees:
            print(employee)

    def edit_employee(self, surname):
        for employee in self.employees:
            if employee.surname == surname:
                print("Знайдено співробітника. Введіть нові дані:")
                employee.position = input("Нова посада: ")
                employee.experience = input("Новий досвід роботи: ")
                employee.portfolio = input("Нове портфоліо: ")
                employee.efficiency = float(input("Новий коефіцієнт ефективності: "))
                employee.technologies = input("Новий стек технологій: ")
                employee.salary = float(input("Нова зарплата: "))
                print("Дані оновлено.\n")
                return
        print("Співробітника не знайдено.\n")

    def sort_by_surname(self):
        sorted_employees = sorted(self.employees, key=lambda e: e.surname)
        for employee in sorted_employees:
            print(employee)

    def find_most_efficient_employee(self):
        if not self.employees:
            print("Немає співробітників для перегляду.\n")
            return
        most_efficient_employee = max(self.employees, key=lambda e: e.efficiency)
        print("Найефективніший співробітник:\n")
        print(most_efficient_employee)


def main():
    database = EmployeeDatabase()

    while True:
        print("Меню:")
        print("1. Додати співробітника")
        print("2. Переглянути всіх співробітників")
        print("3. Редагувати дані співробітника")
        print("4. Сортувати за прізвищем")
        print("5. Показати найефективнішого співробітника")
        print("6. Вихід")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            surname = input("Прізвище: ")
            position = input("Посада: ")
            experience = input("Досвід роботи: ")
            portfolio = input("Портфоліо: ")
            efficiency = float(input("Коефіцієнт ефективності: "))
            technologies = input("Стек технологій: ")
            salary = float(input("Зарплата: "))
            employee = Employee(
                surname,
                position,
                experience,
                portfolio,
                efficiency,
                technologies,
                salary,
            )
            database.add_employee(employee)
            print("Співробітника додано.\n")

        elif choice == "2":
            database.view_employees()

        elif choice == "3":
            surname = input("Введіть прізвище співробітника для редагування: ")
            database.edit_employee(surname)

        elif choice == "4":
            database.sort_by_surname()

        elif choice == "5":
            database.find_most_efficient_employee()

        elif choice == "6":
            break

        else:
            print("Неправильний вибір, спробуйте ще раз.\n")


if __name__ == "__main__":
    main()
