import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# Slicing syntax => array[start:end:step]; step => number of indices to skip each time

# Single indexing #

print("\n--Single indexing--\n")
# Positive indices
print("Value of array[0] : ", array[0])  # [1 2 3 4]
print("Value of array[1] : ", array[1])  # [5 6 7 8]
print("Value of array[2] : ", array[2])
print("Value of array[3] : ", array[3])
# Negative indices
print("Value of array[-1] : ", array[-1])  # [13 14 15 16]
print("Value of array[-2] : ", array[-2])
print("Value of array[-3] : ", array[-3])
print("Value of array[-4] : ", array[-4])

# Row Slicing #
print("\n-- Row Slicing --\n")

# Positive slicing
print("Value of array[0:1] :\n", array[0:1], "\n")
print("Value of array[0:2] :\n", array[0:2], "\n")
print("Value of array[0:3] :\n", array[0:3], "\n")
print("Value of array[0:4] :\n", array[0:4], "\n")

# 0 --> end (or) 0 --> 4 (Both are same)
print("Value of array[0:] :\n", array[0:], "\n")
print("Value of array[1:] :\n", array[1:], "\n")
# [[ 9 10 11 12]
#  [13 14 15 16]]
print("Value of array[2:] :\n", array[2:], "\n")
print("Value of array[3:] :\n", array[3:], "\n")  # [[13 14 15 16]]

print("Value of array[1:2] :\n", array[1:2], "\n")
print("Value of array[1:3] :\n", array[1:3], "\n")
print("Value of array[1:4] :\n", array[1:4], "\n")

print("Value of array[2:3] :\n", array[2:3], "\n")
print("Value of array[2:4] :\n", array[2:4], "\n")

print("Value of array[3:4] :\n", array[3:4], "\n")

# Negative slicing
print("Value of array[-1:] :\n", array[-1:], "\n")  # [[13 14 15 16]]
print("Value of array[-2:] :\n", array[-2:], "\n")
print("Value of array[-3:] :\n", array[-3:], "\n")
print("Value of array[0:-2] :\n", array[0:-2], "\n")

# Step slicing
print("Value of array[1:3:2] :\n", array[1:3:2], "\n")  # [5,6,7,8]
print("Value of array[0::2] :\n", array[0::2], "\n")
print("Value of array[::2] :\n", array[::2], "\n")
print("Value of array[2:4:3] :\n", array[2:4:3], "\n")
print("Value of array[1::4] :\n", array[1::4], "\n")
print("Value of array[0::-2] :\n", array[0::-2], "\n")
print("Value of array[::-2] :\n", array[::-2], "\n")
print("Value of array[2::-2] :\n", array[2::-2], "\n")
print("Value of array[::-1] :\n", array[::-1], "\n")
print("Value of array[::-2] :\n", array[::-2], "\n")
print("Value of array[::-3] :\n", array[::-3], "\n")

# Column slicing => syntax: array[row_start:row_end:row_step, col_start:col_end:col_step]
print("\n-- Column slicing --\n")
print("Value of array[:,0:2] :\n", array[:, 0:2], "\n")
print("Value of array[0:,0:2] :\n", array[0:, 0:2], "\n")
print("Value of array[:,1:3] :\n", array[:, 1:3], "\n")
print("Value of array[:,2:] :\n", array[:, 2:], "\n")
print("Value of array[:,2:4] :\n", array[:, 2:4], "\n")
print("Value of array[0:,2:4] :\n", array[0:, 2:4], "\n")
print("Value of array[:,::2] :\n", array[:, ::2], "\n")
print("Value of array[:,1::2] :\n", array[:, 1::2], "\n")
print("Value of array[:,2::2] :\n", array[:, 2::2], "\n")
print("Value of array[:,::-2] :\n", array[:, ::-2], "\n")
print("Value of array[:,::-1] :\n", array[:, ::-1], "\n")

print("Value of array[0:2,0:2] :\n", array[:2, :2], "\n")
print("Value of array[0:2,2:] :\n", array[:2, 2:], "\n")
print("Value of array[2:,0:2] :\n", array[2:, :2], "\n")
print("Value of array[2:,2:] :\n", array[2:, 2:], "\n")
