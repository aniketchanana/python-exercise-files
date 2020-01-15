# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     for row in csv_reader:
#         print(row)

from csv import DictReader

with open("fighters.csv") as file:
    csv_reader = DictReader(file,delimiter='|')
    for row in csv_reader:
        print(dict(row))