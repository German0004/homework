# Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList, додавши методи очищення списку,
# додавання елемента у довільне місце списку, видалення елемента з кінця та довільного місця списку.


class MyList:
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = []
        self.data = initial_data

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def insert(self, index, item):
        self.data.insert(index, item)

    def clear(self):
        self.data.clear()

    def pop(self, index=-1):
        return self.data.pop(index)

    def remove(self, item):
        self.data.remove(item)

    def print_list(self):
        print(self.data)


# Приклад використання оновленого класу MyList
if __name__ == "__main__":
    # Створення екземпляру класу
    my_list = MyList([1, 2, 3, 4, 5])

    # Додавання елемента у довільне місце списку
    my_list.insert(2, 10)

    # Видалення елемента з кінця списку
    my_list.pop()

    # Видалення елемента з довільного місця списку
    my_list.remove(3)

    # Очищення списку
    my_list.clear()

    # Додавання нового елемента
    my_list.append(100)

    # Виведення списку
    my_list.print_list()

# У цьому оновленому коді класу MyList додані методи:
#
# clear(): для очищення списку.
# insert(index, item): для додавання елемента у довільне місце списку за заданим індексом.
# pop(index=-1): для видалення елемента з кінця списку або за заданим індексом, якщо вказаний.
# remove(item): для видалення першого знайденого елемента зі списку.
