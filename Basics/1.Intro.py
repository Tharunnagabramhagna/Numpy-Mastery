# NumPy (Numerical Python) is the foundational Python library for scientific computing.
# NumPy is simply python intregated with C programming
# Advantages of Numpy => faster execution, memory efficent

# The line for importing numpy
import numpy as np

print(np.__version__)  # line to check the numpy version

# usage of numpy

print("intro to arrays in numpy")
print("Normal Array")
numbers = [1, 2, 3, 4]  # normal list double the number of items in the list
numbers *= 2
print(numbers)

print("Numpy Array")
np_array = np.array([1, 2, 3, 4])
np_array *= 2
print(np_array)
