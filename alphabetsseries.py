# Accept a series of alphabets from the user
a = input("Enter a series of alphabets: ")

a_list = list(a)
#short the list
a_list.sort()

# Convert the sorted list back to a string
new_list = ''.join(a_list)

# Display the sorted alphabets
print("Sorted alphabets:", new_list)
