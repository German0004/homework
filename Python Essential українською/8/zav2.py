# Модифікуйте вихідний код сервісу зі скорочення посилань з ДЗ 7 заняття курсу Python Starter так, щоб він зберігав базу
# посилань на диску і не «забув» при перезапуску. За бажанням можете ознайомитися з модулем shelve
# (https://docs.python.org/3/library/shelve.html), який у даному випадку буде дуже зручним та спростить виконання завдання


# Функція для зберігання бази посилань у файл
def save_links(links):
    with open("links_database.txt", "w") as file:
        for key, value in links.items():
            file.write(f"{key}: {value}\n")


# Функція для завантаження бази посилань з файлу
def load_links():
    try:
        with open("links_database.txt", "r") as file:
            links = {}
            for line in file:
                key, value = line.strip().split(": ")
                links[key] = value
            return links
    except FileNotFoundError:
        return {}


# Завантажуємо базу посилань з файлу, якщо вона є
links = load_links()

exit_choice = "1"
while exit_choice != "0":
    value = input("Enter your link: ")
    key = input("Enter short name of the link: ")
    links[key] = value
    exit_choice = input("Enter 0 to exit or something else to continue: ")

# Зберігаємо базу посилань у файл перед виходом
save_links(links)

search_name = input("Enter search link name: ")
print(links.get(search_name, "Name is not found"))


# Як це працює:
# Функція save_links(links) записує кожен елемент словника links у файл links_database.txt у вигляді "ключ: значення".
# Функція load_links() читає файли із записаними рядками "ключ: значення" і розбиває їх на пари ключ-значення,
# щоб створити словник links.
# Програма працює аналогічно вашому початковому коду, дозволяючи користувачеві вводити нові посилання і короткі назви,
# які потім зберігаються у словнику links.
# При виході з програми (коли користувач ввів 0), словник links зберігається у файл links_database.txt.
# Під час наступного запуску програми дані завантажуються з файлу links_database.txt, щоб відновити попередню базу посилань.
# Цей підхід використовує текстовий формат з простим роздільником для зберігання даних, що може бути зручним для менших
# обсягів даних і простих програм.
