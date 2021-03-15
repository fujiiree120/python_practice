import csv
import collections

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first', 'last', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first': 'mike', 'last': 'jacson', 'address': 'A'})
    writer.writerow({'first': 'mike', 'last': 'jacswwwon', 'address': 'B'})
    writer.writerow({'first': 'mike', 'last': 'jacsorrrn', 'address': 'C'})

with open('names.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    print(csv_reader)
    Names = collections.namedtuple('Names', next(csv_reader))

