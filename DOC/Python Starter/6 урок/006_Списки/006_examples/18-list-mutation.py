# Створення списку чисел
my_list = [5, 1, 5, 7, 8, 1, 0, -23]

# Виведення списку
print(my_list)

# Отримання довжини списку
length = len(my_list)

# Введення індексу
index = length
while not -length <= index < length:
    index = int(input('Введіть індекс списку (від %d до %d): '
                      % (-length, length - 1)))

# Введення нового значення
value = int(input('Введіть нове значення заданого елемента: '))

# Зміна елемента списку
my_list[index] = value

# Виведення списку на екран
print(my_list)
