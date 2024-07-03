from collections import namedtuple

# Створення namedtuple за допомогою кортежу
my_tuple = ('Physics', 'Geography', 'Math', 'English')
Marks = namedtuple('Marks', my_tuple)
marks = Marks(90, 85, 95, 100)
print(marks)
