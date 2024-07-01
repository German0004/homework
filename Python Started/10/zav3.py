# Створіть інженерний калькулятор з використанням модуля math, в якому передбачене меню. Під час створення дотримуйтесь
# правил специфікації PEP 8.


import math

def menu():
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Синус")
    print("6. Косинус")
    print("7. Тангенс")
    print("8. Логарифм")
    print("9. Корінь квадратний")
    print("10. Піднести до степеня")
    print("0. Вихід")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ділення на нуль!"

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def logarithm(a):
    if a > 0:
        return math.log(a)
    else:
        return "Логарифм від'ємного числа!"

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Корінь квадратний з від'ємного числа!"

def power(a, b):
    return math.pow(a, b)

def main():
    while True:
        menu()
        choice = input("Введіть номер операції: ")

        if choice == '0':
            print("Вихід з програми.")
            break

        if choice in ['1', '2', '3', '4', '10']:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            if choice == '1':
                print(f"Результат: {add(a, b)}")
            elif choice == '2':
                print(f"Результат: {subtract(a, b)}")
            elif choice == '3':
                print(f"Результат: {multiply(a, b)}")
            elif choice == '4':
                print(f"Результат: {divide(a, b)}")
            elif choice == '10':
                print(f"Результат: {power(a, b)}")

        elif choice in ['5', '6', '7', '8', '9']:
            a = float(input("Введіть число: "))
            if choice == '5':
                print(f"Результат: {sine(a)}")
            elif choice == '6':
                print(f"Результат: {cosine(a)}")
            elif choice == '7':
                print(f"Результат: {tangent(a)}")
            elif choice == '8':
                print(f"Результат: {logarithm(a)}")
            elif choice == '9':
                print(f"Результат: {square_root(a)}")

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()


# Пояснення:
# Меню: Функція menu() відображає всі доступні операції.
# Операції: Функції для кожної математичної операції (add, subtract, multiply, divide, sine, cosine, tangent, logarithm,
# square_root, power).
# Основний цикл: В main() реалізовано головний цикл, який дозволяє користувачу вибирати операції та вводити потрібні числа.
# Перевірки: Додано перевірки для уникнення ділення на нуль та обчислення логарифма чи кореня з від'ємного числа.
# Цей приклад демонструє базовий інженерний калькулятор з відповідним оформленням коду згідно з PEP 8.