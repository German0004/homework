my_list = [15, 0, 12, -1, 4]

# Сортування за зростанням
my_list.sort()
print('Сортування за зростанням:', my_list)
print(my_list)

# None - тому що метод сортує за зростанням вихідний список, не створюючи новий
print('Сортування за зростанням:', my_list.sort())

my_list2 = sorted(my_list)
print('Сортування за зростанням:', my_list2, '\n')


my_list3 = [15, 0, 12, -1, 4]
# Сортування за cпаданням
my_list3.sort(reverse=True)
print('Сортування за спаданням:', my_list3)

my_list4 = [15, 0, 12, -1, 4]
my_list5 = sorted(my_list4, reverse=True)
print('Сортування за спаданням:', my_list5, '\n')

# Оберненути список спочатку в кінець:
my_list6 = [15, 0, 12, -1, 4]
my_list7 = my_list6.copy()
print('Обернений список спочатку в кінець:', my_list6[::-1])
# Або так:
my_list7.reverse()
print('Обернений список спочатку в кінець:', my_list7, '\n')


my_list8 = [15, 0, 12, -1, 4]
# None - тому що метод сортує за спаданням вихідний список, не створюючи новий
print('Обернений список спочатку в кінець:', my_list8.reverse())
print('Обернений список спочатку в кінець:', my_list8)
my_list9 = [15, 0, 12, -1, 4]
my_list10 = list(reversed(my_list9))
print('Обернений список спочатку в кінець:', my_list10)
