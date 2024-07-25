# Створіть XML-файл із вкладеними елементами та скористайтеся мовою пошуку XPATH. Спробуйте
# здійснити пошук вмісту за створеним документом XML, ускладнюючи свої запити та додаючи нові елементи, якщо буде потрібно.
import xml.etree.ElementTree as ET

# Створюємо кореневий елемент
root = ET.Element("library")

# Створюємо піддерево для книг
books = ET.SubElement(root, "books")

# Додаємо книги
book1 = ET.SubElement(books, "book", id="1")
title1 = ET.SubElement(book1, "title")
title1.text = "The Catcher in the Rye"
author1 = ET.SubElement(book1, "author")
author1.text = "J.D. Salinger"
year1 = ET.SubElement(book1, "year")
year1.text = "1951"

book2 = ET.SubElement(books, "book", id="2")
title2 = ET.SubElement(book2, "title")
title2.text = "To Kill a Mockingbird"
author2 = ET.SubElement(book2, "author")
author2.text = "Harper Lee"
year2 = ET.SubElement(book2, "year")
year2.text = "1960"

# Перетворюємо дерево в XML-строку
tree = ET.ElementTree(root)
tree.write("library.xml")
