# Give an image represented by a NxN matrix, where each pixel in the image is 4 bytes.
# Write a method to rotate the image by 90 degree. Can you do it in place?
# Example:
# Input:    1  2  3  4      Output: 4  8 12 16
#           5  6  7  8              3  7 11 15
#           9 10 11 12              2  6 10 14
#          13 14 15 16              1  5  9 13

# Brute force solution involves O(N) increase in memory
def rotateMatrix(mat, n):
    """
    :param mat:
    :return:
    """
    newmat = []
    for row in range(n):
        newmat.append([])
        for col in range(n):
            newmat[row].append(mat[col][n-row-1])

    return newmat


if __name__ == '__main__':
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    print(rotateMatrix(mat, 4))