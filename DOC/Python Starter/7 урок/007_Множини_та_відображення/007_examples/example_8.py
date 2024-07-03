def function(**kwargs):
    print(kwargs)


function(arg1='value1', arg2='value2')

# Аналогічно можна розпаковувати будь-які відображення у іменовані параметри під час виклику функції.

options = {
    'sep': ', ',
    'end': ';\n'
}

print('value1', 'value2', **options)
