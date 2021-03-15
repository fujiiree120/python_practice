import contextlib

"""
def tag(name):
    def _tag(f):
        def _wrapper():
            print('<{}>'.format(name))
            r = f()
            print('</{}>'.format(name))
            return r
        return _wrapper
    return _tag
@tag('h3')
def f():
     print('test')

f()
"""

@contextlib.contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield
    print('</{}>'.format(name))

@tag('h2')
def f():
    print('test')

f()
