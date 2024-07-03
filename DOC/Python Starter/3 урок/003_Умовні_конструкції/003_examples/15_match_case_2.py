data = input('Введіть у рядок ім\'я, вік, зріст у см, вагу у кг та хоббі, через пробіл: ').split()

if len(data) == 5:
    print(f'Я - {data[0]}, мені - {data[1]}, мій зріст - {data[2]} см, моя вага - {data[3]} кг. Моє хоббі - {data[4]}.')
elif len(data) == 4:
    print(f'Я - {data[0]}, мені - {data[1]}, мій зріст - {data[2]} см, моя вага - {data[3]} кг.')
elif len(data) == 3:
    print(f'Я - {data[0]}, мені - {data[1]}, мій зріст - {data[2]} см.')
elif len(data) == 2:
    print(f'Я - {data[0]}, мені - {data[1]}.')
else:
    print('Некоректні дані')

print()

# Конструкція match/case(працює швидше за конструкцію з використанням if):
match data:
    case name, age, height, weight, hobby:
        print(f'Я - {name}, мені - {age}, мій зріст - {height} см, моя вага - {weight} кг. Моє хоббі - {hobby}.')
    case name, age, height, weight:
        print(f'Я - {name}, мені - {age}, мій зріст - {height} см, моя вага - {weight} кг.')
    case name, age, height:
        print(f'Я - {name}, мені - {age}, мій зріст - {height} см.')
    case name, age:
        print(f'Я - {name}, мені - {age}.')
    case _:
        print('Некоректні дані')
