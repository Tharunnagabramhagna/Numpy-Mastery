import numpy as np

array1 = np.array('Z')
print(f'Dimension of array1 : {array1.ndim}')  # ndim => no. of dimensions

array2 = np.array([1, 2, 3])
print(f'Dimension of array2 : {array2.ndim}')

matrix1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f'Dimension of matrix1 : {matrix1.ndim}')

matrix2 = np.array([['A', 'B', 'C'],
                   ['D', 'E', 'F'],
                   ['G', 'H', '_']])
print(f'Dimension of matrix2 : {matrix2.ndim}')
print("matrix2[0][1] = "+matrix2[0][1])
print("matrix2[1][2] = "+matrix2[1][2])
print("matrix2[2][0] = "+matrix2[2][0])
print("matrix2[1][2] = "+matrix2[1][2])

matrix3 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])
print(f'Dimension of matrix3 : {matrix3.ndim}')
print(matrix3.shape)  # structure => [layer,rows,columns]

# matrix3 = np.array([['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I'],
#                     ['J', 'K', 'L'],['M', 'N', 'O'],['P', 'Q', 'R'],
#                     ['S', 'T', 'U'],['V', 'W', 'X'],['Y', 'Z']]) => This shows error
# the error is due the inhomogeneous shape of the list

# Practice Question => print APPLE
word = matrix3[0, 0, 0] + matrix3[1, 2, 0] + \
    matrix3[1, 2, 0] + matrix3[1, 0, 2] + matrix3[0, 1, 1]
print("The word is ", word)

matrix4 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print(f'Dimension of matrix4 : {matrix4.ndim}')
print(matrix4.shape)
# chain indexing => python concept
print("matrix4[0][1][1] =", matrix4[0][1][1])
# multidimensional indexing => numpy concept
print("matrix4[1,2,1] =", matrix4[1, 2, 1])
print("matrix4[0,0,0] =", matrix4[0, 0, 0])
print("matrix4[0,1,0] =", matrix4[0, 1, 0])
