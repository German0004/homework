# Використовуючи сервіс https://jsonplaceholder.typicode.com/, спробуйте побудувати різні типи запитів та
# обробити відповіді. Необхідно попрактикуватися з urllib та бібліотекою requests. Рекомендується спочатку
# спробувати виконати запити, використовуючи urllib, а потім спробувати реалізувати те саме, використовуючи requests.


# Виконання HTTP-запитів з використанням urllib та requests
# URL для роботи
# Ми будемо використовувати сервіс JSONPlaceholder для виконання наступних запитів:
#
# GET запит для отримання всіх постів.
# GET запит для отримання одного поста.
# POST запит для створення нового поста.
# PUT запит для оновлення існуючого поста.
# DELETE запит для видалення поста.
# Виконання запитів з використанням urllib

import urllib.request
import urllib.parse
import json

# 1. GET запит для отримання всіх постів
url = 'https://jsonplaceholder.typicode.com/posts'
response = urllib.request.urlopen(url)
data = response.read()
posts = json.loads(data)
print("GET всі пости:", posts)

# 2. GET запит для отримання одного поста
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
response = urllib.request.urlopen(url)
data = response.read()
post = json.loads(data)
print(f"GET пост {post_id}:", post)

# 3. POST запит для створення нового поста
url = 'https://jsonplaceholder.typicode.com/posts'
data = json.dumps({
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}).encode('utf-8')
headers = {'Content-Type': 'application/json'}
req = urllib.request.Request(url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
new_post = json.loads(response.read())
print("POST новий пост:", new_post)

# 4. PUT запит для оновлення існуючого поста
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
data = json.dumps({
    'id': post_id,
    'title': 'foo_updated',
    'body': 'bar_updated',
    'userId': 1
}).encode('utf-8')
headers = {'Content-Type': 'application/json'}
req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
response = urllib.request.urlopen(req)
updated_post = json.loads(response.read())
print(f"PUT оновлений пост {post_id}:", updated_post)

# 5. DELETE запит для видалення поста
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
req = urllib.request.Request(url, method='DELETE')
response = urllib.request.urlopen(req)
print(f"DELETE пост {post_id}:", response.status)


# Виконання запитів з використанням requests

import requests

# 1. GET запит для отримання всіх постів
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
posts = response.json()
print("GET всі пости:", posts)

# 2. GET запит для отримання одного поста
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
response = requests.get(url)
post = response.json()
print(f"GET пост {post_id}:", post)

# 3. POST запит для створення нового поста
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = requests.post(url, json=data)
new_post = response.json()
print("POST новий пост:", new_post)

# 4. PUT запит для оновлення існуючого поста
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
data = {
    'id': post_id,
    'title': 'foo_updated',
    'body': 'bar_updated',
    'userId': 1
}
response = requests.put(url, json=data)
updated_post = response.json()
print(f"PUT оновлений пост {post_id}:", updated_post)

# 5. DELETE запит для видалення поста
post_id = 1
url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
response = requests.delete(url)
print(f"DELETE пост {post_id}:", response.status_code)

# Порівняння urllib та requests
# Простота використання:
#
# requests значно спрощує створення і обробку HTTP-запитів.
# urllib потребує більше коду для виконання аналогічних завдань, особливо для POST та PUT запитів.

# Обробка JSON:

# requests має вбудовану підтримку для обробки JSON (метод json()).
# В urllib потрібно окремо декодувати JSON з використанням бібліотеки json.

# Параметри заголовків:

# В requests додавання заголовків дуже просте через параметр headers.
# В urllib потрібно використовувати об'єкт Request і явно задавати заголовки.

# Методи запитів:

# requests підтримує всі HTTP методи (GET, POST, PUT, DELETE) через відповідні функції.
# В urllib методи POST, PUT та DELETE потребують створення об'єкту Request і явного вказування методу.

# Сесії:

# requests підтримує сесії, що дозволяє зберігати куки та іншу інформацію між запитами (через requests.Session).
# В urllib потрібно явно керувати куками та іншими аспектами сесій.