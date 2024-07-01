# Створіть програму, яка має 2 списки цілочисельних значень та друкує список унікальних значень без повтору, які є в
# 1 списку (немає в другому) і навпаки.


int_num = [1, 3, 5, 6, 7, 8, 10]
int_num1 = [12, 2, 4, 7, 9, 10, 11]
print(int_num)
print(int_num1)

unique_num_first = [item for item in int_num if item not in int_num1]
print(f"\nNewlist: {sorted(unique_num_first)}")

unique_num1_first = [item for item in int_num1 if item not in int_num]
print(f"\nNewlist1: {sorted(unique_num1_first)}")
