d = {"alice": 35, "mark": 25, "april": 45, "john": 19}
new_d = {}
for name, age in d.items():
    if name[0] != 'a':
        new_d[name] = age
print(new_d)
