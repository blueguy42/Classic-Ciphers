from collections import OrderedDict
import re
import math

def replaceSubstring(string: str, n: int, step: int, substr: str, replace: str) -> str:
    """Replaces all substrings of length n in a string with a given substring."""
    for i in range(0, len(string)-n+1, step):
        if string[i:i+n] == substr:
            string = string[:i] + replace + string[i+n:]
    return string

def substringFreq(string: str, n: int, step: int, printAll: bool) -> dict:
    """Returns a dictionary of frequencies of substring length n of a string, sorted by frequency.
    First removes all non-alphabetic characters and converts them to uppercase. Goes through string with steps."""
    string = ''.join(filter(str.isalpha, string)).upper()

    freq = {}
    for i in range(0, len(string)-n+1, step):
        if string[i:i+n] in freq:
            freq[string[i:i+n]] += 1
        else:
            freq[string[i:i+n]] = 1
    freq = dict(OrderedDict(sorted(freq.items(), key=lambda i: i[1], reverse=True)))
    
    i=0
    for x in freq:
        if printAll:
            i += 1
            print(f"{i}\t{x}\t{freq[x]}")
        else:
            if freq[x] > 1:
                i += 1
                print(f"{i}\t{x}\t{freq[x]}")
    return freq

def mostFrequentLetter(string: str) -> str:
    """Returns the most frequent letter in a string."""
    return max(set(string), key = string.count)


def allIndexSubstring(string: str, substring: str) -> list[int]:
    """Returns a list of all indexes of a substring in a string."""
    indexes = []
    for m in re.finditer(substring, string):
        indexes.append(m.start())
    return indexes

def differenceArray(array: list[int]) -> list[int]:
    """Returns a list of differences between adjacent elements in an array."""
    diff = []
    for i in range(len(array)-1):
        diff.append(array[i+1]-array[i])
    return diff

def GCDArray(array: list[int]) -> int:
    """Returns the greatest common divisor of all elements in an array."""
    return math.gcd(*array)
