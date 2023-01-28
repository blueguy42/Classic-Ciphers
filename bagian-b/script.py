from collections import OrderedDict

def substringFreq(string: str, n: int, printAll: bool) -> dict:
    """Returns a dictionary of frequencies of substring length n of a string, sorted by frequency.
    First removes all non-alphabetic characters and converts them to uppercase. """
    string = ''.join(filter(str.isalpha, string)).upper()

    freq = {}
    for i in range(len(string)-n+1):
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

def changeBigrams(string: str, bigram1: str, bigram2: str) -> str:
    """Changes all bigrams in a string from bigram1 to bigram2
        if bigram1[0] is in odd position
    """
    newString = ""
    for i in range(0, len(string)-1, 2):
        if string[i:i+2] == bigram1:
            newString += bigram2
        else:
            newString += string[i:i+2]
    if len(string) % 2 == 1:
        newString += string[-1]
    return newString