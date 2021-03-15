import re

m = re.match('a.c', 'abc')
print(m.group())

m = re.search('a.c', 'ddddabcdddd')
print(m.span())

m = re.findall('a.c', 'test abc test abd')
print(m)

m = re.match('ab?', 'abn')
print(m)