import stringparser as sp
import numpy as np

ENCRYPT = 0
DECRYPT = 1

def parseKey(key: str) -> np.array:
    """Parse key to be square matrix"""

    key = sp.stringToAlphabet(key)

    key = ''.join(dict.fromkeys(key))
    key = key.replace('J', '')

    for char in ('ABCDEFGHIKLMNOPQRSTUVWXYZ'):
        if char not in key:
            key += char

    matrixKey = np.array(list(key))
    matrixKey = matrixKey.reshape(5, 5)

    return matrixKey

def parseText(text: str) -> list[str]:
    """ 
        - Replace 'J' with 'I'
        - make bigram
        - add 'X' if there is pair of same character
        - add 'X' if the length of text is odd
    """
    
    text = sp.stringToAlphabet(text)
    text = text.replace('J', 'I')

    bigram = []
    i = 0
    while i < len(text):
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                bigram.append(text[i] + 'X')
                i += 1
            else:
                bigram.append(text[i] + text[i + 1])
                i += 2
        else:
            bigram.append(text[i] + 'X')
            i += 1

    return bigram


def cipher(text: str, key: str, operation=ENCRYPT) -> dict:
    """Encrypt/decrypt plaintext using Playfair cipher with key."""
    
    text = sp.stringToAlphabet(text)
    matrixKey = parseKey(key)
    bigram = parseText(text)

    result = []
    if operation == ENCRYPT:
        for pair in bigram:
            p1 = np.where(matrixKey == pair[0])
            p2 = np.where(matrixKey == pair[1])
            
            if p1[0] == p2[0]:
                result.append(matrixKey[p1[0], (p1[1] + 1) % 5][0] + 
                              matrixKey[p2[0], (p2[1] + 1) % 5][0])

            elif p1[1] == p2[1]:
                result.append(matrixKey[(p1[0] + 1) % 5, p1[1]][0] +
                             matrixKey[(p2[0] + 1) % 5, p2[1]][0])

            else:
                result.append(matrixKey[p1[0], p2[1]][0] +
                             matrixKey[p2[0], p1[1]][0])

    elif operation == DECRYPT:
        for pair in bigram:
            p1 = np.where(matrixKey == pair[0])
            p2 = np.where(matrixKey == pair[1])
            
            if p1[0] == p2[0]:
                result.append(matrixKey[p1[0], (p1[1] - 1) % 5][0] + 
                              matrixKey[p2[0], (p2[1] - 1) % 5][0])

            elif p1[1] == p2[1]:
                result.append(matrixKey[(p1[0] - 1) % 5, p1[1]][0] +
                             matrixKey[(p2[0] - 1) % 5, p2[1]][0])

            else:
                result.append(matrixKey[p1[0], p2[1]][0] +
                             matrixKey[p2[0], p1[1]][0])

    
    return {'key': matrixKey, 'text': text, 'bigram': ' '.join(bigram), 'result': ''.join(result)}






key = "JALAN GANESHA SEPULUH"
text = "memex"
text2 = "TATAYY"

# print(cipher(text, key, ENCRYPT))
print(cipher(text2, key, DECRYPT))



