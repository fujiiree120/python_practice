import re

m = re.match('a.c', 'abc')
print(m.group())

m = re.search('a.c', 'ddddabcdddd')


m = re.findall('a.c', 'test abc test abd')


m = re.match('ab?', 'abn')


m = re.match('[a-zA-z]', 'aaaaaa')


m = re.match('\s', ' ')
print(m)