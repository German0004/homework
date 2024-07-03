from collections import namedtuple

# Створення namedtuple за допомогою списку
lst = ['Physics', 'Geography', 'Math', 'English']
Marks = namedtuple('Marks', lst)
marks = Marks(90, 85, 95, 100)
print(marks)
