# Напишіть програму, яка на вхід отримує параметри кольору (в діапазоні від 0 до 255 для кожного кольору) у форматі RGB
# і виводить на екран кортеж, у якому зберігається колір.


def create_color_tuple(red, green, blue):
    color_tuple = (red, green, blue)
    return color_tuple


while True:
    try:
        red = int(input("Введіть значення для червоного кольору (від 0 до 255): "))
        green = int(input("Введіть значення для зеленого кольору (від 0 до 255): "))
        blue = int(input("Введіть значення для синього кольору (від 0 до 255): "))

        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            print(
                "Неправильне значення кольору. Значення кольору повинно бути в діапазоні від 0 до 255."
            )
            continue

        color = create_color_tuple(red, green, blue)
        print("Кортеж кольору (RGB):", color)

        break
    except ValueError:
        print("Некоректний ввід. Будь ласка, введіть цілі числа.")
