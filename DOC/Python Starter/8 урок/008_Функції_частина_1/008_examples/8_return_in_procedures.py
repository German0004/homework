def hello(name):
    """
    Якщо ім'я порожнє, виходимо з функції
    """
    if not name:
        return
    print('Hello, ', name, '!', sep='')


hello('Alex')
hello('')
hello('Python')
