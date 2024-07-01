# Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting(). Обидва створюють різні
# привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох об'єктів в одній
# функції (функція hello_friend).


class English:
    def greeting(self):
        return "Hello! How are you?"


class Spanish:
    def greeting(self):
        return "¡Hola! ¿Cómo estás?"


def hello_friend():
    # Створення об'єктів двох класів
    english = English()
    spanish = Spanish()

    # Виклик методу greeting() для кожного об'єкта
    print("In English:", english.greeting())
    print("En Español:", spanish.greeting())


# Виклик функції hello_friend для виведення привітань з обох мов
hello_friend()