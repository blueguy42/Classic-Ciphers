import stringparser as sp
import matrixoperation as mo
import numpy as np

ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'
N = 26

def cipher(text: str, key: str, size: int, operation=ENCRYPT) -> dict:
    """Encrypt/decrypt plaintext using Hill cipher with key.

    Returns a dictionary with the type of operation (encyrpt or decrypt), key, original text, and resulting text."""

    if not sp.isAlphabet(key):
        return {'error': 'Key must only contain alphabetical characters.'}
    if len(key) == size*size:
        return {'error': f'Key must be a square matrix with size {size}x{size}.'}

    textNumber = sp.alphabetToNumber(sp.stringToAlphabet(text))
    textMatrix = np.array([textNumber[i:i+size] for i in range(0, len(text), size)])
    textMatrix = textMatrix.transpose()

    keyNumber = sp.alphabetToNumber(sp.stringToAlphabet(key))
    keyMatrix = np.array([keyNumber[i:i+size] for i in range(0, len(key), size)])

    if operation == ENCRYPT:
        """C = KP mod N"""
        cipherMatrix = np.remainder(np.matmul(keyMatrix, textMatrix), N)
        result = sp.numberToAlphabet(cipherMatrix.transpose().flatten())
    
    elif operation == DECRYPT:
        """P = K^-1C mod N"""
        keyInv = mo.getInverseMatrixModulo(keyMatrix, size, N)
        plainMatrix = np.remainder(np.matmul(keyInv, textMatrix), N)
        result = sp.numberToAlphabet(plainMatrix.transpose().flatten())
        
    return {'operation': operation, 'key': key, 'text': text, 'result': result}

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

