from collections import namedtuple

# Створення namedtuple за допомогою множини
subject_set = {'Physics', 'Chemistry', 'Math', 'English'}
Marks = namedtuple('Marks', subject_set)
marks = Marks(90, 85, 95, 100)
print(marks)
