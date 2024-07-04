# import this
# Beautiful is better than ugly.

# bad example


def MyLongNameIsForToDoSomething(a, b, c, d, e, f, g, x, y, t, v):
    pass


# good example
def get_time():
    return "time is ..."


# Explicit is better than implicit.

# bad
def get_args(a, b):
    s = sum([a, b])
    squares = [x ** 2 for x in [s, s + 2, s + 5]]
    print(squares, 'hello')
    return squares[:1]


# good
def get_sum(a, b):
    return sum([a, b])


def get_squares(sum_result):
    return [x ** 2 for x in [sum_result, sum_result + 2, sum_result + 5]]


def print_result(result):
    print(result, 'hello')


def main(a, b):
    s = get_sum(a, b)
    squares = get_squares(s)
    print_result(squares)
    return squares[:1]

# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
