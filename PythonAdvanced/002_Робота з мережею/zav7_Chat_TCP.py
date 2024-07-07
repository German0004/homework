# Створити простий чат на основі протоколу TCP, який дасть змогу під'єднуватися кільком клієнтам та
# обмінюватися повідомленнями.


# Завдання треба робити в різних модулях

# 1_SERVER

import socket
import threading

# Налаштування сервера
HOST = '127.0.0.1'  # Локальний хост
PORT = 12345        # Порт для прослуховування

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Відправка повідомлення всім підключеним клієнтам
def broadcast(message):
    for client in clients:
        client.send(message)

# Обробка повідомлень від клієнтів
def handle_client(client):
    while True:
        try:
            # Прийом повідомлення від клієнта
            message = client.recv(1024)
            broadcast(message)
        except:
            # Видалення і відключення клієнта
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} залишив чат!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Прийом нових підключень
def receive():
    while True:
        client, address = server.accept()
        print(f'Підключено з {str(address)}')

        # Запит і збереження псевдоніма
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Псевдонім клієнта: {nickname}')
        broadcast(f'{nickname} приєднався до чату!'.encode('utf-8'))
        client.send('Підключення до сервера!'.encode('utf-8'))

        # Запуск обробки повідомлень клієнта в окремому потоці
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print('Сервер запущено...')
receive()


# НАСТУПНУ ЧАТИНУ треба скопіювати в інший модуль а можно в декілько мудолів

# 2_CLIENTS

import socket
import threading

# Налаштування клієнта
nickname = input("Введіть ваш псевдонім: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

# Прийом повідомлень від сервера
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Закриття підключення при виникненні помилки
            print("Виникла помилка!")
            client.close()
            break

# Відправка повідомлень на сервер
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Запуск потоків для прийому і відправки повідомлень
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

# Пояснення
#
# Сервер:
#
# Налаштовується для прослуховування на локальному хості і порту.
# Приймає підключення клієнтів і зберігає їх.
# В окремому потоці обробляє повідомлення від кожного клієнта.
# Відправляє отримані повідомлення всім підключеним клієнтам.
#
# Клієнт:
#
# Підключається до сервера.
# Відправляє псевдонім на сервер при підключенні.
# В окремих потоках приймає повідомлення від сервера і відправляє повідомлення на сервер.
# Запуск
# Запустіть серверний код (server.py).
# Запустіть клієнтський код (client.py) у кількох терміналах чи на різних машинах, щоб підключитися до сервера і почати
# обмінюватися повідомленнями.