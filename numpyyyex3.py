import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Reshaping the array
reshaped = arr.reshape(3, 2)
print("Reshaped array:")
print(reshaped)

# Concatenating arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))
print("Concatenated array:")
print(concatenated)

# Splitting arrays
split_array = np.split(concatenated, 3)
print("Split arrays:")
print(split_array)

