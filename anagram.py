s = 'rat'
t = 'cat'
s_list = list(s)
t_list = list(t)
def anagram(s,t):
    if len(s) == len(t):
        for i in range(len(s)):
            if t[i] in s:
                s.remove(t[i])
        if s:
            return False
        else:
            return True
    else:
        return False


print(anagram(s_list,t_list))