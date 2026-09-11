# Goal:
# Implement the mathematical concepts of:
# - Subspace
# - Span
# - Basis
# - Linear Independence
# - Dimension
# - Column Space

# Use NumPy for all problems.

# Do NOT use sklearn or other ML libraries yet.

# ------------------------------------------------------------
# PROBLEM 1 — Verify a Basis of R²
# ------------------------------------------------------------

# Given:

# v1 = np.array([1, 0])
# v2 = np.array([0, 1])

# Tasks:
# 1. Create matrix A using np.column_stack().
# 2. Find the number of vectors.
# 3. Find the rank of A.
# 4. Determine the dimension of the space.
# 5. Determine whether v1 and v2 form a basis of R².

# Print:
# Number of vectors:
# Rank:
# Dimension:
# Basis of R²:

# Ans)

# ------------------------------------------------------------
# PROBLEM 2 — Is This a Basis?
# ------------------------------------------------------------

# Given:

# v1 = np.array([1, 2])
# v2 = np.array([2, 4])

# Tasks:
# 1. Create matrix A.
# 2. Calculate its rank.
# 3. Determine whether the vectors are linearly independent.
# 4. Determine whether they form a basis of R².
# 5. Explain why or why not.

# Expected reasoning:
# A basis must be both:
# - Linearly independent
# - Able to span the required space


# ------------------------------------------------------------
# PROBLEM 3 — Basis of R² with Different Directions
# ------------------------------------------------------------

# Given:

# v1 = np.array([2, 1])
# v2 = np.array([-1, 2])

# Tasks:
# 1. Construct matrix A.
# 2. Calculate rank(A).
# 3. Determine whether the vectors are independent.
# 4. Determine whether they span R².
# 5. Determine whether they form a basis of R².

# Use the relationship:

# For 2 vectors in R²:
# rank = 2
# → independent
# → span R²
# → basis of R²


# ------------------------------------------------------------
# PROBLEM 4 — Find the Dimension of a Span
# ------------------------------------------------------------

# Given:

# v1 = np.array([1, 0, 0])
# v2 = np.array([0, 1, 0])
# v3 = np.array([1, 1, 0])

# Tasks:
# 1. Create matrix A using the vectors as columns.
# 2. Calculate rank(A).
# 3. Determine the dimension of span(v1, v2, v3).
# 4. Determine whether the three vectors form a basis of R³.
# 5. Explain why the dimension is what it is.


# ------------------------------------------------------------
# PROBLEM 5 — Find a Basis from Redundant Vectors
# ------------------------------------------------------------

# Given:

# v1 = np.array([1, 0])
# v2 = np.array([0, 1])
# v3 = np.array([1, 1])

# Tasks:
# 1. Create matrix A.
# 2. Calculate rank(A).
# 3. Determine how many independent directions exist.
# 4. Identify which vectors can be used to form a basis of R².
# 5. Verify your chosen basis using rank.

# Hint:
# You already know that v3 can be represented using v1 and v2.


# ------------------------------------------------------------
# PROBLEM 6 — Column Space
# ------------------------------------------------------------

# Given:

# A = np.array([
#     [1, 2, 3],
#     [2, 4, 6],
#     [1, 1, 2]
# ])

# Tasks:
# 1. Calculate rank(A).
# 2. Determine the dimension of the column space.
# 3. Determine whether all three columns are independent.
# 4. Explain what the column space represents.
# 5. Determine whether the columns form a basis for R³.


# ------------------------------------------------------------
# PROBLEM 7 — Does a Vector Belong to the Span?
# ------------------------------------------------------------

# Given:

# v1 = np.array([1, 2])
# v2 = np.array([2, 1])

# target = np.array([5, 4])

# Determine whether target belongs to:

# span(v1, v2)

# Tasks:
# 1. Construct matrix A from v1 and v2.
# 2. Solve:

# A @ c = target

# 3. Find the coefficients.
# 4. Verify your answer using:

# A @ coefficients

# 5. Print whether target belongs to the span.


# ------------------------------------------------------------
# PROBLEM 8 — Subspace Verification
# ------------------------------------------------------------

# Consider the set:

# S = { [x, y, z] | x + y + z = 0 }

# Tasks:
# 1. Pick at least two vectors that satisfy the condition.
# 2. Verify that they belong to S.
# 3. Express the condition as a system/equation.
# 4. Find independent vectors that can generate S.
# 5. Determine the dimension of S.
# 6. Explain why S is a subspace of R³.


# ------------------------------------------------------------
# PROBLEM 9 — ML-Flavored Feature Space
# ------------------------------------------------------------

# Suppose three feature vectors are:

# feature1 = np.array([1, 2, 3])
# feature2 = np.array([2, 4, 6])
# feature3 = np.array([1, 0, 1])

# Tasks:
# 1. Construct the feature matrix.
# 2. Calculate its rank.
# 3. Determine whether all features provide independent directions.
# 4. Determine the dimension of the feature space.
# 5. Explain what redundant features could mean in an ML dataset.


# ------------------------------------------------------------
# PROBLEM 10 — Build a Basis Checker
# ------------------------------------------------------------

# Create a reusable function:

# check_basis(vectors, dimension)

# The function should:

# 1. Create a matrix using np.column_stack().
# 2. Calculate the matrix rank.
# 3. Count the number of vectors.
# 4. Check whether:

#    rank == number of vectors

# 5. Check whether the vectors can span the requested dimension.
# 6. Print whether the vectors form a basis of the given space.

# Test your function with:

# Test 1:
# [1,0], [0,1]
# dimension = 2

# Test 2:
# [1,2], [2,4]
# dimension = 2

# Test 3:
# [1,0,0], [0,1,0], [0,0,1]
# dimension = 3


# ------------------------------------------------------------
# FINAL INTERVIEW CHALLENGE — PROBLEM 11
# ------------------------------------------------------------

# Given:

# v1 = np.array([1, 2, 0])
# v2 = np.array([0, 1, 1])
# v3 = np.array([1, 3, 1])
# v4 = np.array([2, 1, 3])

# Tasks:

# 1. Construct the matrix.
# 2. Calculate its rank.
# 3. Determine the dimension of its span.
# 4. Determine the maximum number of independent vectors.
# 5. Determine whether all four vectors can form a basis of R³.
# 6. If not, explain why.
# 7. Identify a possible basis from the given vectors.
# 8. Verify your chosen basis using matrix rank.

# Interview question:

# "What is the difference between a set of vectors,
# a spanning set, a basis, and a vector space dimension?"

# ============================================================
# CHECKPOINT COMPLETE WHEN:
# ============================================================

# Problems 1–4 → Foundation
# Problems 5–7 → Practical NumPy
# Problems 8–9 → Subspace + ML connection
# Problem 10 → Reusable implementation
# Problem 11 → Interview challenge

# After Problem 11:
# → Subspaces & Basis checkpoint COMPLETE
# → Move to the next Linear Algebra concept.
# ============================================================