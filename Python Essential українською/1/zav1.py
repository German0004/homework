# Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр. Створіть кілька
# різних книжок. Визначте для нього методи _repr_ та _str_.


class Describer_book:

    def describer(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        print(self.author, self.title, self.year, self.genre)


book1 = Describer_book()
book1.describer("Jack London:", "White Fang,", "1906,", "Adventures")
book2 = Describer_book()
book2.describer("Agatha Christie:", "The Secret Adversary,", "1922,", "Detective")
print(repr(book1))
print(repr(book2))
print(str(book1))
print(str(book2))
