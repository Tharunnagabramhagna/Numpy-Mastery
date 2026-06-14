import numpy as np

# Aggregate functions summarize data and typically
# return a single value.

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15]])

print("Sum of array values : ", np.sum(array))
print("Mean of array values : ", np.mean(array))
print("Standard deviation of array values : ", np.std(array))
print("Variance of array values : ", np.var(array))

print("Maximum value in the array : ", np.max(array))
print("Minimum value in the array : ", np.min(array))
print("Index of the minimum value in the array : ", np.argmin(array))
print("Index of the maximum value in the array : ", np.argmax(array))

# Rows => axis = 1; columns => axis = 0
print("New array (sum of rows) : ", np.sum(array, axis=1))
print("New array (sum of columns) : ", np.sum(array, axis=0))

print("New array (mean of rows) : ", np.mean(array, axis=1))
print("New array (mean of columns) : ", np.mean(array, axis=0))

print("New array (std of rows) : ", np.std(array, axis=1))
print("New array (std of columns) : ", np.std(array, axis=0))

print("New array (variance of rows) : ", np.var(array, axis=1))
print("New array (variance of columns) : ", np.var(array, axis=0))
