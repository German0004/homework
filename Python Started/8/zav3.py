# Створіть програму-калькулятор, яка підтримує наступні операції: додавання, віднімання, множення, ділення, зведення
# в ступінь, зведення до квадратного та кубічного коренів. Всі дані повинні вводитися в циклі, доки користувач не
# вкаже, що хоче завершити виконання програми. Кожна операція має бути реалізована у вигляді окремої функції.
# Функція ділення повинна перевіряти дані на коректність та видавати повідомлення про помилку у разі спроби поділу на нуль.


import math


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Помилка! Ділення на нуль неможливе."
    else:
        return x / y


def square(x, y):
    return x**y


def square_root(x):
    if x < 0:
        return "Помилка! Корінь з від'ємного числа неможливий."
    else:
        return math.sqrt(x)


def cubic_root(x):
    return x ** (1 / 3)


# Головна програма
while True:
    print("\nВиберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Зведення в ступінь")
    print("6. Квадратний корінь")
    print("7. Кубічний корінь")
    print("8. Вихід")

    choice = input("Введіть номер операції: ")

    if choice in ("1", "2", "3", "5"):
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if choice == "1":
            print("Результат:", addition(num1, num2))
        elif choice == "2":
            print("Результат:", subtraction(num1, num2))
        elif choice == "3":
            print("Результат:", multiply(num1, num2))
        elif choice == "5":
            print("Результат:", square(num1, num2))
    elif choice == "4":
        num1 = float(input("Введіть ділене: "))
        num2 = float(input("Введіть дільник: "))
        print("Результат:", divide(num1, num2))
    elif choice == "6":
        num = float(input("Введіть число: "))
        print("Результат:", square_root(num))
    elif choice == "7":
        num = float(input("Введіть число: "))
        print("Результат:", cubic_root(num))
    elif choice == "8":
        print("До побачення!")
        break
    else:
        print("Невірний ввід! Спробуйте ще раз.")
