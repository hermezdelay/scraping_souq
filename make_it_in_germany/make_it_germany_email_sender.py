import csv
from urllib.parse import unquote

with open('make_it_in_germany/make_it_in_germany.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'{line_count} -\t{unquote(row["email"])}')
        line_count += 1
    print(f'Processed {line_count} lines.')
