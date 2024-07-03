def function(a, b):
    if b == a:
        return b
    return b + function(a, b - 1)


number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
print(function(number1, number2))
