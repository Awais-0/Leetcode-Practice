nums = [-1,4,-2,52,13,-4]
def array_product(nums):
    product = 1
    for i in nums:
        product *= i
    return sighfunc(product)

def sighfunc(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0

print(array_product(nums=nums))