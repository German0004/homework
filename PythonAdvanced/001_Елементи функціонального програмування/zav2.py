# Напишіть декоратор, який буде заміряти час виконання для наданої функції.


import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Початок заміру часу
        result = func(*args, **kwargs)
        end_time = time.time()  # Кінець заміру часу
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to execute")
        return result
    return wrapper


@timing_decorator
def example_function():
    time.sleep(2)  # Імітація тривалої роботи функції
    print("Function is done")

example_function()
# У цьому прикладі:

# timing_decorator: Це сам декоратор, який приймає функцію func як аргумент.
# wrapper: Внутрішня функція, яка обгортує оригінальну функцію func.
# start_time і end_time: Використовуються для заміру часу до і після виконання функції.
# elapsed_time: Обчислює тривалість виконання функції.
# print: Виводить ім'я функції та час її виконання.
# При застосуванні цього декоратора до функції example_function, він заміряє і виводить час виконання цієї функції.