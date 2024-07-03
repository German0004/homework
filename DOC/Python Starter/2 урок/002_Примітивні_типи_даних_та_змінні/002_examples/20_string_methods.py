string = "Lorem ipsum dolor sit amet, consectetur adipisicing elit."

# Поділ рядка поелементний, при цьому створюється список
print(string.split())

print(string.strip())
print(string.count('s'))
print(string.replace('Lorem', 'LOREM'))

print(str(len(string)).isdigit())
print(string.title())
print(string.capitalize())
print(string.lower())
print(string.upper())
print(string.center(100, '+'))
my_char = ord(string[0])
print(my_char)
print(chr(my_char))
print('\nstring'.isspace())     # ???????????
print(string.startswith('L'))
print(string.endswith('.'))
print('string'.isalpha())
print(string.casefold())
