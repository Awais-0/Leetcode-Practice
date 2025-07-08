digits = [9,9,9]
s = ''.join([str(i) for i in digits])
m = list(str(int(s) + 1))
s = list([int(i) for i in m])
print(s)