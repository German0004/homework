# Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у класах Contact та UpdateContact та їх
# екземплярах. Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів. Порівняйте їх.
# Зробіть відповідні висновки.


class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"Name: {self.name} {self.surname}, Age: {self.age}, Phone: {self.mob_phone}, Email: {self.email}"

    def send_message(self, message):
        return f"Sending message to {self.mob_phone}: {message}"


class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f"Contact {self.name} {self.surname} works as {self.job}"


# Створення екземплярів класів
contact1 = Contact("Dudin", "Evgen", 42, "123-456-7890", "EvDudin@example.com")
update_contact1 = UpdateContact("Smith", "Jane", 28, "987-654-3210", "jane.smith@example.com", "Engineer")

# Дослідження стану об'єктів до видалення атрибуту
print("Before deletion of 'job' attribute:")
print("\nContact1 __dict__:", contact1.__dict__)
print("Contact1 __base__:", Contact.__base__)
print("Contact1 __bases__:", Contact.__bases__)

print("\nUpdateContact1 __dict__:", update_contact1.__dict__)
print("UpdateContact1 __base__:", UpdateContact.__base__)
print("UpdateContact1 __bases__:", UpdateContact.__bases__)

# Виклик методів та друк інформації
print("\nContact1 get_contact:", contact1.get_contact())
print("Contact1 send_message:", contact1.send_message("Hello, Evgen!"))

print("\nUpdateContact1 get_contact:", update_contact1.get_contact())
print("UpdateContact1 get_message:", update_contact1.get_message())

# Видалення атрибуту 'job'
delattr(UpdateContact, 'job')

# Дослідження стану об'єктів після видалення атрибуту
print("\nAfter deletion of 'job' attribute:")
print("\nContact1 __dict__:", contact1.__dict__)
print("Contact1 __base__:", Contact.__base__)
print("Contact1 __bases__:", Contact.__bases__)

print("\nUpdateContact1 __dict__:", update_contact1.__dict__)
print("UpdateContact1 __base__:", UpdateContact.__base__)
print("UpdateContact1 __bases__:", UpdateContact.__bases__)

# Виклик методів та друк інформації
print("\nContact1 get_contact:", contact1.get_contact())
print("Contact1 send_message:", contact1.send_message("Hello, Evgen!"))

try:
    print("\nUpdateContact1 get_contact:", update_contact1.get_contact())
    print("UpdateContact1 get_message:", update_contact1.get_message())
except AttributeError as e:
    print("\nError:", e)

# Цей код виконує наступні кроки:
#
# Створює два екземпляри класів Contact та UpdateContact.
# Друкує стан об'єктів до видалення атрибуту job.
# Видаляє атрибут job з класу UpdateContact.
# Друкує стан об'єктів після видалення атрибуту job.
# Порівнює стани об'єктів та виводить відповідні висновки.
# Висновки
# До видалення атрибуту job, екземпляр update_contact1 містить цей атрибут, і метод get_message успішно працює.
# Після видалення атрибуту job з класу UpdateContact, спроба доступу до цього атрибуту призводить до помилки AttributeError.
# Видалення атрибуту класу впливає на всі екземпляри цього класу, а не тільки на окремий екземпляр.