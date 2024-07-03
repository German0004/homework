"""
Повернення нового словника з відсортованими значеннями
Після сортування словника за значеннями, щоб зберегти відсортований словник у версіях Python до 3.7, ви повинні
використовувати OrderedDict - доступний у модулі collections. Ці об'єкти є словники, які зберігають порядок вставки.

Ось приклад сортування та використання OrderedDict:
"""
import operator
from collections import OrderedDict

dict1 = {1: 1, 5: 9, 3: 4}
sorted_tuples = sorted(dict1.items(), key=operator.itemgetter(1))
# [(1, 1), (3, 4), (2, 9)]
print(sorted_tuples)

sorted_dict = OrderedDict()
for k, v in sorted_tuples:
    sorted_dict[k] = v

# {1: 1, 3: 4, 5: 9}
print(dict(sorted_dict))
