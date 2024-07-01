# Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact, sent_message. Створити
# клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job. Додати методи get_message. Створити
# екземпляри класів та дослідити стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__.
# Роздрукувати інформацію на екрані.


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

# Дослідження стану об'єктів
print("Contact1 __dict__:", contact1.__dict__)
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

