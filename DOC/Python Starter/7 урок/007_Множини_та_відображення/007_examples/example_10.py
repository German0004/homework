"""
Сортування словника за допомогою циклу for
Ми можемо відсортувати словник за допомогою циклу for. Спочатку ми використовуємо функцію sorted() для впорядкування значень
словника. Потім ми перебираємо відсортовані значення, знаходячи ключі кожного значення. Ми додаємо ці пари
ключ-значення у відсортованому порядку у новий словник.

Примітка. Сортування не дозволяє змінювати порядок словника дома. Записуємо впорядковані пари в абсолютно новий
порожній словник.
"""
dict1 = {1: 1, 5: 9, 3: 4}
# Sort the keys
sorted_keys = sorted(dict1.keys())
print(sorted_keys)
# Sort the values
sorted_values = sorted(dict1.values())
print(sorted_values)
sorted_dict_k, sorted_dict_val = {}, {}

# Sort the keys
for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict_k[k] = dict1[k]
            break

print(sorted_dict_k)
