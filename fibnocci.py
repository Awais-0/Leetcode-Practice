def fibonacci(n):
    start = [0, 1]
    for i in range(0, n):
            temp = start[i]+start[i+1]
            start.append(temp)
    return start[slice(None,n)]

print(fibonacci(8))