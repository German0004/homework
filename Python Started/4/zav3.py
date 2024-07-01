# Використовуючи вкладені цикли та функції print(‘*’, end=’’), print(‘ ‘, end=’’) та print()
# виведіть на екран прямокутний трикутник

b = "*"
print(b)


a = "**"
print(a)


for i in range(1):
    for j in range(4):
        print('*', end='')
    print()

for k in range(1):
    for l in range(7):
        print(f"*", end="")

a = "*"
print(a)