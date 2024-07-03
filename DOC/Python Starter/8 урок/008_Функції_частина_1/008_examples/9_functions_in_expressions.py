def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# Виклик функції може бути частиною виразу
print(add(2, 3) + sub(2, 3))  # => print((2 + 3) + (2 - 3))
