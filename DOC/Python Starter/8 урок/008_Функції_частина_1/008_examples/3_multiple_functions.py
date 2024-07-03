# Функція з минулого прикладу
def print_numbers(limit):
    for i in range(limit):
        print(i)


# Будь-яку логічно завершену дію слід розміщувати у функцію
def main():
    n = int(input("Введіть n: "))
    print_numbers(n)


# Виклик головної функції
main()
