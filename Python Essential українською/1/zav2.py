# Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків. Зробіть так, щоб при виведенні книги
# на екран за допомогою функції print також виводилися відгуки до неї.


class Book_review:

    def __init__(self,review):
        self.review = review
        print(self.review)
class Book:
    def __init__(self,author,title):
        self.author = author
        self.title = title
        print(self.author,self.title)

book = Book("Jack London:", "White Fang")
book = Book_review("Book about White Fang is wonderfull")



