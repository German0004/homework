# Створіть прототип програми «Бібліотека», де є можливість перегляду та внесення змін за структурою: автор: твір.
# Передбачте можливість виведення на екран сортування за автором та твором.


class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return f"Автор: {self.author}, Твір: {self.title}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        for book in self.books:
            print(book)

    def edit_book(self, author, title):
        for book in self.books:
            if book.author == author and book.title == title:
                print("Знайдено книгу. Введіть нові дані:")
                book.author = input("Новий автор: ")
                book.title = input("Новий твір: ")
                print("Дані оновлено.\n")
                return
        print("Книгу не знайдено.\n")

    def sort_by_author(self):
        sorted_books = sorted(self.books, key=lambda b: b.author)
        for book in sorted_books:
            print(book)

    def sort_by_title(self):
        sorted_books = sorted(self.books, key=lambda b: b.title)
        for book in sorted_books:
            print(book)


def main():
    library = Library()

    while True:
        print("Меню:")
        print("1. Додати книгу")
        print("2. Переглянути всі книги")
        print("3. Редагувати книгу")
        print("4. Сортувати за автором")
        print("5. Сортувати за твором")
        print("6. Вихід")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            author = input("Автор: ")
            title = input("Твір: ")
            book = Book(author, title)
            library.add_book(book)
            print("Книгу додано.\n")

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            author = input("Введіть автора книги для редагування: ")
            title = input("Введіть твір для редагування: ")
            library.edit_book(author, title)

        elif choice == "4":
            library.sort_by_author()

        elif choice == "5":
            library.sort_by_title()

        elif choice == "6":
            break

        else:
            print("Неправильний вибір, спробуйте ще раз.\n")


if __name__ == "__main__":
    main()
