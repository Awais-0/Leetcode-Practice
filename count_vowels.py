def count_vowels(s):
    vowels = ['a','e','i','o','u']
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels('aeagsdxu'))
