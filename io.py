import io

with open('a.txt', 'w') as f:
    f.write('test')

with open('a.txt', 'r') as f:
    print(f.read())

f = io.StringIO()
f.write('string')
f.seek(0)
print(f.read())