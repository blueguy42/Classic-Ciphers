from collections import OrderedDict

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

def letterFreq(string: str) -> dict:
    string = stringToAlphabet(string)
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    freq = dict(OrderedDict(sorted(freq.items(), key=lambda i: i[1], reverse=True)))
    i=0
    for x in freq:
        i += 1
        print(f"{i}\t{x}\t{freq[x]}")
    return freq
