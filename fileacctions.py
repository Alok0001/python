#open a file in the append mode and add mew content
with open("C:/Users/VMAdmin/Documents/example.txt", "a") as file:
    file.write("\nThis is the additional content appended to the file.")

with open("C:/Users/VMAdmin/Documents/example.txt", "r") as file:
    for line in file:
        print(line.strip())
