print('''\nМеню:\n\t1. Файл\n\t2. Вид\n\t3. Вихід\n''')

choice = int(input('Ваш вибір: '))

if choice == 1:
    print('Ви вибрали пункт меню "Файл"')
elif choice == 2:
    print('Ви відкрили меню "Вигляд"')
elif choice == 3:
    print('Завершення...')
else:
    print('Некоректний вибір')
