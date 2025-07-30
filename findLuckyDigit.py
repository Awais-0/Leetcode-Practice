def findLucky(arr):
    lucky = []
    if arr:
        for num in arr:
            count = 0
            count = arr.count(num)
            if num == count:
                lucky.append(num)
        return max(lucky)
    return False 

print(findLucky([1,2,2,2,7,7,7,3,3]))