# Створіть список натуральних чисел int_list. Кожне непарне значення списку додайте до нового списку new_list.
# Користувач вводить з клавіатури кількість повторів списку repeat. Здійсніть дублювання списку new_list,
# repeat кількість разів. Очистіть список int_list.


int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for num in int_list:
    if num % 2:
        new_list.append(num)
repeat = [2, 3, 7, 5, 8]
new_list = new_list * 3
int_list1 = int_list.copy()
repeat1 = repeat.copy()

print(repeat * 3)
print(new_list)
print(int_list1 * 3)
print(repeat1 * 3)
int_list.clear()
print(int_list)
