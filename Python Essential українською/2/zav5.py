# Використовуючи код example_10, створіть декоратор @staticmethod для визначення повноліття людини в Україні
# та Америці

from datetime import date

class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

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

class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.print_info()

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan', 2000)
m_per2.print_info()

m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
print(isinstance(m_per4, MyClass1))

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))

# Визначення повноліття в Україні та Америці
print("Is m_per1 adult in Ukraine?", MyClass1.is_adult_ukraine(m_per1.age))
print("Is m_per1 adult in USA?", MyClass1.is_adult_usa(m_per1.age))


# Пояснення змін:
# Додання статичних методів:
# is_adult_ukraine(age) та is_adult_usa(age) статичні методи, які приймають параметр age і повертають True,
# якщо вік перевищує або дорівнює відповідному віку повноліття в Україні (18 років) або в США (21 рік).
# Використання статичних методів:
# Після створення екземпляру класу m_per1, можна викликати ці статичні методи для визначення, чи є особа повнолітньою
# в конкретних країнах.
# Цей код додає функціональність для визначення повноліття в різних контекстах за допомогою статичних методів,
# що дозволяє вам легко перевіряти статус повноліття для об'єктів MyClass1 та його підкласів, які унаслідували ці методи.