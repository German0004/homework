# Створіть програму, яка емулює роботу сервісу зі скорочення посилань. Повинна бути реалізована
# можливість введення початкового посилання та короткої назви і отримання початкового посилання за її назвою.


exit = "1"
links = dict()

while exit != "0":
    value = input("Enter your link: ")
    key = input("Enter short name of the link: ")
    links[key] = value
    exit = input("Enter 0 to exit or something else to continue: ")

name = input("Enter search link name: ")
print(links.get(name,"name is not found"))
