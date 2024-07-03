string = input('Enter a string: ')
# Те ж саме, що if string is not None and string != ''

if string:
    print('The string is {}'.format(string))

number = int(input('Enter a number: '))

if number:
    print('Число не дорівнює нулю')
# Якщо ввести 0:
else:
    print('Число дорівнює нулю')
