a = 2
b = 5

# менше
print(a < b)
# більше
print(b > 3)
# менше або дорівнює
print(a <= 2)
# більше або дорівнює
print(b >= 7)
# подвійне порівняння
print(a < 3 < b)
# рівність
print(a == b)
# нерівність
print(a != b)
# ідентичність об'єктів у пам'яті
print(a is b)
# a та b – різні об'єкти (хоча їх значення можуть бути рівними)
print(a is not b)

string = "some string"
second_string = string
third_string = input('Введіть рядок: ')

print(string is second_string)
print(string is third_string)
