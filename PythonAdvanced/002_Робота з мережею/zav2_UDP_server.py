# Створіть UDP-сервер, який очікує на повідомлення про нові пристрої в мережі. Він приймає повідомлення певного формату,
# де буде ідентифікатор пристрою, і друкує нові під'єднання в консоль. Створіть UDP-клієнта, який надсилатиме унікальний
# ідентифікатор пристрою на сервер, повідомляючи про свою присутність.


# UDP-сервер

import socket

# Створення UDP-сокету
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Прив'язка сокету до адреси і порту
server_socket.bind(('localhost', 12345))
print("UDP the server is running and listening on the port 12345...") # сервер запущено і прослуховується на порту

# Зберігати ідентифікатори пристроїв
devices = set()

while True:
    # Отримання даних від клієнта
    data, client_address = server_socket.recvfrom(1024)
    device_id = data.decode()

    # Друк ідентифікатора пристрою
    if device_id not in devices:
        devices.add(device_id)
        print(f"New device connected: {device_id}") #  Новий пристрій підключено:

    # Відправка підтвердження клієнту (опціонально)
    server_socket.sendto(b'The device is registered', client_address) # Пристрій зареєстровано
# UDP-клієнт

import socket

# Унікальний ідентифікатор пристрою
device_id = "device_12345"

# Створення UDP-сокету
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Відправка даних на сервер
client_socket.sendto(device_id.encode(), ('localhost', 12345))

# Отримання відповіді від сервера (опціонально)
data, server_address = client_socket.recvfrom(1024)
print(f"A response was received from the server: {data.decode()}") # Отримано відповідь від сервера:

# Закриття сокету (опціонально)
client_socket.close()

# Опис роботи
# UDP-сервер:

# Створює UDP-сокет і прив'язує його до порту 12345.
# Прослуховує повідомлення від клієнтів.
# Зберігає унікальні ідентифікатори пристроїв у множині devices.
# При отриманні нового ідентифікатора друкує його в консоль.
# UDP-клієнт:

# Визначає унікальний ідентифікатор пристрою.
# Створює UDP-сокет.
# Відправляє ідентифікатор на сервер.
# Отримує підтвердження від сервера (опціонально).
# Запустіть спочатку сервер, а потім клієнт для перевірки роботи. Ви можете запустити кілька клієнтів з різними ідентифікаторами,
# щоб побачити, як сервер реагує на нові підключення.