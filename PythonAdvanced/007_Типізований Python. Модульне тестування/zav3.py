# Використовуючи модуль sqlite3 та модуль smtplib, реалізуйте реальне додавання користувачів до бази. Мають бути
# реалізовані такі функції та класи:
# ·        клас користувача, що містить у собі такі методи: get_full_name
#          (ПІБ з поділом через пробіл: «Петров Ігор Сергійович»), get_short_name (формату ПІБ: «Петров І. С.»),
#          get_age (повертає вік користувача, використовуючи поле birthday типу datetime.date); метод __str__
#          (повертає ПІБ та дату народження);
# ·        функція реєстрації нового користувача (приймаємо екземпляр нового користувача та відправляємо email
# на пошту користувача з листом подяки).
# ·        функція відправлення email з листом подяки.
# ·        функція пошуку користувачів у таблиці users за іменем, прізвищем і поштою.
#
# Протестувати цей функціонал, використовуючи заглушки у місцях надсилання пошти. Під час штатного запуску
# програми вона має відправляти повідомлення на вашу реальну поштову скриньку (необхідно налаштувати SMTP,
# використовуючи доступи від провайдера вашого email-сервісу).
#
# Приклад налаштування SMTP для сервісу Gmail: https://support.google.com/mail/answer/7126229?hl=ru
# ----------------------------------
#  Створюємо структуру проекту:
# Створимо файл user_registration.py, в якому буде реалізована вся логіка.
#
# 2. Визначаємо класи:

import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, date


class User:
    def __init__(self, first_name, last_name, middle_name, birthday, email):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birthday = birthday
        self.email = email

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_short_name(self):
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    def get_age(self):
        today = date.today()
        return (
            today.year
            - self.birthday.year
            - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        )

    def __str__(self):
        return f"{self.get_full_name()}, {self.birthday}"


# Функції для роботи з базою даних та відправлення email
def create_user(user: User):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            middle_name TEXT,
            birthday TEXT,
            email TEXT
        )
    """
    )

    cursor.execute(
        """
        INSERT INTO users (first_name, last_name, middle_name, birthday, email)
        VALUES (?, ?, ?, ?, ?)
    """,
        (
            user.first_name,
            user.last_name,
            user.middle_name,
            str(user.birthday),
            user.email,
        ),
    )

    conn.commit()
    conn.close()

    # Відправляємо email з підтвердженням
    send_confirmation_email(user.email)


def send_confirmation_email(recipient_email):
    # Налаштування SMTP
    smtp_server = "smtp.gmail.com"  # Замініть на ваш SMTP сервер
    port = 587
    sender_email = "your_email@gmail.com"  # Ваша email адреса
    password = "your_password"  # Ваш пароль

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Дякуємо за реєстрацію!"
    body = "Ви успішно зареєструвалися на нашому сайті!"
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)


def search_user(name, last_name, email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE first_name LIKE ? AND last_name LIKE ? AND email LIKE ?
    """,
        (f"%{name}%", f"%{last_name}%", f"%{email}%"),
    )

    results = cursor.fetchall()
    conn.close()

    users = []
    for row in results:
        user = User(
            row[1], row[2], row[3], datetime.strptime(row[4], "%Y-%m-%d"), row[5]
        )
        users.append(user)

    return users


# Тестуванняv
if __name__ == "__main__":
    # Для тестування без відправки email
    # send_confirmation_email = lambda email: print(f"Email sent to {email}")

    user = User(
        "Ігор", "Петров", "Сергійович", datetime(1990, 1, 1), "igor.petrov@example.com"
    )
    create_user(user)

    # Пошук користувача
    found_users = search_user("Ігор", "Петров", "")
    for user in found_users:
        print(user)

# Важливо:
#
# Налаштування SMTP: Замініть smtp.gmail.com, your_email@gmail.com і your_password на ваші власні дані.
# Безпека: Зберігання паролів у коді не рекомендується. Краще використовувати змінні середовища або файли
# конфігурації для зберігання чутливих даних.
# Додаткові функції: Можна додати функції для оновлення даних користувача, видалення користувача тощо.
# Валідація даних: Перед збереженням даних в базу, варто перевіряти їх на коректність (наприклад, формат email).
# Багатопоточність: Для великої кількості користувачів можна розглянути використання багатопоточності для підвищення
# продуктивності.

# Зауваження:
#
# Код наведено для демонстрації основних принципів. Для реальних проектів рекомендується використовувати більш
# складні схеми аутентифікації та авторизації, а також розглянути питання безпеки даних.
# Для більш масштабних проектів можна використовувати фреймворки для веб-розробки (Django, Flask), які надають
# готові інструменти для роботи з базами даних, формами та іншими аспектами веб-додатків.
# Цей код забезпечує базову функціональність для реєстрації користувачів, зберігання їх даних у базі даних
# SQLite і відправки email-повідомлень. Ви можете розширити його відповідно до ваших потреб.
