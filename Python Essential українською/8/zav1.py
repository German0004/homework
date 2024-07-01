# Напишіть скрипт, який створює текстовий файл і записує до нього 10000 випадкових дійсних чисел. Створіть ще один скрипт,
# який читає числа з файлу та виводить на екран їхню суму.


# Скрипт для створення файлу з випадковими числами (generate_numbers.py):

import random

# Генеруємо 10000 випадкових дійсних чисел
random_numbers = [random.uniform(0, 1000) for _ in range(10000)]

# Записуємо їх у файл
with open("random_numbers.txt", "w") as file:
    for number in random_numbers:
        file.write(f"{number}\n")

print("Файл 'random_numbers.txt' збережено успішно.")
# Скрипт для обчислення суми чисел у файлі (calculate_sum.py):

# Читаємо числа з файлу і обчислюємо їхню суму
with open("random_numbers.txt", "r") as file:
    numbers = [float(line.strip()) for line in file.readlines()]

total_sum = sum(numbers)

print(f"Сума чисел у файлі 'random_numbers.txt': {total_sum}")

# Як це працює:

# Перший скрипт (generate_numbers.py) генерує 10000 випадкових дійсних чисел у діапазоні від 0 до 1000 і записує їх у
# файл random_numbers.txt.

# Другий скрипт (calculate_sum.py) відкриває цей файл, читає числа, обчислює їхню суму і виводить на екран.

# Переконайтеся, що обидва скрипти знаходяться в одній папці з тим же іменем файлу random_numbers.txt, щоб другий скрипт
# міг успішно прочитати дані з файлу.
