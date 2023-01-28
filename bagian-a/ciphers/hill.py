import stringparser as sp
import matrixoperation as mo
import numpy as np

ENCRYPT = 0
DECRYPT = 1
N = 26

def cipher(text: str, key: str, size: int, operation=ENCRYPT):

    textNumber = sp.alphabetToNumber(sp.stringToAlphabet(text))
    textMatrix = np.array([textNumber[i:i+size] for i in range(0, len(text), size)])
    textMatrix = textMatrix.transpose()
    print(textMatrix)
    keyNumber = sp.alphabetToNumber(sp.stringToAlphabet(key))
    keyMatrix = np.array([keyNumber[i:i+size] for i in range(0, len(key), size)])
    print(keyMatrix)

    if operation == ENCRYPT:
        """C = KP mod N"""
        cipherMatrix = np.remainder(np.matmul(keyMatrix, textMatrix), N)
        cipherText = sp.numberToAlphabet(cipherMatrix.transpose().flatten())
        return cipherText
    
    elif operation == DECRYPT:
        """P = K^-1C mod N"""
        keyInv = mo.getInverseMatrixModulo(keyMatrix, size, N)
        plainMatrix = np.remainder(np.matmul(keyInv, textMatrix), N)
        plainText = sp.numberToAlphabet(plainMatrix.transpose().flatten())
        return plainText


# 3X3
key = 'RRFVSVCCT'
# text = 'paymoremoney'
# DECRYPT

# 2X2
key = 'DDCF'
text = 'HELP'

key = 'RRFVSVCCTABCDZAA'
text = 'UBAVZCSJGAAZ'



print(cipher(text, key, 4, DECRYPT))
# print(cipher(text, key, 4, ENCRYPT))

