a, b, c = 1, 2, 3
print(a, b, c)
# міняємо місцями значення двох змінних:
a, b = b, a
print(a, b)
my_tuple = 10, 50, 90
a, b, c = my_tuple
print(a, b, c)

head, *tail = my_tuple
print(head)

print(tail)
print(*tail)

for index, value in enumerate(my_tuple):
    print(index + 1, value)
