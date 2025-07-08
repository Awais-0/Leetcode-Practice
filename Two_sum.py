nums = [3,2,4]
target = 6
# print(nums[3])
# print(len(nums))

def target_index(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            temp = nums[i]+nums[j]
            if temp == target:
                return [i,j]


print(target_index(nums=nums, target=target))