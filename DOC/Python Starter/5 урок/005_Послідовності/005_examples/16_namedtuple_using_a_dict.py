from collections import namedtuple

# Створення namedtuple за допомогою словника
# Стартове значення словника – 0, оскільки значення поля ігнорується кортежем.
dct = {'Physics': 0, 'Geography': 0, 'Math': 0, 'English': 0}
Marks = namedtuple('Marks', dct)
marks = Marks(90, 85, 95, 100)
print(marks)

# Функція _make також приймає об'єкт, що ітерується (у випадку зі словником — значення).
marks = Marks._make({55: 'Physics', 78: 'Geography', 98: 'Math', 90: 'English'})
print(marks)
