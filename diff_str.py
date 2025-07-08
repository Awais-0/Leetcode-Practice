s = 'abcdeee'
t = 'abcdee'

s_list = list(s)
t_list = list(t)

if s:
    for i in s_list:
        if i in t_list:
            t_list.remove(i)
    print(t_list)
            
else:
    print(t)