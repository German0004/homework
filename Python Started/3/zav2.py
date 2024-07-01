# Напишіть програму, яка обчислює значення функції 𝑦 = cos(3x), де - 𝜋 <= x <= 𝜋 та
# вводиться з клавіатури. Відповідь подати у радіанах.

import math

x = float(input("Введіть число x: "))

# pi = 3.14

if -math.pi <= x <= math.pi:
    cos = math.cos(3*x)
    print(f"y = {math.radians(cos)}")
else:
    print("Введіть інше число, будь ласка")