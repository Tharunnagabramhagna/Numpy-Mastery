# NumPy (Numerical Python) is the foundational Python library for scientific computing.
# NumPy is essentially Python integrated with C programming.
# Advantages of NumPy => faster execution, memory efficient

# Line for importing NumPy
import numpy as np

print(np.__version__)  # Line to check the NumPy version

# Usage of NumPy

print("Introduction to arrays in NumPy")
print("Normal List")
numbers = [1, 2, 3, 4]  # A normal list duplicates its items when multiplied.
numbers *= 2
print(numbers)

print("NumPy Array")
np_array = np.array([1, 2, 3, 4])
np_array *= 2
print(np_array)
