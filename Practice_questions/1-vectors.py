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

vector_a = np.array([2, 1])  # vectorA => A
vector_b = np.array([-1, 2])  # vectorB => B

a = int(input("Enter the value of a : "))  # Enter 2
b = int(input("Enter the value of b : "))  # Enter 3

# E.g. if a = 2, b = 3 then res = [4-3, 2+6] = [1,8]
res_vector = (a * vector_a) + (b * vector_b)
# Mathematically => A * x
# res_vector = np.column_stack((vector_a,vector_b)) @ np.array([a,b])

print("Resultant Vector = ", res_vector)

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

vec_a = np.array([1,2])
vec_b = np.array([3,1])

target = np.array([7,5])

# column_stack => Stack 1-D arrays as columns into a 2-D array.
A = np.column_stack((vec_a,vec_b))

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

print("\nQuestion-3 Answer\n")

direction_a = np.array([1,0])
direction_b = np.array([0,1])

target = np.array([4,7])

mat_a = np.column_stack((direction_a, direction_b))

y = np.linalg.solve(mat_a, target)

m = int(y[0])
n = int(y[1])

print("value of m : ",m)
print("value of n : ",n)

print("\nResult : ",np.array([m,n]))
print("Target Reached : ",np.array_equal(target,mat_a @ y))

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

# Ans)

print("\nQuestion-4 Answer\n")

direc = np.array([2,4])
tar = np.array([6,12])

res = tar / direc

if(np.all(res == res[0])):
    print("Target is reachable.")
    print("Scaling Factor :",int(res[0]))
else:
    print("Target is not reachable.")

# Problem 05 — Do These Directions Cover 2D Space?
# -------------------------------------------------
# You are designing a simple 2D movement system for a game.

# The system has two available movement directions:

# directionA = [1, 2]
# directionB = [2, 4]

# The game should allow the player to generate ANY possible
# direction in a 2D coordinate system by combining these two
# directions with different scaling factors.

# Your Task
# ---------
# Determine whether directionA and directionB are sufficient
# to generate every possible 2D vector.

# For example, investigate whether vectors such as:

#     [3, 6]
#     [5, 10]
#     [10, 20]

# can be generated.

# Then consider a vector such as:

#     [1, 0]

# Can the movement system generate it?

# Your solution should:

# 1. Analyze the mathematical relationship between directionA
#    and directionB.

# 2. Determine what kind of vectors their combinations can
#    generate.

# 3. Explain whether their span covers the entire 2D space.

# 4. Use NumPy to experiment with different coefficients.

# 5. Verify your conclusion with at least a few examples.

# Important
# ---------
# Don't immediately use np.linalg.solve().

# This problem is primarily testing your understanding of
# LINEAR COMBINATION and SPAN.

# Think about the relationship between:

#     directionA = [1, 2]
#     directionB = [2, 4]

# before writing the code.


# Interview Question
# ------------------
# An interviewer asks:

# "Can two vectors in R² always span the entire 2D space?"

# Give a clear answer and explain what determines whether
# they can or cannot.


# Expected Learning
# -----------------
# Understand that simply having two vectors does NOT guarantee
# that they span 2D space.

# The relationship between the vectors matters.

# You should be able to recognize when vectors provide
# independent directions and when they are effectively pointing
# along the same direction.

# Ans)

print("\nQuestion-5 Answer\n")

vec1 = np.array([1,2])
vec2 = np.array([2,4])

# Step-1 : Find the relation b/w vectors and also the scaling factor
res = vec2 / vec1
if(np.all(res == res[0])):
    factor = int(res[0])
else:
    print("There is no scaling factor.")

# i.e. vec2 = 2 * vec1
print("Value of Scaling factor :",factor)

# Step-2 : Modify and test the linear combination for span

# a * vec1 + b x vec2
# WKT, vec2 = 2 x vec1
# => a x vec1 + b x 2 x vec1 = (a + 2b) vec1

# Test Cases and Results :
# a = 1, b = 0 => linearComb = [1,2]
# a = 0, b = 1 => linearComb = [2,4] = 2 [1,2]
# a = 2, b = 3 => linearComb = [8,16] = 8 [1,2]
# a = -1, b = 4 => linearComb = [7,14] = 7 [1,2]

i = int(input("Enter the value of i : "))
j = int(input("Enter the value of j : "))

coeff = i + j * factor

linearComb = coeff * vec1

# Step-3 : Show the Linear Combination Result

print("Linear Combination of vec1 and vec2 : ",linearComb)

# Step-4 : Verify if it is a span 

if(np.array_equal(linearComb, coeff * vec1)):
    print(f'{linearComb} belongs to the span of vec1 and vec2')
else:
    print(f'{linearComb} does not belongs to the span of vec1 and vec2')


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

# Ans)

print("\nQuestion-6 Answer\n")

fe_a = np.array([2,1])
fe_b = np.array([1,3])

A = np.column_stack((fe_a,fe_b))
dataPoint = np.array([5,7])
ans = np.linalg.solve(A,dataPoint)

m = ans[0]
n = ans[1]

print("Values of m and n : ",m,n)

# allclose => function used for floating values as we may get approx answers
if(np.allclose((m * fe_a + n * fe_b),dataPoint)):
    print("Data Point can be represented by feA and feB")
else:
    print("Data Point can't be represented by feA and feB")

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

# Ans)

print("\nQuestion-7 Answer\n")

vect_a = np.array([2,1])
vect_b = np.array([-1,2])

# map(datatype, input) => used for numbers 
val1, val2 = map(float,input("Enter the values of val and val2 : ").split())

# Experiment values and Results : 
#  1) val1 = -2  val2 = 0.5 => [-4.5 , 1.0]
#  2) val1 = -4  val2 = 0.9 => [-8.9, -2.2]
#  3) val1 = 0.1 val2 = 1.2 => [-1.0, 2.5]
#  4) val1 = 4.2 val2 = 1.36 => [7.04, 6.92]
#  5) val1 = 2.8 val2 = -1.33 => [6.93, 0.14]
#  6) val1 = 9 val2 = 10 => [8.0, 29.0]
#  7) val1 = 100 val2 = 0 => [200.0, 100.0]
#  8) val1 = 0 val2 = -10 => [10.0, -20.0]
#  9) val1 = 19 val2 = 200 => [-162, 419]
# 10) val1 = 23 val2 = 2.3 => [43.7, 27.6]

com_a = val1 * vect_a
com_b = val2 * vect_b
linear_comb_vec = com_a + com_b

print("Combination of vector-A : ",com_a)
print("Combination of vector-B : ",com_b)
print("Linear Combination  : ", linear_comb_vec)

print("Verification :",np.array_equal(com_a + com_b,linear_comb_vec))

# Problem 08 — Explain Linear Combination and Span
# ------------------------------------------------

# Imagine you are in a machine-learning interview.

# The interviewer gives you two vectors:
#     vectorA = [2, 1]
#     vectorB = [-1, 2]
# and asks:
# "If you can choose any real values for a and b,
# what can you generate using these two vectors?"


# Your Task
# ---------

# PART 1 — Explain Linear Combination
# ------------------------------------
# Explain what this expression means:
#     a * vectorA + b * vectorB
# Do NOT give a textbook definition.
# Explain it as if you were explaining the concept to
# another developer who has never studied linear algebra.


# PART 2 — Explain Span
# ---------------------
# Now explain the difference between:
#     One linear combination
# and
#     The span of vectorA and vectorB.

# Use a simple example to make the difference clear.


# PART 3 — Compare Two Vector Systems
# ------------------------------------
# Consider these two systems:

# System A:

#     vectorA = [1, 2]
#     vectorB = [2, 4]

# System B:

#     vectorA = [2, 1]
#     vectorB = [-1, 2]

# You already experimented with both systems.

# Explain:
#     Why can't System A generate every vector in 2D?
#     Why can System B generate a much larger set of
#     vectors in 2D?


# PART 4 — Coding Demonstration
# -----------------------------
# Write a small NumPy program that demonstrates your explanation.

# Your program should:
# 1. Define the two vectors from System B.
# 2. Accept arbitrary coefficients a and b.
# 3. Calculate their linear combination.
# 4. Print the individual contributions.
# 5. Print the resulting vector.
# 6. Verify that:
#        contributionA + contributionB
#        =
#        resulting vector


# PART 5 — Interview Question
# ---------------------------
# Answer this question in your own words:

# "Does having two vectors in R² automatically mean that
# their span is the entire R²?"

# Explain your reasoning without using a memorized definition.


# Expected Learning
# -----------------
# By the end of this problem, you should be able to clearly
# distinguish:

#     Vector
#        ↓
#     Scalar multiplication
#        ↓
#     Linear combination
#        ↓
#     Span
#        ↓
#     Independent directions

# Ans)

print("\nQuestion-8 Answer\n")

# Part-1 : What is Linear Combination 

# A linear combination is created by multiplying vectors by scalar
# coefficients and adding the resulting vectors.

vect_A = np.array([1,3])
vect_B = np.array([-2,1])

var1, var2 = map(int, input("Enter the values of a and b : ").split())

comb1 = var1 * vect_A
comb2 = var2 * vect_B

linear_combi = comb1 + comb2

print("Combination1 : ",comb1)
print("Combination2 : ",comb2)
print("Linear Combination : ",linear_combi)

# Part-2 : What is a Span

