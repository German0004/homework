from collections import namedtuple

# Створення іменованого кортежу
Marks = namedtuple('Marks', 'Physics Geography Math English')
marks = Marks(90, 85, 95, 100)
# Виведення на екран
print(marks)

'''Зміна значення поля namedtuple
Незважаючи на незмінність, є спосіб, за допомогою якого можна змінювати значення поля. Для цього використовується
функція _replace.
'''
# Використання функції _replace(), яка повертає іменований кортеж із зміненим значенням
marks = marks._replace(Physics=99, Math=99)
print(marks)
# Marks(Physics=99, Geography=78, Math=98, English=90)
