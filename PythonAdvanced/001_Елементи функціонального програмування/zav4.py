# За допомогою написаного Вами декоратору заміряйте та порівняйте швидкість роботи цих 4х варіантів.


import time
import functools

# Декоратор для кешування результатів обчислення функції
def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

# Функція без кешування
def fibonacci_without_cache(n):
    if n <= 1:
        return n
    return fibonacci_without_cache(n-1) + fibonacci_without_cache(n-2)

# Функція з кешем довільної довжини
@functools.lru_cache(None)
def fibonacci_with_arbitrary_cache(n):
    if n <= 1:
        return n
    return fibonacci_with_arbitrary_cache(n-1) + fibonacci_with_arbitrary_cache(n-2)

# Функція з кешем з максимальною кількістю 10 елементів
@functools.lru_cache(maxsize=10)
def fibonacci_with_cache_size_10(n):
    if n <= 1:
        return n
    return fibonacci_with_cache_size_10(n-1) + fibonacci_with_cache_size_10(n-2)

# Функція з кешем з максимальною кількістю 16 елементів
@functools.lru_cache(maxsize=16)
def fibonacci_with_cache_size_16(n):
    if n <= 1:
        return n
    return fibonacci_with_cache_size_16(n-1) + fibonacci_with_cache_size_16(n-2)

# Декоратор для вимірювання часу виконання функції
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Початок заміру часу
        result = func(*args, **kwargs)
        end_time = time.time()  # Кінець заміру часу
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to execute")
        return result
    return wrapper

# Застосування декоратора для вимірювання часу до кожної функції
fibonacci_without_cache_timed = timing_decorator(fibonacci_without_cache)
fibonacci_with_arbitrary_cache_timed = timing_decorator(fibonacci_with_arbitrary_cache)
fibonacci_with_cache_size_10_timed = timing_decorator(fibonacci_with_cache_size_10)
fibonacci_with_cache_size_16_timed = timing_decorator(fibonacci_with_cache_size_16)

# Вимірювання часу виконання кожної функції і виведення результатів
print("Без кешування:")
fibonacci_without_cache_timed(25)

print("\nЗ кешем довільної довжини:")
fibonacci_with_arbitrary_cache_timed(25)

print("\nЗ кешем з максимальною кількістю 10 елементів:")
fibonacci_with_cache_size_10_timed(10)

print("\nЗ кешем з максимальною кількістю 16 елементів:")
fibonacci_with_cache_size_16_timed(16)
