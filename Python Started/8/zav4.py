# Створіть програму, яка складається з функції, яка приймає три числа і повертає їх середнє арифметичне, і головного
# циклу, що запитує у користувача числа і обчислює їх середні значення за допомогою створеної функції.


def arithmetic_mean():
    a = int(input("Input a number: "))
    b = int(input("Input b number: "))
    c = int(input("Input c number: "))
    ari_func = (a + b + c) / 3
    print(f"Arithmetic mean = {ari_func}")


arithmetic_mean()
