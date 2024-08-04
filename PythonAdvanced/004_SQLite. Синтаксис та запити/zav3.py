# Змініть таблицю так, щоби можна було додати не лише витрати, а й прибутки.

import sqlite3

# Підключаємося до бази даних (створюємо її, якщо не існує)
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Створюємо таблицю з доданим полем type
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purpose TEXT NOT NULL,
        amount REAL NOT NULL,
        type TEXT CHECK(type IN ('expense', 'income')) NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Зберігаємо зміни та закриваємо з'єднання
conn.commit()
conn.close()

# Пояснення:
# Поле type: нове поле type зберігатиме тип транзакції (expense або income). Для цього поля встановлено обмеження CHECK, яке гарантує,
# що значення може бути лише expense або income.
# Заміна назви таблиці: можна змінити назву таблиці на transactions, щоб вона була більш узагальненою і включала як витрати, так і прибутки.