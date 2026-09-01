import numpy as np

zero_vec = np.array([0, 0])  # Global Zero Vection for all problems

# Problem 01 — The Redundant Directions
# -------------------------------------
# You are given two vectors representing two possible directions
# in a 2D feature space.
#
# vectorA = [1, 2]
# vectorB = [2, 4]
#
# Determine whether these two vectors are linearly independent
# or linearly dependent.
#
# You have learned that vectors are linearly independent when
# the equation:
#
#     c1 * vectorA + c2 * vectorB = [0, 0]
#
# has only the trivial solution:
#
#     c1 = 0
#     c2 = 0
#
# Your Task:
# 1. Write the zero-vector equation.
# 2. Determine whether a non-trivial solution exists.
# 3. Explain what the result means geometrically.
# 4. Implement your reasoning using NumPy.
#
# Expected Learning:
# Understand how the zero-vector equation can be used to identify
# linear dependence.

# Ans)
print("\nQuestion-1 Answer\n")
vector_A = np.array([1, 2])
vector_B = np.array([2, 4])


A = np.column_stack((vector_A, vector_B))

# Mathematically formula => Ax = 0 (null space form)
# equation-1 : c1 + 2c2 = 0
# equation-2 : 2c1 + 4c2 = 0
# so, eq1 - eq2 => -c1 = 2c2 => c1 = -2c2
# let, c2 = 1 then c1 = -2
# (-2, 1) is a non-trivial solution

consts = np.array([-2, 1])

print("Values of c1 and c2 :", consts[0], consts[1])

# manual checking (A * x == 0)
if (np.array_equal((A @ consts), zero_vec)):
    if (np.all(consts == 0)):
        print("Vector A and B are linearly independent.")
        print("A trivial solution exists for c1 and c2.")
    else:
        print("Vector A and B are linearly dependent.")
        print("A non-trivial solution exists for c1 and c2.")

# Problem 02 — Trivial or Non-Trivial?
# -------------------------------------
# A data scientist is checking whether two feature vectors
# provide independent information.
#
# You are given:
# vectorA = [2, 1]
# vectorB = [4, 2]
#
# Consider:
#     c1 * vectorA + c2 * vectorB = [0, 0]
#
# Your Task:
# 1. Find at least one solution for c1 and c2.
# 2. Determine whether your solution is trivial or non-trivial.
# 3. Based on your solution, classify the vectors as:
#
#        Linearly Independent
#        OR
#        Linearly Dependent
#
# 4. Verify your result using NumPy.
#
# Important:
# Do not simply compare scaling factors.
#
# Use the zero-vector equation you learned in the
# Linear Independence lessons.
#
# Expected Learning:
# Understand why the existence of a non-trivial solution
# indicates linear dependence.

# Ans)
print("\nQuestion-2 Answer\n")
vec_A = np.array([2, 1])
vec_B = np.array([4, 2])

A = np.column_stack((vec_A, vec_B))

# eq1 : 2c1 + 4c2 = 0
# eq2 : c1 + 2c2 = 0
# eq1 - eq2 : c1 + 2c2 = 0 => c1 = -2c2
# let c2 = -3 => c1 = -2(-3) = 6 => c1 = 6, c2 = -3
# (6,-3) is a non-trivial solution

coeffs = np.array([6, -3])

print("Values of c1 and c2 :", coeffs[0], coeffs[1])

if (np.array_equal((A @ coeffs), zero_vec)):
    if (np.all(coeffs == 0)):
        print("\nVec_A and vec_B are Linearly independent.")
        print("c1 and c2 have a trivial solution.")
    else:
        print("\nVec_A and vec_B are Linearly dependent.")
        print("c1 and c2 have a non-trivial solution.")

# Problem 03 — Two Independent Directions in R²
# ----------------------------------------------
# You are designing a 2D feature representation system.
#
# The system contains:
#
# vectorA = [2, 1]
# vectorB = [-1, 2]
#
# Determine whether these vectors are linearly independent.
#
# Consider the equation:
#     c1 * vectorA + c2 * vectorB = [0, 0]
#
# Your Task:
# 1. Write the two scalar equations.
# 2. Solve for c1 and c2.
# 3. Determine whether a non-trivial solution exists.
# 4. Classify the vectors.
# 5. Explain what this means for their span in R².
# 6. Verify your reasoning using NumPy.
#
# Interview Thinking:
# An interviewer asks:
#
# "Why does having two linearly independent vectors in R²
# imply that they span the entire R²?"
#
# Explain this after solving the problem.

# Ans)
print("\nQuestion-3 Answer\n")
vect_A = np.array([2, 1])
vect_B = np.array([-1, 2])

A = np.column_stack((vect_A, vect_B))

# eq1 : 2c1 - c2 = 0
# => c2 = 2c1 ---> eq3
# eq2 : c1 + 2c2 = 0
# eq3 in eq2 => c1 + 2 * (2c1) = 0 => 5c1 = 0 => c1 = 0
# c1 = 0 => c2 = 2 * 0 = 0
# (0,0) is the only trivial solution.
# Therefore, the vectors are linearly independent
# and consequently span R^2.

coeff = np.array([0, 0])
linas = False

if (np.array_equal((A @ coeff), zero_vec)):
    if (np.all(coeff == 0)):
        print("vect_A and vect_B are linearly independent.")
        print("c1 and c2 have a trivial solution.")
        linas = True
    else:
        print("vect_A and vect_B are linearly dependent.")
        print("c1 and c2 have a non-trivial solution.")
else:
    print("Those coefficients of c1 and c2 doesn't satisfy Ax = 0")

if (linas):
    print("\nvect_A and vect_B spans R^2")
else:
    print("vect_A and vect_B won't span R^2")

''' Ans : Because two linearly independent vectors provide two independent directions
          in R^2, their linear combinations can generate every vector in R^2. '''

# Problem 04 — Three Vectors, One Redundant Direction
# ----------------------------------------------------
# You are given three vectors in R²:
# vectorA = [1, 0]
# vectorB = [0, 1]
# vectorC = [1, 1]
#
# A machine-learning system claims that all three vectors are
# independent because they point in different directions.
# Determine whether this claim is correct.
#
# Consider:
#     c1 * vectorA + c2 * vectorB + c3 * vectorC = [0, 0]
#
# Your Task:
# 1. Determine whether a non-trivial solution exists.
# 2. Find one non-trivial set of coefficients.
# 3. Explain which vector is redundant and why.
# 4. Classify the complete set of vectors.
# 5. Explain why having three vectors in R² creates a limitation.
# 6. Verify your result using NumPy.
#
# Important:
# Do not use the two-vector scaling-factor shortcut.
#
# You now have THREE vectors, so use the general definition
# of linear independence.
#
# Expected Learning:
# Understand why the general zero-vector equation works for
# more than two vectors.

# Ans)
print("\nQuestion-4 Answer\n")
vec1 = np.array([1, 0])
vec2 = np.array([0, 1])
vec3 = np.array([1, 1])

A = np.column_stack((vec1,vec2,vec3))

# eq-1 : c1 + c3 = 0
# eq-2 : c2 + c3 = 0
# eq-1 & 2 : c1 = -c3, c2 = -c3
# Let, c3 = 1 then c1 = -1 , c2 = -1

res_coeff = np.array([-1,-1,1])

if(np.array_equal((A @ res_coeff), zero_vec)):
    if(np.all(res_coeff == 0)):
        print("vec1,vec2 and vec3 are linearly independent.")
        print("c1,c2 and c3 have a trivial solution.")
    else:
        print("vec1,vec2 and vec3 are linearly dependent.")
        print("c1,c2 and c3 have a non-trivial solution.")
else:
    print("Those coefficients of c1, c2 and c3 doesn't satisfy Ax = 0")

# Problem 05 — Build a NumPy Independence Checker
# ------------------------------------------------
# You are building a small mathematical utility for an ML
# preprocessing pipeline.
#
# The utility receives a collection of vectors and needs to
# determine whether the vectors are linearly independent.
#
# Start with:
#
# vectorA = [1, 0]
# vectorB = [0, 1]
#
# Then test another system:
#
# vectorC = [1, 1]
#
# Your Task:
# 1. Represent the vectors using NumPy.
# 2. Construct the corresponding matrix.
# 3. Formulate the zero-vector equation:
#
#        A @ x = 0
#
# 4. Determine whether the system has a non-trivial solution.
# 5. Use NumPy to investigate the solution.
# 6. Test your implementation with:
#        [1, 0]
#        [0, 1]
# and:
#        [1, 0]
#        [0, 1]
#        [1, 1]
# 7. Explain why the second system cannot contain three
#    linearly independent vectors in R².
#
# Expected Learning:
# Connect the mathematical definition of linear independence
# with matrix representation and NumPy.

# Ans)
print("\nQuestion-5 Answer\n")


# Problem 06 — Final Interview Challenge
# ---------------------------------------
# Imagine you are in an ML engineering interview.
#
# The interviewer gives you the following vectors:
#
# vectorA = [1, 2]
# vectorB = [2, 4]
# vectorC = [3, 1]
#
# They ask:
#
# "Are these vectors linearly independent?"
#
# Your Task:
# 1. Write the general zero-vector equation:
#
#        c1 * vectorA + c2 * vectorB + c3 * vectorC = [0, 0]
#
# 2. Determine whether a non-trivial solution exists.
# 3. Find one if it exists.
# 4. Classify the vectors.
# 5. Identify the redundant vector, if there is one.
# 6. Explain the result geometrically.
# 7. Implement your reasoning using NumPy.
#
# Final Interview Question:
#
# "What is the difference between checking whether two vectors
# are scalar multiples and using the general definition of
# linear independence?"
#
# Answer this in your own words.
#
# Expected Learning:
# Be able to move from:
#
#     Definition
#          ↓
#     Mathematical equation
#          ↓
#     Non-trivial solution
#          ↓
#     Linear dependence / independence
#          ↓
#     Matrix representation
#          ↓
#     NumPy implementation
#
#
