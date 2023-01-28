import numpy as np

def getCofactor (matrix, p, q, n): 
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

def getDeterminant (matrix, n):
    D = 0
    if n == 1:
        return matrix[0][0]
    sign = 1
    for f in range(n):
        temp = getCofactor(matrix, 0, f, n)
        D += (sign) * (matrix[0][f] * getDeterminant(temp, n - 1))
        sign = -sign
    return D

def getAdjoint (matrix, n):
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

def getInverseMatrixModulo (matrix, n, modulo):
    det = getDeterminant(matrix, n)
    detInv = pow(int(det), -1, modulo)
    adj = getAdjoint(matrix, n)
    return np.remainder(np.multiply(adj, int(detInv)), modulo)
