# Проста умова
number = int(input("Input your digit: "))
if number >= 0:
    print(number)
else:
    print(-number)
# Тернарний оператор
print(number if number >= 0 else -number)

result = 5 if 4 > 3 else 0  # ternary operator; equals to 5
print(result)
result2 = 5 if 3 > 4 else 0  # ternary operator; equals to 0
print(result2)
