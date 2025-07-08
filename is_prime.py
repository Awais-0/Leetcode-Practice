def is_prime(n):
    for i in range(1, n//2):
        if n%i == 0:
            prime = False
        else:
            prime = True
    return prime

print(is_prime(14))