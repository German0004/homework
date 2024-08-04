# Створіть два класи Directory (тека) і File (файл) з типами (анотацією).
# Клас Directory має мати такі поля:
# ·        назва (name типу str);
# ·        батьківська тека (root типу Directory);
# ·        список файлів (список типу files, який складається з екземплярів File);
# ·        список підтек (список типу sub_directories, який складається з екземплярів Directory).
#
# Клас Directory має мати такі поля:
# ·        додавання теки до списку підтек (add_sub_directory, який приймає екземпляр Directory та присвоює поле root
# для приймального екземпляра);
# ·        видалення теки зі списку підтек (remove_sub_directory, який приймає екземпляр Directory та обнуляє поле root.
# Метод також видаляє теку зі списку sub_directories);
# ·        додавання файлу в теку (add_file, який приймає екземпляр File і присвоює йому поле directory – див. клас
# File нижче);
# ·        видалення файлу з теки (remove_file, який приймає екземпляр File та обнуляє у нього поле directory.
# Метод видаляє файл зі списку files).
#
# Клас File має мати такі поля:
# ·        назва (name типу str);
# ·        тека (Directory типу Directory).

from typing import List


class File:
    def __init__(self, name: str, directory: "Directory"):
        self.name = name
        self.directory = directory


class Directory:
    def __init__(self, name: str, root: "Directory" = None):
        self.name = name
        self.root = root
        self.files: List[File] = []
        self.sub_directories: List["Directory"] = []

    def add_sub_directory(self, directory: "Directory"):
        directory.root = self
        self.sub_directories.append(directory)

    def remove_sub_directory(self, directory: "Directory"):
        directory.root = None
        self.sub_directories.remove(directory)

    def add_file(self, file: File):
        file.directory = self
        self.files.append(file)

    def remove_file(self, file: File):
        file.directory = None
        self.files.remove(file)


# Пояснення коду:
#
# Анотації типів: Використання анотацій типів (typing.List) дозволяє чітко вказати, які типи даних очікуються для
# аргументів і повертаються функціями. Це допомагає уникнути помилок під час виконання коду і покращує його читабельність.
# Клас File:
# Має два поля: name (рядок) і directory (об'єкт класу Directory).
# Клас Directory:
# Має поля: name, root (батьківська директорія), files (список файлів) і sub_directories (список піддиректорій).
# Методи add_sub_directory і remove_sub_directory дозволяють додавати і видаляти піддиректорії, відповідно налаштовуючи
# поле root у піддиректорії.
# Методи add_file і remove_file дозволяють додавати і видаляти файли, налаштовуючи поле directory у файлі.
# Пряме циклічне посилання:
# Зверніть увагу на пряме циклічне посилання між класами Directory і File. Це дозволяє створювати складні ієрархічні
# структури файлової системи.
#
# Можливі розширення:
#
# Додаткові атрибути: Можна додати атрибути для зберігання додаткової інформації про файли і директорії (наприклад,
# розмір файлу, дату створення, права доступу).
# Рекурсивні методи: Можна реалізувати рекурсивні методи для обходу всієї файлової системи і виконання різних
# операцій над файлами і директоріями.
# Виключення: Можна додати обробку виключень для випадків, коли намагаються виконати некоректні операції (наприклад,
# видалити несуществуючий файл).
# Приклад використання:
#
# Python
# root = Directory("root")
# sub_dir = Directory("sub_dir", root)
# file1 = File("file1.txt", sub_dir)
#
# root.add_sub_directory(sub_dir)
# root.add_file(file1)
# Використовуйте цей код обачно.
#
# Цей код створює базову структуру файлової системи з кореневою директорією root, піддиректорією sub_dir і
# файлом file1.txt в ній.
#
# Використання анотацій типів робить код більш зрозумілим і дозволяє виявляти потенційні помилки на ранніх етапах розробки.
