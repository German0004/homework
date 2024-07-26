# Для таблиці «матеріалу» з завдання 4 створіть функцію користувача, яка приймає необмежену кількість полів і
# повертає їх конкатенацію.


import json

# Функція для конкатенації необмеженої кількості полів
def concatenate_fields(*args):
    return ''.join(map(str, args))

# Приклад даних таблиці "матеріали"
data = [
    {
        "id": 1,
        "weight": 12.34,
        "height": 56.78,
        "additional_characteristics": [
            ["Color", "Red"],
            ["Density", "1.5 g/cm3"]
        ]
    },
    {
        "id": 2,
        "weight": 23.45,
        "height": 67.89,
        "additional_characteristics": [
            ["Color", "Blue"],
            ["Density", "1.8 g/cm3"]
        ]
    }
]

# Запис даних у файл
with open('materials.json', 'w') as file:
    json.dump(data, file, indent=4)

# Читання даних з файлу
with open('materials.json', 'r') as file:
    data = json.load(file)
    print(data)

# Використання функції для конкатенації полів
for material in data:
    concatenated_fields = concatenate_fields(
        material["id"],
        material["weight"],
        material["height"],
        *(characteristic for characteristic in material["additional_characteristics"])
    )
    print(f'Concatenated fields for material {material["id"]}: {concatenated_fields}')

# Цей код включає функцію concatenate_fields, яка приймає будь-яку кількість аргументів і повертає їх конкатенацію. Функція
# використовується для конкатенації полів кожного матеріалу в таблиці.