def reverse_string(s):
    p = list(s)
    rev_s = []
    for i in range(0, len(p)):
        temp = p.pop()
        rev_s.append(temp)
    return ''.join(rev_s)

print(reverse_string('chacha'))