# Особливість цього файлу в тому, що він виконується
# Виконуватиметься, коли імпортуватиметься пакет, тобто 1 раз!
print('__init__ my_package')

# Усередині цього файлу модулі також можна імпортувати
from .my_module1 import *
from .my_module2 import *

# from . import my_module1, my_module2

__all__ = ['my_module1', 'my_module2']

# . поточний каталог
# .. каталог, що вище
