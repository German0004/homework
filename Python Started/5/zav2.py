# Напишіть програму, в якій користувач вводить із клавіатури діапазон чисел (в діапазоні має бути не менше 5 чисел).
# Вивести на екран суму другого, передостаннього, а також середнього арифметичного значення даної послідовності.


def calculate_sum_and_average(numbers):
    second_number = numbers[1]
    penultimate_number = numbers[-2]
    average = sum(numbers) / len(numbers)
    return second_number, penultimate_number, average


while True:
    try:
        range_start = int(input("Введіть початок діапазону: "))
        range_end = int(input("Введіть кінець діапазону: "))

        if range_end - range_start + 1 < 5:
            print("Діапазон повинен містити не менше 5 чисел. Спробуйте знову.")
            continue

        numbers = list(range(range_start, range_end + 1))

        second_number, penultimate_number, average = calculate_sum_and_average(numbers)

        print(
            "Сума другого та передостаннього чисел:", second_number + penultimate_number
        )
        print("Середнє арифметичне значення послідовності:", average)

        break
    except ValueError:
        print("Некоректний ввід. Будь ласка, введіть цілі числа.")
