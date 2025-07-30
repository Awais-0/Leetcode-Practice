def fancyString(s):
    count = 1
    prev = s[0]
    result = [s[0]]
    for i in range(1, len(s)):
        if(s[i]==prev):
            count = count+1
            if(count < 3):
                result.append(s[i])
        else:
            count = 1
            prev = s[i]
            result.append(prev)
    return "".join(result)
    
print(fancyString("leeetcode"))