# Створіть консольний інтерфейс (CLI) на Python для додавання нових записів до бази даних.

import sqlite3
import os


# Створюємо або підключаємося до бази даних
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database '{db_file}'")
    except sqlite3.Error as e:
        print(e)
    return conn


# Створюємо таблицю, якщо вона ще не існує
def create_table(conn):
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        );
        """
        conn.execute(sql_create_table)
        print("Table 'contacts' created successfully")
    except sqlite3.Error as e:
        print(e)


# Додаємо новий запис до таблиці
def add_contact(conn, name, phone, email):
    try:
        sql_insert = """
        INSERT INTO contacts (name, phone, email)
        VALUES (?, ?, ?)
        """
        conn.execute(sql_insert, (name, phone, email))
        conn.commit()
        print(f"Contact '{name}' added successfully")
    except sqlite3.Error as e:
        print(e)


# Основна функція CLI
def main():
    database = "contacts.db"

    # Підключаємося до бази даних
    conn = create_connection(database)

    if conn is not None:
        # Створюємо таблицю
        create_table(conn)

        while True:
            print("\n=== Contact Management CLI ===")
            print("1. Add a new contact")
            print("2. Exit")

            choice = input("Enter your choice (1 or 2): ")

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email (optional): ")

                add_contact(conn, name, phone, email)

            elif choice == '2':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

        conn.close()
    else:
        print("Error! Cannot connect to the database.")


if __name__ == "__main__":
    main()
