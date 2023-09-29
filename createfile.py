# specify the file path and more
file_path = "C:/Users/VMAdmin/Documents/example.txt"

# open the file in write mode and write content
with open(file_path, "w") as file:
    file.write("Hello, this is content written to a file in your laptop:")

print("file created and content written sucessfull.")

