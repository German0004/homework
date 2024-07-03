"""
*** Кортеж не змінюється, і можна подумати, що це відбуватиметься абсолютно завжди.
Але це не завжди так. У разі наявності об'єктів, що змінюються всередині кортежу, ці самі об'єкти можна модифікувати.
Фактично довжина кортежу не змінилася, але внутрішні елементи могли зазнати зовнішнього впливу
"""

my_tuple = ([1, 2], 3, 4)
print('Length:', len(my_tuple))
print(my_tuple)
my_tuple[0].append(15)
print('Length:', len(my_tuple))
print(my_tuple)
my_tuple[0].extend([21, 14, 16, 17, 10])
print('Length:', len(my_tuple))
print(my_tuple)
my_tuple[0].extend('add')
print('Length:', len(my_tuple))
print(my_tuple)

print(len(my_tuple[0]))
