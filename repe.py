import datetime
import json
import pprint
d = datetime.datetime.now()
print(d)
print(str(d))
print((repr(d)))

class Point(object):
    def __repr__(self):
        return 'reprrepr'
    def __str__(self):
        return 'string'

p = Point()
print('{0!r} {0} {0!s}'.format(p))

l = ['apple', 'orange', 'banana']
l.insert(0, l[:])
pp = pprint.PrettyPrinter()
pp.pprint(l)

print(json.dumps(l, indent=4))