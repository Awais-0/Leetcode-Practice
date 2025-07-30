def maxSum(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
        
    result = [key for key, value in freq.items() if key > 0]
    
    return(sum(result))
    

print(maxSum([1,1,0,1,1]))