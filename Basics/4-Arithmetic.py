import numpy as np

# Scalar Arithmetic (+,-,*,/,%,**)

arr = np.array([1, 2, 3])

print("Addition :", arr + 9)
print("Subtraction :", arr - 1)
print("Multiplication : ", arr * 4)
print("Division : ", arr / 8)
print("Modulo ", arr % 2)
print("Power : ", arr ** 3)

# Vertorized math functions

array = np.array([10.02, 9.318, 27.83])

print("Square root of Array : ", np.sqrt(array))
print("Pi value : ", np.pi)
print("Round off the Array : ", np.round(array))  # convert to int
print("Ceil of the Array : ", np.ceil(array))  # increase value
print("Floor of the Array : ", np.floor(array))  # decrease value

# Practice  => Print area of a circle from the given radii

radii = np.array([4, 5, 6])

print("Area of Circle :", np.pi* radii ** 2)

# Element-wise Arithemtic

arr1 = np.array([10,20,30])
arr2 = np.array([5,10,15])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 % arr2)
print(arr1 % arr2)

# Comparsion Operators

marks = np.array([98,20,100,92,95,97])

print("Perfect Score Students : ",marks[marks == 100])
print("Pass Score Students : ",marks[marks >= 40])
print("Fail Score Students : ",marks[marks < 40])

marks[marks < 40] = 0

print("Credits of Students : ",marks)