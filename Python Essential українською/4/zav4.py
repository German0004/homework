# Опишіть свій клас винятку. Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе певне значення, і перехопіть
# цей виняток під час виклику функції.


# Щоб створити власний клас винятку в Python, потрібно успадкувати його від базового класу Exception або від одного з
# його нащадків. Ось як можна це зробити:

# Визначення власного класу винятку
class CustomException(Exception):
    def __init__(self, message="Це моя власна помилка"):
        self.message = message
        super().__init__(self.message)

# Функція, яка викидає виняток на певному умові
def raise_exception(value):
    if value == 42:
        raise CustomException("Користувач ввів заборонене значення: 42")

# Перехоплення винятку під час виклику функції
try:
    user_input = int(input("Введіть число: "))
    raise_exception(user_input)
except CustomException as ce:
    print(f"Виняток під час виконання програми: {ce}")
except ValueError:
    print("Потрібно ввести ціле число")
except Exception as e:
    print(f"Неочікувана помилка: {e}")
# Основні моменти:

# Клас винятку CustomException: Цей клас успадковується від базового класу Exception. У конструкторі можна передати власне
# повідомлення для винятку. Суперклас Exception викликається для ініціалізації власного повідомлення.

# Функція raise_exception: Ця функція перевіряє, чи введене користувачем значення дорівнює 42. Якщо так, вона викидає виняток
# CustomException з власним повідомленням.

# Перехоплення винятку: Під час виклику функції raise_exception, виняток CustomException може бути перехоплений у
# блоках except. Використовуючи except CustomException as ce, ми можемо отримати доступ до об'єкта винятку і вивести
# його повідомлення.