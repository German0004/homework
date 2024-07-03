from collections import namedtuple

Marks = namedtuple('Marks', 'Physics Geography Math English')
# Створення іменованого кортежу
marks = Marks(90, 85, 95, 100)
print(marks)

# Доступ до імен полів namedtuple в python можна отримати тим же способом, що і в кортежах - за допомогою індексу:

print(marks[0])
print(marks[3])

# Також можна використовувати назви полів за аналогією з атрибутами екземпляра класу:
print(marks.Physics)
print(marks.English)

# Поля можна отримати за допомогою функції getattr():
print('Отримання поля за допомогою функції getattr():', getattr(marks, 'English'))
print(marks[-1])
