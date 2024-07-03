# Введення рядка
string = input('Введіть рядок: ')

# Перевірка, чи є в цьому рядку символ q
if 'q' in string:
    print('У цьому рядку є символ "q"')
else:
    print('У цьому рядку немає символу "q"')
    string += 'q'
print(string)
