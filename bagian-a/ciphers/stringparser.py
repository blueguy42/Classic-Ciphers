def isAlphabet(string: str) -> bool:
    """Checks if a string is an alphabet string, i.e. only contains alphabetic characters."""
    return string.isalpha()

def stringToAlphabet(string: str) -> str:
    """Converts a string to an alphabet string, getting rid of all non-alphabetic characters and converting them to uppercase."""
    return ''.join(filter(str.isalpha, string)).upper()

def alphabetToNumber(string: str) -> list[int]:
    """Converts an alphabet string to a list of numbers, where each number represents the index of the letter in the alphabet."""
    return [ord(char) - 65 for char in string]

def numberToAlphabet(numbers: list[int]) -> str:
    """Converts a list of numbers to an alphabet string, where each number represents the index of the letter in the alphabet."""
    return ''.join([chr(char + 65) for char in numbers])

def stringToASCII(string: str) -> list[int]:
    """Converts a string to a list of ASCII numbers."""
    return [ord(char) for char in string]

def ASCIItoString(ascii: list[int]) -> str:
    """Converts a list of ASCII numbers to a string."""
    return ''.join([chr(char) for char in ascii])