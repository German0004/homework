# Використовуючи код example_10, створіть декоратори @classmethod для формування переліку об'єктів, які підрахують
# кількість повнолітніх людей в Україні та Америці.


from datetime import date

class MyClass1:
    people = []

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
        MyClass1.people.append(self)

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @staticmethod
    def is_adult_ukraine(age):
        return age >= 18

    @staticmethod
    def is_adult_usa(age):
        return age >= 21

    @classmethod
    def count_adults_ukraine(cls):
        count = 0
        for person in cls.people:
            if cls.is_adult_ukraine(person.age):
                count += 1
        return count

    @classmethod
    def count_adults_usa(cls):
        count = 0
        for person in cls.people:
            if cls.is_adult_usa(person.age):
                count += 1
        return count


class MyClass2(MyClass1):
    color = 'White'



m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan', 2000)
m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)

# Виклик @classmethod для підрахунку повнолітніх

print("Number of adults in Ukraine:", MyClass1.count_adults_ukraine())
print("Number of adults in USA:", MyClass1.count_adults_usa())


# Пояснення:

# В класі MyClass1 додано статичний список people, в який додаються всі створені об'єкти через конструктор __init__.
# Декоратор @classmethod для підрахунку повнолітніх:

# count_adults_ukraine() і count_adults_usa() є @classmethod, які проходять по списку people і використовують статичні
# методи is_adult_ukraine() та is_adult_usa() для визначення кількості повнолітніх осіб в Україні та США відповідно.
# Використання @classmethod:

# Після створення об'єктів можна викликати MyClass1.count_adults_ukraine() та MyClass1.count_adults_usa() для отримання
# кількості повнолітніх в кожній з країн.

# Цей підхід дозволяє вам ефективно підрахувати кількість повнолітніх людей в різних країнах, використовуючи методи класу
# та статичні методи для визначення статусу повноліття.