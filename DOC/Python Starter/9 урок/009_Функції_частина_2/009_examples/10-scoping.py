def outer_function():
    # створення локальної змінної var
    var = 8

    def inner_function():
        # вказує, що необхідно використовувати глобальну змінну
        global var
        # 0
        print(var)
        var = 10

    # 8
    print(var)
    # виклик внутрішньої функції
    inner_function()
    # 8
    print(var)


# создание глобальной переменной var
var = 0
# 0
print(var)
outer_function()
# 10
print(var)
