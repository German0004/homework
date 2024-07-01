# Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).


class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.data[self.index]
        else:
            raise StopIteration


# Приклад використання ітератора
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    reverse_iter = ReverseIterator(my_list)
    for item in reverse_iter:
        print(item)
# У цьому коді:
#
# Клас ReverseIterator ініціалізується списком data, який потрібно ітерувати у зворотньому порядку.
# Метод __iter__ повертає сам ітератор (self).
# Метод __next__ повертає поточний елемент списку self.data[self.index] і зменшує self.index на одиницю. Якщо self.index
# стає менше нуля, піднімається виняток StopIteration, що позначає кінець ітерації.