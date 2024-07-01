# Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль фрази відповідно
# "Hello from Base" та "Hello from Child", using classmethod (@classmethod) decorator.


class Base:
    @classmethod
    def method(cls):
        print("Hello from Base")

class Child(Base):
    @classmethod
    def method(cls):
        print("Hello from Child")

# Приклад використання методу method() з обох класів
Base.method()   # Виведе: Hello from Base
Child.method()  # Виведе: Hello from Child

# У цьому прикладі:
# •	Клас Base має метод method(), який викликається через клас і виводить фразу "Hello from Base".
# •	Клас Child успадковує клас Base і також має свій власний метод method(), який викликається через
# клас Child і виводить фразу "Hello from Child".
# Декоратор @classmethod вказує Python, що метод повинен бути викликаний на рівні класу, а не на
# рівні екземпляра класу. Таким чином, метод method() доступний для виклику як через клас Base, так
# і через клас Child, і відповідно виводить різні повідомлення залежно від класу, з якого він викликається.