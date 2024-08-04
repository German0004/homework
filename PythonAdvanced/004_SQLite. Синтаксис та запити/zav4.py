# Створіть агрегатні функції для підрахунку загальної кількості  витрат i прибуткiв за місяць. Забезпечте
# відповідний інтерфейс користувача.


import sqlite3
from datetime import datetime

# Підключаємося до бази даних (створюємо її, якщо не існує)
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()


# Функція для отримання загальної суми за типом транзакцій (витрати або прибутки) за місяць
def get_monthly_total(conn, transaction_type, year, month):
    cursor = conn.cursor()
    query = '''
        SELECT SUM(amount) FROM transactions
        WHERE type = ? AND strftime('%Y', timestamp) = ? AND strftime('%m', timestamp) = ?
    '''
    cursor.execute(query, (transaction_type, str(year), f'{month:02}'))
    result = cursor.fetchone()[0]
    return result if result is not None else 0.0


# Інтерфейс для користувача
def main():
    database = "expenses.db"

    # Підключаємося до бази даних
    conn = sqlite3.connect(database)

    while True:
        print("\n=== Transaction Management CLI ===")
        print("1. Add a new transaction")
        print("2. View total expenses for a month")
        print("3. View total income for a month")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            purpose = input("Enter purpose: ")
            amount = float(input("Enter amount: "))
            transaction_type = input("Enter type (expense/income): ").lower()

            if transaction_type not in ['expense', 'income']:
                print("Invalid type. Please enter 'expense' or 'income'.")
                continue

            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO transactions (purpose, amount, type)
                VALUES (?, ?, ?)
            ''', (purpose, amount, transaction_type))
            conn.commit()
            print(f"Transaction '{purpose}' added successfully")

        elif choice == '2':
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (MM): "))
            total_expenses = get_monthly_total(conn, 'expense', year, month)
            print(f"Total expenses for {year}-{month:02}: {total_expenses}")

        elif choice == '3':
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (MM): "))
            total_income = get_monthly_total(conn, 'income', year, month)
            print(f"Total income for {year}-{month:02}: {total_income}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    conn.close()


if __name__ == "__main__":
    main()

# Пояснення:
# Функція get_monthly_total: Ця функція обчислює загальну суму витрат або прибутків за конкретний місяць, використовуючи
# SQL-запит із функцією SUM. Вона приймає тип транзакції (expense або income), рік і місяць як аргументи.
#
# Користувацький інтерфейс:
#
# Опція 1: Додає нову транзакцію (витрати або прибутки).
# Опція 2: Показує загальну суму витрат за вказаний місяць і рік.
# Опція 3: Показує загальну суму прибутків за вказаний місяць і рік.
# Опція 4: Вихід з програми.
# Використання: Ви можете додавати транзакції та переглядати загальні суми витрат і прибутків за конкретний місяць.