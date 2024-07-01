# Використовуючи код з завдання 2, створити 2 екземпляри обох класів. Використати функції isinstance() – для перевірки екземплярів
# класу (за яким класом створені) та issubclass() – для перевірки і визначення класу-нащадка.


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
contact2 = Contact("Ivanov", "Ivan", 35, "555-123-4567", "ivan.ivanov@example.com")

update_contact1 = UpdateContact("Smith", "Jane", 28, "987-654-3210", "jane.smith@example.com", "Engineer")
update_contact2 = UpdateContact("Doe", "John", 40, "789-654-3210", "john.doe@example.com", "Manager")

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

# Перевірка екземплярів класу за допомогою isinstance()
print("\nПеревірка екземплярів класу за допомогою isinstance():")
print(f"contact1 is instance of Contact: {isinstance(contact1, Contact)}")
print(f"contact1 is instance of UpdateContact: {isinstance(contact1, UpdateContact)}")
print(f"update_contact1 is instance of Contact: {isinstance(update_contact1, Contact)}")
print(f"update_contact1 is instance of UpdateContact: {isinstance(update_contact1, UpdateContact)}")

# Перевірка класу-нащадка за допомогою issubclass()
print("\nПеревірка класу-нащадка за допомогою issubclass():")
print(f"UpdateContact is subclass of Contact: {issubclass(UpdateContact, Contact)}")
print(f"Contact is subclass of UpdateContact: {issubclass(Contact, UpdateContact)}")

# Цей код:
#
# Створює два екземпляри класу Contact і два екземпляри класу UpdateContact.
# Використовує функцію isinstance() для перевірки, до якого класу належать екземпляри.
# Використовує функцію issubclass() для перевірки, чи є один клас нащадком іншого.
# Вивід цього коду допоможе вам зрозуміти, як працюють функції isinstance() і issubclass().
