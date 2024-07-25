# Попрацюйте зі створенням власних діалектів, довільно вибираючи правила для CSV-файлів. Зареєструйте створені
# діалекти та попрацюйте, використовуючи їх зі створенням/читанням файлом.


import csv

# Створення власного діалекту
csv.register_dialect(
   'my_dialect',
    delimiter=';',
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
    skipinitialspace=True
)

# Використання діалекту для запису CSV-файлу
data = [
    ["Name", "Age", "City"],
    ["John James", "18", "New York"],
    ["Jane Jones", "23", "Los Angeles"],
    ["Emily Stics", "22", "Chicago"]
]


with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='my_dialect')
    writer.writerows(data)


with open('data.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='my_dialect')
    for row in reader:
        print(row)

# Пояснення
# Створення діалекту:
#
# delimiter=';': Встановлює роздільник стовпців у CSV на ;.
# quotechar='"': Встановлює символ для обрамлення текстових даних на ".
# quoting=csv.QUOTE_MINIMAL: Встановлює мінімальне обрамлення текстових даних, тільки коли це необхідно.
# skipinitialspace=True: Пропускає початкові пробіли після роздільника.
# Запис у CSV-файл:
#
# Використовуємо метод csv.writer() з параметром dialect='my_dialect' для запису даних у файл з використанням
# створеного діалекту.
# Читання з CSV-файлу:
#
# Використовуємо метод csv.reader() з параметром dialect='my_dialect' для читання даних з файлу з використанням
# створеного діалекту. Цей код створює CSV-файл з даними, використовуючи власний діалект, а потім читає дані з
# цього файлу, використовуючи той самий діалект.
