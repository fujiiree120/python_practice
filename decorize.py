import functools

@functools.lru_cache()
def long_func(n):
    r = 0
    for i in range(10000000):
        r += n * 1
    return r

for i in range(10):
    print(long_func(i))


for i in range(10):
    print(long_func(i))