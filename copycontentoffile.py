#creating to files
f1_path = "C:/Users/VMAdmin/Documents/example.txt"
f2_path = "C:/Users/VMAdmin/Documents/file1.txt"


with open(f1_path, "r") as f1:
    f1_content = f1.read()
with open(f2_path, "w") as f2:
    f2.write(f1_content)

