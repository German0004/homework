# Напишіть програму яка буде виводити 25 перших чисел Фібоначі, використовуючи для цього три наведені в тексті заняття
# функції — без кешу, з кешем довільної довжини, з кешем з модулю functools з максимальною кількістю 10 елементів та з
# кешем з модулю functools з максимальною кількістю 16 елементів.


# Щоб реалізувати програму, яка обчислює і виводить перші 25 чисел Фібоначчі з використанням трьох різних методів
# кешування, можна написати наступний код:
#
# Без кешу
# З кешем довільної довжини (використовуючи словник)
# З кешем з модуля functools з максимальною кількістю 10 елементів
# З кешем з модуля functools з максимальною кількістю 16 елементів
# Ось приклад такої програми:

import functools

# 1. Функція без кешу
def fibonacci_no_cache(n):
    if n <= 1:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

# 2. Функція з кешем довільної довжини (використовуючи словник)
cache_dict = {}
def fibonacci_with_custom_cache(n):
    if n in cache_dict:
        return cache_dict[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci_with_custom_cache(n - 1) + fibonacci_with_custom_cache(n - 2)
    cache_dict[n] = result
    return result

# 3. Функція з кешем з модуля functools з максимальною кількістю 10 елементів
@functools.lru_cache(maxsize=10)
def fibonacci_with_lru_cache_10(n):
    if n <= 1:
        return n
    return fibonacci_with_lru_cache_10(n - 1) + fibonacci_with_lru_cache_10(n - 2)

# 4. Функція з кешем з модуля functools з максимальною кількістю 16 елементів
@functools.lru_cache(maxsize=16)
def fibonacci_with_lru_cache_16(n):
    if n <= 1:
        return n
    return fibonacci_with_lru_cache_16(n - 1) + fibonacci_with_lru_cache_16(n - 2)

# Виведення перших 25 чисел Фібоначчі для кожного методу
print("Без кешу:")
for i in range(25):
    print(fibonacci_no_cache(i), end=" ")
print("\n")

print("З кешем довільної довжини:")
for i in range(25):
    print(fibonacci_with_custom_cache(i), end=" ")
print("\n")

print("З кешем з functools (maxsize=10):")
for i in range(25):
    print(fibonacci_with_lru_cache_10(i), end=" ")
print("\n")

print("З кешем з functools (maxsize=16):")
for i in range(25):
    print(fibonacci_with_lru_cache_16(i), end=" ")
print("\n")

# Пояснення коду:
# Функція без кешу: fibonacci_no_cache(n) - проста рекурсивна функція для обчислення чисел Фібоначчі без використання кешу.
# Функція з кешем довільної довжини: fibonacci_with_custom_cache(n) - використовує словник cache_dict для зберігання вже обчислених значень чисел Фібоначчі.
# Функція з кешем з модуля functools з максимальною кількістю 10 елементів: fibonacci_with_lru_cache_10(n) - використовує декоратор functools.lru_cache(maxsize=10) для кешування останніх 10 значень.
# Функція з кешем з модуля functools з максимальною кількістю 16 елементів: fibonacci_with_lru_cache_16(n) - використовує декоратор functools.lru_cache(maxsize=16) для кешування останніх 16 значень.
# Програма виводить перші 25 чисел Фібоначчі для кожного з цих методів.