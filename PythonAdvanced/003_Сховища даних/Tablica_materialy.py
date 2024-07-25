# Створіть таблицю «матеріали» з таких полів: ідентифікатор, вага, висота та додаткові характеристики матеріалу. Поле «додаткові
# характеристики матеріалу» має зберігати у собі масив, кожен елемент якого є кортежем із двох значень:
# перше – назва характеристики, а друге – її значення.

# Використання JSON для зберігання данних
# [
#     {
#         "id": 1,
#         "weight": 12.34,
#         "height": 56.78,
#         "additional_characteristics": [
#             ["Color", "Red"],
#             ["Density", "1.5 g/cm3"]
#         ]
#     },
#     {
#         "id": 2,
#         "weight": 23.45,
#         "height": 67.89,
#         "additional_characteristics": [
#             ["Color", "Blue"],
#             ["Density", "2.0 g/cm3"]
#         ]
#     }
# ]

# Операціії з JSON
import json

# Запис даних у файл
data = [
    {
        "id": 1,
        "weight": 12.34,
        "height": 56.78,
        "additional_characteristics": [
            ["Color", "Red"],
            ["Density", "1.5 g/cm3"]
        ]
    }
]

with open('materials.json', 'w') as file:
    json.dump(data, file, indent=4)

# Читання даних з файлу
with open('materials.json', 'r') as file:
    data = json.load(file)
    print(data)


