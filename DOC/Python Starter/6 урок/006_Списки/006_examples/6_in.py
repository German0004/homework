# Для перевірки входження елемента до списку використовується операція in

# Створення списку
my_list = [5, 7, 9, 1, 10, 2]

# Введення значення
value = int(input('Введіть число: '))

# Перевірка, чи є дане число у списку
if value in my_list:
    print('Число входить до списку')
else:
    print('Число не входить до списку')
    my_list.append(value)
print(my_list)

for element in my_list:
    element *= 2
    print(element)

my_list = [1, 2, 3, 4, 5, 6]
even_list = []
for list_element in my_list:
    if list_element % 2 == 0:
        even_list.append(list_element)
print(even_list)
print(my_list)
