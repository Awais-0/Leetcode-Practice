def longest_palindromic_substring(s):
    l = list(s)
    rev_l = list(reversed(l))
    out = []

    for i in range(len(l)):
        if l[i] == rev_l[i]:
            out.append(l[i])
    
    return ''.join(out)

print(longest_palindromic_substring('badad'))
        