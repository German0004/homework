def func(index, count):
    return {
        "ID": index,
        "values": ["{}_{}".format(index, value) for value in range(count)]
    }


def generate(count):
    return [func(i, j) for i, j in zip(range(count), list(range(count))[::-1])]


r = generate(10)
# print(r)
f = [value for sublist in r for value in sublist['values']]
print(f)
