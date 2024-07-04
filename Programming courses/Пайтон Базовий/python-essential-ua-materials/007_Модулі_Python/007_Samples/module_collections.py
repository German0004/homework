import collections

a = [1, 1, 2, 3, 3, 3]
counts = collections.Counter(a)
print(counts)

dict_of_lists = collections.defaultdict(list)
for value in range(1, 11):
    if value % 2 == 0:
        dict_of_lists['even'].append(value)
    else:
        dict_of_lists['odd'].append(value)
print(dict(dict_of_lists))

counts = collections.defaultdict(int)
for value in a:
    counts[value] += 1
print(counts)

d = collections.deque([1, 2, 3])
d.popleft()
d.append(4)
d.appendleft(6)
d.pop()
print(d)
