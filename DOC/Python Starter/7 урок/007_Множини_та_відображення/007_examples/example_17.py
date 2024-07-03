my_shelf = dict()
author = input('Введіть автора (q - завершити):')

while author != 'q':
    books = list()
    book = input('Введіть книгу (s - стоп):')
    while book != 's':
        books.append(book)
        book = input('Введіть книгу (s - стоп):')
    my_shelf[author] = books
    author = input('Введіть автора (q - завершити):')

for author in my_shelf:
    print(author, '-', my_shelf[author])
