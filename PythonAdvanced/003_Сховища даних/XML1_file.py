import xml.etree.ElementTree as ET

# Завантажуємо XML-документ
tree = ET.parse("library.xml")
root = tree.getroot()

# Виконуємо запити XPATH
# 1. Знайдемо всі книги
books = root.findall(".//book")
print("All books:")
for book in books:
    print(book.find("title").text)

# 2. Знайдемо книгу за id
book = root.find(".//book[@id='1']")
print("\nBook with id=1:")
print(book.find("title").text)

# 3. Знайдемо автора книги за її назвою
book = root.find(".//book[title='To Kill a Mockingbird']")
print("\nAuthor of 'To Kill a Mockingbird':")
print(book.find("author").text)

# 4. Знайдемо всі книги, написані після 1950 року
books = root.findall(".//book[year>'1950']")
print("\nBooks published after 1950:")
for book in books:
    print(book.find("title").text)
