# Write an algorithm such that if an element in an NxN matrix is 0, it's entire row and columns are set to 0:

def zeroMatrix(matrix):
    """
    :return: return the matrix with 0 in rows and columns if any cell is 0
    """
    n = len(matrix)

    cellWithZeros = []
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 0:
                cellWithZeros.append((row,col))

    for cell in cellWithZeros:
        for i in range(n):
            matrix[i][cell[0]] = 0
        for j in range(n):
            matrix[cell[1]][j] = 0

    return matrix

if __name__ == '__main__':
    mat = [[1, 2, 3, 4],
           [5, 0, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    print(zeroMatrix(mat))