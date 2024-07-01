# Створіть клас Editor, який містить методи view_document та edit_document. Нехай метод edit_document виводить на екран інформацію
# про те, що редагування документів недоступне для безкоштовної версії. Створіть підклас ProEditor, у якому цей метод буде
# перевизначено. Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor.
# Викликайте методи перегляду та редагування документів.


class Editor:
    def view_document(self):
        print("Document content is displayed here.")

    def edit_document(self):
        print("Editing documents is not available in the free version.")


class ProEditor(Editor):
    def __init__(self, license_key):
        self.license_key = license_key

    def edit_document(self):
        if self.license_key == "valid_key":  # Перевірка на наявність правильного ліцензійного ключа
            print("Editing document.\nYou have full access.")
        else:
            super().edit_document()  # Викликаємо метод edit_document з батьківського класу


def main():
    license_key = input("Enter license key: ")

    if license_key == "valid_key":
        editor = ProEditor(license_key)
    else:
        editor = Editor()

    # Перегляд і редагування документів
    editor.view_document()
    editor.edit_document()


if __name__ == "__main__":
    main()
