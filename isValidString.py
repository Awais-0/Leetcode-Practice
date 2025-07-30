import re

def isValid(word):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    if len(word) < 3:
        return False
    if re.match("^[A-Za-z0-9]*$", word):
        foundVowels = [char for char in word if char in vowels]
        if not foundVowels:
            return False
        else:
            foundConsonants = [char for char in word if char in consonants]
            if not foundConsonants:
                return False
            return True
    else:
        return False
print(isValid('aadw3'))