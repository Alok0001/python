#creating a list of numbers
numbers = [1,2,3,4,5]

#Accessing elements of the list
print("first element:",numbers[0])
print("last element",numbers[-1])

#slicing the list
print("slice [1:4]",numbers[1:4])
print("slice[:3]",numbers[:3]) #begin with first element till 3
print("slice[2:]",numbers[2:]) # begin with 2nd element till last element

# modifying elements of the list
numbers[0] = 10
numbers[-1]= 58
print("modified element",numbers[0])
print("modified element [-1]",numbers[-1])

#adding elements to the end of the list
numbers.append(6)
numbers.append(7)

#removing elements from the list
removed_element = numbers.pop(3)
print("removed elements",removed_element)

#looping through the list
print("list elements:")
for num in numbers:
    print(num)

# length of the array
list_length = len(numbers)
print("length of the array:",list_length)



