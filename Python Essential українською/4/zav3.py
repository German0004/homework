# Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи. Конструктор має генерувати
# виняток, якщо вказано неправильні дані. Введіть список працівників із клавіатури. Виведіть усіх співробітників, які були
# прийняті після цього року.


class Employee:
    def __init__(self, name, surname, department, start_year):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(department, str) or not isinstance(start_year, int):
            raise ValueError("Invalid data type for employee attributes")

        if start_year < 1900 or start_year > 2100:
            raise ValueError("Invalid start year for employee")

        self.name = name
        self.surname = surname
        self.department = department
        self.start_year = start_year

# Функція для введення списку працівників з клавіатури
def input_employees():
    employees = []
    while True:
        try:
            name = input("Enter employee's name (or 'exit' to finish): ")
            if name.lower() == 'exit':
                break

            surname = input("Enter employee's surname: ")
            department = input("Enter employee's department: ")
            start_year = int(input("Enter employee's start year: "))

            # Створення об'єкта Employee і додавання до списку
            employee = Employee(name, surname, department, start_year)
            employees.append(employee)
            print("Employee added successfully!")

        except ValueError as ve:
            print(f"Error: {ve}")

    return employees

# Функція для виведення співробітників, які були прийняті після певного року
def print_employees_after_year(employees, year):
    print(f"\nEmployees hired after {year}:")
    for employee in employees:
        if employee.start_year > year:
            print(f"{employee.name} {employee.surname}, Department: {employee.department}, Start Year: {employee.start_year}")

# Введення списку працівників з клавіатури
employees_list = input_employees()

# Виведення співробітників, які були прийняті після певного року (наприклад, після 2010 року)
print_employees_after_year(employees_list, 2010)
# У цьому прикладі:
#
# Клас Employee має конструктор __init__, який перевіряє правильність типів даних і коректність значень для
# полів name, surname, department і start_year. Функція input_employees() використовується для введення даних
# про співробітників з клавіатури. Вона продовжує працювати, доки користувач не введе "exit". У разі виявлення
# помилки (наприклад, неправильного формату даних), вона виводить повідомлення про помилку і продовжує роботу.
# Функція print_employees_after_year() приймає список співробітників і рік, і виводить на екран інформацію про
# тих співробітників, які були прийняті після вказаного року.