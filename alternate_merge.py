word1 = 'ghawree'
word2 = 'ofceefffffa'
output = []
w1_list = list(word1)
w2_list = list(word2)

if len(word1) > len(word2):
    for i in range(0,len(word2)):
        output.append(w1_list[i])
        output.append(w2_list[i])
    for i in range(len(word2), len(word1)):
        output.append(w1_list[i])
else:
    for i in range(0,len(word1)):
        output.append(w1_list[i])
        output.append(w2_list[i])
    for i in range(len(word1), len(word2)):
        output.append(w2_list[i])

print(''.join(output))