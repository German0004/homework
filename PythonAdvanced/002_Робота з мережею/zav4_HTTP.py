# Вивчіть основні поняття, розглянуті в уроці, а також особливості роботи з HTTP-протоколами в Python, використовуючи
# бібліотеки urllib та requests.


# Основні поняття HTTP

# HTTP (HyperText Transfer Protocol) - це протокол для передачі гіпертексту (тексту, зображень, відео) в Інтернеті.
# Він працює за принципом клієнт-сервер: клієнт надсилає запит до сервера, сервер обробляє запит і повертає відповідь.

# Основні компоненти HTTP-запиту:

# Метод запиту: Вказує дію, яку потрібно виконати. Основні методи:
# GET: Отримання даних з сервера.
# POST: Відправка даних на сервер.
# PUT: Оновлення даних на сервері.
# DELETE: Видалення даних на сервері.
# HEAD: Отримання лише заголовків відповіді.
# OPTIONS: Отримання підтримуваних методів для ресурсу.
# URL (Uniform Resource Locator): Вказує адресу ресурсу.
# Заголовки: Містять додаткову інформацію про запит або відповідь.
# Тіло: Містить дані, які передаються (тіло зазвичай використовується в запитах POST, PUT).
# Основні компоненти HTTP-відповіді:
# Код стану: Вказує результат запиту. Основні коди:
# 200 OK: Запит успішно виконано.
# 404 Not Found: Ресурс не знайдено.
# 500 Internal Server Error: Внутрішня помилка сервера.
# Заголовки: Містять додаткову інформацію про відповідь.
# Тіло: Містить дані, які повертаються (тіло зазвичай використовується для передачі HTML, JSON, XML і т.д.).
# Робота з HTTP-протоколами в Python

# Бібліотека urllib
# urllib - це стандартна бібліотека Python для роботи з URL і HTTP-запитами. Основні модулі:

# urllib.request: Містить функції для відкриття та читання URL.
# urllib.parse: Містить функції для розбору URL.
# urllib.error: Містить винятки, які можуть бути викликані під час роботи з urllib.request.
# urllib.robotparser: Для розбору файлів robots.txt.


# Приклад використання urllib.request

import urllib.request

url = 'http://www.example.com'
response = urllib.request.urlopen(url)
html = response.read()

print(html)
# Надсилання запиту з даними

import urllib.parse
import urllib.request

url = 'http://www.example.com'
data = urllib.parse.urlencode({'key': 'value'}).encode()
req = urllib.request.Request(url, data=data)
response = urllib.request.urlopen(req)
result = response.read()

print(result)

# Бібліотека requests
# requests - це популярна стороння бібліотека для роботи з HTTP-запитами в Python. Вона значно спрощує процес відправки
# HTTP-запитів та обробки відповідей.

# Приклад використання requests

import requests

url = 'http://www.example.com'
response = requests.get(url)
html = response.text

print(html)

# Надсилання POST-запиту


import requests

url = 'http://www.example.com'
data = {'key': 'value'}
response = requests.post(url, data=data)
result = response.text

print(result)

# Основні відмінності між urllib та requests
# Простота використання: requests має простіший і зрозуміліший синтаксис.
# Обробка JSON: requests має вбудовану підтримку для обробки JSON (метод response.json()).
# Обробка сесій: requests підтримує сесії (клас requests.Session), що дозволяє зберігати куки та іншу інформацію між запитами.
# Менше налаштувань: requests автоматично обробляє багато аспектів HTTP-запитів, таких як кодування, редиректи, тощо.