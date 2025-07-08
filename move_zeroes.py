m = [3,2,0,6,0,5]

for i in range(len(m)):
    if m[i] == 0:
        m.remove(0)
        m.append(0)

print(m)