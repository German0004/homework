from collections import namedtuple

# оголошення ФАБРИКИ іменованих кортежів - іменованого кортежу, що може використовуватися для створення
# нескінченної кількості аналогічних структур
Marks = namedtuple('Marks', 'Physics Geography Math English')
# цей рядок створює іменований кортеж
marks1 = Marks(90, 85, 95, 100)
print("У Івана наступний табель:", marks1)

marks2 = Marks(30, 55, 75, 80)
print("У Дарії наступний табель:", marks2)
