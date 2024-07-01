# Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як властивості. Ознайомтеся
# з декоратором property у Python. Створіть клас, що описує температуру і дозволяє задавати та отримувати температуру за
# шкалою Цельсія та Фаренгейта, причому дані можуть бути задані в одній шкалі, а отримані в іншій.


class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9


# Приклад використання класу Temperature
temp = Temperature()

# Задаємо температуру у Цельсіях і отримуємо її у Фаренгейтах
temp.celsius = 25
print(f'Temperature in Celsius: {temp.celsius} C')
print(f'Temperature in Fahrenheit: {temp.fahrenheit} F')

# Задаємо температуру у Фаренгейтах і отримуємо її у Цельсіях
temp.fahrenheit = 77
print(f'Temperature in Celsius: {temp.celsius} C')
print(f'Temperature in Fahrenheit: {temp.fahrenheit} F')


# У цьому прикладі:
#
# Є два методи @ property(celsius і fahrenheit), які дозволяють отримувати значення температури в обох шкалах.
# Є два методи з декоратором @ < property_name >.setter(celsius і fahrenheit),
# що дозволяють встановлювати значення  температури в обох шкалах. Таким чином, клас Temperature дозволяє
# зручно працювати з температурою в шкалах Цельсія та Фаренгейта,
# а властивості забезпечують інкапсуляцію та контроль доступу до даних.

# Властивості (properties) у Python дозволяють створювати спеціальні методи для доступу до атрибутів класу,
# що надають контроль над читанням, записом і видаленням значень цих атрибутів.
# Використовуючи декоратор property, ми можемо забезпечити інкапсуляцію і контроль за доступом до даних.

# Прикінцевий @celsius.setter використовується як частина декларації властивості у Python, що дозволяє
# вам встановлювати значення для відповідної властивості через встановлену функцію, яка слідує за
# декоратором @property. В основному, це забезпечує можливість присвоювати значення атрибуту
# через вираз присвоєння, подібно до того, як ви робите це зі звичайними атрибутами об'єкта.