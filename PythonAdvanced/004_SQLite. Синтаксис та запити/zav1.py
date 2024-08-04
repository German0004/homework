# Зробіть таблицю для підрахунку особистих витрат із такими полями: id, призначення, сума, час.
import sqlite3

# Підключаємося до бази даних (створюємо її, якщо не існує)
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Створюємо таблицю
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purpose TEXT NOT NULL,
        amount REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Зберігаємо зміни та закриваємо з'єднання
conn.commit()
conn.close()

# Пояснення:
# Підключення до бази даних:
#
# sqlite3.connect('expenses.db') створює або відкриває базу даних з іменем expenses.db.
# Виконання SQL-запиту:
#
# cursor.execute(''' ... ''') використовується для виконання SQL-запиту в базі даних.
# Збереження змін:
#
# conn.commit() зберігає зміни в базі даних.
# Закриття з'єднання:
#
# conn.close() закриває з'єднання з базою даних, щоб уникнути витоків пам'яті.
# Цей код створить таблицю expenses, якщо вона ще не існує, і працюватиме без помилок.