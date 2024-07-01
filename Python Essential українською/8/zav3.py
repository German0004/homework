# Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON.


import pickle
import json

# Список товарів у форматі словника
products = [
    {"id": 1, "name": "Годинник", "price": 150.0, "quantity": 10},
    {"id": 2, "name": "Фотоапарат", "price": 550.0, "quantity": 5},
    {"id": 3, "name": "Смартфон", "price": 800.0, "quantity": 8},
    {"id": 4, "name": "Навушники", "price": 100.0, "quantity": 15}
]

# Зберігаємо список товарів за допомогою pickle
with open('products.pkl', 'wb') as pickle_file:
    pickle.dump(products, pickle_file)

# Зберігаємо список товарів у форматі JSON
with open('products.json', 'w') as json_file:
    json.dump(products, json_file, indent=4)

print("Список товарів був серіалізований і збережений у файлі 'products.pkl' (pickle) та 'products.json' (JSON).")


# Як це працює:
# Створення списку товарів: Ми створюємо список products, який містить декілька товарів у вигляді словників з
# ключами id, name, price і quantity.

# Серіалізація у форматі pickle:

# Ми використовуємо pickle.dump(products, pickle_file) для серіалізації списку products у бінарний файл products.pkl. pickle
# дозволяє зберегти дані у вигляді, придатному для подальшого використання в Python.

# Серіалізація у форматі JSON:

# Ми використовуємо json.dump(products, json_file, indent=4) для серіалізації списку products у файл products.json у
# форматі JSON. json зберігає дані у текстовому форматі, який є популярним для обміну даними між різними програмами.
# Цей код демонструє як серіалізувати дані за допомогою pickle і json, що є частими методами для збереження структурованих
# даних у Python.