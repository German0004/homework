# Напишіть програму-калькулятор, яка підтримує такі операції: додавання, віднімання, множення,
# ділення та піднесення до ступеня.
# Програма має видавати повідомлення про помилку та продовжувати роботу під час введення некоректних даних,
# діленні на нуль та зведенні нуля в негативний степінь.


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

def power(x, y):
    if x == 0 and y < 0:
        raise ValueError("Zero cannot be raised to a negative power")
    return x ** y

def calculator():

    while True:
        try:
            print("\nCalculator Menu:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Power")
            print("6. Exit")

            choice = int(input("Enter your choice (1-6): "))

            if choice == 6:
                print("Exiting the calculator. Goodbye!")
                break

            if choice < 1 or choice > 6:
                raise ValueError("Invalid choice. Please enter a number between 1 and 6")

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == 4:
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            elif choice == 5:
                result = power(num1, num2)
                print(f"Result: {num1} ** {num2} = {result}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

# Викликаємо головну функцію калькулятора
calculator()