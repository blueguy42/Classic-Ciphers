from . import stringparser as sp
from . import matrixoperation as mo
import numpy as np

ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'
N = 26

def cipher(text: str, key: str, size: int, operation=ENCRYPT) -> dict:
    """Encrypt/decrypt plaintext using Hill cipher with key. Adds padding of X if text length is not a multiple of size.

    Returns a dictionary with the type of operation (encyrpt or decrypt), key, original text, and resulting text."""

    if not sp.isAlphabet(key):
        return {'error': 'Key must only contain alphabetical characters.'}
    if len(key) != size*size:
        return {'error': f'Key must be a square matrix with size {size}x{size}.'}

    text = sp.stringToAlphabet(text)
    lenText = len(text)
    if lenText % size != 0:
        text += 'X' * (size - (lenText % size))

    textNumber = sp.alphabetToNumber(sp.stringToAlphabet(text))
    textMatrix = np.array([textNumber[i:i+size] for i in range(0, len(text), size)])
    textMatrix = textMatrix.transpose()

    keyNumber = sp.alphabetToNumber(sp.stringToAlphabet(key))
    keyMatrix = np.array([keyNumber[i:i+size] for i in range(0, len(key), size)])
    
    if not mo.isInverseMatrix(keyMatrix,size,N):
        return {'error': 'Key matrix is not invertible.'}

    if operation == ENCRYPT:
        """C = KP mod N"""
        cipherMatrix = np.remainder(np.matmul(keyMatrix, textMatrix), N)
        result = (sp.numberToAlphabet(cipherMatrix.transpose().flatten()))
    
    elif operation == DECRYPT:
        """P = K^-1C mod N"""
        keyInv = mo.getInverseMatrixModulo(keyMatrix, size, N)
        plainMatrix = np.remainder(np.matmul(keyInv, textMatrix), N)
        result = (sp.numberToAlphabet(plainMatrix.transpose().flatten())).lower()
        
    return {'operation': operation, 'key': key, 'text': text, 'result': result}