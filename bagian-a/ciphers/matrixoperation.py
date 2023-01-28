import numpy as np

def getCofactor(matrix: list[list[int]], p: int, q: int, n: int) -> list[list[int]]:
    """Get cofactor of matrix[p][q], n is the size of matrix."""

    i = 0
    j = 0
    temp = [[0 for x in range(n)] for y in range(n)]
    for row in range(n):
        for col in range(n):
            if row != p and col != q:
                temp[i][j] = matrix[row][col]
                j += 1
                if j == n - 1:
                    j = 0
                    i += 1
    return temp

def getDeterminant(matrix: list[list[int]], n: int) -> int:
    """Get determinant of matrix, n is the size of matrix."""

    D = 0
    if n == 1:
        return matrix[0][0]
    sign = 1
    for f in range(n):
        temp = getCofactor(matrix, 0, f, n)
        D += (sign) * (matrix[0][f] * getDeterminant(temp, n - 1))
        sign = -sign
    return D

def getAdjoint (matrix: list[list[int]], n: int) -> list[list[int]]:
    """Get adjoint of matrix, n is the size of matrix."""

    adj = [[0 for x in range(n)] for y in range(n)]
    if n == 1:
        adj[0][0] = 1
        return adj
    sign = 1
    for i in range(n):
        for j in range(n):
            temp = getCofactor(matrix, i, j, n)
            sign = ((i + j) % 2 == 0) and 1 or -1
            adj[j][i] = (sign) * (getDeterminant(temp, n - 1))
    return adj

def getInverseMatrixModulo(matrix: list[list[int]], n: int, modulo: int) -> list[list[int]]:
    """Get inverse of matrix, n is the size of matrix."""

    det = getDeterminant(matrix, n)
    detInv = pow(int(det), -1, modulo)
    adj = getAdjoint(matrix, n)
    return np.remainder(np.multiply(adj, int(detInv)), modulo)

def isInverseMatrix(matrix: list[list[int]], n: int, modulo: int) -> bool:
    """Check if there is inverse of matrix, n is the size of matrix."""
    try:
        det = getDeterminant(matrix, n)
        detInv = pow(int(det), -1, modulo)
    except:
        return False
    return True