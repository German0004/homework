#Створіть функцію-генератор чисел Фібоначчі. Застосуйте до неї декоратор, який залишатиме в послідовності
# лише парні числа.


# Декоратор для відфільтровування парних чисел в генераторі Фібоначчі
def filter_even_numbers(generator_func):
    def wrapper():
        for num in generator_func():
            if num % 2 == 0:
                yield num
    return wrapper

# Генератор для послідовності Фібоначчі
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Застосування декоратора до генератора Фібоначчі
fibonacci_generator_filtered = filter_even_numbers(fibonacci_generator)

# Виведення перших 25 парних чисел Фібоначчі
count = 25
for i, num in enumerate(fibonacci_generator_filtered(), 1):
    print(num, end=" ")
    if i == count:
        break
print()

# У цій програмі:
#
# fibonacci_generator - це функція-генератор, яка створює послідовність чисел Фібоначчі.
# filter_even_numbers - це декоратор, який відфільтровує парні числа з результатів генератора.
# fibonacci_generator_filtered - це генератор, який отримується застосуванням декоратора filter_even_numbers до fibonacci_generator.
# В циклі for виводяться перші 25 парних чисел з послідовності Фібоначчі за допомогою отриманого фільтрованого генератора.