# Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr(). Застосувати ці функції до
# кожного з атрибутів класів, подивитися до чого це призводить.


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
contact1 = Contact("Doe", "John", 30, "123-456-7890", "john.doe@example.com")
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
print("Contact1 send_message:", contact1.send_message("Hello, John!"))

print("\nUpdateContact1 get_contact:", update_contact1.get_contact())
print("UpdateContact1 get_message:", update_contact1.get_message())

# Використання hasattr(), getattr(), setattr(), delattr()
attributes = ['surname', 'name', 'age', 'mob_phone', 'email', 'job']

for attr in attributes:
    print(f"\nChecking attribute '{attr}' in contact1:")
    if hasattr(contact1, attr):
        print(f"contact1 has attribute '{attr}' with value: {getattr(contact1, attr)}")
    else:
        print(f"contact1 does not have attribute '{attr}'")

    if hasattr(update_contact1, attr):
        print(f"update_contact1 has attribute '{attr}' with value: {getattr(update_contact1, attr)}")
    else:
        print(f"update_contact1 does not have attribute '{attr}'")

# Set new values for attributes
print("\nSetting new values for attributes...")
setattr(contact1, 'age', 31)
setattr(update_contact1, 'job', 'Senior Engineer')

print("New value of contact1 age:", getattr(contact1, 'age'))
print("New value of update_contact1 job:", getattr(update_contact1, 'job'))

# Delete attributes
print("\nDeleting 'mob_phone' from contact1 and update_contact1...")
delattr(contact1, 'mob_phone')
delattr(update_contact1, 'mob_phone')

print("Checking if 'mob_phone' exists after deletion:")
print("contact1 has mob_phone:", hasattr(contact1, 'mob_phone'))
print("update_contact1 has mob_phone:", hasattr(update_contact1, 'mob_phone'))
