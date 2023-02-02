from . import stringparser as sp
from math import gcd

ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'

ALPHABETICAL = 26
BYTELENGTH = 256

def validateKey(n: int, m: int) -> bool:
    """Validate key, m must be relatively prime with n."""
    return gcd(n, m) == 1

def cipher(text, keyM: int, keyB: int, operation=ENCRYPT, n=ALPHABETICAL) -> dict:
    """Encrypt/decrypt plaintext using Affine cipher with key.
    
    Returns a dictionary with the type of operation (encyrpt or decrypt), alphabet size, M & B key, original text, and resulting text."""

    if not validateKey(n, keyM):
        return {'error': f'Key M is not relatively prime with alphabet size, {n}.'}
    if not 0 < keyB < n:
        return {'error': f'Key B must be in range 0 < b < {n}.'}
    
    if n == ALPHABETICAL:
        text = sp.stringToAlphabet(text)
        textNumbers = sp.alphabetToNumber(text)
    elif n == BYTELENGTH:
        textNumbers = text

    if operation == ENCRYPT:
        """ENCRYPT -> C ≡ mP + b (mod n)"""
        result = [((keyM * p + keyB) % n) for p in textNumbers]
    elif operation == DECRYPT:
        """DECRYPT -> P ≡ m^-1(C - b) (mod n)"""
        mInverse = pow(keyM, -1, n)
        result = [((mInverse * (c - keyB)) % n) for c in textNumbers]
    
    if n == ALPHABETICAL:
        result = sp.numberToAlphabet(result)
        if operation == DECRYPT:
            result = result.lower()
    elif n == BYTELENGTH:
        result = bytes(result)

    return {'operation': operation, 'n': n, 'keyM': keyM, 'keyB': keyB, 'text': text, 'result': result}
