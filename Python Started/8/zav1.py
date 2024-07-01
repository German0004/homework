# Створіть функцію, яка відображає привітання для користувача із заданим ім'ям. Якщо ім'я не вказано, вона
# повинна виводити привітання для користувача з Вашим ім'ям


def Your_name(name=input("Enter your name: ")):
    if not name:
        print("Hello my name is Evgen, please enter your name")
    else:
        print(f"Your name is {name}")
        print("Hello i`m your friend :)")

Your_name()

