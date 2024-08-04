# Create an Exchange Rates To USD db using API Monobank (api.monobank.ua). Do requests via request lib,
# parse results, write it into db. (3 examples required)
# Example:
# Table - Exchange Rate To USD:
#
# id (INT PRIMARY KEY) - 1, 2, 3, ...
# currency_name (TEXT) - UAH
# currency_value (REAL) - 39.5
# current_date (DATETIME) - 10/22/2022 7:00 PM


import sqlite3
import requests
from datetime import datetime


# Функція для створення та підключення до бази даних
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


# Функція для створення таблиці обмінних курсів
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_name TEXT NOT NULL,
            currency_value REAL NOT NULL,
            current_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()


# Функція для вставки даних у таблицю
def insert_exchange_rate(conn, currency_name, currency_value):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO exchange_rates (currency_name, currency_value, current_date)
        VALUES (?, ?, ?)
    ''', (currency_name, currency_value, datetime.now()))
    conn.commit()


# Функція для отримання обмінних курсів з API Monobank
def fetch_exchange_rates():
    url = "https://api.monobank.ua/bank/currency"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


# Основна функція для отримання даних та збереження їх у базу даних
def main():
    database = "exchange_rates.db"
    conn = create_connection(database)
    create_table(conn)

    try:
        rates = fetch_exchange_rates()

        # Припустимо, що дані містять обмінні курси для UAH (на приклад, 978 - USD)
        for rate in rates:
            currency_code = rate['currencyCodeA']
            if currency_code == 978:  # USD
                currency_name = "UAH"
                currency_value = rate['rateBuy']  # або 'rateSell', залежно від ваших потреб
                insert_exchange_rate(conn, currency_name, currency_value)

        print("Exchange rates successfully updated in the database.")

    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

Для
створення
бази
даних
обмінних
курсів
до
USD
з
використанням
API
Monobank, ви
можете
виконати
наступні
кроки:

Отримайте
дані
з
API
Monobank
Розпізнайте
дані
Запишіть
їх
у
базу
даних
SQLite
Ось
повний
приклад
коду
на
Python, який
демонструє
цей
процес:

1.
Встановлення
необхідних
бібліотек
Якщо
у
вас
ще
не
встановлена
бібліотека
requests, ви
можете
встановити
її
за
допомогою
pip:

bash
Копіювати
код
pip
install
requests
2.
Код
Python
для
отримання
даних
та
збереження
їх
у
базі
даних
python
Копіювати
код
import sqlite3
import requests
from datetime import datetime


# Функція для створення та підключення до бази даних
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


# Функція для створення таблиці обмінних курсів
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_name TEXT NOT NULL,
            currency_value REAL NOT NULL,
            current_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()


# Функція для вставки даних у таблицю
def insert_exchange_rate(conn, currency_name, currency_value):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO exchange_rates (currency_name, currency_value, current_date)
        VALUES (?, ?, ?)
    ''', (currency_name, currency_value, datetime.now()))
    conn.commit()


# Функція для отримання обмінних курсів з API Monobank
def fetch_exchange_rates():
    url = "https://api.monobank.ua/bank/currency"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


# Основна функція для отримання даних та збереження їх у базу даних
def main():
    database = "exchange_rates.db"
    conn = create_connection(database)
    create_table(conn)

    try:
        rates = fetch_exchange_rates()

        # Припустимо, що дані містять обмінні курси для UAH (на приклад, 978 - USD)
        for rate in rates:
            currency_code = rate['currencyCodeA']
            if currency_code == 978:  # USD
                currency_name = "UAH"
                currency_value = rate['rateBuy']  # або 'rateSell', залежно від ваших потреб
                insert_exchange_rate(conn, currency_name, currency_value)

        print("Exchange rates successfully updated in the database.")

    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

Для
створення
бази
даних
обмінних
курсів
до
USD
з
використанням
API
Monobank, ви
можете
виконати
наступні
кроки:

Отримайте
дані
з
API
Monobank
Розпізнайте
дані
Запишіть
їх
у
базу
даних
SQLite
Ось
повний
приклад
коду
на
Python, який
демонструє
цей
процес:

1.
Встановлення
необхідних
бібліотек
Якщо
у
вас
ще
не
встановлена
бібліотека
requests, ви
можете
встановити
її
за
допомогою
pip:

bash
Копіювати
код
pip
install
requests
2.
Код
Python
для
отримання
даних
та
збереження
їх
у
базі
даних
python
Копіювати
код
import sqlite3
import requests
from datetime import datetime


# Функція для створення та підключення до бази даних
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


# Функція для створення таблиці обмінних курсів
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exchange_rates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency_name TEXT NOT NULL,
            currency_value REAL NOT NULL,
            current_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()


# Функція для вставки даних у таблицю
def insert_exchange_rate(conn, currency_name, currency_value):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO exchange_rates (currency_name, currency_value, current_date)
        VALUES (?, ?, ?)
    ''', (currency_name, currency_value, datetime.now()))
    conn.commit()


# Функція для отримання обмінних курсів з API Monobank
def fetch_exchange_rates():
    url = "https://api.monobank.ua/bank/currency"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


# Основна функція для отримання даних та збереження їх у базу даних
def main():
    database = "exchange_rates.db"
    conn = create_connection(database)
    create_table(conn)

    try:
        rates = fetch_exchange_rates()

        # Припустимо, що дані містять обмінні курси для UAH (на приклад, 978 - USD)
        for rate in rates:
            currency_code = rate['currencyCodeA']
            if currency_code == 978:  # USD
                currency_name = "UAH"
                currency_value = rate['rateBuy']  # або 'rateSell', залежно від ваших потреб
                insert_exchange_rate(conn, currency_name, currency_value)

        print("Exchange rates successfully updated in the database.")

    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")

    finally:
        conn.close()


if __name__ == "__main__":
    main()

# Пояснення:

# create_connection(db_file): Підключається до SQLite бази даних. create_table(conn): Створює таблицю для зберігання обмінних курсів.

# insert_exchange_rate(conn, currency_name, currency_value): Вставляє новий запис з обмінним курсом у таблицю.

# fetch_exchange_rates(): Виконує HTTP запит до API Monobank і отримує дані у форматі JSON. main():

# Основна функція, яка отримує дані з API та зберігає їх у базу даних. Зауваження: API Monobank: В даному прикладі ми використовуємо URL для отримання
# обмінних курсів.Можливо, вам знадобиться перевірити

# актуальність URL і структуру відповіді у документації API Monobank. Обробка помилок: Ми обробляємо можливі помилки при запиті до API.
# Збереження даних: Ми використовуємо datetime.now() для збереження дати і часу запиту.
