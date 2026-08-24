import numpy as np

# Problem 01 — Build a New Vector
# --------------------------------
# You are given two vectors representing two independent directions
# in a 2D space.

# vectorA = [2, 1]
# vectorB = [-1, 2]

# Using a coefficient of 2 for vectorA and b of 3 for vectorB,
# create the resulting vector.

# First calculate the result manually.
# Then reproduce the same operation using NumPy.

# Expected learning:
# Understand how multiple vectors can be combined to create
# a new vector.

# Ans)

# formula for linear combination
# res = aA + bB

print("Question-1 Answer\n")
vectorA = np.array([2, 1])  # vectorA => A
vectorB = np.array([-1, 2])  # vectorB => B

a = int(input("Enter the value of a : "))  # Enter 2
b = int(input("Enter the value of b : "))  # Enter 3

# E.g. if a = 2, b = 3 then res = [4-3, 2+6] = [1,8]
resVector = (a * vectorA) + (b * vectorB)
# resVector = np.column_stack(vectorA,vectorB) @ np.array([a,b]) # Mathematically => A * x

print("Resultant Vector = ", resVector)

# Problem 02 — Reconstruct the Target
# ------------------------------------
# A target vector is represented as:

# target = [7, 5]

# You are given two base vectors:

# vectorA = [1, 2]
# vectorB = [3, 1]

# Your task is to determine whether the target can be created
# by combining vectorA and vectorB.

# If possible, find the coefficients and verify your result
# using NumPy.

# Expected learning:
# Understand how a vector can be represented using other vectors.

# Ans)

print("\nQuestion-2 Answer\n")
vecA = np.array([1,2])
vecB = np.array([3,1])

target = np.array([7,5])

# column_stack => Stack 1-D arrays as columns into a 2-D array.
A = np.column_stack((vecA,vecB))

# linalg => contains linear algebra functions 
x = np.linalg.solve(A,target) # slove => sloves A * x = b type of problem

p = x[0]
q = x[1]

print("Value of p : ",p)
print("Value of q : ", q)

# Here, A @ x => A * x (@ => used in direct matrix multiplication)
if(np.array_equal(target, A @ x)): 
    print("Target is a possible linear combination.")
else:
    print("Target is not a possible linear combination.")


# Problem 03 — Can These Vectors Reach the Target?
# -------------------------------------------------
# Imagine two vectors define the directions available to a robot
# moving on a 2D grid.

# directionA = [1, 0]
# directionB = [0, 1]

# The robot wants to reach:

# target = [4, 7]

# Can the robot reach the target using only these two directions?

# If yes, determine the required coefficients and verify your
# answer using NumPy.

# Expected learning:
# Understand the idea of span through a practical situation.

# Ans)




# Problem 04 — A Limited Direction System
# ----------------------------------------
# A navigation system allows movement only in the direction:

# direction = [2, 4]

# The system needs to reach:

# target = [6, 12]

# Determine whether the target is reachable using the available
# direction.

# If it is reachable, find the required scaling factor.

# Verify your answer using NumPy.

# Expected learning:
# Understand how the span of a single vector behaves.


# Problem 05 — Do These Directions Cover 2D Space?
# -------------------------------------------------
# You are designing a simple 2D movement system using:

# vectorA = [1, 2]
# vectorB = [2, 4]

# The system should be capable of generating any possible
# 2D direction.

# Can these two vectors achieve that?

# Don't rely only on calculation. Analyze the relationship
# between the vectors and explain your reasoning.

# Use NumPy to experiment with different coefficients and
# observe the vectors you can generate.

# Expected learning:
# Build intuition for span and why some vectors provide
# more freedom than others.


# Problem 06 — Representing Data Using Features
# ---------------------------------------------
# Imagine a machine-learning dataset where two vectors represent
# two available feature directions:

# featureA = [2, 1]
# featureB = [1, 3]

# A new data point is:

# dataPoint = [5, 7]

# Determine whether this data point can be represented as a
# linear combination of the two feature vectors.

# If possible, find the coefficients and verify the result
# using NumPy.

# Expected learning:
# Connect linear combinations with feature representations
# used in machine learning.


# Problem 07 — Exploring a Vector Space
# --------------------------------------
# You are given two vectors:

# vectorA = [2, 1]
# vectorB = [-1, 2]

# Write a small NumPy program that allows you to change the
# coefficients of these vectors and generates the resulting
# vector.

# Experiment with several different coefficient values.

# Your goal is not just to calculate one answer, but to observe
# how changing the coefficients changes the resulting vector.

# Expected learning:
# Develop an intuitive understanding of span by experimentation.


# Problem 08 — Interview Challenge
# ---------------------------------
# Suppose an interviewer asks:

# "What's the difference between a linear combination and a span?"

# Explain the difference using a simple real-world analogy
# instead of giving a textbook definition.

# Then demonstrate your explanation with two vectors and a
# small NumPy example.