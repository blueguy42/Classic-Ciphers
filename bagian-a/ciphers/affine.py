import stringparser as sp
from math import gcd

ENCRYPT = 0
DECRYPT = 1

def validateKey(n: int, m: int) -> bool:
    """Validate key, m must be relatively prime with n"""
    return gcd(n, m) == 1

def cipher(text: str, keyM, keyB, operation=ENCRYPT):
    """Encrypt/decrypt plaintext using Affine cipher with key."""

    n = 26          # Assumption
    if not validateKey(n, keyM):
        return {'error': 'Key is not valid'}
    
    text = sp.stringToAlphabet(text)
    textNumbers = sp.alphabetToNumber(text)

    result = []
    if operation == ENCRYPT:
        """ENCRYPT -> C ≡ mP + b (mod n)"""
        for P in textNumbers:
            result.append((keyM * P + keyB) % n)
    elif operation == DECRYPT:
        """DECRYPT -> P ≡ m^-1(C - b) (mod n)"""

        mInverse = -1
        for X in range(1, n):
            if (((keyM % n) * (X % n)) % n == 1):
                mInverse = X
                break
        
        if mInverse == -1:
            return {'error': 'Key is not valid'}
        else:
            for C in textNumbers:
                result.append((mInverse * (C - keyB)) % n)
    
    return sp.numberToAlphabet(result)


print(cipher('kripto', 7, 10, ENCRYPT))
print(cipher('CZOLNE', 7, 10, DECRYPT))
