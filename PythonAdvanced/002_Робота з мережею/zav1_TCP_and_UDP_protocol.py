# Вивчіть основні поняття, розглянуті на уроці, а також особливості роботи з TCP та UDP протоколами в Python.


# Основні поняття TCP та UDP протоколів
# TCP (Transmission Control Protocol)
# З'єднаний протокол: TCP встановлює з'єднання між клієнтом і сервером перед передачею даних, що забезпечує надійність зв'язку.
# Надійність: TCP гарантує доставку даних в правильному порядку та без втрат.
# Контроль помилок: TCP використовує механізми контрольних сум і повторну передачу втрачених пакетів для забезпечення цілісності даних.
# Контроль потоку: TCP забезпечує управління потоком даних для уникнення перевантаження мережі.
# UDP (User Datagram Protocol)
# Безз'єднаний протокол: UDP не встановлює з'єднання перед передачею даних, що робить його швидшим, але менш надійним.
# Менша надійність: UDP не гарантує доставку даних і не забезпечує їх правильний порядок.
# Менші затримки: Оскільки немає механізмів контролю, UDP підходить для додатків, які потребують швидкої передачі даних
# (наприклад, потокове відео або онлайн-ігри).
# Робота з TCP та UDP в Python
# TCP в Python
# Для роботи з TCP в Python використовується модуль socket.

#                   Приклад TCP сервера:
import socket

# Створення TCP сокету
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Прив'язка сокету до адреси і порту
server_socket.bind(('localhost', 12345))

# Початок прослуховування (максимум 5 одночасних підключень)
server_socket.listen(5)
print("Сервер запущено і прослуховується на порту 12345...")

while True:
    # Прийняття підключення
    client_socket, client_address = server_socket.accept()
    print(f"Підключено клієнта з адресою: {client_address}")

    # Отримання даних від клієнта
    data = client_socket.recv(1024)
    print(f"Отримано дані: {data.decode()}")

    # Відправка відповіді клієнту
    client_socket.sendall(b'Привіт від сервера!')

    # Закриття з'єднання з клієнтом
    client_socket.close()

#                   Приклад TCP клієнта:
import socket

# Створення TCP сокету
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Підключення до сервера
client_socket.connect(('localhost', 12345))

# Відправка даних на сервер
client_socket.sendall(b'Привіт сервер!')

# Отримання відповіді від сервера
data = client_socket.recv(1024)
print(f"Отримано відповідь: {data.decode()}")

# Закриття з'єднання
client_socket.close()


# UDP в Python
# Для роботи з UDP в Python також використовується модуль socket.

#                   Приклад UDP сервера:
import socket

# Створення UDP сокету
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Прив'язка сокету до адреси і порту
server_socket.bind(('localhost', 12345))
print("UDP сервер запущено і прослуховується на порту 12345...")

while True:
    # Отримання даних від клієнта
    data, client_address = server_socket.recvfrom(1024)
    print(f"Отримано дані від {client_address}: {data.decode()}")

    # Відправка відповіді клієнту
    server_socket.sendto(b'Привіт від UDP сервера!', client_address)

#                   Приклад UDP клієнта:
import socket

# Створення UDP сокету
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Відправка даних на сервер
client_socket.sendto(b'Привіт UDP сервер!', ('localhost', 12345))

# Отримання відповіді від сервера
data, server_address = client_socket.recvfrom(1024)
print(f"Отримано відповідь: {data.decode()}")

# Закриття сокету (опціонально)
client_socket.close()
Підсумок
TCP підходить для додатків, де важлива надійність передачі даних, таких як веб-сервери, бази даних, файлообмінні протоколи.
UDP підходить для додатків, де важлива швидкість і низька затримка, таких як потокове відео, голосові та відео дзвінки,
онлайн-ігри.
Ці приклади демонструють основи використання TCP та UDP протоколів у Python для створення серверів та клієнтів.
