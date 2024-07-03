x = int(input('x = '))

if 0 < x < 7:
    print('Значення x входить у заданий діапазон, продовжуємо')
    y = 2 * x - 5

    if y < 0:
        print('Значення y негативне')
    else:
        if y > 0:
            print('Значення y позитивне')
        else:
            print('y = 0')
