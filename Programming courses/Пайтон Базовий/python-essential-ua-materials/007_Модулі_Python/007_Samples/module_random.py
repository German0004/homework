import random

print(random.random())
print(random.randint(0, 10))
print(random.choice([1, 2, 3, 4, 5]))
random.seed(3)
seq = [1, 2, 3, 4, 6]
random.shuffle(seq)
print(seq)
