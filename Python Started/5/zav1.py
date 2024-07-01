# Створіть програму, яка зчитує рядок, в якому знаходиться ПІБ користувача і перевіряє, чи складається рядок з літер,
# при чому кожне слово має бути записане з великої літери. Вивести результат на екран.


def check_name(name):
    words = name.split()

    for word in words:
        if not word.isalpha() or not word.istitle():
            return False
    return True


user_input = input("Введіть ваше ПІБ: ")

if check_name(user_input):
    print("Рядок складається з літер, кожне слово записане з великої літери.")
else:
    print("Рядок не відповідає вимогам.")
