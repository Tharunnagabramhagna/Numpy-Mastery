import numpy as np

'''Broadcasting allows NumPy to perform operations on arrays
with different shapes by virtually expanding dimensions
so they match the larger array's shape.'''

# The dimensions have the same size.
# OR
# One of the dimensions has a size of 1.

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])
print("-- Broadcasting-1 --\n")
print("Shape of array1 : ", array1.shape)  # (1,4)
print("Shape of array2 : ", array2.shape)  # (4,1)

# Both arrays satisfy the condition that one dimension should be 1, so broadcasting is possible.

print("Resultant Array : \n", array1 * array2)
print("Shape of resultant array : ", (array1 * array2).shape)

# arr1 = np.array([[1,2,3,4],[5,6,7,8]])
# arr2 = np.array([[1],[2],[3],[4]])

# print(arr1.shape) => (2,4)
# print(arr2.shape) => (4,1)

# print(arr1 * arr2) => Broadcasting is not possible (since 2 != 4)

arr1 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])
arr2 = np.array([[1], [2], [3], [4]])
print("\n-- Broadcasting-2 --\n")
print("Shape of arr1 : ", arr1.shape)  # (4,4)
print("Shape of arr2 : ", arr2.shape)  # (4,1)

# Broadcasting is possible because both row counts are 4, and one column size is 1.

print("Product of arr1 and arr2 : \n", arr1*arr2)
print("Shape of Product array : ", (arr1*arr2).shape)  # (4,4)

# array3 = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]])
# array4 = np.array([[1,2],[3,4],[5,6],[7,8]])

# print(array3.shape) => (4,4)
# print(array4.shape) => (4,2)

# print(array3*array4) => Broadcasting is not possible because 4 != 2 in the columns.

print("\n-- Printing a Multiplication Table from 1 to 10 --\n")
arr3 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
arr4 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print("Shape of arr3 : ", arr3.shape)  # (1,10)
print("Shape of arr4 : ", arr4.shape)  # (10,1)

print("Multiplication Tables : \n")
print(arr3*arr4)
print("Shape of tables : ", (arr3*arr4).shape)  # (10,10)
