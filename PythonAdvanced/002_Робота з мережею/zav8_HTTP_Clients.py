# Створіть HTTP-клієнта, який прийматиме URL ресурсу, тип методу та словник як передавальні дані (опціональний).
# Виконувати запит з отриманим методом на отриманий ресурс, передаючи дані відповідним методом, та друкувати на консоль
# статус-код, заголовки та тіло відповіді.


# Для створення HTTP-клієнта, який приймає URL ресурсу, тип методу та словник з даними (опціонально), можна
# використати бібліотеку requests.

import requests

def http_client(url, method, data=None):
    """
    Виконує HTTP запит.

    :param url: URL ресурсу
    :param method: Тип методу (GET, POST, PUT, DELETE)
    :param data: Словник з даними для передачі (опціонально)
    """
    method = method.upper()

    try:
        if method == 'GET':
            response = requests.get(url, params=data)
        elif method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url, json=data)
        else:
            print("Невідомий метод HTTP.")
            return

        print(f"Статус-код: {response.status_code}")
        print("Заголовки:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        print("\nТіло відповіді:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Сталася помилка: {e}")

# Приклад використання
url = "https://jsonplaceholder.typicode.com/posts"
method = "POST"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

http_client(url, method, data)


# Пояснення
# Функція http_client:
#
# Приймає параметри url, method та data.
# Визначає метод запиту (GET, POST, PUT, DELETE) і виконує відповідний запит.
# Обробляє відповідь, друкуючи на консоль статус-код, заголовки та тіло відповіді.
# Виправляє загальні помилки під час виконання запиту, виводячи відповідне повідомлення.
# Приклад використання:
#
# Використовує функцію http_client для відправлення POST запиту на ресурс https://jsonplaceholder.typicode.com/posts
# з передачею даних.
#
# Запуск
#
# Скопіюйте код в файл, наприклад http_client.py.
# Запустіть файл за допомогою Python:
#
# sh
#
#
# python http_client.py
# Цей клієнт є гнучким і підтримує основні методи HTTP. Ви можете використовувати його для відправлення запитів на
# різні ресурси з різними методами та даними.