# Створіть програму, яка перевіряє, чи є паліндромом введена фраза.


def is_palindrome(phrase):
    # Видалення пробілів і перетворення до нижнього регістру
    cleaned_phrase = "".join(char.lower() for char in phrase if char.isalnum())
    # Перевірка, чи є фраза паліндромом
    return cleaned_phrase == cleaned_phrase[::-1]


# Отримання введеної фрази від користувача
input_phrase = input("Введіть фразу: ")

# Перевірка, чи є фраза паліндромом
if is_palindrome(input_phrase):
    print("Фраза є паліндромом.")
else:
    print("Фраза не є паліндромом.")


# Пояснення коду:
#
# Функція is_palindrome(phrase):
#
# Видаляє всі пробіли, розділові знаки та інші непотрібні символи, залишаючи лише літери та цифри. Для цього використовуємо
# генератор списку, який перевіряє, чи є кожен символ буквено-цифровим (char.isalnum()) та перетворює його до нижнього
# регістру (char.lower()).
# Перевіряє, чи є очищена фраза рівною своєму зворотному вигляду (cleaned_phrase == cleaned_phrase[::-1]). Якщо так, то
# фраза є паліндромом.
# Отримання введеної фрази:
#
# Використовуємо функцію input() для отримання фрази від користувача.
# Перевірка фрази на паліндром:
#
# Викликаємо функцію is_palindrome(input_phrase) та виводимо відповідне повідомлення залежно від результату.
# Програма працює для будь-якої введеної фрази та коректно визначає, чи є вона паліндромом, ігноруючи пробіли, розділові
# знаки та регістр символів.
