
nums = [3,1,5,7]

def arithematic(nums):
    num_sorted = sorted(nums)
    result = list(num_sorted[i+1] - num_sorted[i] for i in range(len(num_sorted)-1))
    return all( x == result[0] for x in result)

print(arithematic(nums=nums))