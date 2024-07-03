my_dict = {'key': 'value', 10: True, 0.2: "hello"}
print(my_dict)
print(my_dict.get('key2', -1))
d = {1: 10, 2: 20}
print(d.items())
d.clear()
print(d)
d = {"1": "world", "2": "a"}

print(d.popitem())
print(d)
d = {1: 3, 2: 4, 5: 2}
d1 = {55: 6, 45: 3}
d.update(d1)
print(d)
print(d.values())
