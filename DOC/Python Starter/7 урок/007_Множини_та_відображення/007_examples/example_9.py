"""Огляд операцій зі словниками"""

phonebook = {
    "Jack": "032-846",
    "Guido": "917-333",
    "Mario": "120-422",
    # остання кома ігнорується
    "Mary": "890-532",
}

# len(phonebook) – кількість елементів.
print(len(phonebook), "entries found")

print()

# d[key] – отримання значення із ключем key. Якщо такий ключ не існує і відображення
# реалізує спеціальний метод __missing__(self, key), то він викликається.
# Якщо ключ не існує і метод __missing__ не визначений, викидається виняток KeyError.
try:
    print("Mary:", phonebook["Mary"])
    print("Lumberjack:", phonebook["Lumberjack"])
except KeyError as e:
    print("No entry for", *e.args)

print()

# d[key] = value – змінити значення або створити нову пару ключ-значення, якщо ключ не існує.
phonebook["Lumberjack"] = "000-777"
print(phonebook)
# key in d, key not in d – перевірка наявності ключа у відображенні.
for person in ("Guido", "Mary", "Ahmed"):
    if person in phonebook:
        print(person, "is in the phonebook")
    else:
        print("No entry found for", person)

print()

# iter(d) – те саме, що iter(d.keys()).
print("People in the phonebook:")
for person in phonebook:
    print(person)

print()

# copy() – створити неповну копію словника.
phonebook_copy = phonebook.copy()
print("Phonebook:", phonebook)
print("Phonebook copy:", phonebook_copy)

print()

# clear() – видалити всі елементи словника.
phonebook_copy.clear()
print("Phonebook:", phonebook)
print("Phonebook copy:", phonebook_copy)

print()

# (метод класу) dict.fromkeys(sequence[, value]) – створює новий словник з
# ключами з послідовності sequence та заданим значенням (за замовчуванням – None).
numbers_dict = dict.fromkeys(range(3), 42)
print(numbers_dict)

print()

# d.get(key[, default]) – безпечне набуття значення за ключом (ніколи не викидає KeyError).
# Якщо ключ не знайдено, повертається значення default (за замовчуванням – None).
for key in range(5):
    print("{}:".format(key), numbers_dict.get(key, 0))

print()

# d.items() – Python 3 повертає об'єкт подання словника, відповідний парам (двохелементним кортежам)
# виду (ключ, значення). У Python 2 повертає відповідний список, а метод iteritems() повертає ітератор.
# Аналогічний метод Python 2.7 – viewitems().
print("Items:", phonebook.items())

# d.keys() – Python 3 повертає об'єкт подання словника, відповідний ключам словника. У Python 2 повертає відповідний
# список, а метод iterkeys() повертає ітератор. Аналогічний метод у Python 2.7 - viewkeys ().
print("Keys:", phonebook.keys())

# d.values() – Python 3 повертає об'єкт подання словника, відповідний значенням.
# У Python 2 повертає відповідний список, а # метод itervalues() повертає ітератор. Аналогічний метод у Python 2.7 –
# viewvalues().
print("Values:", phonebook.values())

print()

# d.pop(key[, default]) – якщо ключ key існує, видаляє елемент зі словника та повертає його значення.
# Якщо ключ не існує і встановлено значення default, повертається це значення, інакше викидається виняток KeyError.
number = phonebook.pop("Lumberjack")
print("Deleted Lumberjack (was " + number + ")")
print(phonebook)

print()

# d.popitem() – видаляє довільну пару ключ-значення та повертає її. Якщо словник порожній, виникає виняток KeyError.
# Метод корисний для алгоритмів, які обходять словник, видаляючи вже оброблені значення (наприклад,
# певні алгоритми, пов'язані з теорією графів).
person = phonebook.popitem()
print("Popped {} (phone: {})".format(*person))

print()

print(phonebook)

# d.setdefault(key[, default]) – якщо ключ key існує, повертає відповідне значення.
# Інакше створює елемент із ключем key та значенням default. default за промовчанням дорівнює None.
for person in ("Jack", "Liz"):
    phone = phonebook.setdefault(person, "000-000")
    print("{}: {}".format(person, phone))

print(phonebook)

print()

# d.update(mapping) – приймає або інший словник або відображення, або ітерабельний об'єкт, що складається з
# ітерабельних об'єктів - пар ключ-значення, або названі аргументи. Додає відповідні елементи до словника,
# # Перезаписуючи елементи із існуючими ключами.
phonebook.update({"Alex": "832-438", "Alice": "231-987"})
print(phonebook)
phonebook.update([("Joe", "217-531"), ("James", "783-428")])
print(phonebook)
phonebook.update(Carl="783-923", Victoria="386-486")
print(phonebook)
