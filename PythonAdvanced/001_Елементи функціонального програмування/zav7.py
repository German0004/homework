# Створіть звичайну функцію множення двох чисел. Створіть карированну функцію
# множення двох чисел. Частково застосуйте її до одного аргументу, до двох аргументiв.


def normal_function(a, b):
    return a * b

# Використання звичайної функції
result = normal_function(3, 4)
print(f"Результат звичайної функції: {result}")


# Карирована функція множення двох чисел

def curried_normal_function(a):
    def inner(b):
        return a * b
    return inner

# Використання карированої функції
# Часткове застосування до одного аргументу
multiply_by_3 = curried_normal_function(3)

# Застосування частково застосованої функції до другого аргументу
result1 = multiply_by_3(4)

# Можна одразу застосувати обидва аргументи
result2 = curried_normal_function(3)(5)

print(f"Результат карированої функції (часткове застосування): {result1}")
print(f"Результат карированої функції (одразу два аргументи): {result2}")


# Пояснення:
#
# Звичайна функція multiply(a, b):
#
# Приймає два аргументи a і b.
# Повертає результат множення a * b.
# Приклад використання: multiply(3, 4) повертає 12.
# Карирована функція curried_multiply(a):
#
# Приймає один аргумент a.
# Повертає внутрішню функцію inner(b), яка приймає другий аргумент b і повертає результат множення a * b.
# Приклад використання: curried_multiply(3) повертає функцію, яку можна застосувати до другого аргументу, наприклад,
# multiply_by_3(4), що повертає 12.
# Можна одразу застосувати обидва аргументи: curried_multiply(3)(4) повертає 12.
# Таким чином, карирована функція дозволяє частково застосовувати аргументи, що може бути корисним у функціональному
# програмуванні та при створенні більш гнучких функцій.