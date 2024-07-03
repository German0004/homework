def outer_function():
    # створення локальної змінної var
    var = 8

    def inner_function():
        # вказує, що необхідно використовувати змінну із зовнішньої функції
        nonlocal var
        # 8
        print(var)
        var = 10

    # 8
    print(var)
    # виклик внутрішньої функції
    inner_function()
    # 10
    print(var)


# створення глобальної змінної var
var = 0
# 0
print(var)
outer_function()
# 0
print(var)
