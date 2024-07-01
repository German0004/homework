# З клавіатури вводиться рядок, в якому є інформація про прізвище, ім'я, дату народження, електронну адресу та відгук
# про курси учня.
# Написати функцію, яка, використовуючи регулярні вирази, витягне дані з рядка і поверне словник.


import re

def extract_student_info(input_string):
    # Регулярні вирази для витягування даних
    name_pattern = r'Прізвище:\s*(\w+),\s*Ім\'я:\s*(\w+)'  # шаблон для прізвища і імені
    dob_pattern = r'Дата народження:\s*(\d{2}\.\d{2}\.\d{4})'  # шаблон для дати народження (формат: dd.mm.yyyy)
    email_pattern = r'Електронна адреса:\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'  # шаблон для електронної адреси
    review_pattern = r'Відгук про курси:\s*(.*)'  # шаблон для відгуку про курси учня

    # Пошук за допомогою регулярних виразів
    name_match = re.search(name_pattern, input_string)
    dob_match = re.search(dob_pattern, input_string)
    email_match = re.search(email_pattern, input_string)
    review_match = re.search(review_pattern, input_string)

    # Створення словника з витягнутими даними
    student_info = {}
    if name_match:
        student_info['Прізвище'] = name_match.group(1)
        student_info['Ім\'я'] = name_match.group(2)
    if dob_match:
        student_info['Дата народження'] = dob_match.group(1)
    if email_match:
        student_info['Електронна адреса'] = email_match.group(1)
    if review_match:
        student_info['Відгук про курси'] = review_match.group(1)

    return student_info

# Приклад використання:
input_string = """
Прізвище: Іванов, Ім'я: Петро
Дата народження: 15.05.2000
Електронна адреса: petro.ivanov@example.com
Відгук про курси: Курси були цікаві і корисні, дуже задоволений результатом.
"""
student_info = extract_student_info(input_string)
print(student_info)

# У цій функції:

# Використовуються регулярні вирази для пошуку інформації про прізвище, ім'я, дату народження, електронну адресу та відгук про курси.
# Кожний шаблон розбиває рядок із введеної інформації на відповідні частини і додає ці частини до словника student_info.
# На виході функція повертає словник із зібраною інформацією про студента.