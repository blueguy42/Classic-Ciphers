import stringparser as sp

STANDARD = 0
AUTOKEY = 1
EXTENDED = 2
ENCRYPT = 0
DECRYPT = 1

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

def cipher(text: str, key: str, operation=ENCRYPT, type=STANDARD) -> dict:
    """Encrypt/decrypt plaintext using Vigenere cipher with key."""

    result = ''
    if type == STANDARD or type == AUTOKEY:
        text = sp.stringToAlphabet(text)
        key = parseKey(text, sp.stringToAlphabet(key), operation, type)

        textNum = sp.alphabetToNumber(sp.stringToAlphabet(text))
        keyNum = sp.alphabetToNumber(sp.stringToAlphabet(key))
        if operation == ENCRYPT:
            result = sp.numberToAlphabet([(textNum[i] + keyNum[i]) % 26 for i in range(len(textNum))])
        elif operation == DECRYPT:
            result = sp.numberToAlphabet([(textNum[i] - keyNum[i]) % 26 for i in range(len(textNum))])
    elif type == EXTENDED:
        key = parseKey(text, key, operation, type)

        textASCII = sp.stringToASCII(text)
        keyASCII = sp.stringToASCII(key)
        if operation == ENCRYPT:
            result = sp.ASCIItoString([(textASCII[i] + keyASCII[i]) % 256 for i in range(len(textASCII))])
        elif operation == DECRYPT:
            result = sp.ASCIItoString([(textASCII[i] - keyASCII[i]) % 256 for i in range(len(textASCII))])

    return {'key': key, 'text': text, 'result': result}

pt = """Dinas Pendidikan Kota Ternate meminta kepada pihak sekolah dan
orang tua siswa untuk jenjang pendidikan SD dan SMP se-Kota Ternate
untuk melarang para siswa membawa permainan lato-lato yang sedang
tren itu ke sekolah, karena akan mengganggu kegiatan belajar mengajar
yang dinilai berbahaya sehingga mengantisipasi kecelakaan bagi anak di
daerah itu."""
ct = """VMYALHYAGIVMVAGCIGDTWVYAMWGRPIFXLKXHUQDPALLKLWEBOAZHLNHJUAJTMEDILOUHQTMOUEGBUAJPWROIWAENQSVHLNLEJFHKGXLTXJHNWEMREUDEYYDRSRRPTJUFLSOEXEFTUJDPWVXABFUAOALSWAMGSNQGKIOAGYNEHNAXFKXKYXRLSLVAKWHNDKSRXEGYANQGYYVEZAUGDNTIWACSLZHNYEUAKQUAJDARTLTAVRUBSLLYTKYULNYKLMXFANQTAWTPTKCXHCWPLKTSHODGAEYADVCQDEJESIMM"""
k = "selatsunda"
print(cipher(pt,k,ENCRYPT,STANDARD))
# print(cipher(ct,k,DECRYPT,STANDARD))