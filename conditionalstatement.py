# user input for age
age = int(input("enter your age: "))

# conditional statement
if age < 18:
    print("you are a minor,")
elif age >= 18 and age <65:
    print("you are an adult")
else:
    print("you are a senior citizen")
