# Відкрийте файл fix_me.py із папки homework. Використовуючи звичайний текстовий редактор (Notepad), виправте всі
# помилки оформлення коду згідно з PEP 8.


# файл fix_me.py


#       Декоратори ф-цій


import webbrowser


def validator(func):
    def wrapper(url):
        if "." in url
            func(url)
        else:
            print("Посилання не вірне")

    return wrapper


@validator  # @ - додає декоратор для ф-ції
def open_url(url):
    webbrowser.open(url)


open_url("https://itproger.com/ua")
