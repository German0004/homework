# Напишіть програму-калькулятор, в якій користувач зможе обрати операцію, ввести необхідні числа
# та отримати результат. Операції, які необхідно реалізувати: додавання, віднімання, множення, ділення,
# зведення в ступінь, квадратний корінь, кубічний корінь, синус, косинус та тангенс числа.

import math


s = float(input("""Оберіть арифметичну операцію: \n1 додавання \n2 віднімання \n3 множення \n4 ділення \n5 зведення
в ступінь(k ** n) \n6 квадратний корінь(тільки першого числа)
 \n7 кубічний корінь(тільки першого числа)
  \n8 sin(тільки першого числа) 
  \n9 cos(тільки першого числа) \n10 tg(тільки першого числа) \n """))


k = float(input("Веедіть перше число: "))
n = float(input("Веедіть друге число: "))

if s == 1:
    d = k + n

if s == 2:
    d = k - n

if s == 3:
    d = k * n

if s == 4:
    d = k / n

if s == 5:
    d = k ** n
if s == 6:
    d = math.sqrt(k)


print("Результат чисел = ", d)

