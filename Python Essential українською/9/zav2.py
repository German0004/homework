# Повторіть інформацію про розглянуті на уроці стандартні модулі. Ознайомтеся також із модулями calendar, heapq, bisect, array, enum.

# Стандартні модулі Python:
# os:

# Дозволяє взаємодіяти з операційною системою, виконувати системні команди, працювати з файловою системою.
# Приклади використання: os.listdir(), os.path.exists(), os.mkdir()
# sys:

# Надає доступ до змінних і функцій, що взаємодіють з інтерпретатором Python.
# Приклади використання: sys.argv, sys.exit(), sys.path
# math:

# Містить математичні функції, такі як тригонометричні, логарифмічні, показникові.
# Приклади використання: math.sqrt(), math.sin(), math.log()
# random:

# Забезпечує функціонал для генерації випадкових чисел.
# Приклади використання: random.randint(), random.choice(), random.shuffle()
# datetime:

# Дозволяє працювати з датами і часом.
# Приклади використання: datetime.datetime.now(), datetime.timedelta, datetime.date
# json:

# Дозволяє працювати з JSON (JavaScript Object Notation) форматами.
# Приклади використання: json.load(), json.dump(), json.loads()
# Модулі для ознайомлення:
# calendar:
# Надає функції для роботи з календарями.
# Приклади використання: calendar.month(), calendar.isleap(), calendar.weekday()

# import calendar

# # Виводить календар на місяць
# print(calendar.month(2024, 7))
#
  #  Перевірка, чи є рік високосним
# print(calendar.isleap(2024))
# heapq:
# Надає алгоритми для роботи з чергами з пріоритетом (heap queue).
# Приклади використання: heapq.heappush(), heapq.heappop(), heapq.heapify()


# import heapq

  #  Створення черги з пріоритетом
# heap = []
# heapq.heappush(heap, (1, 'task 1'))
# heapq.heappush(heap, (3, 'task 3'))
# heapq.heappush(heap, (2, 'task 2'))

  #  Вилучення елемента з найвищим пріоритетом
# print(heapq.heappop(heap))
# bisect:
# Надає функції для роботи з відсортованими списками.
# Приклади використання: bisect.bisect(), bisect.insort()


# import bisect

  # Вставка елемента у відсортований список
# sorted_list = [1, 2, 4, 5]
# bisect.insort(sorted_list, 3)
# print(sorted_list)
# array:
# Надає масиви, що ефективніше використовують пам'ять, ніж списки.
# Приклади використання: array.array(), array.append(), array.pop()


# import array

  # Створення масиву цілих чисел
# arr = array.array('i', [1, 2, 3, 4])
# arr.append(5)
# print(arr)
# enum:
# Дозволяє створювати перерахування, які є набором символічних імен, пов'язаних з унікальними, постійними значеннями.
# Приклади використання: enum.Enum, enum.auto()


# from enum import Enum, auto

# class Color(Enum):
#     RED = auto()
#     GREEN = auto()
#     BLUE = auto()

  #  Доступ до елементів перерахування
# print(Color.RED)
# print(Color.RED.name)
# print(Color.RED.value)
# Ці модулі розширюють можливості Python, надаючи зручні інструменти для вирішення різних завдань, від роботи з календарями та масивами
# до алгоритмів сортування і черг з пріоритетом.