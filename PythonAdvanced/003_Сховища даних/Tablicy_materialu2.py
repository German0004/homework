# Для таблиці «матеріалу» з завдання 4 створіть користувальницьку агрегатну функцію, яка рахує середнє значення ваги всіх
# матеріалів вислідної вибірки й округляє значення до цілого.


import json
import math

def calculate_average_weight(file_path):
    # Читання даних з файлу
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Перевірка, чи дані не порожні
    if not data:
        return "No data available"

    # Обчислення загальної ваги та кількості матеріалів
    total_weight = 0
    count = 0

    for item in data:
        if 'weight' in item:
            total_weight += item['weight']
            count += 1

    # Перевірка, чи є хоча б один матеріал
    if count == 0:
        return "No valid weights found"

    # Обчислення середнього значення ваги
    average_weight = total_weight / count

    # Округлення до цілого
    return round(average_weight)

# Виклик функції та виведення результату
file_path = 'materials.json'
average_weight = calculate_average_weight(file_path)
print(f"The average weight, rounded to the nearest integer, is: {average_weight}")


# Пояснення коду:
# Читання даних: Відкриває файл materials.json і завантажує його вміст у змінну data.
# Перевірка на порожні дані: Якщо data порожній, функція поверне відповідне повідомлення.
# Обчислення загальної ваги та кількості: Ітерує по кожному елементу в data, додаючи значення ваги до total_weight і
# рахуючи кількість записів.
# Обчислення середнього значення: Ділить загальну вагу на кількість матеріалів.
# Округлення до цілого: Використовує функцію round() для округлення середнього значення до найближчого цілого числа.
