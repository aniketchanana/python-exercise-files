# from csv import DictWriter

# with open("example.csv","w") as file:
#     headers=["name","breed","age"]
#     csv_writer = DictWriter(file,fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "name":"aniket",
#         "age":20,
#         "breed":"indian"
#     })

print({"name":"aniket","last":"chanana"}.keys())

# from csv import DictReader

# with open("fighters.csv") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         print(row)