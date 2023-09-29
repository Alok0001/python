# creating a dictionary of students information
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
#Accessing values in the dictionary
print("name:",student["name"])
print("age:",student["age"])

#modifying values in the dictionary
student["gpa"] = 4.0

#adding a new key-value pair to the dictionary
student["universirty"] = "Abc university"

#Checking if a key in the dictionary or value
print("is 'major' in the dictionary", "major" in student)
print("is 'grade' in the dictionary", "grade" in student)

#length of the dictionary
dic_length = len(student)
print("length of the dictionary is:",dic_length)

#looping through the dictionary values
print("dictionary values")
for value in student.values():
    print(value)

#looping through the key
print("Dictionary keys:")
for key in student.keys():
    print(key)


