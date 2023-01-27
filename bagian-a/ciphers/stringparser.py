def stringToAlphabet(string: str) -> str:
    return ''.join(filter(str.isalpha, string)).upper()

def alphabetToNumber(string: str) -> list[int]:
    return [ord(char) - 65 for char in string]

def numberToAlphabet(numbers: list[int]) -> str:
    return ''.join([chr(char + 65) for char in numbers])

def stringToASCII(string: str) -> list[int]:
    return [ord(char) for char in string]

def ASCIItoString(ascii: list[int]) -> str:
    return ''.join([chr(char) for char in ascii])