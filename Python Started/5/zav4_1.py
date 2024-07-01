# Ознайомтеся за допомогою документації з класами namedtuple та deque модуля collections. Створіть фабрику іменованих
# кортежів оцінок для учнів однієї групи з предметів: алгебра, геометрія, історія, інформатика, географія. Вивести дані на екран.

from collections import deque

# Створення deque
grades_queue = deque([student1, student2, student3])

# Виведення даних на екран
print("Оцінки учнів у черзі:")
for idx, student_grades in enumerate(grades_queue, start=1):
    print(f"Учень {idx}: {student_grades}")
