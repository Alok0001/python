import csv

# writing data to a csv file
data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]
with open("C:/Users/VMAdmin/Documents/data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# reading data from a csv file
with open("C:/Users/VMAdmin/Documents/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)