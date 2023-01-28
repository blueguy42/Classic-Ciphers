import stringparser as sp
from math import gcd

ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'

ALPHABETICAL = 26
BYTELENGTH = 256

def validateKey(n: int, m: int) -> bool:
    """Validate key, m must be relatively prime with n"""
    return gcd(n, m) == 1

def cipher(text: str, keyM: int, keyB: int, operation=ENCRYPT, n=ALPHABETICAL):
    """Encrypt/decrypt plaintext using Affine cipher with key."""

    if not validateKey(n, keyM):
        return {'error': f'Key is not relatively prime with character set size, {n}.'}
    if not 0 < keyB < n:
        return {'error': f'Key b must be in range 0 < b < {n}.'}
    
    if n == ALPHABETICAL:
        text = sp.stringToAlphabet(text)
        textNumbers = sp.alphabetToNumber(text)
    elif n == BYTELENGTH:
        textNumbers = sp.stringToASCII(text)

    if operation == ENCRYPT:
        """ENCRYPT -> C ≡ mP + b (mod n)"""
        result = [((keyM * p + keyB) % n) for p in textNumbers]
    elif operation == DECRYPT:
        """DECRYPT -> P ≡ m^-1(C - b) (mod n)"""
        mInverse = pow(keyM, -1, n)
        result = [((mInverse * (c - keyB)) % n) for c in textNumbers]
    
    if n == ALPHABETICAL:
        result = sp.numberToAlphabet(result)
    elif n == BYTELENGTH:
        result = sp.ASCIItoString(result)

    return {'operation': operation, 'n': n, 'keyM': keyM, 'keyB': keyB, 'text': text, 'result': result}


# print(cipher('lho he assalamu\'alaikum wr. wb.', 19, 19, ENCRYPT, BYTELENGTH))
print(cipher('\x17ËPsË\x92sF\x9c\x9cF\x17F*ÂøF\x17FÞ\x04Â*sè\x89}sèY}', 19, 19, DECRYPT, BYTELENGTH))
