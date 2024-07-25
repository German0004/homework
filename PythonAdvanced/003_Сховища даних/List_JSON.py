# Створіть прості словники та конвертуйте їх у JSON. Збережіть JSON у файлі та спробуйте завантажити дані з файлу.

import json

# Створення простих словників
data = {
    "name": "Evgen Dudin",
    "age": 42,
    "city": "Lutsk",
    "is_student": True,
    "courses": ["Math", "Science", "English"]
}

# Конвертація словників у JSON
json_data = json.dumps(data, indent=4)

# Збереження JSON у файл
with open("data.json", "w", encoding='utf-8') as file:
    file.write(json_data)

print("Дані збережено у файл data.json")

# Завантаження даних з файлу
with open("data.json", "r", encoding='utf-8') as file:
    loaded_data = json.load(file)

print("Завантажені дані:")
print(loaded_data)

# Пояснення:
#
# Створення простих словників:
#
# Ми створюємо словник data, який містить різні типи даних.
# Конвертація словників у JSON:
#
# Використовуємо функцію json.dumps() для конвертації словника у JSON. Параметр indent=4 робить JSON більш читабельним.
# Збереження JSON у файл:
#
# Використовуємо контекстний менеджер with open для відкриття файлу в режимі запису ("w") та записуємо JSON-дані у файл.
# Завантаження даних з файлу:
#
# Знову використовуємо контекстний менеджер with open для відкриття файлу в режимі читання ("r") та завантажуємо JSON-дані з файлу за допомогою функції json.load().
