# Створіть дві функції, що обчислюють значення певних алгебраїчних виразів. На екрані виведіть таблицю значень
# цих функцій від -5 до 5 з кроком 0.5.


def quadratic_expression(x):
    return x**2 + 2


def cubic_expression(x):
    return x**3 - x


def print_table(start, end, step, func):
    print(" x    |   f(x)   ")
    print("----------------")
    x = start
    while x <= end:
        result = func(x)
        print("{:5.2f} | {:8.2f}".format(x, result))
        x += step


print("Таблиця значень квадратного виразу x**2 + 2:")
print_table(-5, 5, 0.5, quadratic_expression)

print("\nТаблиця значень кубічного виразу x**3 - x:")
print_table(-5, 5, 0.5, cubic_expression)
