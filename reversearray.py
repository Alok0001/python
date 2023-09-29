def reverse(arr):
    return arr[::-1]

n= int(input("enter the numbers of elements:"))
arr =[]

for i in range(n):
    element = int(input(f"enter the element{i+1} :"))
    arr.append(element)
# print the array
print("orginal array:",arr)
#print the reversed array

print("reversed array:",reverse(arr))
