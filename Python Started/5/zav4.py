# Ознайомтеся за допомогою документації з класами namedtuple та deque модуля collections. Створіть фабрику іменованих
# кортежів оцінок для учнів однієї групи з предметів: алгебра, геометрія, історія, інформатика, географія. Вивести дані на екран.


from collections import namedtuple

# Створення іменованого кортежу для оцінок
Grade = namedtuple(
    "Grade", ["алгебра", "геометрія", "історія", "інформатика", "географія"]
)


# Створення фабрики оцінок для учнів
def create_student_grades(algebra, geometry, history, computer_science, geography):
    return Grade(
        алгебра=algebra,
        геометрія=geometry,
        історія=history,
        інформатика=computer_science,
        географія=geography,
    )


# Оцінки для різних учнів
student1 = create_student_grades(90, 85, 95, 88, 92)
student2 = create_student_grades(88, 92, 87, 90, 91)
student3 = create_student_grades(95, 90, 91, 85, 89)

# Виведення даних на екран
print("Оцінки учня 1:", student1)
print("Оцінки учня 2:", student2)
print("Оцінки учня 3:", student3)
