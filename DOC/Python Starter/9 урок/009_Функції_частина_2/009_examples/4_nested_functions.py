def outer_function():
    # оголошення функції локально
    def inner_function():
        print('Внутрішня функція')

    print('Зовнішня функція')
    # виклик функції
    inner_function()


# виклик зовнішньої функції
outer_function()
# помилка, тут ця функція недоступна
# inner_function()
