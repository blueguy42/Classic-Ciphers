import stringparser as sp

STANDARD = 0
AUTOKEY = 1
EXTENDED = 2
ENCRYPT = 0
DECRYPT = 1

def parseKey(text: str, key: str, type=STANDARD, operation=ENCRYPT) -> str:
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

def encrypt(plaintext: str, key: str, type=STANDARD) -> dict:
    """Encrypt plaintext using Vigenere cipher with key."""

    # encrypt
    ciphertext = ''
    if type == STANDARD or type == AUTOKEY:
        plaintext = sp.stringToAlphabet(plaintext)
        key = parseKey(plaintext, sp.stringToAlphabet(key), type, ENCRYPT)

        plainNum = sp.alphabetToNumber(sp.stringToAlphabet(plaintext))
        keyNum = sp.alphabetToNumber(sp.stringToAlphabet(key))

        ciphertext = sp.numberToAlphabet([(plainNum[i] + keyNum[i]) % 26 for i in range(len(plainNum))])
    elif type == EXTENDED:
        plainASCII = sp.stringToASCII(plaintext)
        keyASCII = sp.stringToASCII(key)
        ciphertext = sp.ASCIItoString([(plainASCII[i] + keyASCII[i]) % 256 for i in range(len(plainASCII))])

    return {'key': key, 'plaintext': plaintext, 'result': ciphertext}

def decrypt(ciphertext: str, key: str, type=STANDARD) -> dict:
    """Decrypt ciphertext using Vigenere cipher with key."""
    
    # decrypt
    plaintext = ''
    if type == STANDARD or type == AUTOKEY:
        ciphertext = sp.stringToAlphabet(ciphertext)
        key = parseKey(ciphertext, sp.stringToAlphabet(key), type, DECRYPT)

        cipherNum = sp.alphabetToNumber(sp.stringToAlphabet(ciphertext))
        keyNum = sp.alphabetToNumber(sp.stringToAlphabet(key))

        plaintext = sp.numberToAlphabet([(cipherNum[i] - keyNum[i]) % 26 for i in range(len(cipherNum))])
    elif type == EXTENDED:
        cipherASCII = sp.stringToASCII(ciphertext)
        keyASCII = sp.stringToASCII(key)
        plaintext = sp.ASCIItoString([(cipherASCII[i] - keyASCII[i]) % 256 for i in range(len(cipherASCII))])

    return {'key': key, 'ciphertext': ciphertext, 'result': plaintext}


# pt = """Dinas Pendidikan Kota Ternate meminta kepada pihak sekolah dan
# orang tua siswa untuk jenjang pendidikan SD dan SMP se-Kota Ternate
# untuk melarang para siswa membawa permainan lato-lato yang sedang
# tren itu ke sekolah, karena akan mengganggu kegiatan belajar mengajar
# yang dinilai berbahaya sehingga mengantisipasi kecelakaan bagi anak di
# daerah itu."""
# ct = """VMYALHYAGIGQXAFZSGDBHZXAGOAXMBRKNKXTMHMXVAAUWTKRLPPKAXGVKBRTBDSVGNAHTMOKBMFFAHTIYXMMQRKNTHHQDVVUZSRCRWAGWDCSXOIGTNODRLTVUAZJKDEDIJWNSTMSAOIHARYEUOAJLPXFXABBYNYGLSOAGURRRTAXXKRYXBSYIAEKVWRKOVAUWEEKTANQGHWITOGTNTHYVEPIRFEAHEUAAYRZKQONRLRGBRXEIUIJAAFLZOGNAKEFKHVGOYIBEFOKRVMDIZASVLEIMLNKKDVEAKZAUIDX"""
# k = "selatsunda"
# print(encrypt(pt,k,AUTOKEY))
# print(decrypt(ct,k,AUTOKEY))