import numpy as np

'''Filtering refers to the process of selecting elements
from an array that match a given condition.'''

# Assume these are the ages of people in a college classroom.
ages = np.array([[19,27,35,46,52,16,67,98,100],
                 [18,17,29,49,14,20,22,92,82]])

# Boolean indexing for filtering
teens = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]
print("\n-- Boolean indexing filtering --\n")
print("Teenagers in class : ", teens)
print("Adults in class : ", adults)
print("Seniors in class : ", seniors)
print("Even ages in class : ", evens)
print("Odd ages in class : ", odds)

# Filtering using the where function (we get the same dimensions as the original array)
# where function syntax => np.where(condition, x, y)
# y value => 0 (or) -1 (or) np.nan (NaN: not a number)
Teens = np.where(ages < 18, ages, np.nan)
Adults = np.where((ages >= 18) & (ages < 65), ages, 0)
Seniors = np.where(ages > 65, ages, -1)
print("\n-- Where function filtering --\n")
print("Teenagers in class : \n", Teens)
print("Adults in class : \n", Adults)
print("Seniors in class : \n", Seniors)
