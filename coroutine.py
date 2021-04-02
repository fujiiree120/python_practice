def g_hello():
    yield 'hello1'
    yield 'hello2'
    yield 'hello3'

def f_hello():
    r = yield from 'hello'
    yield r
g = g_hello()
f = f_hello()
print(next(f))
print(next(f))
print(next(f))

print(next(f))

