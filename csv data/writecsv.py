# r=write using list and write using dictionary
from csv import writer

with open("fighters2.csv","w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character","name"])