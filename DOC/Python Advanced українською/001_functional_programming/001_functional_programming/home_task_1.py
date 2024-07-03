# Напишіть декоратор, який буде для переданої функції заміряти час виконання.
# Напишіть програму яка буде виводити 25 перших чисел Фібоначі, використовуючи
# для цього три наведені в тексті заняття функції - без кеша, з кешем довільної
# довжини, з кешем з модулю functools з максимальною кількістю 10 елементів.
# За допомогою написаного Вами декоратора заміряйте і порівняйте швидкість роботи
# ціх трьох варіантів.


import time
import functools

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.5f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def fib_no_cache(n):
    if n <= 1:
        return n
    else:
        return fib_no_cache(n-1) + fib_no_cache(n-2)

@timer_decorator
def fib_cache(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    else:
        result = fib_cache(n-1, cache) + fib_cache(n-2, cache)
        cache[n] = result
        return result

@functools.lru_cache(maxsize=10)
def fib_lru_cache(n):
    if n <= 1:
        return n
    else:
        return fib_lru_cache(n-1) + fib_lru_cache(n-2)

@timer_decorator
def fib_lru_cache_timed(n):
    return fib_lru_cache(n)

def print_fibonacci_sequence(fib_func, n):
    for i in range(n):
        print(fib_func(i), end=" ")
    print()

print("Fibonacci sequence without cache:")
print_fibonacci_sequence(fib_no_cache, 25)

print("\nFibonacci sequence with cache:")
print_fibonacci_sequence(fib_cache, 25)

print("\nFibonacci sequence with functools lru_cache:")
print_fibonacci_sequence(fib_lru_cache_timed, 25)