import json

#writing data in a JSON file
data = { "name": "Alice","age": 30, "city": "New York"}
with open("C:/Users/VMAdmin/Documents/data.json", "w") as file:
    json.dump(data,file)

#Reading Data from a Json file
with open("C:/Users/VMAdmin/Documents/data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)

