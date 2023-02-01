from . import stringparser as sp

STANDARD = 'standard'
AUTOKEY = 'autokey'
EXTENDED = 'extended'

ENCRYPT = 'encrypt'
DECRYPT = 'decrypt'

def parseKey(text: str, key: str, operation=ENCRYPT, type=STANDARD) -> str:
    """Parse key to be the same length as text."""
    if type == STANDARD or type == EXTENDED:
        if len(key) < len(text):
            key = (key * (len(text) // len(key) + 1))[:len(text)]
    elif type == AUTOKEY:
        if operation == ENCRYPT:
            key = key + text[:len(text) - len(key)]
        elif operation == DECRYPT:
            textKey = text[:len(text) - len(key)]
            textKeyNum = sp.alphabetToNumber(textKey)
            for i in range(len(textKey)):
                key += sp.numberToAlphabet([(textKeyNum[i] - sp.alphabetToNumber(key[i])[0]) % 26])
    return key

def cipher(text, key: str, operation=ENCRYPT, type=STANDARD) -> dict:
    """Encrypt/decrypt plaintext using Vigenere cipher with key.
    
    Returns a dictionary with the type of operation (encyrpt or decrypt), type of vigenere cipher (standard, autokey, or extended), key, original text, and resulting text."""

    result = ''
    if type == STANDARD or type == AUTOKEY:
        text = sp.stringToAlphabet(text)
        key = parseKey(text, sp.stringToAlphabet(key), operation, type)

        textNum = sp.alphabetToNumber(sp.stringToAlphabet(text))
        keyNum = sp.alphabetToNumber(sp.stringToAlphabet(key))
        if operation == ENCRYPT:
            result = sp.numberToAlphabet([(textNum[i] + keyNum[i]) % 26 for i in range(len(textNum))])
        elif operation == DECRYPT:
            result = (sp.numberToAlphabet([(textNum[i] - keyNum[i]) % 26 for i in range(len(textNum))])).lower()
    elif type == EXTENDED:
        key = parseKey(text, key, operation, type)

        textASCII = text
        keyASCII = sp.stringToASCII(key)
        if operation == ENCRYPT:
            result = bytes([(textASCII[i] + keyASCII[i]) % 256 for i in range(len(textASCII))])
        elif operation == DECRYPT:
            result = bytes([(textASCII[i] - keyASCII[i]) % 256 for i in range(len(textASCII))])

    return {'operation': operation, 'type': type, 'key': key, 'text': text, 'result': result}