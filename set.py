# creating a set of fruits # to store unique elements in unorder way
fruits = {"apple","banana","oranage"}

#adding an element to the set
fruits.add("grape")

#removing an element from set
fruits.remove("banana")

#checking  if the element is there (searching)
print("is 'apple' in the set ","apple" in fruits)
print("is 'banana' in the set","banana"in fruits)

#length of the set
set_length = len(fruits)
print("length of set is:",set_length)

#looping through the set
print("set element:")
for fruit in fruits:
    print(fruit)
