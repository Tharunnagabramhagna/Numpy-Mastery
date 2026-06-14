import numpy as np

# Random numbers concept
print("-- Random Numbers Concept --\n")
rng = np.random.default_rng()

print("Rolling a die...")

# Good practice => Add both low and high
print("Value : ", rng.integers(low=1, high=6))
print("\nPrinting a random number from 1 to 100...")
print("Random number : ", rng.integers(low=1, high=100))  # (or) print(rng.integers(1, 100)) [Both are the same]

rng1 = np.random.default_rng(seed=1)  # seed = 1 => sets a fixed value sequence

print("\n1D Array : ", rng1.integers(low=1, high=10, size=3))

rng2 = np.random.default_rng()

print("2D Array : \n", rng2.integers(low=1, high=100, size=(2, 3)))  # (row, col)
print("3D Array : \n", rng2.integers(low=1, high=100, size=(3, 2, 3)))  # (layer, row, col)

# Random floating-point values
print("\n-- Random Floating Points --\n")
print("Random float number : ", np.random.uniform())  # random float between 0 and 1
print("Float number in range : ", np.random.uniform(low=-1, high=2))  # range => -1 to 2

print("1D float Array : ", np.random.uniform(low=-1, high=1, size=3))
print("2D float Array : \n", np.random.uniform(low=2, high=10, size=(4, 3)))
np.random.seed(seed=1)  # Seed method
print("3D float Array : \n", np.random.uniform(low=-1, high=100, size=(3, 2, 2)))

# Random Shuffle of an Array
rng3 = np.random.default_rng()

print("\nShuffling an array...")

array = np.array([1,2,3,4,5])

print("Array before shuffling : ", array)
rng3.shuffle(array)
print("Array after shuffling : ", array)

# Random choice in string-type arrays

rng4 = np.random.default_rng()

print("\nRandom choice in items...")

fruits = np.array(["Apple", "Banana", "Pineapple", "Grapes", "Orange"])
fruit = rng.choice(fruits)

print("\nFruit-1")
print("Random fruit : ", fruit)
print("1D Array of fruits : ", rng.choice(fruits, size=3))
print("2D Array of fruits : \n", rng.choice(fruits, size=(3, 2)))
print("3D Array of fruits : \n", rng.choice(fruits, size=(2, 3, 3)))

fruits_emoji = np.array(["🍎","🍌","🍍","🍇","🍊"])
single_fruit = rng.choice(fruits_emoji)

print("\nFruit-2")
print("Random fruit : ", single_fruit)
print("1D Array of fruits : ", rng.choice(fruits_emoji, size=3))
print("2D Array of fruits : \n", rng.choice(fruits_emoji, size=(2, 4)))
print("3D Array of fruits : \n", rng.choice(fruits_emoji, size=(3, 2, 4)))


shop_emoji = np.array(["👕","👖","👗","👜","👟"])
single_item = rng.choice(shop_emoji)

print("\nShopping items")
print("Random item : ", single_item)
print("1D Array of items : ", rng.choice(shop_emoji, size=3))
print("2D Array of items : \n", rng.choice(shop_emoji, size=(2, 3)))
print("3D Array of items : \n", rng.choice(shop_emoji, size=(4, 2, 5)))
