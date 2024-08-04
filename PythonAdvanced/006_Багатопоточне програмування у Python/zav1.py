# Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань, використовуючи Thread,
# і заміряйте швидкість їхнього виконання, а потім заміряйте швидкість обчислення, використовуючи той же
# набір завдань на ThreadPoolExecutor. Як приклади використовуйте останні значення, від мінімальних і до
# максимально можливих, щоб побачити приріст або втрату продуктивності.

import threading
import time
from concurrent.futures import ThreadPoolExecutor


def factorial(n):
    """Обчислює факторіал числа."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def calculate_factorial_with_threads(numbers):
    """Обчислює факторіали чисел у окремих потоках."""
    threads = []
    results = []
    for num in numbers:
        thread = threading.Thread(target=factorial, args=(num,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
        results.append(thread.result)
    return results


def calculate_factorial_with_executor(numbers):
    """Обчислює факторіали чисел за допомогою ThreadPoolExecutor."""
    with ThreadPoolExecutor() as executor:
        results = executor.map(factorial, numbers)
    return list(results)


if __name__ == "__main__":
    # Діапазон чисел для обчислення факторіалу
    numbers = list(range(1, 21))

    # Замір часу для обчислення з використанням потоків
    start_time = time.time()
    results_threads = calculate_factorial_with_threads(numbers)
    end_time = time.time()
    print(f"Час виконання з використанням потоків: {end_time - start_time} секунд")

    # Замір часу для обчислення з використанням ThreadPoolExecutor
    start_time = time.time()
    results_executor = calculate_factorial_with_executor(numbers)
    end_time = time.time()
    print(
        f"Час виконання з використанням ThreadPoolExecutor: {end_time - start_time} секунд"
    )

    # Перевірка результатів (необов'язково)
    assert results_threads == results_executor

# Пояснення коду:

# Функція factorial: Рекурсивна функція для обчислення факторіалу.
# Функція calculate_factorial_with_threads: Створює окремий потік для кожного числа і запускає обчислення паралельно.
# Функція calculate_factorial_with_executor: Використовує ThreadPoolExecutor для автоматичного управління пулом потоків.
# Основний блок: Визначає список чисел, запускає обчислення обома методами і вимірює час виконання.
# Аналіз результатів

# Вплив GIL: В Python існує Global Interpreter Lock (GIL), який обмежує паралельність виконання чистого Python коду
# в одному процесі. Це означає, що навіть якщо ми створюємо багато потоків, лише один з них зможе виконувати байт-код
# Python одночасно.
# Виграш від ThreadPoolExecutor: Незважаючи на GIL, ThreadPoolExecutor може бути ефективнішим, оскільки він краще
# управляє ресурсами і може делегувати деякі операції в CPython, обходячи GIL.
# Вплив введення-виводу: Якщо обчислення включають введення-вивід, багатопоточність може дати значний приріст
# продуктивності, оскільки потоки можуть блокуватися на операціях вводу-виводу, звільняючи інші потоки для
# виконання обчислень.

# Додаткові міркування

# Вибір діапазону чисел: Для більших чисел різниця у часі виконання може бути більш помітною.
# Складність обчислень: Якщо обчислення більш складні, ніж обчислення факторіалу, ефективність багатопоточності
# може бути вищою.
# Навантаження на процесор: Кількість доступних ядер процесора обмежує максимальну кількість потоків, які можуть
# виконуватися одночасно.
# Використання інших бібліотек: Існують інші бібліотеки, такі як multiprocessing, які дозволяють обходити GIL і
# досягти більшої паралельності.
