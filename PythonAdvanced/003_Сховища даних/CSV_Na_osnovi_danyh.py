# Створіть функцію, яка формує CSV-файл на основі даних, введених користувачем через консоль. Файл має містити
# такі стовпчики: імена, прізвища, дати народження та місто проживання. Реалізуйте можливості перезапису цього файлу, додавання
# нових рядків до наявного файлу, рядкового читання з файлу та конвертації всього вмісту у формати XML та JSON.


import csv
import json
import xml.etree.ElementTree as ET
import os

def get_user_input():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    city = input("Enter city of residence: ")
    return [name, surname, dob, city]

def write_csv(file_path, data, mode='w'):
    with open(file_path, mode, newline='') as csvfile:
        writer = csv.writer(csvfile)
        if mode == 'w':
            writer.writerow(["Name", "Surname", "Date of Birth", "City of Residence"])
        writer.writerow(data)

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def csv_to_json(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return json.dumps(data, indent=4)

def csv_to_xml(file_path):
    root = ET.Element("People")
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            person = ET.SubElement(root, "Person")
            for key, value in row.items():
                child = ET.SubElement(person, key.replace(" ", ""))
                child.text = value
    return ET.tostring(root, encoding='unicode', method='xml')

def main():
    file_path = 'data.csv'

    while True:
        print("\nMenu:")
        print("1. Create or overwrite CSV file")
        print("2. Add new row to CSV file")
        print("3. Read CSV file")
        print("4. Convert CSV to JSON")
        print("5. Convert CSV to XML")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = get_user_input()
            write_csv(file_path, data, mode='w')
        elif choice == '2':
            data = get_user_input()
            write_csv(file_path, data, mode='a')
        elif choice == '3':
            if os.path.exists(file_path):
                read_csv(file_path)
            else:
                print("File does not exist.")
        elif choice == '4':
            if os.path.exists(file_path):
                json_data = csv_to_json(file_path)
                print(json_data)
            else:
                print("File does not exist.")
        elif choice == '5':
            if os.path.exists(file_path):
                xml_data = csv_to_xml(file_path)
                print(xml_data)
            else:
                print("File does not exist.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# Пояснення коду

# get_user_input: Функція, яка запитує у користувача дані через консоль.

# write_csv: Функція для запису даних у CSV-файл. Вона може працювати в режимі перезапису (mode='w') або додавання
# нових рядків (mode='a').

# read_csv: Функція для рядкового читання CSV-файлу і виведення вмісту на консоль.

# csv_to_json: Функція для конвертації CSV-файлу у формат JSON.

# csv_to_xml: Функція для конвертації CSV-файлу у формат XML.

# main: Головна функція, яка надає меню для вибору дій користувача та викликає відповідні функції.

# Цей код забезпечує основні операції з CSV-файлом та дозволяє користувачу працювати з даними, використовуючи
# консольний інтерфейс.
