# Написати функцію, яка за допомогою регулярних виразів з файлу витягує дані про дату народження, телефон та електронну адресу.
# Дані потрібно записати до іншого файлу.


import re

def extract_data(input_file, output_file):
    # Відкриття вхідного файлу для читання
    with open(input_file, 'r', encoding='utf-8') as file:
        input_data = file.read()

    # Регулярні вирази для пошуку дати народження, телефону та електронної адреси
    dob_pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'  # формат дати: dd.mm.yyyy
    phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'  # формат телефону: 123-456-7890
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # формат електронної адреси

    # Пошук в тексті за допомогою регулярних виразів
    dates_of_birth = re.findall(dob_pattern, input_data)
    phones = re.findall(phone_pattern, input_data)
    emails = re.findall(email_pattern, input_data)

    # Запис даних до вихідного файлу
    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write("Dates of Birth:\n")
        for dob in dates_of_birth:
            out_file.write(dob + "\n")
        out_file.write("\nPhone Numbers:\n")
        for phone in phones:
            out_file.write(phone + "\n")
        out_file.write("\nEmail Addresses:\n")
        for email in emails:
            out_file.write(email + "\n")

# Приклад використання функції:
input_file = 'input.txt'  # замініть шлях до свого вхідного файлу
output_file = 'output.txt'  # шлях до файлу, куди будуть записані витягнуті дані

extract_data(input_file, output_file)


# У цьому прикладі:

# input_file - це шлях до вашого вхідного файлу, з якого ви хочете витягнути дані.
# output_file - це шлях до файлу, в який будуть записані знайдені дати народження,
# телефонні номери та електронні адреси.
# Переконайтеся, що ваш вхідний файл (input.txt) містить відповідний текст, що містить дати народження,
# телефонні номери та електронні адреси у вказаних форматах.