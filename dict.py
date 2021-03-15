import collections

d = {}

l = ['a', 'b','b', 'c', 'c', 'c']
for word in l:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(d)

d = collections.defaultdict(int)
l = ['a', 'b','b', 'c', 'c', 'c']
for word in l:
    d[word] += 1

print(d)

c = collections.Counter()
for word in l:
    c[word] += 1

print(c)
print(c.most_common(1))