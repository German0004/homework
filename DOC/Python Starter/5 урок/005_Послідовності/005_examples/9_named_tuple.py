from collections import namedtuple

# Іменований кортеж
Person = namedtuple('Person', 'name surname phonenumber')
named_tuple = Person('Іван', 'Іванов', 321456)
print(named_tuple)

Person(name='Іван', surname='Іванов', phonenumber=1236548)
print(named_tuple[0])
print(named_tuple[1])
print(named_tuple[-1])

